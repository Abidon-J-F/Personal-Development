/*
This is an Aliens vs Humans Portfolio program.
Author: Abidon Jude Fernandes
Date: 04/2024 – 06/2024
*/

package aliens_vs_humans_portfolio;

public class Battlefield {
	
	private String entityName;
	private String battlefieldID;
	
	public Battlefield(String name) {
		this.entityName = name;
		battlefieldID = null;
	}

	public String getEntityName() {
		return entityName;
	}

	public void setEntityName(String entityName) {
		this.entityName = entityName;
	}

	public String getBattlefieldID() {
		return battlefieldID;
	}

	public void setBattlefieldID(String battlefieldID) {
		this.battlefieldID = battlefieldID;
	}
	
	@Override
	public String toString() {
		return "Battlefield ID: " + battlefieldID + "\nEntity name: " + entityName;
	}
}
