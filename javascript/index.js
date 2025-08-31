function abc(){
    console.log(abc.xyz)
}

abc()
abc.xyz = 400
abc.xyz = 200
abc()

const numbers = [1,2,3,4]
numbers[100]=500
console.log(numbers)

//console.log(typeof typeof 100)

const arr=[...'Praveen']
console.log(arr)

console.log(parseInt('10+2'))
console.log(parseInt('7FM'))  // 7, Cuando encuentra caracter invalido detiene la conversion
console.log(parseInt('M7F')) // NaN
console.log(parseInt('F1','16')) // 15*16 + 1*16^0 = 241