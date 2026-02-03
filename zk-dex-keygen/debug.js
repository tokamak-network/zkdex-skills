// debug.js - babyjubjub 객체 구조 디버깅

const { babyjubjub } = require('@noble/curves/misc.js');

console.log('🔍 babyjubjub 객체 구조 확인:');
console.dir(babyjubjub, { depth: 5 });

console.log('\n🔍 CURVE 존재 여부:', 'CURVE' in babyjubjub ? 'Yes' : 'No');
if (babyjubjub.CURVE) {
  console.log('🔍 Fp 존재 여부:', 'Fp' in babyjubjub.CURVE ? 'Yes' : 'No');
}