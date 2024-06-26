/*
This is an Aliens vs Humans Portfolio program.
Author: Abidon Jude Fernandes
Date: 04/2024 – 06/2024
*/

package aliens_vs_humans_portfolio;

public class Aliens extends Entity {
	
	private String aliensPlanet;

	public Aliens(String name, String aliensPlanet, int integer) {
		super(name);
		this.aliensPlanet = aliensPlanet;
		setBattlefieldID("A-" + integer);
	}

	public String getAliensPlanet() {
		return aliensPlanet;
	}

	public void setAliensPlanet(String aliensPlanet) {
		this.aliensPlanet = aliensPlanet;
	}
	
	@Override
	public String toString() {
		return super.toString() + "\nAliens Planet Base: " + getAliensPlanet();
	}
		
}
