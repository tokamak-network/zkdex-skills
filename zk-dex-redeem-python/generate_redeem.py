#!/usr/bin/env python3
"""
ZK-DEX Redeem Note 생성 스크립트.

소유자의 비밀키(sk)로부터 공개키를 파생하고,
자신을 owner로 하는 리딤 노트를 생성합니다.
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


def generate_redeem_note(sk, value, token_type=0, salt=None):
    """
    리딤 노트를 생성합니다.

    소유자의 sk로부터 pk를 파생하고, 자신을 owner로 하는 regular note 생성.

    Args:
        sk: 소유자 비밀키 (int 또는 hex str)
        value: 환전 금액 (int 또는 hex str)
        token_type: 토큰 타입 (int 또는 hex str, 기본 0 = ETH)
        salt: 솔트 (int 또는 hex str, None이면 자동 생성)

    Returns:
        dict: {'note': Note, 'account': Account}
    """
    account = Account(sk)
    note = Note.from_public_key(account.pk_x, account.pk_y, value, token_type, salt)
    return {'note': note, 'account': account}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ZK-DEX 리딤 노트 생성")
    parser.add_argument("--sk", required=True, help="소유자 비밀키 (hex 또는 int)")
    parser.add_argument("--value", required=True, help="환전 금액 (int 또는 hex)")
    parser.add_argument("--token-type", default="0x0", help="토큰 타입 (기본: 0x0 = ETH)")
    parser.add_argument("--salt", default=None, help="솔트 (hex, 미지정 시 자동 생성)")
    parser.add_argument("--proof", action="store_true", help="ZK proof 생성")
    args = parser.parse_args()

    result = generate_redeem_note(
        args.sk,
        args.value,
        args.token_type,
        args.salt,
    )

    note = result['note']
    account = result['account']

    output = {
        "noteHash": note.hash(),
        "noteRaw": note.to_dict(),
        "owner": {
            "address": account.address,
            "publicKey": {
                "x": account.pk_x_hex,
                "y": account.pk_y_hex,
            }
        }
    }

    if args.proof:
        from zkdex_lib.proof import generate_redeem_proof
        sk_int = int(args.sk, 16) if args.sk.startswith("0x") else int(args.sk)
        proof_result = generate_redeem_proof(note, sk_int)
        output["proof"] = proof_result

    print(json.dumps(output, indent=2))
