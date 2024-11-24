# Clifford Gate Generator: 
The Clifford group encompasses a set of quantum operations that map the set of n-fold Pauli group products into itself. It is most famously studied for its use in quantum error correction. https://en.wikipedia.org/wiki/Clifford_group.
Requested librairie to run the function: 
- Numpy 
- Qiskit

# 1 Qubit Clifford Gates

The 1 qubit set of Clifford gates is composed of the following gates:

### Identity:
$$
I = \begin{pmatrix} 1 & 0 \\\\ 0 & 1 \end{pmatrix}
$$

### Gate $X$:
$$
X = \begin{pmatrix} 0 & 1 \\\\ 1 & 0 \end{pmatrix}
$$

### Gate $Y$:
$$
Y = \begin{pmatrix} 0 & -i \\\\ i & 0 \end{pmatrix}
$$

### Gate $Z$:
$$
Z = \begin{pmatrix} 1 & 0 \\\\0 & -1 \end{pmatrix}
$$

### Hadamard Gate:
$$
H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\\\ 1 & -1 \end{pmatrix}
$$

### Gate $S$:
$$
S = \begin{pmatrix} 1 & 0 \\\\ 0 & i \end{pmatrix}
$$

### Gate $V$:
$$
V = H S H S = \frac{1}{2} \begin{pmatrix} 1 + i & 1 + i \\\\ 1 - i & -1 + i \end{pmatrix}
$$

### Gate $W$:
$$
W = V V
$$

## Combinations of the gates:

$$
\{ 
V, \\
V X, \\
V Y, \\
V Z, \\
W X, \\
W Y, \\
W Z, \\
H X, \\
H Y, \\
H Z, \\
H, \\
H V, \\
H V X, \\
H V Y, \\
H V Z, \\
H W, \\
H W X, \\
H W Y, \\
H W Z, \\
W
\}
$$
