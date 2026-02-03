from zkdex_utils import Note, Account
import web3


def generate_redeem_note(owner_sk, value, token_type="0x0"):
    """
    환전(리딤)을 위한 리딤 노트를 생성합니다.
    """
    # 소유자 계정 생성
    owner_account = Account(owner_sk)
    owner_zk_address = owner_account.zkAddressFormat
    
    # 리딤 노트 생성
    # owner는 환전을 요청하는 사용자의 zk 주소
    redeem_note = Note(
        owner=owner_zk_address,
        value=value,
        type=token_type,
        viewKey="0x01", # 기본 뷰 키
        salt=web3.Web3.soliditySha3(['string'], ['redeem']).hex() # 고유한 솔트
    )
    
    return redeem_note


if __name__ == "__main__":
    # 예시: 비밀키와 가치로 리딤 노트 생성
    sk = "137215550892293264522532280805192033568"
    value = "1000000000000000000"
    token_type = "0x0" # 기본 토큰 타입
    
    note = generate_redeem_note(sk, value, token_type)
    print(f"리딤 노트 해시: {note.getNoteHash()}")
    print(f"리딤 노트 Raw: {note.getNoteRaw()}")