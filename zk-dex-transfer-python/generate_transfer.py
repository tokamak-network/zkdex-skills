from zkdex_utils import Note, Account
import web3


def generate_transfer_note(from_sk, to_zk_address, value):
    """
    송금을 위한 트랜스퍼 노트를 생성합니다.

    """
    # 송신자 계정 생성
    from_account = Account(from_sk)
    
    # 수신자의 zk 주소를 가져옵니다 (여기서는 인자로 받음)
    to_address = to_zk_address
    
    # 송금 노트 생성
    # owner는 수신자의 zk 주소로 설정
    transfer_note = Note(
        owner=to_address,
        value=value,
        type="0x0",  # 기본 토큰 타입
        viewKey="0x01", # 기본 뷰 키
        salt=web3.Web3.soliditySha3(['string'], ['transfer']).hex() # 솔리디티의 keccak256과 동일한 해시
    )
    
    return transfer_note


if __name__ == "__main__":
    # 예시: 비밀키와 수신자 주소로 트랜스퍼 노트 생성
    sk = "137215550892293264522532280805192033568"
    to_address = "zk2aGHYonwumtLAG7SNKjharksCP3r"
    value = "1000000000000000000"
    
    note = generate_transfer_note(sk, to_address, value)
    print(f"트랜스퍼 노트 해시: {note.getNoteHash()}")
    print(f"트랜스퍼 노트 Raw: {note.getNoteRaw()}")