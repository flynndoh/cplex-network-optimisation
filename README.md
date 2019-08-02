# Basic Breakdown

To run ```generate-lp.py``` simply perform: ```python3 generate-lp.py```

This will iterate through Y values on the range 3-8, and X = 9 and Z = 9. When the process is complete, all output will be stored in the ```tests``` folder, labeled test 3 through 8.

To run CPLEX on any test output, simply perform: ``` cplex -c "read test-Y.lp" "optimize" "display solution variables -" > result-Y.txt```

To run analysis, navigate to results and perform: ``` python3 output-values.py < result-Y.txt```