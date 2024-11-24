import numpy as np
from qiskit.circuit.library import UnitaryGate


def random_clifford_gate(idx=None):
    """return a (random or not clifford gate) from the 1 qubit clifford gate set. 
    if idx is None:
        return a random clifford gate from the 1 qubit clifford gate set.
    else:
        return a specific clifford gate from the 1 qubit clifford gate set.
    Args:
        idx (int, o<= idx <24): the index of the wanted clifford gate set. Defaults to None.

    Returns:
        UnitaryGate object
    """
    X = np.array([[0,1],  [1,0]])
    Y = np.array( [[0,-1j], [1j,0]])
    Z = np.array( [[1,0],  [0,-1]])
    I = np.array( [[1,0],  [0,1]])
    S=np.array([[1,0],  [0,1j]])
    H= np.array([[1/np.sqrt(2),1/np.sqrt(2)],  [1/np.sqrt(2),-1/np.sqrt(2)]])
    V=H@S@H@S
    W=V@V
    if idx==None:
        idx = np.random.randint(0,23)
    if idx>=24:
        print("idx out of range, idx need to be between 0 and 23")
    if idx == 0:
        return UnitaryGate(I)                    
    elif idx == 1:
         return UnitaryGate(X)                      
    elif idx == 2:
         return UnitaryGate(Y)                     
    elif idx == 3:
         return UnitaryGate(Z) 
    elif idx == 4:
        return UnitaryGate(V)                  
    elif idx == 5:
        return UnitaryGate(V@X)
    elif idx == 6:
        return UnitaryGate(V@Y)               
    elif idx == 7:
       return UnitaryGate(V@Z)
    elif idx == 8:
        return UnitaryGate(W@X)             
    elif idx == 9:
        return UnitaryGate(W@Y)             
    elif idx == 10:
        return UnitaryGate(W@Z)
    elif idx == 11:
        return UnitaryGate(H@X)
    elif idx == 12:
        return UnitaryGate(H@Y)
    elif idx == 13:
        return UnitaryGate(H@Z)                     
    elif idx == 14:
        return UnitaryGate(H)
    elif idx == 15:
        return UnitaryGate(H@V)                    
    elif idx == 16:
        return UnitaryGate(H@V@X)
    elif idx == 17:
        return UnitaryGate(H@V@Y)       
    elif idx == 18:
        return UnitaryGate(H@V@Z)            
    elif idx == 19:
        return UnitaryGate(H@W)     
    elif idx == 20:
        return UnitaryGate(H@W@X)             
    elif idx == 21:
        return UnitaryGate(H@W@Y)                     
    elif idx == 22:
        return UnitaryGate(H@W@Z)                
    elif idx == 23:
        return UnitaryGate(W)     



def add_random_clifford(circuit):
    clifford_gate=[]
    for qubits in range(circuit.num_qubits):
        clifford_gate.append(random_clifford_gate())
        circuit.append(clifford_gate[-1],[qubits])
    circuit.measure_all()
    return clifford_gate, circuit