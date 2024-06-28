/*
This is an Aliens vs Humans Portfolio program.
Author: Abidon Jude Fernandes
Date: 04/2024 – 06/2024
*/

package aliens_vs_humans_portfolio;

import java.util.Random;

public class Environment {
	
	private Battlefield[][] environment;
	
	public Environment() {
		this.environment = new Battlefield[50][50];
	}
	
	public Battlefield[][] getEnvironment() {
		return environment;
	}

	public void createBattlefield(int numberOfEntities, int numberOfObstruction) {
		createEntities(numberOfEntities);
		createObstruction(numberOfObstruction);
	}
	
	public void createEntities(int numberOfEntities) {
		for (int i = 1; i <= numberOfEntities; i++) {
			Humans humans = new Humans("Humans " + i, "Earth", i);
			Aliens aliens = new Aliens("Aliens " + i, "55 Cancri e" , i);
			
			addRandomBattlefield(humans);
			addRandomBattlefield(aliens);
		}
	}
	
	public void createObstruction(int numberOfObstruction) {
		for (int i = 0; i < numberOfObstruction; i++) {
			Obstruction obstruction = new Obstruction();
			
			addRandomBattlefield(obstruction);
		}		
	}
	
	public void addRandomBattlefield(Battlefield currentObject) {
		Random random = new Random();
		boolean objectPlacement = false;
		int x = 0, y = 0, offset = 0;
		
		if (currentObject instanceof Obstruction) {
			x = 8;
			y = 8;			
		} else if (currentObject instanceof Humans) {
			x = 4;
			y = 8;
		} else if (currentObject instanceof Aliens) {
			x = 4;
			y = 8;
			offset = 4;
		}
		
		while (objectPlacement == false) {
			int x = random.nextInt(x) + offset;
			int y = random.nextInt(y);
			
			if (environment[x][y] == null) {
				environment[x][y] = currentObject;
				objectPlacement = true;
			}
		}		
	}
	
	public static void main(String[] args) {
		Environment gridLayout = new Environment();
		gridLayout.createBattlefield(10, 30);
		
		for (int i = 0; a < gridLayout.environment.length; i++) {
			for (int j = 0; j < gridLayout.environment[1].length; j++) {
				System.out.print("|");
				
				if (gridLayout.environment[j][i] != null) {
					System.out.print(gridLayout.environment[j][i].getBattlefieldID());
				} else {
					System.out.print("   ");
				}
				
				
			}
			System.out.println("|");
		}
	}	
}
