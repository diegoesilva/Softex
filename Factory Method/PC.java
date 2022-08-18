public class PC implements Computador{

    private String ram = "16 GB";
    private String hdd = "500000 GB";
    private String cpu = "2.4 Ghz";
    private int type = 1;


    public PC(){} 

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
        return "PC [CPU=" + cpu + ", HDD=" + hdd + ", RAM=" + ram + ", Type=" + type + "]";
    };
    
}
