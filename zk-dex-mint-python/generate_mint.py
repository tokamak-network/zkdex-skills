#!/usr/bin/env python3
"""
ZK-DEX Mint Note 생성 스크립트.

공개키(pk.x, pk.y)와 값(value), 토큰 타입으로 민트 노트를 생성하고
Poseidon 해시를 계산합니다.
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


def generate_mint_note(owner_pk_x, owner_pk_y, value, token_type=0, salt=None):
    """
    민트 노트를 생성합니다.

    Regular note: owner0=pk.x, owner1=pk.y, vk0=pk.x, vk1=pk.y

    Args:
        owner_pk_x: 수신자 공개키 x좌표 (int 또는 hex str)
        owner_pk_y: 수신자 공개키 y좌표 (int 또는 hex str)
        value: 민팅 금액 (int 또는 hex str)
        token_type: 토큰 타입 (int 또는 hex str, 기본 0 = ETH)
        salt: 솔트 (int 또는 hex str, None이면 자동 생성)

    Returns:
        Note 객체
    """
    return Note.from_public_key(owner_pk_x, owner_pk_y, value, token_type, salt)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ZK-DEX 민트 노트 생성")
    parser.add_argument("--owner-pk-x", required=True, help="수신자 공개키 x (hex)")
    parser.add_argument("--owner-pk-y", required=True, help="수신자 공개키 y (hex)")
    parser.add_argument("--value", required=True, help="민팅 금액 (int 또는 hex)")
    parser.add_argument("--token-type", default="0x0", help="토큰 타입 (기본: 0x0 = ETH)")
    parser.add_argument("--salt", default=None, help="솔트 (hex, 미지정 시 자동 생성)")
    parser.add_argument("--proof", action="store_true", help="ZK proof 생성 (--sk 필수)")
    parser.add_argument("--sk", default=None, help="비밀키 (hex 또는 int, --proof 시 필수)")
    args = parser.parse_args()

    note = generate_mint_note(
        args.owner_pk_x,
        args.owner_pk_y,
        args.value,
        args.token_type,
        args.salt,
    )

    result = {
        "noteHash": note.hash(),
        "noteRaw": note.to_dict(),
    }

    if args.proof:
        if not args.sk:
            parser.error("--proof requires --sk")
        from zkdex_lib.proof import generate_mint_proof
        sk_int = int(args.sk, 16) if args.sk.startswith("0x") else int(args.sk)
        proof_result = generate_mint_proof(note, sk_int)
        result["proof"] = proof_result

    print(json.dumps(result, indent=2))
