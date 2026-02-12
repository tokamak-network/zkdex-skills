"""
BabyJubJub account utilities compatible with circomlibBabyJub.js.

- derive_public_key(sk) -> (x, y) using Base8 scalar multiplication
- derive_address(pk_x, pk_y) -> 160-bit Poseidon-based address
- Account class combining sk, pk, address
"""

import os
import sys

# Import sapling_jubjub from zk-dex-keygen-python (sibling directory)
_keygen_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'zk-dex-keygen-python')
if _keygen_dir not in sys.path:
    sys.path.insert(0, _keygen_dir)

from sapling_jubjub import Point, Fq, Fr, r_j

from .poseidon import poseidon

# BabyJubJub Base8 generator point (same as circomlibjs)
BASE_POINT = Point(
    Fq(5299619240641551281634865583518297030282874472190772894086521144482721001553),
    Fq(16950150798460657717958625567821834550301663161624707787222815936182638968203)
)

MASK_160 = (1 << 160) - 1


def derive_public_key(sk_int):
    """
    Derive BabyJubJub public key from secret key.

    Args:
        sk_int: secret key as int

    Returns:
        tuple: (pk_x: int, pk_y: int)
    """
    sk = Fr(sk_int % r_j)
    pk = BASE_POINT * sk
    return (pk.u.s, pk.v.s)


def derive_address(pk_x, pk_y):
    """
    Derive 160-bit address from public key using Poseidon hash.
    address = truncate_to_160_bits(Poseidon(pk.x, pk.y))

    Args:
        pk_x: public key x coordinate (int)
        pk_y: public key y coordinate (int)

    Returns:
        str: 40 hex chars (no 0x prefix)
    """
    h = poseidon([pk_x, pk_y])
    addr = h & MASK_160
    return format(addr, '040x')


class Account:
    """
    BabyJubJub account with secret key, public key, and Poseidon-based address.
    Compatible with circomlibBabyJub.js Account.
    """

    def __init__(self, sk_int):
        """
        Args:
            sk_int: secret key as int or hex string
        """
        if isinstance(sk_int, str):
            sk_int = int(sk_int, 16) if sk_int.startswith('0x') else int(sk_int)
        self.sk = sk_int
        self.pk_x, self.pk_y = derive_public_key(sk_int)
        self.address = derive_address(self.pk_x, self.pk_y)

    @staticmethod
    def generate():
        """Generate a new random account."""
        seed = os.urandom(32)
        sk_int = int.from_bytes(seed, 'little') % r_j
        return Account(sk_int)

    @property
    def pk_x_hex(self):
        return '0x' + format(self.pk_x, '064x')

    @property
    def pk_y_hex(self):
        return '0x' + format(self.pk_y, '064x')

    @property
    def sk_hex(self):
        return '0x' + format(self.sk, '064x')
