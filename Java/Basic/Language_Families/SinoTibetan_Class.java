 /*
  This Sino-Tibetan Class is part of the Language Families program.
  Author: Abidon Jude Fernandes
  Date: 03/07/2022
  */

class SinoTibetan extends Language {
  SinoTibetan(String languageName, int speakers) {
    super(languageName, speakers, "Asia", "subject-object-verb");
    if (languageName.contains("Chinese")) {
      this.wordOrder = "subject-verb-object";
    }
  }
}
