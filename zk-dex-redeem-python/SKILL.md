---
name: zk-dex-redeem-python
description: "Generate zk-DEx redeem note. Run `python generate_redeem.py --sk <key> --value <amount>` to create a Poseidon note hash for redemption."
---

# zk-dex-redeem-python

Python-based redeem note generation for zk-DEx. Creates a 7-input Poseidon note hash compatible with the circom redeem (mint/burn) circuit. The owner's secret key is used to derive the public key, which becomes the note owner. Uses the shared `zkdex_lib` library (pure Python, no npm/web3 dependency).

## Dependencies

- `zkdex_lib/` (shared library: Poseidon hash, Note, Account)
- Python 3.x
- Node.js + snarkjs (ZK proof 생성 시에만 필요)

## Usage

```bash
# 노트만 생성
python generate_redeem.py \
  --sk <owner_secret_key> \
  --value <amount> \
  --token-type <hex>     # optional, default: 0x0 (ETH)
  --salt <hex>           # optional, auto-generated if omitted

# 노트 + ZK proof 생성
python generate_redeem.py \
  --sk <owner_secret_key> \
  --value <amount> \
  --proof
```

## Output Format

```json
{
  "noteHash": "0x2367a0c1...",
  "noteRaw": {
    "owner0": "0x...",
    "owner1": "0x...",
    "value": "0x...",
    "token": "0x...",
    "vk0": "0x...",
    "vk1": "0x...",
    "salt": "0x..."
  },
  "owner": {
    "address": "c63db0d1...",
    "publicKey": { "x": "0x...", "y": "0x..." }
  },
  "proof": {
    "a": ["<uint256>", "<uint256>"],
    "b": [["<uint256>", "<uint256>"], ["<uint256>", "<uint256>"]],
    "c": ["<uint256>", "<uint256>"],
    "input": ["<noteHash>", "<value>", "<tokenType>"]
  }
}
```

- **proof** (optional): Groth16 proof for mint_burn_note circuit. Only present with `--proof` flag.
  - Uses the same circuit as mint (mint_burn_note)
  - `input`: public signals `[noteHash, value, tokenType]`

## Structure

- `generate_redeem.py`: CLI script for redeem note generation
