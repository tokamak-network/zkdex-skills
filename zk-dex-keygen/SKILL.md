# SKILL.md - zk-dex-keygen

## Description

A skill for generating key pairs for ZK DEX based on the BabyJubJub curve. Uses the `@noble/curves` library to avoid WASM dependencies and is implemented in pure JavaScript. Emphasizes stability and lightweight design.

## Usage

```javascript
const { generateKeypair, normalizePrivateKey } = require('@zkdex/skills/zk-dex-keygen');

// Generate key pair
const { sk, pk } = generateKeypair();

// Normalize secret key
const normalizedSk = normalizePrivateKey(sk);
```

## API

### `generateKeypair()`

- **Returns:** `{ sk: Uint8Array, pk: [bigint, bigint] }`
- Generates a random secret key and public key pair.

### `normalizePrivateKey(key)`
- **Parameters:** `key: Uint8Array | bigint`
- **Returns:** `Uint8Array`
- Converts secret keys in various formats to a normalized `Uint8Array`.

## Dependencies

- `@noble/curves`
- `@noble/hashes`