# SKILL.md - zk-dex-transfer-python

## Description

This skill is a Python-based `zk-dex-transfer` module. It generates transfer notes for asset transfers in zk-DEx, leveraging the `zkdex-utils` library.

## Dependencies

- `zkdex-utils` (npm package)
- Python 3.x
- `web3.py`

## Usage

1. Run the `generate_transfer.py` script.
2. The `generate_transfer_note()` function returns a transfer note based on the transfer information.

## Structure

- `generate_transfer.py`: Main script containing the transfer note generation logic.

## Note

This skill uses the `Note` and `Account` classes from the `zkdex-utils` package to generate notes compatible with the existing zk-DEx protocol.