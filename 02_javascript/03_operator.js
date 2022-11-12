// 연산자

// 문자열 이어붙이기
console.log('My' + " car")
console.log('1' + 2)
console.log(1 + 2)

// + 템플릿 리터럴
const shoesPrice = 200000
console.log('이 신발의 가격은 ' + shoesPrice + '원 입니다.')
console.log(`이 신발의 가격은 ${shoesPrice}원 입니다.`) // 이게 템플릿 리터럴 - 위와 같음


// -------------------------------------------------------------


// 산술 연산자 (Numeric operators)
console.log(2 + 1)
console.log(2 - 1)
console.log(2 * 3)
console.log(4 / 2)
console.log(10 % 3)
console.log(10 ** 2)


// -------------------------------------------------------------


// 증감 연산자 (Increment and Decrement operators)
// let count = 1
// const preIncrement = ++count
// console.log(`count: ${count}, preIncrement: ${preIncrement}`)

let num = 10
const postnum = num++

console.log(`num: ${num}, postCount: ${postnum}`)


// -------------------------------------------------------------


// 대입연산자 (Assignment operators)
const shirtsPrice = 100000
const pantsPrice = 80000
let totalPrice = 0

totalPrice += shirtsPrice // totalPrice = totalPrice + shirtsPrice 와 동일
console.log(totalPrice)
totalPrice += pantsPrice // totalPrice = totalPrice + pantsPrice 와 동일 
console.log(totalPrice)

totalPrice -= shirtsPrice // totalPrice = totalPrice - shirtsPrice 와 동일
console.log(totalPrice) 