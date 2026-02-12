#!/usr/bin/env python3
"""
ZK-DEX Transfer Note 생성 스크립트.

송신자의 비밀키(sk)와 수신자의 공개키(pk.x, pk.y)로
트랜스퍼 노트를 생성하고 Poseidon 해시를 계산합니다.
"""

import os
import sys
import json
import argparse

# zkdex_lib import
_parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _parent_dir not in sys.path:
    sys.path.insert(0, _parent_dir)

from zkdex_lib.note import Note
from zkdex_lib.account import Account


def generate_transfer_note(sk, to_pk_x, to_pk_y, value, token_type=0, salt=None):
    """
    트랜스퍼 노트를 생성합니다.

    수신자의 공개키를 owner로 사용하는 regular note를 생성.

    Args:
        sk: 송신자 비밀키 (int 또는 hex str) - 소유권 증명용
        to_pk_x: 수신자 공개키 x좌표 (int 또는 hex str)
        to_pk_y: 수신자 공개키 y좌표 (int 또는 hex str)
        value: 송금 금액 (int 또는 hex str)
        token_type: 토큰 타입 (int 또는 hex str, 기본 0 = ETH)
        salt: 솔트 (int 또는 hex str, None이면 자동 생성)

    Returns:
        dict: {'note': Note, 'sender': Account}
    """
    sender = Account(sk)
    note = Note.from_public_key(to_pk_x, to_pk_y, value, token_type, salt)
    return {'note': note, 'sender': sender}


def _load_note_json(path):
    """JSON 파일에서 Note 객체를 로드합니다."""
    with open(path) as f:
        data = json.load(f)
    raw = data.get("noteRaw", data)
    return Note(
        raw["owner0"], raw["owner1"], raw["value"],
        raw["token"], raw["vk0"], raw["vk1"], raw["salt"]
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ZK-DEX 트랜스퍼 노트 생성")
    parser.add_argument("--sk", required=True, help="송신자 비밀키 (hex 또는 int)")
    parser.add_argument("--to-pk-x", required=True, help="수신자 공개키 x (hex)")
    parser.add_argument("--to-pk-y", required=True, help="수신자 공개키 y (hex)")
    parser.add_argument("--value", required=True, help="송금 금액 (int 또는 hex)")
    parser.add_argument("--token-type", default="0x0", help="토큰 타입 (기본: 0x0 = ETH)")
    parser.add_argument("--salt", default=None, help="솔트 (hex, 미지정 시 자동 생성)")
    parser.add_argument("--proof", action="store_true", help="ZK proof 생성 (추가 인자 필요)")
    parser.add_argument("--old-note0", default=None, help="기존 노트 0 JSON 파일 경로 (--proof 시 필수)")
    parser.add_argument("--old-note1", default=None, help="기존 노트 1 JSON 파일 경로 (없으면 empty note)")
    parser.add_argument("--change-salt", default=None, help="거스름 노트 솔트 (hex, 미지정 시 자동 생성)")
    parser.add_argument("--sk1", default=None, help="두 번째 비밀키 (hex, old-note1 소유자)")
    args = parser.parse_args()

    result = generate_transfer_note(
        args.sk,
        args.to_pk_x,
        args.to_pk_y,
        args.value,
        args.token_type,
        args.salt,
    )

    note = result['note']
    sender = result['sender']

    output = {
        "noteHash": note.hash(),
        "noteRaw": note.to_dict(),
        "sender": {
            "address": sender.address,
            "publicKey": {
                "x": sender.pk_x_hex,
                "y": sender.pk_y_hex,
            }
        }
    }

    if args.proof:
        if not args.old_note0:
            parser.error("--proof requires --old-note0 (기존 노트 JSON 파일 경로)")

        from zkdex_lib.proof import generate_transfer_proof

        sk0_int = int(args.sk, 16) if args.sk.startswith("0x") else int(args.sk)
        sk1_int = 0
        if args.sk1:
            sk1_int = int(args.sk1, 16) if args.sk1.startswith("0x") else int(args.sk1)

        old0 = _load_note_json(args.old_note0)
        old1 = None
        if args.old_note1:
            old1 = _load_note_json(args.old_note1)

        # 거스름 노트: 송신자에게 돌아감 (old0.value - transfer.value)
        old0_value = old0.value
        old1_value = old1.value if old1 else 0
        transfer_value = note.value
        change_value = old0_value + old1_value - transfer_value

        change_salt = args.change_salt
        if change_salt is None:
            import os as _os
            change_salt = int.from_bytes(_os.urandom(32), 'big')

        change_note = Note.from_public_key(
            sender.pk_x, sender.pk_y, change_value, note.token, change_salt
        )
        output["changeNote"] = {
            "noteHash": change_note.hash(),
            "noteRaw": change_note.to_dict(),
        }

        proof_result = generate_transfer_proof(
            old0, old1, note, change_note, sk0_int, sk1_int
        )
        output["proof"] = proof_result

    print(json.dumps(output, indent=2))
