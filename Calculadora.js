/*Com os conceitos aprendidos, crie um programa de calculadora que: 

receba dois valores, que devem ser salvos em variáveis; 
o usuário deve colocar qual operador ele vai utilizar por meio dos símbolos aritméticos; 
com os dois valores e o operador definido, o programa deve fazer a operação e retornar o resultado; 
se houver divisão, você deve retornar o resultado e a sobra, caso haja alguma. */

let prompt = require('prompt-sync')();

let num1 = parseFloat(prompt("Informe um número: "))
let num2 = parseFloat(prompt("Informe outro número: "))
let op = prompt("Informe a operação desejada. \n\n+ para adição, \n- para subtração, \n* para multiplicação \n/ para divisão:  ")

switch (op) {
  case '+':
    console.log(num1+num2)
    break
  case '-':
    console.log(num1-num2)
    break
  case '*':
    console.log(num1*num2)
    break
  case '/':
    if (num2 == 0) {
      console.log("Impossível dividir por zero.")
      break }
    else if((num1%num2)!=0){
      	console.log("Resultado:",parseInt(num1/num2), "Resto:", num1%num2) }
    else
        console.log(num1/num2)
  }
