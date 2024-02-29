 /*
  This Language Class is part of the Language Families program.
  Author: Abidon Jude Fernandes
  Date: 03/07/2022
  */
class Language {

  protected String name;
  protected int numSpeakers;
  protected String regionsSpoken;
  protected String wordOrder;
  
  Language(String langName, int speakers, String regions, String wdOrder) {
    this.name = langName;
    this.numSpeakers = speakers;
    this.regionsSpoken = regions;
    this.wordOrder = wdOrder;
  } 

   public void getInfo() {
    System.out.println(this.name + " is spoken by " + this.numSpeakers + " people mainly in " + this.regionsSpoken + ".");
    System.out.println("The language follows the word order: " + this.wordOrder);
    }

  public static void main(String[] args) {
    Language spanish = new Language("Italian", 68000000, "Italy, San Marino, Vatican City, Switzerland, Slovenia, Croatia", "subject-verb-object");
    spanish.getInfo();

    Mayan kiche = new Mayan("Ki'che'", 2330000);
    kiche.getInfo();

  SinoTibetan mandarin = new SinoTibetan("Mandarin Chinese", 1110000000);
  mandarin.getInfo();
  SinoTibetan burmese = new SinoTibetan("Burmese", 43000000);
  burmese.getInfo();
  }

}
