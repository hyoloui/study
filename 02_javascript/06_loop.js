// // 반복문

// // while 문
// let temperature = 20
// while (temperature < 25) {
// 	console.log(`${temperature}도 정도면 적당한 온도입니다.`)
// 	temperature++ // 증감연산자를 활용해서 온도를 변화시킵니다.
// }

// // for 문
// for (let temperature = 20; temperature < 25; temperature++){
// 	console.log(`${temperature}도 정도면 적당한 온도 입니다.`)
// }

// for (let number = 1; number <= 10; number++){
// 	if (number % 3 === 0){
// 		console.log(`${number}는 3으로 나눠서 떨어지는 숫자 입니다.`)
// 	}
// }

// quiz
for (let i = 1; i <= 20; i++){
	if(i % 2 === 0){
		console.log(`${i}는 짝수입니다.`)
	} else{
		console.log(`${i}는 홀수입니다.`)
	}
}