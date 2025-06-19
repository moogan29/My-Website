# ---------------------------------------------- LIBRARY IMPORT 1--------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from qutip import *

# ---------------------------------------------- QUANTUM STATES 1--------------------------------------------------------------

# |0> and |1>
Init0 = basis(2, 0)
Init1 = basis(2, 1)

#  | i > and | -i >
i_state = (Init0 + 1j * Init1).unit()
neg_i_state= (Init0 - 1j * Init1).unit()

#  | + > and | -- >
plus_state = (Init0 +  Init1).unit()
neg_state = (Init0 - Init1).unit()

# ---------------------------------------------- RABI + TIME VALUES 1 ---------------------------------------------------------------

Ω =  np.pi

Tlist = np.linspace(1, 5, 500)

# ---------------------------------------------- RABI + TIME VALUES 1 ---------------------------------------------------------------

HX = Ω * sigmax() 
HZ = Ω * sigmaz()  
HY = Ω * sigmay()  

# Define observable: projection onto excited state |1>
Excited_Proj_neg_state  = neg_state * neg_state.dag()



QuantumState_List = [Init0, Init1,i_state,neg_i_state,plus_state,neg_state]
QuantumState_List_name  = ["|0⟩", "|1⟩","|i⟩","|-i⟩","|+⟩","|-⟩"]
Hamiltonians = [HX,HY,HZ]
Hamiltonians_names = ['Pauli-X','Pauli-Y','Pauli-Z']

for U in range (0, len(Hamiltonians)):

    for i in range (0,len(QuantumState_List)):
        
        # Time evolution
        result = mesolve(Hamiltonians[U], QuantumState_List[i],Tlist, [], [Excited_Proj_neg_state])

        # Plotting the probability of being in state |1>

        plt.figure(figsize=(8, 4))
        plt.gcf().canvas.manager.set_window_title(QuantumState_List_name[i])
        plt.plot(Tlist, result.expect[0], label=QuantumState_List_name[i])
        plt.xlabel('Time')
        plt.ylabel('Excited State Probability')
        plt.title('Rabi Oscillations under '+str(Hamiltonians_names[U])+' Hamiltonian')
        plt.grid(True)
        plt.legend()

plt.show()
