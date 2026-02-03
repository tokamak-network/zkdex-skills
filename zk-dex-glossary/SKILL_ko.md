# SKILL.md - zk-dex-glossary

## 설명

이 스킬은 토카막의 zk-DEx 프로젝트에서 사용되는 핵심 용어들을 정리한 용어집입니다. `ZKDIPs` 문서와 `zkdex-utils` 소스 코드를 기반으로 작성되었습니다.

## 용어 정리

### ZKDIP (ZK-DEX Improvement Proposal)
zk-DEx 플랫폼의 표준을 설명하는 제안서입니다. 프로토콜 사양, 클라이언트 API, 컨트랙트 표준 등을 정의합니다.

### zk 주소 (zk address)
zk-DEx에서 자산을 수령할 수 있는 목적지 식별자입니다. 이더리움 계정 하나에 여러 개의 zk 주소가 있을 수 있습니다.
- **생성 방식**: `zk` + base58(sha256(pubkey.x + pubkey.y)[12:])
- **예시**: `zk2aGHYonwumtLAG7SNKjharksCP3r`

### 노트 (Note)
zk-DEx에서 자산을 나타내는 단위입니다. 마치 물리적인 현금 노트처럼, 소유자(owner), 가치(value), 타입(type), 뷰 키(viewKey), 솔트(salt) 등의 정보를 포함합니다.

### 노트 해시 (Note Hash)
노트의 고유한 해시값입니다. 자산의 주소로 사용되며, `sha256(owner + value + type + viewKey + salt)`로 계산됩니다.

### 뷰 키 (View Key)
노트의 소유자가 노트를 조회할 수 있도록 허용하는 키입니다. 소유자만이 자산을 사용할 수 있지만, 뷰 키를 통해 제3자에게 조회를 허락할 수 있습니다.

### 솔트 (Salt)
노트의 고유성을 보장하기 위해 사용되는 난수입니다. 동일한 정보로도 다른 노트를 생성할 수 있게 해줍니다.

### OwnerType (소유자 유형)
노트의 소유자 유형을 구분합니다.
- **External**: 일반적인 외부 계정 (예: 이더리움 주소)
- **Note**: 다른 노트가 소유자인 경우 (스마트 노트)

## 참고

이 용어집은 `ZKDIP-2`, `ZKDIP-5` 문서 및 `zkdex-utils` 라이브러리의 `Account.js`, `Note.js` 파일을 기반으로 작성되었습니다.