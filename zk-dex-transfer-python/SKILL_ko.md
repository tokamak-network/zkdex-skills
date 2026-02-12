# SKILL.md - zk-dex-transfer-python

## 설명

Python 기반 zk-DEx 트랜스퍼 노트 생성 모듈. circom 트랜스퍼 회로와 호환되는 7-input Poseidon 노트 해시를 생성합니다. 송신자의 비밀키는 소유권 증명에, 수신자의 공개키는 노트 소유자로 사용됩니다. 공유 `zkdex_lib` 라이브러리를 사용 (순수 Python, npm/web3 의존성 없음).

## 의존성

- `zkdex_lib/` (공유 라이브러리: Poseidon 해시, Note, Account)
- Python 3.x

## 사용법

```bash
python generate_transfer.py \
  --sk <송신자_비밀키> \
  --to-pk-x <hex> \
  --to-pk-y <hex> \
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
  },
  "sender": {
    "address": "c63db0d1...",
    "publicKey": { "x": "0x...", "y": "0x..." }
  }
}
```

## 구조

- `generate_transfer.py`: 트랜스퍼 노트 생성 CLI 스크립트
