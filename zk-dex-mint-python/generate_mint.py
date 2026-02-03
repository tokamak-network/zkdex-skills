from zkdex_utils import Note, Account
import web3


def generate_mint_note(owner_zk_address, value, token_type="0x0"):
    """
    민팅을 위한 민트 노트를 생성합니다.
    """
    # 민트 노트 생성
    # owner는 자산을 받을 수신자의 zk 주소
    mint_note = Note(
        owner=owner_zk_address,
        value=value,
        type=token_type,
        viewKey="0x01", # 기본 뷰 키
        salt=web3.Web3.soliditySha3(['string'], ['mint']).hex() # 고유한 솔트
    )
    
    return mint_note


if __name__ == "__main__":
    # 예시: 수신자 주소와 가치로 민트 노트 생성
    owner_address = "zk2aGHYonwumtLAG7SNKjharksCP3r"
    value = "1000000000000000000"
    token_type = "0x0" # 기본 토큰 타입
    
    note = generate_mint_note(owner_address, value, token_type)
    print(f"민트 노트 해시: {note.getNoteHash()}")
    print(f"민트 노트 Raw: {note.getNoteRaw()}")