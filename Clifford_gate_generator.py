import numpy as np
from qiskit.circuit.library import UnitaryGate
from qiskit import QuantumCircuit

def random_clifford_gate(self, idx:int=None )-> UnitaryGate:
        """return either a random clifford gate or a choosen clifford gate depending on the value of idx.
            idx=0: return UnitaryGate(I)
            idx=1: return UnitaryGate(X)
            idx=2: return UnitaryGate(Y)
            idx=3: return UnitaryGate(Z)
            idx=4: return UnitaryGate(V)
            idx=5: return UnitaryGate(V@X)
            idx=6: return UnitaryGate(V@Y)
            idx=7: return UnitaryGate(V@Z)
            idx=8: return UnitaryGate(W@X)
            idx=9: return UnitaryGate(W@Y)
            idx=10: return UnitaryGate(W@Z)
            idx=11: return UnitaryGate(H@X)
            idx=12: return UnitaryGate(H@Y)
            idx=13: return UnitaryGate(H@Z)
            idx=14: return UnitaryGate(H)
            idx=15: return UnitaryGate(H@V)
            idx=16: return UnitaryGate(H@V@X)
            idx=17: return UnitaryGate(H@V@Y)
            idx=18: return UnitaryGate(H@V@Z)
            idx=19: return UnitaryGate(H@W)
            idx=20: return UnitaryGate(H@W@X)
            idx=21: return UnitaryGate(H@W@Y)
            idx=22: return UnitaryGate(H@W@Z)
            idx=23: return UnitaryGate(W)
            idx= None: return randomly one of the previous Unitary gate 
        Args:
            idx (int, optional): index of the wanted clifford gate. if None return a random clifford gate. Defaults to None.
    
        Returns:
            UnitaryGate: Clifford Unitary gate object
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
        if idx>=24 or idx<0:
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

def add_random_clifford(self, circuit: QuantumCircuit)->tuple[list[UnitaryGate], QuantumCircuit]:
    """Add a random clifford gate for each qubits in a given circuit. add a "measure_all()" instruction after adding the clifford gates.

    Args:
        circuit (QuantumCircuit): circuit to add clifford gates

    Returns:
        tuple[list[UnitaryGate], QuantumCircuit]: the list of clifford gates applied to the circuit and the new circuit with the gate added
    """
    clifford_gate=[]
    for qubits in range(circuit.num_qubits):
        clifford_gate.append(self.random_clifford_gate())
        circuit.append(clifford_gate[-1],[qubits])
    circuit.measure_all()
    return clifford_gate, circuit