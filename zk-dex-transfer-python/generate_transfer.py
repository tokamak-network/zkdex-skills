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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ZK-DEX 트랜스퍼 노트 생성")
    parser.add_argument("--sk", required=True, help="송신자 비밀키 (hex 또는 int)")
    parser.add_argument("--to-pk-x", required=True, help="수신자 공개키 x (hex)")
    parser.add_argument("--to-pk-y", required=True, help="수신자 공개키 y (hex)")
    parser.add_argument("--value", required=True, help="송금 금액 (int 또는 hex)")
    parser.add_argument("--token-type", default="0x0", help="토큰 타입 (기본: 0x0 = ETH)")
    parser.add_argument("--salt", default=None, help="솔트 (hex, 미지정 시 자동 생성)")
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
    print(json.dumps(output, indent=2))
