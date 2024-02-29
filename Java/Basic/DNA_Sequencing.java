 /*
  This is a DNA Sequencing program.
  Author: Abidon Jude Fernandes
  Date: 06/06/2022
  */

public class DNA {
  
  public static void main(String[] args) {
             
    //  -. .-.   .-. .-.   .
    //    \   \ /   \   \ / 
    //   / \   \   / \   \  
    //  ~   `-~ `-`   `-~ `-
    String dna1 = "ATGCGATACGCTTGA";
    String dna2 = "ATGCGATACGTGA";
    String dna3 = "ATTAATATGTACTGA";

    //String dna = dna1;
    //String dna = dna2;
    String dna = dna3;
    
    int length = dna.length();
    System.out.println("Length: " + length);

    int beginning = dna.indexOf("ATG");
    System.out.println("Start: " + beginning);

    int end = dna.indexOf("TGA");
    System.out.println("Start: " + end);

    if (beginning != -1 && 
        end != -1 && 
        (end - beginning) % 3 == 0){
      
    String protein = dna.substring(beginning, end+3); 
    System.out.println("Protein: " + protein);    
    } else {
    System.out.println("No protein.");
    }
  }
}
