#!/usr/bin/env node
/**
 * ZK proof generation CLI wrapper for snarkjs.
 *
 * Usage: echo '{"circuit":"mint_burn_note","inputs":{...}}' | node generate_proof.js
 * Output: {"proof":{"a":[...],"b":[[...],[...]],"c":[...]},"publicSignals":[...]}
 *
 * Reads JSON from stdin, runs groth16.fullProve(), outputs formatted proof to stdout.
 */

const snarkjs = require('/Users/kevin/dev/zkdex/zk-dex/node_modules/snarkjs');
const path = require('path');
const fs = require('fs');

const CIRCUITS_DIR = '/Users/kevin/dev/zkdex/zk-dex/circuits-circom/build';

/**
 * Format proof for smart contract call (Groth16 format).
 * Matches snarkjsUtils.js formatProofForContract — includes b-coordinate swap.
 */
function formatProofForContract(proof, publicSignals) {
    return {
        a: [proof.pi_a[0], proof.pi_a[1]],
        b: [
            [proof.pi_b[0][1], proof.pi_b[0][0]],
            [proof.pi_b[1][1], proof.pi_b[1][0]]
        ],
        c: [proof.pi_c[0], proof.pi_c[1]],
        input: publicSignals
    };
}

async function main() {
    // Read all stdin
    const chunks = [];
    for await (const chunk of process.stdin) {
        chunks.push(chunk);
    }
    const raw = Buffer.concat(chunks).toString('utf8');

    let request;
    try {
        request = JSON.parse(raw);
    } catch (e) {
        process.stderr.write(`Invalid JSON input: ${e.message}\n`);
        process.exit(1);
    }

    const { circuit, inputs } = request;
    if (!circuit || !inputs) {
        process.stderr.write('Missing "circuit" or "inputs" in JSON input\n');
        process.exit(1);
    }

    const wasmPath = path.join(CIRCUITS_DIR, circuit, `${circuit}_js`, `${circuit}.wasm`);
    const zkeyPath = path.join(CIRCUITS_DIR, circuit, `${circuit}.zkey`);

    if (!fs.existsSync(wasmPath)) {
        process.stderr.write(`WASM file not found: ${wasmPath}\n`);
        process.exit(1);
    }
    if (!fs.existsSync(zkeyPath)) {
        process.stderr.write(`zkey file not found: ${zkeyPath}\n`);
        process.exit(1);
    }

    try {
        const { proof, publicSignals } = await snarkjs.groth16.fullProve(
            inputs,
            wasmPath,
            zkeyPath
        );

        const formatted = formatProofForContract(proof, publicSignals);
        process.stdout.write(JSON.stringify(formatted) + '\n');
        process.exit(0);
    } catch (e) {
        process.stderr.write(`Proof generation failed: ${e.message}\n`);
        process.exit(1);
    }
}

main();
