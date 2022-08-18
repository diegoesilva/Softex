public class Server implements Computador{

    private String ram = "128 GB";
    private String hdd = "2000000 GB";
    private String cpu = "14.4 Ghz";
    private int type = 2;


    public Server(){} /* Construtor */

    public String getRam(){
        return this.ram;
    };
    public String getHDD(){
        return this.hdd;
    };
    public String getCPU(){
        return this.cpu;
    };
    public int getType(){
        return this.type;
    }
    public void createProduct() {
     
    }

    public String toString() {
        return "Server [CPU=" + cpu + ", HDD=" + hdd + ", RAM=" + ram + ", Type=" + type + "]";
    };
    
}
