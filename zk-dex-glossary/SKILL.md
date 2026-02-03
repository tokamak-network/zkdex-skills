# SKILL.md - zk-dex-glossary

## Description

This skill is a glossary of core terms used in Tokamak's zk-DEx project. It is based on the `ZKDIPs` documents and the `zkdex-utils` source code.

## Term Definitions

### ZKDIP (ZK-DEX Improvement Proposal)
A proposal document that defines standards for the zk-DEx platform. It specifies protocol specifications, client APIs, contract standards, and more.

### zk Address
A destination identifier in zk-DEx for receiving assets. Multiple zk addresses can exist under a single Ethereum account.
- **Generation**: `zk` + base58(sha256(pubkey.x + pubkey.y)[12:])
- **Example**: `zk2aGHYonwumtLAG7SNKjharksCP3r`

### Note
A unit representing an asset in zk-DEx. Like a physical cash note, it contains information such as owner, value, type, viewKey, and salt.

### Note Hash
The unique hash value of a note. Used as the asset's address, calculated as `sha256(owner + value + type + viewKey + salt)`.

### View Key
A key that allows the note owner to grant third parties the ability to view the note. Only the owner can spend the asset, but the view key enables read-only access.

### Salt
A random number used to ensure the uniqueness of a note. Allows different notes to be created even with identical information.

### OwnerType
Specifies the type of note owner.
- **External**: A regular external account (e.g., Ethereum address)
- **Note**: When another note is the owner (smart note)

## Note

This glossary is based on `ZKDIP-2`, `ZKDIP-5`, and the `Account.js`, `Note.js` files in the `zkdex-utils` library.