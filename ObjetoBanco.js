/* Crie um código com um objeto chamado “Banco”. Ele deverá ter propriedades que incluem conta, saldo, 
tipo de conta e agência e os seus métodos devem ser: buscar saldo, depósito, saque e número da conta.

Observações:
- buscar saldo deve retornar o valor atual do saldo;
- para o depósito, você deverá passar um valor como parâmetro e adicioná-lo no saldo final do objeto;
- para o saque, você deverá passar um valor como parâmetro e subtraí-lo no saldo final do objeto;
- o número da conta deve retornar o número da conta. */

function Banco (conta, saldo, tipo_de_conta, agencia){
        this.conta = conta;
        this.saldo = saldo;
        this.tipo = tipo_de_conta;
        this.agencia = agencia;
        this.buscarSaldo = function(){
            return this.saldo;
        }
        this.saque = function(valor){
            if (valor > this.saldo){
                console.log("Saldo insuficiente.")
            }
            else{
                console.log("Saque efetuado com sucesso!")
                this.saldo -= valor
            }
        }
        this.deposito = function(valor){
            this.saldo += valor;
        }
        this.numeroConta = function(){
            return this.conta
             }
}


/*Instanciando e testando*/

let minhaConta = new Banco("15989-X", 15000, "F", "03.842")


console.log("Saldo:", minhaConta.buscarSaldo())
minhaConta.deposito(2750)
console.log("Novo saldo:", minhaConta.buscarSaldo())
minhaConta.saque(10000)
console.log("Novo saldo:", minhaConta.buscarSaldo())
console.log("Número da conta:", minhaConta.numeroConta())