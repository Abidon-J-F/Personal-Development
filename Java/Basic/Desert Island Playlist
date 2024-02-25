 /*
  This is a Desert Island Playlist program.
  Author: Abidon Jude Fernandes
  Date: 11/03/2022
  */

import java.util.ArrayList;

class Playlist {
  
  public static void main(String[] args) {
    ArrayList<String> desertIslandPlaylist = new ArrayList<String>();
    desertIslandPlaylist.add("Mozart - Eine kleine Nachtmusik");
    desertIslandPlaylist.add("Beethoven - Für Elise");
    desertIslandPlaylist.add("Mozart - Overture from The Marriage of Figaro");
    desertIslandPlaylist.add("J.S. Bach - Toccata and Fugue in D minor");
    desertIslandPlaylist.add("Beethoven - Symphony No.5 in C minor");
    desertIslandPlaylist.add("Grieg - In the Hall of the Mountain King from Peer Gynt Suite");

    System.out.println(desertIslandPlaylist);
    System.out.println(desertIslandPlaylist.size());
    desertIslandPlaylist.remove("Grieg - In the Hall of the Mountain King from Peer Gynt Suite");
    System.out.println(desertIslandPlaylist.size());
    System.out.println(desertIslandPlaylist);

    int indexA = desertIslandPlaylist.indexOf("Beethoven - Symphony No.5 in C minor");
    int indexB = desertIslandPlaylist.indexOf("Mozart - Overture from The Marriage of Figaro");
    
    String tempA = "Beethoven - Symphony No.5 in C minor";
    
    desertIslandPlaylist.set(indexA, "Mozart - Overture from The Marriage of Figaro");
    desertIslandPlaylist.set(indexB, tempA);
    
    System.out.println(desertIslandPlaylist);

  }
  
}
