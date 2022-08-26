public class Carro extends Veiculo{

    public Carro(String modelo, String marca, String cor, int numeroRodas){ /* Construtor com parâmetros */
        this.modelo = modelo;
        this.marca = marca;
        this.cor = cor;
        this.numeroRodas = numeroRodas;
    }

    public Carro(){ /* Construtor sem parâmetros, pra facilitar a vida do programador */
        this.modelo = "Fusca";
        this.marca = "Volkswagen";
        this.cor = "Branco";
        this.numeroRodas= 4;

    }
   
    @Override
    public Veiculo clone() {
        Carro novo = new Carro();
        
        novo.setModelo(this.modelo);
        novo.setMarca(this.marca);
        novo.setCor(this.cor);
        novo.setNumeroRodas(this.numeroRodas);

        return novo;

    }
   
}