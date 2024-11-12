from qiskit import QuantumCircuit
import numpy as np


def random_clifford_gate():
    idx = np.random.randint(0, 24)
    clifford_gate = QuantumCircuit(1)
    if idx == 0:
        clifford_gate.id(0)                      # Identity
    elif idx == 1:
        clifford_gate.x(0)                      # X
    elif idx == 2:
        clifford_gate.y(0)                      # Y
    elif idx == 3:
        clifford_gate.z(0)                      # Z
    elif idx == 4:
        clifford_gate.h(0)                      # H
    elif idx == 5:
        clifford_gate.s(0)                      # S
    elif idx == 6:
        clifford_gate.sdg(0)                    # S†
    elif idx == 7:
        clifford_gate.h(0)
        clifford_gate.s(0)                      # HS
    elif idx == 8:
        clifford_gate.h(0)
        clifford_gate.sdg(0)                    # HS†
    elif idx == 9:
        clifford_gate.s(0)
        clifford_gate.h(0)                      # SH
    elif idx == 10:
        clifford_gate.sdg(0)
        clifford_gate.h(0)                      # S†H
    elif idx == 11:
        clifford_gate.s(0)
        clifford_gate.x(0)                      # SX
    elif idx == 12:
        clifford_gate.s(0)
        clifford_gate.y(0)                      # SY
    elif idx == 13:
        clifford_gate.s(0)
        clifford_gate.z(0)                      # SZ
    elif idx == 14:
        clifford_gate.sdg(0)
        clifford_gate.x(0)                      # S†X
    elif idx == 15:
        clifford_gate.sdg(0)
        clifford_gate.y(0)                      # S†Y
    elif idx == 16:
        clifford_gate.sdg(0)
        clifford_gate.z(0)                      # S†Z
    elif idx == 17:
        clifford_gate.h(0)
        clifford_gate.s(0)
        clifford_gate.x(0)                      # HSX
    elif idx == 18:
        clifford_gate.h(0)
        clifford_gate.sdg(0)
        clifford_gate.x(0)                      # HS†X
    elif idx == 19:
        clifford_gate.h(0)
        clifford_gate.s(0)
        clifford_gate.y(0)                      # HSY
    elif idx == 20:
        clifford_gate.h(0)
        clifford_gate.sdg(0)
        clifford_gate.y(0)                      # HS†Y
    elif idx == 21:
        clifford_gate.h(0)
        clifford_gate.s(0)
        clifford_gate.z(0)                      # HSZ
    elif idx == 22:
        clifford_gate.h(0)
        clifford_gate.sdg(0)
        clifford_gate.z(0)                      # HS†Z
    elif idx == 23:
        clifford_gate.h(0)
        clifford_gate.y(0)        
    return clifford_gate



def add_random_clifford(circuit: QuantumCircuit): 
    Gate = []
    for qubits in range(circuit.num_qubits): # add a random Clifford gates to each qubit
        clifford_gate = random_clifford_gate()
        Gate.append(clifford_gate)
        circuit = circuit.compose(clifford_gate, [qubits])
    return Gate, circuit # return the list of added gates and the updated circuit
