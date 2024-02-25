  /*
  This is a Mad Libs program which generates different stories
  Author: Abidon Jude Fernandes
  Date: 23/01/2022
  */

public class MadLibs {

    public static void main(String[] args){
      
      String name1 = "John";
      String adjective1 = "relaxed";
      String adjective2 = "beautiful";
      String adjective3 = "frightened";
      String verb1 = "shout";
      String noun1 = "Covenant";
      String noun2 = "Sangheili";
      String noun3 = "music";
      String noun4 = "Humans";
      String noun5 = "Farkas Lake";
      String noun6 = "Prophets";
      String name2 = "Cotana";
      int number = 2552;
      String place1 = "Reach";

      //The story
      String story = "This morning "+name1+" woke up feeling "+adjective1+". 'It is going to be a "+adjective2+" day!' Outside, a bunch of "+noun1+"s were protesting to keep "+noun2+" in stores. They began to "+verb1+" to the rhythm of the "+noun3+", which made all the "+noun4+"s very "+adjective3+". Concerned, "+name1+" texted "+name2+", who flew "+name1+" to "+place1+" and dropped "+name1+" in a puddle of frozen "+noun5+". "+name1+" woke up in the year "+number+", in a world where "+noun6+"s ruled the world.";

      System.out.println(story);
    }       
}
