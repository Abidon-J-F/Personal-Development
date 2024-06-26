/*
This is an Aliens vs Humans Portfolio program.
Author: Abidon Jude Fernandes
Date: 04/2024 – 06/2024
*/

package aliens_vs_humans_portfolio;

import java.util.Random;

public class Entity extends Battlefield{
	
	private int health;
	private int weaponAccuracy;
	private int deflection;
	private boolean areYouAlive;
	
	public Entity(String name) {
		super(name);
		health = 1000;
		weaponAccuracy = defaultStat(100, 500);
		deflection = defaultStat(10, 60);
		areYouAlive = true;
	}	
	
	public int getHealth() {
		return health;
	}
		
	public void setHealth(int newHealth) {
		health = newHealth;
	}
	

	public boolean deleteHealth(int deletedHealth) {
		int newHealth = getHealth() - deletedHealth;
		
		if (newHealth <= 0) {
			setHealth(0);
			setEntityExistence(false);
			return false;
		} else {
			setHealth(newHealth);
			return true;
		}
	}

	public int getWeaponAccuracy() {
		return weaponAccuracy;
	}
	
	public void setWeaponAccuracy(int weaponAccuracy) {
		this.weaponAccuracy = weaponAccuracy;
	}
	
	public int getDeflection() {
		return deflection;
	}
	
	public void setDeflection(int deflection) {
		this.deflection = deflection;
	}
	

	public int defaultStat(int land, int sky) {
		Random random = new Random();
		
		int startingIntegerValue = random.nextInt(sky - land) + land;
		
		if (startingIntegerValue < 0) {
			startingIntegerValue = 0;
		} else if (startingIntegerValue > 100) {
			startingIntegerValue = 100;
		}
		
		return startingIntegerValue;
	}
	
	public boolean isEntityExistence() {
		return areYouAlive;
	}
	
	public void setEntityExistence(boolean areYouAlive) {
		this.areYouAlive = areYouAlive;
	}
	
	@Override
	public String toString() {
		return super.toString() + "\nHealth: " + getHealth() + "\nWeapon Accuracy: "
				+ getWeaponAccuracy() + "\nDeflection: " + getDeflection();
	}
	
}
