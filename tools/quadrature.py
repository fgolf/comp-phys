import numpy as np

## approximate integral using midpoint rule
## the argument f is the function to be integrated
## following function the user should provide either:
##   - 3 arguments a,b,N where a = interval start, b = interval end, N is number of subintervals
##   - 1 argument x, a numpy array specifying the subintervals
def midpoint(f,*args):
    if len(args) == 3:
        x = np.linspace(args[0],args[1],args[2]+1)
    elif len(args) == 1:
        x = np.array(args[0])
    midx = 0.5*(x[:-1]+x[1:])
    widthx = x[1:]-x[:-1]
    return np.sum(widthx*f(midx))

## approximate integral using trapezoid rule
## the argument f is the function to be integrated
## following function the user should provide either:
##   - 3 arguments a,b,N where a = interval start, b = interval end, N is number of subintervals
##   - 1 argument x, a numpy array specifying the subintervals
def trapezoid(f,*args):
    if len(args) == 3:
        x = np.linspace(args[0],args[1],args[2]+1)
    elif len(args) == 1:
        x = np.array(args[0])
    widthx = x[1:]-x[:-1]
    return np.sum(0.5*widthx*(f(x[:-1])+f(x[1:])))

## approximate integral using Simpson's rule
## the argument f is the function to be integrated
## following function the user should provide either:
##   - 3 arguments a,b,N where a = interval start, b = interval end, N is number of subintervals
##   - 1 argument x, a numpy array specifying the subintervals
def simpson(f,*args):
    if len(args) == 3:
        x = np.linspace(args[0],args[1],args[2]+1)
    elif len(args) == 1:
        x = np.array(args[0])
    midx = 0.5*(x[:-1]+x[1:])
    widthx = x[1:]-x[:-1]
    return np.sum((widthx/6.)*(f(x[:-1])+4*f(midx)+f(x[1:]))) 
