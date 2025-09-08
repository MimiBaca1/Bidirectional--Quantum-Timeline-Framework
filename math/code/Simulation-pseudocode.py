import numpy as np

# Constants
hbar = 1.0545718e-34  # Planck constant (J·s)

# Time evolution operators (simplified)
def forward_wavefunction(H, psi_0, t):
    return np.exp(-1j * H * t / hbar) @ psi_0

def backward_wavefunction(H, psi_0, t):
    return np.exp(1j * H * t / hbar) @ psi_0

# Bidirectional observable expectation
def bidirectional_expectation(O, psi_t, psi_minus_t):
    return 0.5 * (psi_t.conj().T @ O @ psi_t + psi_minus_t.conj().T @ O @ psi_minus_t)

# Bidirectional entanglement entropy
def bidirectional_entropy(rho_t, rho_minus_t):
    def entropy(rho):
        return -np.trace(rho @ np.log(rho + 1e-12))  # Avoid log(0)
    return 0.5 * (entropy(rho_t) + entropy(rho_minus_t))

# Fibonacci time sampling
def fibonacci_times(t0, delta_t, N):
    F = [0, 1]
    for i in range(2, N):
        F.append(F[-1] + F[-2])
    return [t0 + f * delta_t for f in F], [t0 - f * delta_t for f in F]
