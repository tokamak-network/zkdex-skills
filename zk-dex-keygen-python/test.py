from generate_keypair import generate_keypair

print("🔑 BabyJubJub 키 페어 생성 중... (Python 기반)")
keys = generate_keypair()
print(f"비밀키 (sk): {keys['sk']}")
print(f"공개키 (pk): {keys['pk']}")