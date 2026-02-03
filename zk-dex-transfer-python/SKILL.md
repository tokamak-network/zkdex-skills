# SKILL.md - zk-dex-transfer-python

## 설명

이 스킬은 Python 기반의 `zk-dex-transfer` 모듈입니다. `zkdex-utils` 라이브러리를 활용하여 zk-DEx에서 자산을 송금하기 위한 트랜스퍼 노트를 생성합니다.

## 의존성

- `zkdex-utils` (npm 패키지)
- Python 3.x
- `web3.py`

## 사용법

1. `generate_transfer.py` 스크립트를 실행합니다.
2. `generate_transfer_note()` 함수가 송금 정보를 기반으로 트랜스퍼 노트를 반환합니다.

## 구조

- `generate_transfer.py`: 트랜스퍼 노트 생성 로직을 포함한 메인 스크립트.

## 참고

이 스킬은 `zkdex-utils` 패키지의 `Note` 및 `Account` 클래스를 활용하여, 기존의 zk-DEx 프로토콜과 호환되는 노트를 생성합니다.