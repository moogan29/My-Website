# ---------------------------------------------- LIBRARY IMPORT 1--------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from qutip import *

# ---------------------------------------------- RABI + TIME VALUES 1 ---------------------------------------------------------------

Ω =  np.pi

tlist = np.linspace(1, 5, 500)

# ---------------------------------------------- RABI + TIME VALUES 1 ---------------------------------------------------------------

HX = Ω * sigmax() 
HZ = Ω * sigmaz()  
HY = Ω * sigmay()

# ---------------------------------------------- QUANTUM STATES 1--------------------------------------------------------------

# |0> and |1>
Init0 = basis(2, 0)
Init1 = basis(2, 1)

#  | i > and | -i >
i_state = (Init0 + 1j * Init1).unit()
neg_i_state= (Init0 - 1j * Init1).unit()

#  | + > and | -- >
plus_state = (Init0 +  Init1).unit()
neg_state= (Init0 - Init1).unit()

# ---------------------------  MESOLVE  --------------------------------

QuantumState_List = [Init0, Init1,i_state,neg_i_state,plus_state,neg_state]
QuantumState_List_name  = ["|0⟩", "|1⟩","|i⟩","|-i⟩","|+⟩","|-⟩"]

for i in range (0,len(QuantumState_List)):
    

    HX_evolution = mesolve(HZ, QuantumState_List[i], tlist)


    HX_x_vals = [expect(sigmax(), state) for state in HX_evolution.states]
    HX_y_vals = [expect(sigmay(), state) for state in HX_evolution.states]
    HX_z_vals = [expect(sigmaz(), state) for state in HX_evolution.states]

    # Create Bloch sphere object

    # X rotation
    b_x = Bloch()
    b_x.point_color = ['r']
    b_x.add_points([HX_x_vals, HX_y_vals, HX_z_vals])
    b_x.title = ['X-axis Rabi Rotation']
    b_x.show()

    # Set the window (figure) title
    fig = b_x.fig
    fig.canvas.manager.set_window_title(QuantumState_List_name[i])

