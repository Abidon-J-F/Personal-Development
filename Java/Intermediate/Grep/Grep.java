/*
This is a Grep program.
Author: Abidon Jude Fernandes
Date: 04/2024 – 04/2024
Description: Grep is a pattern-matching engine executable in most default terminal environments. 
It is capable of searching input files for matches to patterns, outputting any results to standard output.
*/

import java.util.regex.Pattern;
import java.util.regex.Matcher;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Grep {
  public Grep() {}
  
public static void main(String[] args) {
    String fName = "";
    File f;
    Scanner s;

    Pattern pattern = Pattern.compile("\\w*\\d+\\w*");

    String line;
    Matcher matcher;

    
    for (int fileNumber = 1; fileNumber <= 5; fileNumber++) {
      fName = "TestFile" + fileNumber + ".txt";
      try {
        f = new File(fName);
        s = new Scanner(f);
        
        while (s.hasNextLine()) {
          line = s.nextLine();
          matcher = pattern.matcher(line);

          if (matcher.find()) {
            System.out.println(fName + ":" + line);
          } 
        }
        s.close();
      } catch (FileNotFoundException e) {
        System.out.println("Problem opening file.");
        e.printStackTrace();
        return;
      }
    }

  }
}
