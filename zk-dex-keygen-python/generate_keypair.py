from sapling_jubjub import Point, Fq, Fr, JUBJUB_COFACTOR, r_j
import os

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


if __name__ == "__main__":
    # 테스트: 키 페어 생성 및 출력
    keys = generate_keypair()
    print("🔑 BabyJubJub 키 페어 생성 완료!")
    print(f"비밀키 (sk): {keys['sk']}")
    print(f"공개키 (pk): {keys['pk']}")
    print(f"공개키 x: {keys['pk'].u}")
    print(f"공개키 y: {keys['pk'].v}")