# zkdex skills

The `zkdex skills` package is a collection of reusable skill modules for Tokamak's zk-DEx project. This package is implemented in Python and provides stable cryptographic operations without WASM dependencies.

## Included Modules

The package includes the following skill modules:

- `zk-dex-keygen-python`: Generates key pairs using the `BabyJubJub` curve.
- `zk-dex-transfer-python`: Creates transfer notes for asset transfers.
- `zk-dex-mint-python`: Creates mint notes for issuing new assets.
- `zk-dex-redeem-python`: Creates redeem notes for redeeming assets.
- `zk-dex-glossary`: A glossary that compiles the core terms of the zk-DEx project.

Each module can be used independently. For detailed usage, please refer to the `SKILL.md` file in each module.

## Installation

1. Clone this repository.
   ```bash
   git clone <repository-url>
   ```

2. Install the required dependencies. Some modules may require the `zkdex-utils` npm package.
   ```bash
   npm install zkdex-utils@0.9.5
   ```

## License

This project is distributed under the MIT License.