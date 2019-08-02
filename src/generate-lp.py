"""
COSC364 - Internet Technology and Engineering
Flynn Doherty (frd15), 17391809
Nick Walton (njw125), 51304961
"""


import sys


# ------------ CONSTANTS ---------------------------------------------------

N = 2  # Number of different paths
VOLUME =  lambda x, z: (2 * x + z)

# ==========================================================================



# ------------ HEADER ------------------------------------------------------

def write_header(file_stream):
    """ """
    file_stream.write("Minimize\n")
    file_stream.write("  obj:  r\n")

# ==========================================================================



# ------------ CONSTRAINTS -------------------------------------------------

def write_contraints(file_stream, X, Y, Z):
    """ """
    file_stream.write("\nSubject To\n")
    write_demand_flow(file_stream, X, Y, Z)
    write_source_constraints(file_stream, X, Y, Z)
    write_transit_constraints(file_stream, X, Y, Z)
    write_destination_constraints(file_stream, X, Y, Z)
    write_demand_volume_constraints(file_stream, X, Y, Z)
    write_util_constraints(file_stream, X, Y, Z)


def write_demand_flow(file_stream, X, Y, Z):
    """ Demand flow"""
    for x in range(1, X):
        for y in range(1, Y):
            for z in range(1, Z):
                route = "{}{}{}".format(x, y, z)
                file_stream.write("  demflow{}:  {} x{} - {} bin{} = 0\n".format(route, N, route, VOLUME(x,z), route))    


def write_source_constraints(file_stream, X, Y, Z):
    """ Source capacity """
    for x in range(1, X):
        for y in range(1, Y):
            route = "{}{}".format(x, y)
            file_stream.write("  srccap{}:   ".format(route))
            for z in range(1, Z):
                file_stream.write(" x{}".format(route+str(z)))
                if (z != Z-1):
                    file_stream.write(" +")                 
            file_stream.write(" - c{} <= 0".format(route))    
            file_stream.write("\n")


def write_transit_constraints(file_stream, X, Y, Z):
    """ Transit load """
    for y in range(1, Y):
        file_stream.write("  transload{}:  ".format(y))    
        for x in range(1, X):
            route = "x{}{}".format(x, y)
            for z in range(1, Z):                 
                file_stream.write("{}".format(route+str(z)))
                if (z != Z-1):
                    file_stream.write(" + ")        
            if (x != X-1):
                file_stream.write(" + ")    
        file_stream.write(" - r <= 0".format(route))    
        file_stream.write("\n")


def write_destination_constraints(file_stream, X, Y, Z):
    """ Destination capacity """
    for y in range(1, Y):
        for z in range(1, Z):
            route = "{}{}".format(y, z)
            file_stream.write("  destcap{}:  ".format(route))
            for x in range(1, X):
                file_stream.write(" x{}".format(str(x)+route))
                if (x != X-1):
                    file_stream.write(" +")                 
            file_stream.write(" - d{} <= 0".format(route))    
            file_stream.write("\n")


def write_demand_volume_constraints(file_stream, X, Y, Z):
    """ Demand volume """
    for x in range(1, X):
        for z in range(1, Z):
            file_stream.write("  dmndvol{}{}:  ".format(x, z))

            for y in range(1, Y):
                route = "{}{}{}".format(x, y, z)
                file_stream.write(" x{} ".format(route))
                if (y != Y-1):
                    file_stream.write("+")                 
            file_stream.write("= {}".format(VOLUME(x,z)))    
            file_stream.write("\n")


def write_util_constraints(file_stream, X, Y, Z):
    """ Utilisation """
    for x in range(1, X):
        for z in range(1, Z):
            file_stream.write("  util{}{}:     ".format(x, z))

            for y in range(1, Y):
                route = "{}{}{}".format(x, y, z)
                file_stream.write(" bin{} ".format(route))
                if (y != Y-1):
                    file_stream.write("+")                 
            file_stream.write("= {}".format(N))    
            file_stream.write("\n")

# ==========================================================================



# ------------ BOUNDS ------------------------------------------------------

def write_bounds(file_stream, X, Y, Z):
    file_stream.write("\nBounds\n")
    write_all_routes(file_stream, X, Y, Z)
    write_source_transit_routes(file_stream, X, Y, Z)
    write_transit_destination_routes(file_stream, X, Y, Z)
    file_stream.write("  r    >= 0\n")


def write_all_routes(file_stream, X, Y, Z):
    for x in range(1, X):
        for y in range(1, Y):
            for z in range(1, Z):
                file_stream.write("  x{}{}{} >= 0\n".format(x, y, z))


def write_source_transit_routes(file_stream, X, Y, Z):
    for x in range(1, X):
        for y in range(1, Y):
            file_stream.write("  c{}{}  >= 0\n".format(x, y))


def write_transit_destination_routes(file_stream, X, Y, Z):
    for y in range(1, Y):
        for z in range(1, Z):
            file_stream.write("  d{}{}  >= 0\n".format(y, z))

# ==========================================================================



# ------------ BINARIES ----------------------------------------------------

def write_binaries(file_stream, X, Y, Z):
    """ Writes the binaries to the file"""
    file_stream.write("\nBinaries\n")

    for x in range(1, X):
        for y in range(1, Y):
            for z in range(1, Z):
                file_stream.write("  bin{}{}{}".format(x,y,z))
            file_stream.write("\n")

def write_exit(file_stream):
    """ Dumps exit to the file. """
    file_stream.write("\nEnd\n")

# ==========================================================================



# ------------ EXECUTE -----------------------------------------------------

def write_lp(file_stream, X, Y, Z):
    """ Backbone of the application. """
    X += 1
    Y += 1
    Z += 1

    write_header(file_stream)
    write_contraints(file_stream, X, Y, Z)
    write_bounds(file_stream, X, Y, Z)
    write_binaries(file_stream, X, Y, Z)
    write_exit(file_stream)
    
def main():
    """ Iterates through a given range (3-8) for Y. """
    X = 9
    Z = 9
    for Y in range(3,9):        
        output_filename = "tests/test-{}.lp".format(Y)    
        file_stream = open(output_filename, "w+")
        write_lp(file_stream, X, Y, Z)
        file_stream.close()

# ==========================================================================


if (__name__ == "__main__"):
    main()

