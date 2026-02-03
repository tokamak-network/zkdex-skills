# SKILLSET.md - zkdex skills

이 문서는 `zkdex skills` 패키지에 포함된 모든 스킬 모듈을 정의합니다.

## 포함된 스킬 모듈

- `zk-dex-keygen-python`: Python 기반의 `BabyJubJub` 키 페어 생성 모듈. `barryWhiteHat/baby_jubjub_ecc` 리포지토리의 검증된 구현체를 사용합니다.
- `zk-dex-transfer-python`: Python 기반의 트랜스퍼 노트 생성 모듈. 자산 송금을 위해 사용됩니다.
- `zk-dex-mint-python`: Python 기반의 민트 노트 생성 모듈. 새로운 자산을 발행하기 위해 사용됩니다.
- `zk-dex-redeem-python`: Python 기반의 리딤 노트 생성 모듈. 자산을 환전하기 위해 사용됩니다.
- `zk-dex-glossary`: zk-DEx 프로젝트에서 사용되는 핵심 용어들을 정리한 용어집 모듈.

## 설치

1. 이 리포지토리를 클론합니다.
2. `projects/tokamak-zk-dex/skills` 디렉토리에 모든 스킬 모듈을 배치합니다.

## 사용법

각 스킬 모듈은 독립적으로 사용할 수 있습니다. 사용 방법은 각 모듈의 `SKILL.md` 파일을 참조하세요.

## 라이선스

MIT 라이선스 하에 배포됩니다.