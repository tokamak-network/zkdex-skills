# SKILL.md - zk-dex-keygen-python

## 설명

이 스킬은 Python 기반의 `zk-dex-keygen` 모듈입니다. `@noble/curves` 라이브러리의 타입 문제를 해결하기 위해, `barryWhiteHat/baby_jubjub_ecc` 리포지토리의 Python 구현체를 기반으로 합니다. `BabyJubJub` 곡선을 사용하여 zk-Dex 애플리케이션을 위한 키 페어를 생성하고 zkdex keystore JSON 포맷으로 내보냅니다.

## 의존성

- `sapling_jubjub.py` 파일 (기존 `baby_jubjub_ecc` 리포지토리에서 가져옴)
- `cryptography` Python 패키지 (AES-256-GCM 암호화용)
- Python 3.x

## 사용법

```bash
python generate_keypair.py --password <비밀번호>
# 또는
python generate_keypair.py -p <비밀번호>
```

`--password` (`-p`) 인자는 필수이며, keystore에서 비밀키를 암호화하는 데 사용할 비밀번호를 지정합니다.

## 출력 포맷

스크립트는 stdout으로 JSON 객체를 출력합니다:

```json
{
  "address": "352642512be6419630d0fbf6a42e510f85030587",
  "publicKey": {
    "x": "0x...",
    "y": "0x..."
  },
  "keystore": {
    "crypto": {
      "cipher": "aes-256-gcm",
      "ciphertext": "...",
      "cipherparams": { "iv": "..." },
      "kdf": "scrypt",
      "kdfparams": { "n": 16384, "r": 8, "p": 1, "dklen": 32, "salt": "..." },
      "mac": "..."
    },
    "version": 1
  },
  "exportedAt": 1770846855188
}
```

- **address**: `sha256(pk.x || pk.y)`의 마지막 20바이트 (40 hex chars)
- **publicKey**: BabyJubJub 공개키 좌표, `0x` prefix 포함 (각 64 hex chars)
- **keystore**: scrypt KDF + AES-256-GCM으로 암호화된 비밀키
- **exportedAt**: 밀리초 타임스탬프

## 구조

- `generate_keypair.py`: 키 페어 생성 및 keystore 내보내기 로직을 포함한 메인 스크립트.
- `sapling_jubjub.py`: `BabyJubJub` 곡선의 필드 및 점 연산을 정의한 파일.

## 참고

이 스킬은 `@noble/curves` 기반의 기존 `zk-dex-keygen` 모듈의 대체안으로 개발되었습니다. 보다 안정적이고 검증된 Python 구현체를 사용함으로써, WASM 의존성 없이도 신뢰할 수 있는 키 생성을 보장합니다.