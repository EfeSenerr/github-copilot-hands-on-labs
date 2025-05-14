    package com.mycompany.app;

    import java.io.IOException;
    import com.mycompany.app.StarWarsCharacterDTO;

    /**
     * Main application class
     */
    public class App {
        public static void main(String[] args) {
            System.out.println("Star Wars API Client");

            StarWarsAPI api = new StarWarsAPIImpl();

            try {
                System.out.println("Getting Luke Skywalker's information...");
                StarWarsCharacterDTO luke = api.getLukeSkywalker();
                System.out.println("Name: " + luke.getName());
                System.out.println("Height: " + luke.getHeight() + " cm");
                System.out.println("Mass: " + luke.getMass() + " kg");
                System.out.println("Hair color: " + luke.getHair_color());
                System.out.println("Eye color: " + luke.getEye_color());

                System.out.println("\nGetting Darth Vader's information...");
                StarWarsCharacterDTO vader = api.getDarthVader();
                System.out.println("Name: " + vader.getName());
                System.out.println("Height: " + vader.getHeight() + " cm");
                System.out.println("Mass: " + vader.getMass() + " kg");
                System.out.println("Hair color: " + vader.getHair_color());
                System.out.println("Eye color: " + vader.getEye_color());
            } catch (IOException | InterruptedException e) {
                System.err.println("Error: " + e.getMessage());
                e.printStackTrace();
            }
        }
    }