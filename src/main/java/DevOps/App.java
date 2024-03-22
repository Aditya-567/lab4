package DevOps;

public class App {
    public void greetings() {
        System.out.println("Hello World!");
    }

    public void greetings(String name) {
        System.out.println("Hello " + name + "!");
    }

    public static void main(String[] args) {
        App app = new App();
        app.greetings();
        app.greetings("DevOps");
    }
}
