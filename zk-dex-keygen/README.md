# zk-dex-keygen

BabyJubJub 곡선을 기반으로 ZK DEX용 키 페어를 생성하는 모듈입니다. `@noble/curves` 라이브러리를 사용하여 WASM 의존성을 피하고 순수 JavaScript로 구현되어 있습니다.

## 기능

- `generateKeypair()`: 랜덤한 비밀키와 공개키 쌍을 생성합니다.
- `normalizePrivateKey(key)`: 다양한 형식의 비밀키를 정규화된 `Uint8Array`로 변환합니다.

## 설치

```bash
npm install
```

## 사용법

```javascript
const { generateKeypair, normalizePrivateKey } = require('./index.js');

// 키 페어 생성
const { sk, pk } = generateKeypair();
console.log('비밀키:', sk);
console.log('공개키:', pk);

// 비밀키 정규화
const normalizedSk = normalizePrivateKey(sk);
```

## API

### `generateKeypair()`

**Returns:**

- `sk` (`Uint8Array`): 정규화된 비밀키 (32바이트)
- `pk` (`[bigint, bigint]`): 공개키 좌표 (x, y)

### `normalizePrivateKey(key)`

정규화되지 않은 비밀키를 안전하게 정규화합니다.

**Parameters:**

- `key` (`Uint8Array` | `bigint`): 정규화할 비밀키

**Returns:** `Uint8Array` - 정규화된 비밀키

**Throws:** `Error` - 잘못된 키 형식일 경우
