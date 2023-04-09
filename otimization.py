"""solving optimization problem using python"""

# importing the necessary python libraries(scipy)
import scipy
from scipy import optimize
from scipy.optimize import linprog

"""Next is we define the necessary Z values known as the objective function
NOTE: since we are maximizing, the values of the objective constraint will become negative"""
cost_variableZ = [-4,-5,-9,-11]

"""Now, we put the constraints function in form of arrays of matrices using 'tuples' and 
seperating each one by a comma(,)""" 
constraints = [(1,1,1,1,), (7,5,3,2), (3, 5, 10, 15)]

"""Lastly, we define our variable 'rhs_constraints' which is the right hand side of our constaint
functions and seperate the value for each constraint function by a comma """
rhs_contraints = [15,120,100]

# solving for the optimal solution using our imported librarie and package
optimal_solution = scipy.optimize,linprog(cost_variableZ,constraints,rhs_contraints, 
                                          method = "highs")

# Printing the optimal solution
print(f"The optimal solution is {optimal_solution}")