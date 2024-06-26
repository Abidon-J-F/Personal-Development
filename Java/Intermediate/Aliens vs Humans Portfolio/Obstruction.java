/*
This is an Aliens vs Humans Portfolio program.
Author: Abidon Jude Fernandes
Date: 04/2024 – 06/2024
*/

package aliens_vs_humans_portfolio;

import java.util.Random;

public class Obstruction extends Battlefield {
	
	public enum type {
		  Hurricane, 
		  Earthquake, 
		  Volcano
	}

	private type obstructionType;
	
	public Obstruction() {
		super(null);
		randomiseObstructionType();
	}
	
	public Obstruction(type type) {
		super(null);
		setObstructionType(type);
	}

	public type getObstructionType() {
		return obstructionType;
	}
	
	private void randomiseObstructionType() {
		Random random = new Random();
		
		int randomType = random.nextInt(3);
		
		switch(randomType) {
		case 0:
			setObstructionType(type.Hurricane);
			break;
		case 1:
			setObstructionType(type.Earthquake);
			break;
		case 2:
			setObstructionType(type.Volcano);
			break;
		}
	}
	
	public void setObstructionType(type obstructionType) {
		this.obstructionType = obstructionType;
		
		switch(obstructionType) {
		case Hurricane:
			this.setBattlefieldID(" @ ");
			setEntityName("Hurricane");
			break;
		case Earthquake:
			this.setBattlefieldID(" % ");
			setEntityName("Earthquake");
			break;
		case Volcano:
			this.setBattlefieldID(" ^ ");
			setEntityName("Volcano");
			break;
		}
	}
}
