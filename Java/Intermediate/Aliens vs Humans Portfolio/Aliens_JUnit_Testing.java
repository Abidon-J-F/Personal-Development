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
import aliens_vs_humans_portfolio.Aliens;


@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class TestAliens {
	
	private Aliens testAliens;
	
	@BeforeAll
	public void testAliensGear() {
		this.testAliens = new Aliens("test", "testAliensPlanet", 1);
	}

	@Test
	public void testAliensPlanet() {
		this.testAliens.setAliensPlanet("testAliensPlanet_2");
		assertEquals("testAliensPlanet_2", this.testAliens.getAliensPlanet());
	}
	
	@Test
	void testToString() {
		testAliens.setWeaponAccuracy(99);
		testAliens.setDeflection(90);
		assertEquals("ID: A-1 \nName: Test \nHealth: 1000 \nWeapon Accuracy: 99\nDeflection: 90" 
				+ "\nAliens Planet Base:    testAliensPlanet", testAliens.toString());
	}
}
