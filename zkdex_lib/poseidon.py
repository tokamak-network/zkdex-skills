"""
circomlibjs-compatible Poseidon hash implementation.

Direct port of circomlibjs/src/poseidon_reference.js.
Uses pre-extracted C (round constants) and M (MDS matrix) from circomlibjs.

Supports t=3 (2 inputs) and t=8 (7 inputs).
"""

from .poseidon_constants import C, M

MODULUS = 21888242871839275222246405745257275088548364400416034343698204186575808495617

N_ROUNDS_F = 8
N_ROUNDS_P = [56, 57, 56, 60, 60, 63, 64, 63, 60, 66, 60, 65, 70, 60, 64, 68]


def _pow5(x):
    x2 = (x * x) % MODULUS
    x4 = (x2 * x2) % MODULUS
    return (x4 * x) % MODULUS


def poseidon(inputs):
    """
    Compute circomlibjs-compatible Poseidon hash.

    Args:
        inputs: list of integers (1 to 16 elements)

    Returns:
        int: hash value in BN128 field
    """
    assert 0 < len(inputs) <= len(N_ROUNDS_P)

    t = len(inputs) + 1
    n_rounds_f = N_ROUNDS_F
    n_rounds_p = N_ROUNDS_P[t - 2]

    if t not in C or t not in M:
        raise ValueError(f"Poseidon constants not available for t={t}. Supported: {list(C.keys())}")

    c = C[t]
    m = M[t]

    state = [0] + [x % MODULUS for x in inputs]

    for r in range(n_rounds_f + n_rounds_p):
        # AddRoundConstants
        state = [(state[i] + c[r * t + i]) % MODULUS for i in range(t)]

        # S-box (pow5)
        if r < n_rounds_f // 2 or r >= n_rounds_f // 2 + n_rounds_p:
            # Full round
            state = [_pow5(x) for x in state]
        else:
            # Partial round
            state[0] = _pow5(state[0])

        # MDS mix
        new_state = []
        for i in range(t):
            acc = 0
            for j in range(t):
                acc = (acc + m[i][j] * state[j]) % MODULUS
            new_state.append(acc)
        state = new_state

    return state[0]


def poseidon_hex(inputs):
    """
    Compute Poseidon hash and return as 0x-prefixed hex string.

    Args:
        inputs: list of integers

    Returns:
        str: 0x-prefixed 64-char hex string
    """
    h = poseidon(inputs)
    return '0x' + format(h, '064x')
