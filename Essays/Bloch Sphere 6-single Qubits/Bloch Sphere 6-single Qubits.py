import numpy as np
import matplotlib.pyplot as plt
from qutip import *

# System parameters
Ω =  np.pi   # Rabi frequency in radians per unit time ( 1 pi )


Tlist = np.linspace(0, 5, 500)  # Time points


# Define two-level system operators (pauli x y and z )
HX = Ω * sigmax()  # Driving Hamiltonian: H = (Ω) * σx

HZ = Ω * sigmaz()  # Driving Hamiltonian: H = (Ω) * σz

HY = Ω * sigmay()  # Driving Hamiltonian: H = (Ω) * σy


# ---------------------------------------------- creating the standard states ---------------------------------------------------------------

# |0> and |1>
Init0 = basis(2, 0)
Init1 = basis(2, 1)

#  | i > and | -i >
i_state = (Init0 + 1j * Init1).unit()
neg_i_state= (Init0 - 1j * Init1).unit()

#  | + > and | -- >
plus_state = (Init0 +  Init1).unit()
neg_state= (Init0 - Init1).unit()


print(Init0, Init1, i_state, neg_i_state)

# Solve time evolution (we don’t need observables here)

QuantumState_List = [Init0, Init1,i_state,neg_i_state,plus_state,neg_state]
QuantumState_List_name  = ["|0⟩", "|1⟩","|i⟩","|-i⟩","|+⟩","|-⟩"]

for i in range (0,len(QuantumState_List)):
    
    HX_evolution = mesolve(HX,QuantumState_List[i],Tlist,[],[sigmax()])
    HY_evolution = mesolve(HY,QuantumState_List[i],Tlist,[],[sigmay()])
    HZ_evolution = mesolve(HZ,QuantumState_List[i],Tlist,[],[sigmaz()])

    print(HX_evolution)
    x_vals = HX_evolution.expect[0]
    y_vals = HY_evolution.expect[0]
    z_vals = HZ_evolution.expect[0]

    # X rotation
    b_x = Bloch()
    b_x.point_color = ['r']

    b_x.add_points([HX_evolution.expect[0][0], HY_evolution.expect[0][0],HZ_evolution.expect[0][0]])
    
    
    b_x.title = ['X-axis Rabi Rotation']
    b_x.show()

    # Set the window (figure) title
    fig = b_x.fig
    fig.canvas.manager.set_window_title(QuantumState_List_name[i])










