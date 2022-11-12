// function calculateAvg(price1, price2) {
//   const sum = price1 + price2
//   console.log(`두 상품의 가격 총합은 ${sum}입니다.`)
//   const avg = sum / 2
//   return avg
// }

// const priceA = 1000
// const priceB = 2000
// const avg1 = calculateAvg(priceA, priceB)
// console.log(`A와 B의 평균은 ${avg1}입니다.`)

// const priceC = 2000
// const priceD = 3000
// const avg2 = calculateAvg(priceC, priceD)
// console.log(`C와 D의 평균은 ${avg2}입니다.`)

// quiz

function 라면별가격(a, b, c){
  const sum = a + b + c
  const avg = sum / 3
  return console.log(`라면은 평균 ${avg}원`)
}

라면별가격(4500, 6100, 5600)
// console.log(avg)

// 함수와 매개변수 활용하여 
function 라면평균가격(라면1, 라면2, 라면3) {
	const 평균 = (라면1 + 라면2 + 라면3) / 3
	return 평균
}

const 신라면 = 6200
const 진라면 = 4800
const 짜파게티 = 7000
const 오늘 = 라면평균가격(신라면, 진라면, 짜파게티)
console.log(`오늘의 라면 평균가격: ${오늘}`)