import sys

file_stream = open(sys.argv[1], 'r')
line = file_stream.readline()

def process_cplex(line):
    """ 
        Takes in a cplex output file and parses it. 
        Returns demand flows, and various capacity metrics. 
    """
    all_demand_flows = []
    max_capacity = 0
    nonzero_capacity = 0
    max_link = None

    while (line != ''):
        if line.startswith("Total"):
            processing_time = line
            print("Processing time: {}".format(processing_time))

        elif line.startswith('r'):
            r = line.strip('\n').split(' ')[-1]

        elif line.startswith('x'):
            line = line.strip('\n').split(' ')
            all_demand_flows.append((line[0], float(line[-1])))

        elif (line.startswith('c') or line.startswith('d')):
            capacity = float(line.strip('\n').split(' ')[-1])
            if(capacity > max_capacity):
                max_capacity = capacity
                max_link = str(line.strip('\n').split(' ')[0])
            nonzero_capacity += 1

        line = file_stream.readline()

    return all_demand_flows, nonzero_capacity, max_link, max_capacity


def determine_transit_loads(all_demand_flows):
    """ Iterates through all demand flows and returns the transit loads. """
    transit_loads = {}

    for demand_flow in all_demand_flows:
        flow = demand_flow[1]
        transit_node = demand_flow[0][2]
            
        load = transit_loads.get(transit_node)
        if (load != None):
            load += flow
            transit_loads.update({transit_node:load})
        else:
            transit_loads.update({transit_node:flow})

    return transit_loads


def determine_max_min(transit_loads):
    """ Iterates through all transit loads and determines the spread. """
    max_load = None
    min_load = None

    for load in sorted(transit_loads.keys()):
        print("{}: {}".format(load, transit_loads.get(load)))

        if(max_load == None or transit_loads.get(load) > max_load):
            max_load = transit_loads.get(load)

        if(min_load == None or transit_loads.get(load) < min_load):
            min_load = transit_loads.get(load)

    return max_load - min_load


def print_metrics(nonzero_capacity, max_link, max_capacity, spread):
    """ Outputs various metrics to the console. """
    print("Spread value: {}".format(spread))
    print("Non-zero capacity links: {}".format(nonzero_capacity))
    print("Max capacity link: Link {}: {}".format(max_link, max_capacity))


def main():
    """ Backbone of the application. """
    all_demand_flows, nonzero_capacity, max_link, max_capacity = process_cplex(line)
    transit_loads = determine_transit_loads(all_demand_flows)
    spread = determine_max_min(transit_loads)
    print_metrics(nonzero_capacity, max_link, max_capacity, spread)


if (__name__ == "__main__"):
    main()
