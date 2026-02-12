"""
Note class compatible with Note.js.

hash = Poseidon(owner0, owner1, value, token, vk0, vk1, salt)

Regular notes: owner0=pkX, owner1=pkY, vk0=pkX, vk1=pkY
"""

import os
from .poseidon import poseidon


def _to_int(v):
    """Convert hex string, int, or other to int."""
    if isinstance(v, int):
        return v
    if isinstance(v, str):
        if not v or v == '0x0' or v == '0x00':
            return 0
        return int(v, 16) if v.startswith('0x') else int(v)
    return 0


def _pad_hex(v, length=64):
    """Convert int to 0x-prefixed zero-padded hex string."""
    return '0x' + format(v, '0%dx' % length)


class Note:
    """
    ZK-DEX Note with 7-input Poseidon hash.

    Fields (all stored as int):
        owner0, owner1: Owner identification (regular: pk.x, pk.y)
        value: Note amount
        token: Token type
        vk0, vk1: Viewing key (regular: pk.x, pk.y)
        salt: Random salt
    """

    def __init__(self, owner0, owner1, value, token, vk0, vk1, salt):
        self.owner0 = _to_int(owner0)
        self.owner1 = _to_int(owner1)
        self.value = _to_int(value)
        self.token = _to_int(token)
        self.vk0 = _to_int(vk0)
        self.vk1 = _to_int(vk1)
        self.salt = _to_int(salt)

    def hash(self):
        """
        Compute 7-input Poseidon hash.

        Returns:
            str: 0x-prefixed 64-char hex string
        """
        h = poseidon([
            self.owner0, self.owner1, self.value,
            self.token, self.vk0, self.vk1, self.salt
        ])
        return '0x' + format(h, '064x')

    def hash_int(self):
        """Compute Poseidon hash as integer."""
        return poseidon([
            self.owner0, self.owner1, self.value,
            self.token, self.vk0, self.vk1, self.salt
        ])

    def to_dict(self):
        """Serialize note fields to dict with hex strings."""
        return {
            'owner0': _pad_hex(self.owner0),
            'owner1': _pad_hex(self.owner1),
            'value': _pad_hex(self.value),
            'token': _pad_hex(self.token),
            'vk0': _pad_hex(self.vk0),
            'vk1': _pad_hex(self.vk1),
            'salt': _pad_hex(self.salt),
        }

    @staticmethod
    def from_public_key(pk_x, pk_y, value, token, salt=None):
        """
        Create a regular note from a public key.
        owner0=pk.x, owner1=pk.y, vk0=pk.x, vk1=pk.y

        Args:
            pk_x: public key x (int or hex str)
            pk_y: public key y (int or hex str)
            value: note value (int or hex str)
            token: token type (int or hex str)
            salt: random salt (int or hex str, auto-generated if None)

        Returns:
            Note
        """
        if salt is None:
            salt = int.from_bytes(os.urandom(32), 'big')
        pk_x = _to_int(pk_x)
        pk_y = _to_int(pk_y)
        return Note(pk_x, pk_y, _to_int(value), _to_int(token), pk_x, pk_y, _to_int(salt))


EMPTY_NOTE = Note(0, 0, 0, 0, 0, 0, 0)
