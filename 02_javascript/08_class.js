// 클래스 (Class)  선언
class 라면만들기 {
  constructor(맛, 면발, 가격) {
    this.맛 = 맛
    this.면발 = 면발
    this.가격 = 가격
    }
    
    재채기(){
      console.log(`${맛}스프가 코에 들어갔습니다! 에취!!!`)
    }
}

const 매운라면 = new 라면만들기('매움','보통', '4000')
매운라면.재채기()


class Notebook {
  constructor(name, price, company) {
    this.name = name
    this.price = price
    this.company = company
  }
}

// 클래스로 객체(Object) 타입 생성
const notebook1 = new Notebook('Macbook', 2000000, 'Apple')

console.log(notebook1)
console.log(notebook1.name)
console.log(notebook1.price)
console.log(notebook1.company)


// ----------------------------------------------------
// 클래스 선언과 메소드 정의

class Product {
  constructor(name, price) {
    this.name = name
    this.price = price
  }

  printInfo() {
    console.log(`name: ${this.name}, price: ${this.price}`)
  }
}

const notebook = new Product('Macbook', 200000)

notebook.printInfo()


// ----------------------------------------------------
// 객체 리터럴

const computer = {
  name : 'Macbook',
  price: 200000,
  printInfo: function () {
    console.log(`상품명: ${this.name}, 가격: ${this.price}`)
  }
}

computer.printInfo()



// ----------------------------------------------------



// quiz
class Ramen {
  constructor(name, hot, price) {
    this.name = name
    this.hot = hot
    this.price = price
  }

  printInfo(){
    console.log(`신상 라면 '${this.name}'입니다. ${this.hot}맵기로, 가격은 ${this.price}원 이에요~`)
  }
}

const shinRamen = new Ramen('쉰라면', '너무 매운', 2000)
const jjangRamen = new Ramen('짱라면', '안매운', 12000)
shinRamen.printInfo()
jjangRamen.printInfo()

const kimchi = {
  name: '민수네',
  size: 2,
  price: 20000,
  printInfo: function(){
    console.log(`${this.name}집 김치 ${this.size} 포기 입니다. ${this.price}에 팔아요.`)
  }
}
kimchi.printInfo();