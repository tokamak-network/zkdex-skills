# SKILL.md - zk-dex-keygen-python

## Description

This skill is a Python-based `zk-dex-keygen` module. To resolve type issues with the `@noble/curves` library, it is based on the Python implementation from the `barryWhiteHat/baby_jubjub_ecc` repository. It generates key pairs for zk-Dex applications using the `BabyJubJub` curve.

## Dependencies

- `sapling_jubjub.py` file (imported from the original `baby_jubjub_ecc` repository)
- Python 3.x

## Usage

1. Run the `generate_keypair.py` script.
2. The `generate_keypair()` function returns a random secret key and its corresponding public key.

## Structure

- `generate_keypair.py`: Main script containing the key pair generation logic.
- `sapling_jubjub.py`: File defining field and point operations for the `BabyJubJub` curve.

## Note

This skill was developed as an alternative to the existing `zk-dex-keygen` module based on `@noble/curves`. By using a more stable and verified Python implementation, it ensures reliable key generation without WASM dependencies.