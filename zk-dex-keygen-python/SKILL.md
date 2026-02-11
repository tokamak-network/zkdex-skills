# SKILL.md - zk-dex-keygen-python

## Description

This skill is a Python-based `zk-dex-keygen` module. To resolve type issues with the `@noble/curves` library, it is based on the Python implementation from the `barryWhiteHat/baby_jubjub_ecc` repository. It generates key pairs for zk-Dex applications using the `BabyJubJub` curve and exports them in the zkdex keystore JSON format.

## Dependencies

- `sapling_jubjub.py` file (imported from the original `baby_jubjub_ecc` repository)
- `cryptography` Python package (for AES-256-GCM encryption)
- Python 3.x

## Usage

```bash
python generate_keypair.py --password <password>
# or
python generate_keypair.py -p <password>
```

The `--password` (`-p`) argument is required and specifies the password used to encrypt the private key in the keystore.

## Output Format

The script outputs a JSON object to stdout:

```json
{
  "address": "352642512be6419630d0fbf6a42e510f85030587",
  "publicKey": {
    "x": "0x...",
    "y": "0x..."
  },
  "keystore": {
    "crypto": {
      "cipher": "aes-256-gcm",
      "ciphertext": "...",
      "cipherparams": { "iv": "..." },
      "kdf": "scrypt",
      "kdfparams": { "n": 16384, "r": 8, "p": 1, "dklen": 32, "salt": "..." },
      "mac": "..."
    },
    "version": 1
  },
  "exportedAt": 1770846855188
}
```

- **address**: Last 20 bytes of `sha256(pk.x || pk.y)` (40 hex chars)
- **publicKey**: BabyJubJub public key coordinates with `0x` prefix (64 hex chars each)
- **keystore**: Private key encrypted with scrypt KDF + AES-256-GCM
- **exportedAt**: Millisecond timestamp

## Structure

- `generate_keypair.py`: Main script containing key pair generation and keystore export logic.
- `sapling_jubjub.py`: File defining field and point operations for the `BabyJubJub` curve.

## Note

This skill was developed as an alternative to the existing `zk-dex-keygen` module based on `@noble/curves`. By using a more stable and verified Python implementation, it ensures reliable key generation without WASM dependencies.