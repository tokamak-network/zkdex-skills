from sapling_jubjub import Point, Fq, Fr, JUBJUB_COFACTOR, r_j
import os
import hashlib
import json
import time
import argparse
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# BabyJubJub 곡선의 Base Point (B)
BASE_POINT = Point(
    Fq(5299619240641551281634865583518297030282874472190772894086521144482721001553),
    Fq(16950150798460657717958625567821834550301663161624707787222815936182638968203)
)


def generate_keypair():
    """
    BabyJubJub 키 페어를 생성합니다.

    Returns:
        dict: {'sk': 비밀키 (Fr), 'pk': 공개키 (Point)}
    """
    # 1. 랜덤 시드 생성
    seed = os.urandom(32)
    # 2. 시드를 정수로 변환
    seed_int = int.from_bytes(seed, 'little')
    # 3. 곡선의 차수(r)로 모듈러 연산을 수행하여 비밀키 생성
    secret_key = Fr(seed_int % r_j)  # r_j는 sapling_jubjub.py에 정의되어 있음
    # 4. 공개키 생성 (sk * Base Point)
    public_key = BASE_POINT * secret_key

    return {
        'sk': secret_key,
        'pk': public_key
    }


def derive_address(pk):
    """
    공개키에서 address를 파생합니다 (zkdex-utils Account.js 참조).
    sha256(pk.x_hex + pk.y_hex)의 마지막 20바이트(40 hex chars).
    """
    pk_x_hex = format(pk.u.s, '064x')
    pk_y_hex = format(pk.v.s, '064x')
    concat_hex = pk_x_hex + pk_y_hex
    hash_bytes = hashlib.sha256(bytes.fromhex(concat_hex)).hexdigest()
    return hash_bytes[24:]  # 마지막 40 hex chars (20 bytes)


def encrypt_keystore(sk_int, password):
    """
    비밀키를 scrypt + AES-256-GCM으로 암호화합니다.
    """
    salt = os.urandom(32)
    iv = os.urandom(16)

    # scrypt KDF
    derived_key = hashlib.scrypt(
        password.encode('utf-8'),
        salt=salt,
        n=16384, r=8, p=1, dklen=32
    )

    # AES-256-GCM 암호화
    sk_bytes = sk_int.to_bytes(32, 'big')
    aesgcm = AESGCM(derived_key)
    # AESGCM.encrypt returns ciphertext + tag (16 bytes) concatenated
    encrypted = aesgcm.encrypt(iv, sk_bytes, None)
    ciphertext = encrypted[:-16]
    mac = encrypted[-16:]

    return {
        "crypto": {
            "cipher": "aes-256-gcm",
            "ciphertext": ciphertext.hex(),
            "cipherparams": {"iv": iv.hex()},
            "kdf": "scrypt",
            "kdfparams": {
                "n": 16384,
                "r": 8,
                "p": 1,
                "dklen": 32,
                "salt": salt.hex()
            },
            "mac": mac.hex()
        },
        "version": 1
    }


def export_keystore(password):
    """
    키 페어를 생성하고 keystore JSON 포맷으로 반환합니다.
    """
    keys = generate_keypair()
    sk = keys['sk']
    pk = keys['pk']

    address = derive_address(pk)
    public_key = {
        "x": "0x" + format(pk.u.s, '064x'),
        "y": "0x" + format(pk.v.s, '064x')
    }
    keystore = encrypt_keystore(sk.s, password)
    exported_at = int(time.time() * 1000)

    return {
        "address": address,
        "publicKey": public_key,
        "keystore": keystore,
        "exportedAt": exported_at
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="BabyJubJub keystore 생성")
    parser.add_argument("--password", "-p", required=True, help="keystore 암호화 비밀번호")
    args = parser.parse_args()

    result = export_keystore(args.password)
    print(json.dumps(result, indent=2))
