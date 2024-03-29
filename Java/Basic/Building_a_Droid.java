  /*
  This is a Droid program. It is designed to create new droids.
  Author: Abidon Jude Fernandes
  Date: 22/02/2022
  */

public class Droid {
  
  int batteryLevel;
  String name;
  
  public String toString(){
    return "Hello, I'm " + name + " the droid";
  }

  public Droid(String droidName) {
    name = droidName;
    batteryLevel = 100;
    System.out.println("Current Battery Level: " + batteryLevel);
  }

  public void performTask(String task){
    System.out.println(name + " is performing task: " + task);
    batteryLevel = batteryLevel - 10;
    System.out.println("Current Battery Level: " + batteryLevel);
  }

  public void energyReport(){
    System.out.println("Battery Level: " + batteryLevel);

  }

  public void energyTransfer(Droid transferEnergyDroid) {
    int tempVariable = transferEnergyDroid.batteryLevel;
    transferEnergyDroid.batteryLevel = this.batteryLevel;
    this.batteryLevel = tempVariable;
  }

  public static void main(String[] args) {
    Droid Codey = new Droid ("Codey");
    System.out.println(Codey);
    Codey.performTask("Running");
    Codey.energyReport();

    System.out.println(" ");

    Droid Bob = new Droid ("Bob");
    System.out.println(Bob);
    Bob.performTask("Swimming");
    Bob.performTask("Gaming");
    Bob.energyReport();

    System.out.println(" ");

    Codey.energyTransfer(Bob);
    //Bob.energyTransfer(Codey);
    Codey.energyReport();
    Bob.energyReport();
  }
}
