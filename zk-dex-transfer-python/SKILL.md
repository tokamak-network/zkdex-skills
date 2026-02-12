# SKILL.md - zk-dex-transfer-python

## Description

Python-based transfer note generation for zk-DEx. Creates a 7-input Poseidon note hash compatible with the circom transfer circuit. The sender's secret key is used for ownership proof, and the recipient's public key becomes the note owner. Uses the shared `zkdex_lib` library (pure Python, no npm/web3 dependency).

## Dependencies

- `zkdex_lib/` (shared library: Poseidon hash, Note, Account)
- Python 3.x

## Usage

```bash
python generate_transfer.py \
  --sk <sender_secret_key> \
  --to-pk-x <hex> \
  --to-pk-y <hex> \
  --value <amount> \
  --token-type <hex>     # optional, default: 0x0 (ETH)
  --salt <hex>           # optional, auto-generated if omitted
```

## Output Format

```json
{
  "noteHash": "0x05fa764f...",
  "noteRaw": {
    "owner0": "0x...",
    "owner1": "0x...",
    "value": "0x...",
    "token": "0x...",
    "vk0": "0x...",
    "vk1": "0x...",
    "salt": "0x..."
  },
  "sender": {
    "address": "c63db0d1...",
    "publicKey": { "x": "0x...", "y": "0x..." }
  }
}
```

## Structure

- `generate_transfer.py`: CLI script for transfer note generation
