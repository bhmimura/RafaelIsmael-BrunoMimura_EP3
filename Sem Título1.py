from scipy import *
from numpy import *
from matplotlib.pyplot import *
from scipy.integrate import odeint

T = list(range(1000))

Tq0 = 50

Tamb = -10
Tcpu = 90
Q0 =834.5
Lp = 0.3
Kp = 0.17
Ap = 24
Hp = 500

V = 3.89
hh = 10.45-V+10*V**0.5
Kh = 50000
Ah = 1
Ac = 0.04
Lh = 0.15

def func1 (Tq, t):
    dTdt = -(((Tq-Tamb)/((Lp/(Kp*Ap)+(1/(Hp*Ap)*16.69)))))
    return dTdt 


Y = odeint (func1, Tq0, T)

plot (T, Y)
show ()