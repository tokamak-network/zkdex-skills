# zk-dex-keygen

A module for generating key pairs for ZK DEX based on the BabyJubJub curve. Implemented in pure JavaScript using the `@noble/curves` library to avoid WASM dependencies.

## Features

- `generateKeypair()`: Generates a random secret key and public key pair.
- `normalizePrivateKey(key)`: Converts secret keys in various formats to a normalized `Uint8Array`.

## Installation

```bash
npm install
```

## Usage

```javascript
const { generateKeypair, normalizePrivateKey } = require('./index.js');

// Generate key pair
const { sk, pk } = generateKeypair();
console.log('Secret key:', sk);
console.log('Public key:', pk);

// Normalize secret key
const normalizedSk = normalizePrivateKey(sk);
```

## API

### `generateKeypair()`

**Returns:**

- `sk` (`Uint8Array`): Normalized secret key (32 bytes)
- `pk` (`[bigint, bigint]`): Public key coordinates (x, y)

### `normalizePrivateKey(key)`

Safely normalizes an unnormalized secret key.

**Parameters:**

- `key` (`Uint8Array` | `bigint`): Secret key to normalize

**Returns:** `Uint8Array` - Normalized secret key

**Throws:** `Error` - If the key format is invalid
