public class Calculadora {
    private Strategy strategy;
    
    public void setStrategy(Strategy strategy){
        this.strategy = strategy;
    }
    public int executeStrategy(int a, int b){
        return strategy.executar(a, b);
    }
}
