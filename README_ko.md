# zkdex skills

`zkdex skills` 패키지는 토카막의 zk-DEx 프로젝트를 위한 재사용 가능한 스킬 모듈들의 모음입니다. 이 패키지는 Python 기반으로 구현되어 있으며, WASM 의존성 없이도 안정적인 암호학 연산을 제공합니다.

## 포함된 모듈

이 패키지에는 다음과 같은 스킬 모듈이 포함되어 있습니다:

- `zk-dex-keygen-python`: `BabyJubJub` 곡선을 사용하여 키 페어를 생성합니다.
- `zk-dex-transfer-python`: 자산 송금을 위한 트랜스퍼 노트를 생성합니다.
- `zk-dex-mint-python`: 새로운 자산을 발행하기 위한 민트 노트를 생성합니다.
- `zk-dex-redeem-python`: 자산을 환전하기 위한 리딤 노트를 생성합니다.
- `zk-dex-glossary`: zk-DEx 프로젝트의 핵심 용어들을 정리한 용어집입니다.

각 모듈은 독립적으로 사용할 수 있으며, 자세한 사용법은 각 모듈의 `SKILL.md` 파일을 참조하세요.

## 설치

1. 이 리포지토리를 클론합니다.
   ```bash
   git clone <repository-url>
   ```

2. 필요한 의존성을 설치합니다. 일부 모듈은 `zkdex-utils` npm 패키지가 필요할 수 있습니다.
   ```bash
   npm install zkdex-utils@0.9.5
   ```

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.