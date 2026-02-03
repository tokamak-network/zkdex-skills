# SKILL.md - zk-dex-keygen

## 설명

BabyJubJub 곡선을 기반으로 ZK DEX용 키 페어를 생성하는 스킬입니다. `@noble/curves` 라이브러리를 사용하여 WASM 의존성을 피하고 순수 JavaScript로 구현되어 있습니다. 안정성과 경량화를 강조합니다.

## 사용법

```javascript
const { generateKeypair, normalizePrivateKey } = require('@zkdex/skills/zk-dex-keygen');

// 키 페어 생성
const { sk, pk } = generateKeypair();

// 비밀키 정규화
const normalizedSk = normalizePrivateKey(sk);
```

## API

### `generateKeypair()`

- **Returns:** `{ sk: Uint8Array, pk: [bigint, bigint] }`
- 랜덤한 비밀키와 공개키 쌍을 생성합니다.

### `normalizePrivateKey(key)`
- **Parameters:** `key: Uint8Array | bigint`
- **Returns:** `Uint8Array`
- 다양한 형식의 비밀키를 정규화된 `Uint8Array`로 변환합니다.

## 의존성

- `@noble/curves`
- `@noble/hashes`