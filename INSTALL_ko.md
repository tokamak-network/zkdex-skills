# zkdex-skills 설치 가이드

이 가이드는 zkdex-skills 모듈을 [nanobot](https://github.com/tokamak-network/eth-nanobot)에 설치하는 방법을 설명합니다.

> nanobot 설치 및 설정은 [eth-nanobot 리포지토리](https://github.com/tokamak-network/eth-nanobot)를 참조하세요.

## 사전 요구사항

- nanobot 설치 및 설정 완료 (`~/.nanobot/config.json` 존재)
- Python 3.11+ 및 `cryptography` 패키지 (`pip install cryptography`)

## 1. 스킬 리포지토리 클론

```bash
git clone https://github.com/tokamak-network/zkdex-skills.git ~/.nanobot/workspace/zkdex-skills
```

## 2. 스킬 등록

Nanobot은 `~/.nanobot/workspace/skills/` 디렉토리에서 스킬을 자동 탐색합니다. 각 스킬 모듈에 대한 심볼릭 링크를 생성합니다:

```bash
mkdir -p ~/.nanobot/workspace/skills
cd ~/.nanobot/workspace/skills

ln -s ../zkdex-skills/zk-dex-keygen-python .
ln -s ../zkdex-skills/zk-dex-keygen .
ln -s ../zkdex-skills/zk-dex-transfer-python .
ln -s ../zkdex-skills/zk-dex-mint-python .
ln -s ../zkdex-skills/zk-dex-redeem-python .
ln -s ../zkdex-skills/zk-dex-glossary .
```

각 스킬 디렉토리에 `SKILL.md` 파일이 있으면 자동으로 인식됩니다. 별도의 설정은 필요하지 않습니다.

## 3. 확인

nanobot을 재시작(`nanobot gateway` 또는 `nanobot chat`)한 후 다음과 같이 확인합니다:

> "어떤 스킬을 가지고 있어?"

### keygen 직접 테스트

```bash
cd ~/.nanobot/workspace/zkdex-skills/zk-dex-keygen-python
python generate_keypair.py --password test123
```

address, publicKey, 암호화된 keystore, 타임스탬프가 포함된 JSON이 출력됩니다.

## 디렉토리 구조

```
~/.nanobot/workspace/
├── zkdex-skills/                    # 이 리포지토리
│   ├── zk-dex-keygen-python/
│   │   ├── SKILL.md
│   │   ├── generate_keypair.py
│   │   └── sapling_jubjub.py
│   ├── zk-dex-transfer-python/
│   ├── zk-dex-mint-python/
│   ├── zk-dex-redeem-python/
│   ├── zk-dex-keygen/
│   └── zk-dex-glossary/
└── skills/                          # Nanobot 스킬 탐색 디렉토리
    ├── zk-dex-keygen-python -> ../zkdex-skills/zk-dex-keygen-python
    ├── zk-dex-keygen -> ../zkdex-skills/zk-dex-keygen
    ├── zk-dex-transfer-python -> ../zkdex-skills/zk-dex-transfer-python
    ├── zk-dex-mint-python -> ../zkdex-skills/zk-dex-mint-python
    ├── zk-dex-redeem-python -> ../zkdex-skills/zk-dex-redeem-python
    └── zk-dex-glossary -> ../zkdex-skills/zk-dex-glossary
```

## 문제 해결

- **스킬이 표시되지 않을 때** — 심볼릭 링크 확인: `ls -la ~/.nanobot/workspace/skills/`. 변경 후 게이트웨이 재시작.
- **`ModuleNotFoundError: cryptography`** — `pip install cryptography` 실행
- **`ModuleNotFoundError: sapling_jubjub`** — `zk-dex-keygen-python/` 디렉토리 내에서 스크립트 실행
