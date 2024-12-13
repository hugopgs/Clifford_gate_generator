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
        gates = [I, X, Y, Z, V, V @ X, V @ Y, V @ Z, W @ X, W @ Y, W @ Z,
                H @ X, H @ Y, H @ Z, H, H @ V, H @ V @ X, H @ V @ Y, H @ V @ Z,
                H @ W, H @ W @ X, H @ W @ Y, H @ W @ Z, W]

        if idx is None:
            idx = np.random.randint(0, len(gates))
        elif idx < 0 or idx >= len(gates):
            raise ValueError("Index out of range. Must be between 0 and 23.")

        return UnitaryGate(gates[idx])


def add_random_clifford(self, circuit: QuantumCircuit) -> tuple[list[UnitaryGate], QuantumCircuit]:
    """
    Add random Clifford gates to each qubit of a given circuit and append measurement operations.

    Args:
        circuit (QuantumCircuit): Circuit to which Clifford gates are added.

    Returns:
        tuple[list[UnitaryGate], QuantumCircuit]:
            List of Clifford gates applied to the circuit and the updated circuit.
    """
    clifford_gates = []
    for qubit in range(self.nq):
        gate = self.random_clifford_gate()
        clifford_gates.append(gate)
        circuit.append(gate, [qubit])
    circuit.measure_all()
    return clifford_gates, circuit
