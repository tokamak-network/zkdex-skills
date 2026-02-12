# SKILL.md - zk-dex-mint-python

## 설명

Python 기반 zk-DEx 민트 노트 생성 모듈. circom 민트 회로와 호환되는 7-input Poseidon 노트 해시를 생성합니다. 공유 `zkdex_lib` 라이브러리를 사용 (순수 Python, npm/web3 의존성 없음).

## 의존성

- `zkdex_lib/` (공유 라이브러리: Poseidon 해시, Note 클래스)
- Python 3.x

## 사용법

```bash
python generate_mint.py \
  --owner-pk-x <hex> \
  --owner-pk-y <hex> \
  --value <금액> \
  --token-type <hex>     # 선택, 기본: 0x0 (ETH)
  --salt <hex>           # 선택, 미지정 시 자동 생성
```

## 출력 포맷

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
- **noteRaw**: 7개 노트 필드, 모두 0x prefix 64자리 hex 문자열
- Regular note: `owner0=pk.x`, `owner1=pk.y`, `vk0=pk.x`, `vk1=pk.y`

## 구조

- `generate_mint.py`: 민트 노트 생성 CLI 스크립트
