public class App {

    public static void main(String[] args) {
        
        PublisherConcreto p = new PublisherConcreto();

        Subscriber s1 = new SubscriberConcreto();
        Subscriber s2 = new SubscriberConcreto();
        Subscriber s3 = new SubscriberConcreto();

        p.attach(s1);
        p.attach(s2);
        p.attach(s3);

        p.setEstado("Novo estado"); /* Exemplo de mudança de estado para testar notificações */

    }
    
}
