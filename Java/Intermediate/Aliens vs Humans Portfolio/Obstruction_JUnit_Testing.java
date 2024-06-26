/*
This is an Aliens vs Humans Portfolio JUnit testing program.
Author: Abidon Jude Fernandes
Date: 04/2024 – 06/2024
*/

package aliens_vs_humans_portfolio;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;
import aliens_vs_humans_portfolio.Obstruction;

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class TestObstruction {
	
	private Obstruction testObstruction;
	private Obstruction testRandomObstruction;
	
	@BeforeAll
	public void testObstructionGear() {
		testObstruction = new Obstruction(Obstruction.type.Hurricane);
		testRandomObstruction = new Obstruction();
	}
	
	@Test
	void testObstructionType() {
		assertEquals(Obstruction.type.Hurricane, testObstruction.getObstructionType()); 
	}
	
	@Test
	void testObstructionBattlefieldID() {
		testObstruction.setObstructionType(Obstruction.type.Hurricane);
		assertEquals(" @ ", testObstruction.getBattlefieldID());
		assertEquals("Hurricane", testObstruction.getEntityName());
		
		testObstruction.setObstructionType(Obstruction.type.Earthquake);
		assertEquals(" % ", testObstruction.getBattlefieldID());
		assertEquals("Earthquake", testObstruction.getEntityName());
		
		testObstruction.setObstructionType(Obstruction.type.Volcano);
		assertEquals(" ^ ", testObstruction.getBattlefieldID());
		assertEquals("Volcano", testObstruction.getEntityName());
	}
	
	@Test
	void testRandomiseObstructionType() {
		boolean isHurricane = false;
		boolean isEarthquake = false;
		boolean isVolcano = false;
		boolean foundEverything = false;
		
		while(foundEverything == false) {
			while(isHurricane == false || isEarthquake == false || isVolcano == false) {
				testRandomObstruction = new Obstruction();
				
				if (testRandomObstruction.getObstructionType() == Obstruction.type.Hurricane) {
					isHurricane = true;
				} else if (testRandomObstruction.getObstructionType() == Obstruction.type.Earthquake) {
					isEarthquake = true;
				} else if (testRandomObstruction.getObstructionType() == Obstruction.type.Volcano) {
					isVolcano = true;
				}
			}
			
			foundEverything = true;
		}
		
		assertTrue(foundEverything);
	}
}
