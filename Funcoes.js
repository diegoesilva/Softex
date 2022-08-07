let prompt = require('prompt-sync')();

function resultadoImc(imc){                                   /* Função padrão com retorno */
    if (imc < 18.5){
        return "Baixo peso"
    }
    else if (imc >= 18.5 && imc <=24.9){
        return "Peso normal"
    }
    else if (imc >= 25 && imc <=29.9){
        return "Excesso de peso"
    }
    else if (imc >= 30 && imc <=35){
        return "Obesidade"
    }
    else if (imc > 35){
        return "Obesidade extrema"
    }
}

let calcImc = (peso, altura) => peso/(altura*altura)        /* Função arrow */ 

function principal(){                                      /* Função padrão sem parâmetros */

    let peso = parseFloat(prompt("\nInforme seu peso: "))
    let altura = parseFloat(prompt("Informe sua altura: "))

    let imc = calcImc(peso, altura)

    console.log("Resultado:", resultadoImc(imc))
    

}

principal()