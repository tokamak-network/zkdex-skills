"""
ZK proof generation via Node.js subprocess (snarkjs Groth16).

Calls generate_proof.js with circuit inputs via stdin,
returns formatted proof from stdout.
"""

import json
import os
import subprocess

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_GENERATE_PROOF_JS = os.path.join(_SCRIPT_DIR, 'generate_proof.js')

MASK_254 = (1 << 254) - 1


def generate_proof(circuit_name: str, inputs: dict) -> dict:
    """
    Node.js subprocess로 snarkjs Groth16 proof 생성.

    Args:
        circuit_name: 회로 이름 (e.g., 'mint_burn_note', 'transfer_note')
        inputs: 회로 입력값 dict (모든 값은 decimal string)

    Returns:
        dict: {
            "a": [str, str],
            "b": [[str, str], [str, str]],
            "c": [str, str],
            "input": [str, ...]
        }

    Raises:
        RuntimeError: proof 생성 실패 시
    """
    request = json.dumps({"circuit": circuit_name, "inputs": inputs})

    result = subprocess.run(
        ["node", _GENERATE_PROOF_JS],
        input=request,
        capture_output=True,
        text=True,
        timeout=120,
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"Proof generation failed for {circuit_name}: {result.stderr.strip()}"
        )

    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as e:
        raise RuntimeError(
            f"Invalid proof output: {e}\nstdout: {result.stdout[:500]}"
        )


def generate_mint_proof(note, sk: int) -> dict:
    """
    mint_burn_note 회로 proof 생성. mint와 redeem 모두 사용.

    Args:
        note: Note 객체 (owner0, owner1, value, token, vk0, vk1, salt)
        sk: 비밀키 (int)

    Returns:
        dict: formatted proof for contract
    """
    inputs = {
        "noteHash": str(note.hash_int()),
        "value": str(note.value & MASK_254),
        "tokenType": str(note.token & MASK_254),
        "owner0": str(note.owner0),
        "owner1": str(note.owner1),
        "vk0": str(note.vk0),
        "vk1": str(note.vk1),
        "salt": str(note.salt & MASK_254),
        "sk": str(sk & MASK_254),
    }
    return generate_proof("mint_burn_note", inputs)


def _note_fields(note):
    """Note 객체에서 7개 필드를 decimal string dict로 추출."""
    if note is None:
        return {k: "0" for k in ("owner0", "owner1", "value", "token", "vk0", "vk1", "salt")}
    return {
        "owner0": str(note.owner0),
        "owner1": str(note.owner1),
        "value": str(note.value),
        "token": str(note.token),
        "vk0": str(note.vk0),
        "vk1": str(note.vk1),
        "salt": str(note.salt),
    }


def generate_transfer_proof(old0, old1, new_note, change, sk0: int, sk1: int = 0) -> dict:
    """
    transfer_note 회로 proof 생성.

    Args:
        old0: 기존 노트 0 (Note 객체)
        old1: 기존 노트 1 (Note 객체 또는 None → empty note)
        new_note: 수신 노트 (Note 객체)
        change: 거스름 노트 (Note 객체)
        sk0: 송신자 비밀키 (int)
        sk1: 두 번째 비밀키 (int, 기본 0)

    Returns:
        dict: formatted proof for contract
    """
    from .note import EMPTY_NOTE

    if old1 is None:
        old1 = EMPTY_NOTE

    # 해시 계산
    o0_hash = str(old0.hash_int())
    o1_hash = str(old1.hash_int())
    new_hash = str(new_note.hash_int())
    change_hash = str(change.hash_int())

    o0 = _note_fields(old0)
    o1 = _note_fields(old1)
    n = _note_fields(new_note)
    c = _note_fields(change)

    inputs = {
        # Public inputs
        "o0Hash": o0_hash,
        "o1Hash": o1_hash,
        "newHash": new_hash,
        "changeHash": change_hash,
        # Old note 0
        "o0Owner0": o0["owner0"],
        "o0Owner1": o0["owner1"],
        "o0Value": o0["value"],
        "o0Type": o0["token"],
        "o0Vk0": o0["vk0"],
        "o0Vk1": o0["vk1"],
        "o0Salt": o0["salt"],
        # Old note 1
        "o1Owner0": o1["owner0"],
        "o1Owner1": o1["owner1"],
        "o1Value": o1["value"],
        "o1Type": o1["token"],
        "o1Vk0": o1["vk0"],
        "o1Vk1": o1["vk1"],
        "o1Salt": o1["salt"],
        # New note
        "nOwner0": n["owner0"],
        "nOwner1": n["owner1"],
        "nValue": n["value"],
        "nType": n["token"],
        "nVk0": n["vk0"],
        "nVk1": n["vk1"],
        "nSalt": n["salt"],
        # Change note
        "cOwner0": c["owner0"],
        "cOwner1": c["owner1"],
        "cValue": c["value"],
        "cType": c["token"],
        "cVk0": c["vk0"],
        "cVk1": c["vk1"],
        "cSalt": c["salt"],
        # Secret keys
        "sk0": str(sk0),
        "sk1": str(sk1),
    }
    return generate_proof("transfer_note", inputs)


def generate_redeem_proof(note, sk: int) -> dict:
    """
    redeem proof 생성. mint_burn_note 회로 재사용.

    Args:
        note: Note 객체
        sk: 비밀키 (int)

    Returns:
        dict: formatted proof for contract
    """
    return generate_mint_proof(note, sk)
