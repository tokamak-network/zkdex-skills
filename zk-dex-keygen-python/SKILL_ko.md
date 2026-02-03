# SKILL.md - zk-dex-keygen-python

## 설명

이 스킬은 Python 기반의 `zk-dex-keygen` 모듈입니다. `@noble/curves` 라이브러리의 타입 문제를 해결하기 위해, `barryWhiteHat/baby_jubjub_ecc` 리포지토리의 Python 구현체를 기반으로 합니다. 이는 `BabyJubJub` 곡선을 사용하여 zk-Dex 애플리케이션을 위한 키 페어를 생성합니다.

## 의존성

- `sapling_jubjub.py` 파일 (기존 `baby_jubjub_ecc` 리포지토리에서 가져옴)
- Python 3.x

## 사용법

1. `generate_keypair.py` 스크립트를 실행합니다.
2. `generate_keypair()` 함수가 랜덤한 비밀키와 이를 기반으로 한 공개키를 반환합니다.

## 구조

- `generate_keypair.py`: 키 페어 생성 로직을 포함한 메인 스크립트.
- `sapling_jubjub.py`: `BabyJubJub` 곡선의 필드 및 점 연산을 정의한 파일.

## 참고

이 스킬은 `@noble/curves` 기반의 기존 `zk-dex-keygen` 모듈의 대체안으로 개발되었습니다. 보다 안정적이고 검증된 Python 구현체를 사용함으로써, WASM 의존성 없이도 신뢰할 수 있는 키 생성을 보장합니다.