import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class generate_test {

    static Random random = new Random();
    static int bound = 4;   // grid size of game board, initialed is 4, i.e. easy
    static int num_files = 10000;
    static int num_lines = 500;

    public static void main(String[] args) {
        BufferedWriter writer = null;
        for (int i = 0; i < num_files; i ++) {
            // output generated files to `tests/`
            File file = new File("tests" + "//" + "at" + (i+1) + ".txt");
            try {
                file.createNewFile();
            } catch (IOException e) {
                e.printStackTrace();
            }
            try {
                writer = new BufferedWriter(new FileWriter(file));
                // generate commands
                for (int j = 0; j < num_lines; j++) {
                    int seed = random.nextInt(20);
                    if (seed == 0) {
                        writer.write(debug_gen());
                    }
                    else if (seed == 1 || seed == 2 || seed == 3){
                        writer.write ("undo");
                    }
                    else if (seed == 4 || seed == 5 || seed == 6){
                        writer.write("redo");
                    }
                    else if (seed == 7) {
                        writer.write("give_up");
                    }
                    else if (seed == 8){
                        writer.write(custom_gen());
                    }
                    else if (seed == 9){
                        // give up after each new_game command
                        writer.write(new_game_gen());
                        writer.newLine();
                        writer.write("give_up");
                    }
                    else if (seed < 15){
                        writer.write("fire(" + coordinate_gen() + ")");
                    }
                    else{
                        writer.write("bomb(" + coordinate_gen() + "," + coordinate_gen() + ")");
                    }
                    if (j != (num_lines-1)) {
                        writer.newLine();
                    }
                }
            } catch (IOException ex) {
            } finally {
                try {
                    writer.close();
                } catch (Exception ex) {
                }
            }
        }
    }
    static String debug_gen(){
        int level = random.nextInt(4);
        switch (level){
            default:
                bound = 4;
                return ("debug_test(easy)");
            case 1:
                bound = 6;
                return ("debug_test(medium)");
            case 2:
                bound = 8;
                return ("debug_test(hard)");
            case 3:
                bound = 12;
                return ("debug_test(advanced)");
        }
    }
    static String new_game_gen(){
        int level = random.nextInt(4);
        switch (level){
            default:
                return ("new_game(easy)");
            case 1:
                return ("new_game(medium)");
            case 2:
                return ("new_game(hard)");
            case 3:
                return ("new_game(advanced)");
        }
    }
    static String custom_gen(){
		/*
        // 4 <= grid_size <= 12
        int grid_size = random.nextInt(9) + 4;
        // (GRID_SIZE // 3) <= number_of_ships <= (GRID_SIZE // 2) + 1
        int number_of_ships = random.nextInt((grid_size/2)+1) + grid_size / 3;
        // NUMBER_OF_SHIPS * (NUMBER_OF_SHIPS + 1) // 2 <= max_shots <= (GRID_SIZE)^2
        int max_shots = random.nextInt(grid_size^2) + number_of_ships * (number_of_ships + 1)/2;
        // (GRID_SIZE // 3) <= n <= (GRID_SIZE // 2) + 1
        int number_of_bombs = random.nextInt((grid_size/2)+1) + grid_size / 3;
        // update grid size
        bound = grid_size;
        // error check
        if (number_of_ships > 7){
            while (number_of_ships > 7){
                number_of_ships = number_of_ships - 1;
            }
        }
        if (max_shots > 144){
            while (max_shots > 144){
                max_shots = max_shots - 1;
            }
        }
        if (number_of_bombs > 7){
            while (number_of_bombs > 7){
                number_of_bombs = number_of_bombs - 1;
            }
        }
		*/
		// GRID_SIZE = 4..12	
        int grid_size = random.nextInt(9) + 4;
        // NUMBER_OF_SHIPS = 1..7
        int number_of_ships = random.nextInt(7) + 1;
        // MAX_SHOTS = 1..144 
        int max_shots = random.nextInt(144) + 1;
        // NUMBER_OF_BOMBS = 1..7
        int number_of_bombs = random.nextInt(7) + 1;
        // update grid size
        bound = grid_size;
        return ("custom_setup_test (" + grid_size + "," + number_of_ships + "," + max_shots + "," + number_of_bombs + ")");
    }
    static String coordinate_gen () {
        int row = random.nextInt(bound);
        int col = random.nextInt(bound) + 1;
        switch (row) {
            default:
                return "[A," + col + "]";
            case 1:
                return "[B," + col + "]";
            case 2:
                return "[C," + col + "]";
            case 3:
                return "[D," + col + "]";
            case 4:
                return "[E," + col + "]";
            case 5:
                return "[F," + col + "]";
            case 6:
                return "[G," + col + "]";
            case 7:
                return "[H," + col + "]";
            case 8:
                return "[I," + col + "]";
            case 9:
                return "[J," + col + "]";
            case 10:
                return "[K," + col + "]";
            case 11:
                return "[L," + col + "]";
        }
    }
}
