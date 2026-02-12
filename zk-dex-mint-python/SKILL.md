# SKILL.md - zk-dex-mint-python

## Description

Python-based mint note generation for zk-DEx. Creates a 7-input Poseidon note hash compatible with the circom mint circuit. Uses the shared `zkdex_lib` library (pure Python, no npm/web3 dependency).

## Dependencies

- `zkdex_lib/` (shared library: Poseidon hash, Note class)
- Python 3.x

## Usage

```bash
python generate_mint.py \
  --owner-pk-x <hex> \
  --owner-pk-y <hex> \
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
  }
}
```

- **noteHash**: `Poseidon(owner0, owner1, value, token, vk0, vk1, salt)` — 64 hex chars
- **noteRaw**: All 7 note fields as 0x-prefixed 64-char hex strings
- Regular note: `owner0=pk.x`, `owner1=pk.y`, `vk0=pk.x`, `vk1=pk.y`

## Structure

- `generate_mint.py`: CLI script for mint note generation
