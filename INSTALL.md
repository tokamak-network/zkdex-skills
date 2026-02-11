# zkdex-skills Installation Guide

This guide explains how to install the zkdex-skills modules into [nanobot](https://github.com/tokamak-network/eth-nanobot).

> For nanobot installation and configuration, see the [eth-nanobot repository](https://github.com/tokamak-network/eth-nanobot).

## Prerequisites

- nanobot installed and configured (`~/.nanobot/config.json` exists)
- Python 3.11+ with `cryptography` package (`pip install cryptography`)

## 1. Clone the Skills Repository

```bash
git clone https://github.com/tokamak-network/zkdex-skills.git ~/.nanobot/workspace/zkdex-skills
```

## 2. Register Skills

Nanobot discovers skills from `~/.nanobot/workspace/skills/`. Create symlinks for each skill module:

```bash
mkdir -p ~/.nanobot/workspace/skills
cd ~/.nanobot/workspace/skills

ln -s ../zkdex-skills/zk-dex-keygen-python .
ln -s ../zkdex-skills/zk-dex-keygen .
ln -s ../zkdex-skills/zk-dex-transfer-python .
ln -s ../zkdex-skills/zk-dex-mint-python .
ln -s ../zkdex-skills/zk-dex-redeem-python .
ln -s ../zkdex-skills/zk-dex-glossary .
```

Each skill directory contains a `SKILL.md` file. Nanobot automatically detects and loads them — no additional configuration is needed.

## 3. Verify

Restart nanobot (`nanobot gateway` or `nanobot chat`) and ask:

> "What skills do you have?"

### Test keygen directly

```bash
cd ~/.nanobot/workspace/zkdex-skills/zk-dex-keygen-python
python generate_keypair.py --password test123
```

This outputs a JSON keystore with address, publicKey, encrypted keystore, and timestamp.

## Directory Structure

```
~/.nanobot/workspace/
├── zkdex-skills/                    # This repository
│   ├── zk-dex-keygen-python/
│   │   ├── SKILL.md
│   │   ├── generate_keypair.py
│   │   └── sapling_jubjub.py
│   ├── zk-dex-transfer-python/
│   ├── zk-dex-mint-python/
│   ├── zk-dex-redeem-python/
│   ├── zk-dex-keygen/
│   └── zk-dex-glossary/
└── skills/                          # Nanobot skill discovery directory
    ├── zk-dex-keygen-python -> ../zkdex-skills/zk-dex-keygen-python
    ├── zk-dex-keygen -> ../zkdex-skills/zk-dex-keygen
    ├── zk-dex-transfer-python -> ../zkdex-skills/zk-dex-transfer-python
    ├── zk-dex-mint-python -> ../zkdex-skills/zk-dex-mint-python
    ├── zk-dex-redeem-python -> ../zkdex-skills/zk-dex-redeem-python
    └── zk-dex-glossary -> ../zkdex-skills/zk-dex-glossary
```

## Troubleshooting

- **Skills not showing up** — Check symlinks: `ls -la ~/.nanobot/workspace/skills/`. Restart gateway after changes.
- **`ModuleNotFoundError: cryptography`** — Run `pip install cryptography`
- **`ModuleNotFoundError: sapling_jubjub`** — Run the script from within the `zk-dex-keygen-python/` directory
