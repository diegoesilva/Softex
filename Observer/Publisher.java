import java.util.ArrayList;
import java.util.List;

public abstract class  Publisher{

    private List<Subscriber> subscribers = new ArrayList<>();

    public void attach(Subscriber s){
        this.subscribers.add(s);
    }

    public void detach(Subscriber s){
        this.subscribers.remove(s);
    }
    public void notifyObservers(){
        for (Subscriber subscriber : subscribers){
            subscriber.update();
        }
    }

}