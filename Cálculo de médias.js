/*Crie dois códigos de sistema de notas para uma escola. O primeiro código deve ser um programa que informa se o aluno reprovou, ou não, com base nas três notas que ele adicionou ao programa. Utilize, no mínimo, um operador de atribuição e um operador ternário. 
O segundo código é um programa que o aluno deve escrever duas notas e o retorno informa a nota mínima que ele deve tirar na próxima prova para poder passar com nota sete.*/

/*PROGRAMA 1*/
let n1 = parseFloat(prompt("Informe a primeira nota: "))
let n2 = parseFloat(prompt("Informe a segunda nota: "))
let n3 = parseFloat(prompt("Informe a terceira nota: "))

let media = (n1 + n2 + n3)/3
let resposta = media >= 7 ? "APROVADO": "REPROVADO"
console.log("\nResultado final:", resposta)

/*PROGRAMA 2*/

let nt1 = parseFloat(prompt("\nInforme a primeira nota: "))
let nt2 = parseFloat(prompt("Informe a segunda nota: "))
let md = 21-(nt1+nt2)

console.log("Nota necessária:", md)