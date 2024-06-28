/*
This is an Aliens vs Humans Portfolio program.
Author: Abidon Jude Fernandes
Date: 04/2024 – 06/2024
*/

package aliens_vs_humans_portfolio;

public class Humans extends Entity {
	
	private String humansPlanet;
	
	public Humans(String name, String humansPlanet, int integer) {
		super(name);
		this.humansPlanet = humansPlanet;
		setBattlefieldID("H-" + integer);
	}

	public String getHumansPlanet() {
		return humansPlanet;
	}

	public void setHumansPlanet(String humansPlanet) {
		this.humansPlanet = humansPlanet;
	}
	
	@Override
	public String toString() {
		return super.toString() + "\nHumans Planet Base: " + getHumansPlanet();
	}
}
