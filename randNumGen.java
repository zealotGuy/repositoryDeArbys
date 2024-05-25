// wow its some java code which i spent some time working on
// this is actually my first official java "project" as i only did smaller stuff before

import java.util.Random;
import java.util.Scanner;
class Main {
  public static boolean numero_or_not(String input){
    try{
      Integer.parseInt(input);
      return true;
    }
    catch(NumberFormatException e){
      return false;
    }
  }
  public static void main(String[] args) {
    Random rand = new Random();
    int level = 1;
    int roll = rand.nextInt(1,1000);
    int roll1 = Integer.valueOf(roll);
    roll1 = roll;
    
    Integer.toString(roll1);
    Scanner scan1 = new Scanner(System.in);
    boolean start = true;
    int guesses = 20;
    while (start == true) {
      if (level == 1){
        roll = rand.nextInt(1,1000);
      }
      if (level == 2){
        roll = rand.nextInt(1,500);
      }
      if (level == 3){
        roll = rand.nextInt(1,100);
      }
      if (level == 4){
        System.out.println("Good job, you beat the game!");
        System.out.println("Now get out.");
        break;
      }
      String playerGuess = "";
      while (true) {
        if (level == 1){
          System.out.println("Guess a number between 1-1000, but you have 20 guesses.");
        }
        else if (level == 2){
          System.out.println("Guess a number between 1-500, but you have 15 guesses.");
        }
        else if (level == 3){
          System.out.println("Guess a number between 1-100, but you have 10 guesses.");
        }
        playerGuess = scan1.nextLine();
        if (numero_or_not(playerGuess) == true) {
          break;
        }
        else {
          System.out.println("Please enter an actual number please.");
        }
      }
        int guess = Integer.valueOf(playerGuess);
      if (guess == roll1) {
        System.out.println("You guessed the number!");
        Scanner scan3 = new Scanner(System.in);
        System.out.println("Would you like to play again? (y/n)");
        String playAgain1 = scan3.nextLine();
        if (playAgain1.equals("y")) {
          level += 1;
          if (level == 2){
            roll1 = rand.nextInt(1,500);
            guesses = 15;
          }
          else if (level == 3){
            roll1 = rand.nextInt(1,100);
            guesses = 10;
          }
          
          print4lines();     
          continue;
          }
        if (playAgain1.equals("n")){
          start = false;
          System.out.println("Thanks for playing!");
          }
        }  
      else if (guess > roll1) {
        System.out.println("Your guess was too high.");
        guesses -= 1;
        System.out.println("You have " + guesses + " guesses left.");
      }
      else {
        System.out.println("Your guess was too low.");
        guesses = guesses - 1;
        System.out.println("You have " + guesses + " guesses left.");
      }
      
      if (guesses == 0) {
        System.out.println("You ran out of guesses.");
        Scanner scan2 = new Scanner(System.in);
        System.out.println("Would you like to play again? (y/n)");
        String playAgain = scan2.nextLine();
        if (playAgain.equals("y")) {
          guesses = 10;
          print4lines();
          if (level == 1){
            roll1 = rand.nextInt(1,1000);
            guesses = 20;
          }
          if (level == 2){
            roll1 = rand.nextInt(1,500);
            guesses = 15;
          }
          if (level == 3){
            roll1 = rand.nextInt(1,100);
            guesses = 10;
          }
        }
        if (playAgain.equals("n")){
          start = false;
          System.out.println("Thanks for playing!");
        }
      }
    }
  }   
  static void print4lines() {
    System.out.println("");
    System.out.println("");
    System.out.println("");
    System.out.println("");
  }
}
