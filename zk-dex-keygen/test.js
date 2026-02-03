// test.js - zk-dex-keygen 모듈 테스트 스크립트

const { generateKeypair } = require('./index.js');

console.log('🔑 BabyJubJub 키 페어 생성 중... (noble-curves 기반)');
const { sk, pk } = generateKeypair();
console.log('\n✅ 생성 완료!');
console.log(`비밀키 (sk): [${Array.from(sk).join(', ')}]`);
console.log(`공개키 (pk): [${pk.map(coord => coord.toString()).join(', ')}]`);