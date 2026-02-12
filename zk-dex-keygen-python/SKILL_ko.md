# SKILL.md - zk-dex-keygen-python

## 설명

Python 기반 BabyJubJub 키페어 생성 모듈. BabyJubJub 곡선을 사용하여 키페어를 생성하고 암호화된 keystore JSON 포맷으로 내보냅니다. 주소 파생은 **Poseidon 해시** (circomlibjs 호환)를 사용하여 온체인 회로 구현과 일치합니다.

## 의존성

- `sapling_jubjub.py` (BabyJubJub 곡선 연산, `baby_jubjub_ecc`에서 가져옴)
- `zkdex_lib/` (공유 라이브러리: Poseidon 해시, Account, Note)
- `cryptography` Python 패키지 (AES-256-GCM 암호화용)
- Python 3.x

## 사용법

```bash
python generate_keypair.py --password <비밀번호>
# 또는
python generate_keypair.py -p <비밀번호>
```

## 출력 포맷

```json
{
  "address": "914e04dccf3cd308ad6d0848df14ea5752e2b298",
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

- **address**: `truncate_to_160_bits(Poseidon(pk.x, pk.y))` — 40 hex chars, circomlibjs `pubKeyToAddress` 호환
- **publicKey**: BabyJubJub 공개키 좌표, `0x` prefix 포함 (각 64 hex chars)
- **keystore**: scrypt KDF + AES-256-GCM으로 암호화된 비밀키
- **exportedAt**: 밀리초 타임스탬프

## 구조

- `generate_keypair.py`: 메인 스크립트 — 키페어 생성, Poseidon 주소 파생, keystore 내보내기
- `sapling_jubjub.py`: BabyJubJub 곡선 필드 및 점 연산
- `sapling_utils.py`: 비트/바이트 변환 유틸리티
