/* Desenvolva um código e crie nele:

- um objeto com, no mínimo, três propriedades;
- um array de tamanho três no mínimo;
- duas funções, a primeira lista as propriedades do objeto e a segunda, os elementos do array.*/

let cachorro = {Nome: "Rex",
               Raça: "Vira-lata",
               Idade: 13}

let array = [1,1,2,3,5,8,13,21]

function listar(objeto){
  for (let i in objeto){
    console.log(i)
  }
}

function varrer(array){
  for(let i of array){
    console.log(i)
  }
}

/* Testando funções */

listar(cachorro); 
varrer(array);