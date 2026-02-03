# SKILL.md - zk-dex-mint-python

## Description

This skill is a Python-based `zk-dex-mint` module. It generates mint notes for issuing new assets in zk-DEx, leveraging the `zkdex-utils` library.

## Dependencies

- `zkdex-utils` (npm package)
- Python 3.x
- `web3.py`

## Usage

1. Run the `generate_mint.py` script.
2. The `generate_mint_note()` function returns a mint note based on the minting information.

## Structure

- `generate_mint.py`: Main script containing the mint note generation logic.

## Note

This skill uses the `Note` class from the `zkdex-utils` package to generate notes compatible with the existing zk-DEx protocol.