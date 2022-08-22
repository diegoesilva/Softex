public class Bicicleta extends Veiculo {

    public Bicicleta(){
        this.modelo = "T-Type";
        this.marca = "Caloi";
        this.cor = "Preta";
        this.numeroRodas= 2;
    }

    @Override
   public Veiculo clone() {
        Bicicleta novo = new Bicicleta();
        
        novo.setModelo(this.modelo);
        novo.setMarca(this.marca);
        novo.setCor(this.cor);
        novo.setNumeroRodas(this.numeroRodas);

        return novo;

    }
}
