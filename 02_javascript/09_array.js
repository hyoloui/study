// 배열 (Array)
const 무지개 = ['빨', '주', '노', '초', '파', '남', '보']

console.log(무지개[0])
console.log(무지개[1])
console.log(무지개[2])
console.log(무지개[3])
console.log(무지개[4])
console.log(무지개[5])
console.log(무지개[6])
console.log(무지개[7]) //undefined

//배열의 마지막 요소 꺼내기
console.log(무지개[무지개.length-1])


// ----------------------------------------------------


// push('추가할 요소') = 배열의 맨 마지막에 추가됨.
무지개.push('black')
console.log(무지개)


// ----------------------------------------------------


// pop() = 배열의 맨 마지막요소가 삭제됨.
무지개.pop()
console.log(무지개)


// ----------------------------------------------------

for (const 색 of 무지개){
  console.log(색)
}

// 배열과 반복문
const fruits = ['사과', '배', '감', '오렌지', '귤']
for (let i = 0; i < fruits.length; i++){
  console.log(fruits[i])
}


// 간단하게
for (const fruit of fruits){
  console.log(fruit)
}

// quiz

const pay = [5000,6000,3000,7000,8000,9000,2000,4000,1000,10000]
let total = 0

for (const p of pay){
  total += p
}

let avg = total / pay.length
console.log(`합계: ${total}, 평균: ${avg}`)
