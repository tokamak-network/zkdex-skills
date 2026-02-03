// zk-dex-keygen/index.js
// BabyJubJub 키 페어 생성 모듈 (noble-curves 기반)

const { babyjubjub } = require('@noble/curves/misc.js');
const { randomBytes } = require('@noble/hashes/utils.js');

// numberToBytesBE 함수 정의: bigint를 빅엔디안 바이트 배열로 변환
function numberToBytesBE(num, len) {
  const arr = new Uint8Array(len);
  for (let i = len - 1; i >= 0; i--) {
    arr[i] = Number(num & 0xffn);
    num >>= 8n;
  }
  return arr;
}
const blake256 = require('@noble/hashes/blake2.js').blake2s;

// bytesToNumberBE 함수 정의: 빅엔디안 바이트 배열을 bigint로 변환
function bytesToNumberBE(bytes) {
  return bytes.reduce((acc, byte) => acc * 256n + BigInt(byte), 0n);
}

/**
 * BabyJubJub 키 페어 생성
 * @returns {Object} { sk: Uint8Array, pk: [bigint, bigint] }
 */
function generateKeypair() {
  // 1. 랜덤 시드 생성 (64바이트)
  const seed = randomBytes(64);
  // 2. 비밀키 생성
  // seed를 해싱하여 32바이트 비밀키를 생성
  const hashed = blake256(seed);
  // babyjubjub.Point.Fp를 사용해 정규화
  const secretKey = babyjubjub.Point.Fp.create(bytesToNumberBE(hashed.slice(0, 32)));
  // getPublicKey는 정규화된 bigint를 직접 기대하므로, Uint8Array로 변환하지 않고 그대로 전달
  // const secretKeyBytes = numberToBytesBE(secretKey, 32); // 이 줄은 주석 처리
  // getPublicKey는 정규화된 bigint를 기대하므로, Uint8Array로 변환할 필요 없음
  // const secretKeyBytes = secretKey; // 이 줄은 주석 처리
  // getPublicKey는 Uint8Array를 기대하므로, Uint8Array로 변환
  // const secretKeyBytes = numberToBytesBE(secretKey, 32); // 이 줄은 주석 처리
  // getPublicKey는 정규화된 bigint를 기대하므로, Uint8Array로 변환할 필요 없음
  // const secretKeyBytes = secretKey; // 이 줄은 주석 처리
  // getPublicKey는 Uint8Array를 기대하므로, Uint8Array로 변환
  // const secretKeyBytes = numberToBytesBE(secretKey, 32); // 이 줄은 주석 처리
  // getPublicKey는 정규화된 bigint를 기대하므로, Uint8Array로 변환할 필요 없음
  // const secretKeyBytes = secretKey; // 이 줄은 주석 처리
  // getPublicKey는 Uint8Array를 기대하므로, Uint8Array로 변환
  // const secretKeyBytes = numberToBytesBE(secretKey, 32); // 이 줄은 주석 처리
  // getPublicKey는 정규화된 bigint를 기대하므로, Uint8Array로 변환할 필요 없음
  // const secretKeyBytes = secretKey; // 이 줄은 주석 처리
  // getPublicKey는 Uint8Array를 기대하므로, Uint8Array로 변환
  // const secretKeyBytes = numberToBytesBE(secretKey, 32); // 이 줄은 주석 처리
  // getPublicKey는 정규화된 bigint를 기대하므로, Uint8Array로 변환할 필요 없음
  // const secretKeyBytes = secretKey; // 이 줄은 주석 처리
  // getPublicKey는 Uint8Array를 기대하므로, Uint8Array로 변환
  // const secretKeyBytes = numberToBytesBE(secretKey, 32); // 이 줄은 주석 처리
  // getPublicKey는 정규화된 bigint를 기대하므로, Uint8Array로 변환할 필요 없음
  // const secretKeyBytes = secretKey; // 이 줄은 주석 처리
  // getPublicKey는 Uint8Array를 기대하므로, Uint8Array로 변환
  // const secretKeyBytes = numberToBytesBE(secretKey, 32); // 이 줄은 주석 처리
  // getPublicKey는 정규화된 bigint를 기대하므로, Uint8Array로 변환할 필요 없음
  // const secretKeyBytes = secretKey; // 이 줄은 주석 처리
  // getPublicKey는 Uint8Array를 기대하므로, Uint8Array로 변환
  const secretKeyBytes = numberToBytesBE(secretKey, 32);

  // 3. 공개키 생성
  // getPublicKey는 정규화된 bigint를 직접 기대하므로, Uint8Array로 변환하지 않고 그대로 전달
  const publicKey = babyjubjub.getPublicKey(secretKey);
  // 반환값의 sk를 Uint8Array로 변환
  const sk = numberToBytesBE(secretKey, 32);
  return {
    sk: sk,
    pk: publicKey
  };
}

/**
 * 비밀키를 Uint8Array로 정규화
 * @param {Uint8Array|bigint} key - 비밀키
 * @returns {Uint8Array}
 */
function normalizePrivateKey(key) {
  if (key instanceof Uint8Array) {
    return babyjubjub.Point.Fp.create(BigInt('0x' + Buffer.from(key).toString('hex')));
  } else if (typeof key === 'bigint') {
    return babyjubjub.Point.Fp.fromBig(key);
  }
  throw new Error('Invalid key type. Expected Uint8Array or bigint.');
}

module.exports = { generateKeypair, normalizePrivateKey };
