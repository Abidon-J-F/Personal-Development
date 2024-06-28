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
import aliens_vs_humans_portfolio.Humans;

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class TestHumans {
	
	private Humans testHumans;
	
	@BeforeAll
	public void testHumanGear() {
		testHumans = new Humans("test", "testHumansPlanet", 1);
	}

	@Test
	public void testHumansPlanet() {
		this.testHumans.setHumansPlanet("testHumansPlanet_2");
		assertEquals("testHumansPlanet_2", this.testHumans.getHumansPlanet());
	}
	
	@Test
	void testToString() {
		testHuman.setWeaponAccuracy(80);
		testHuman.setDeflection(40);
		assertEquals("ID: H-1 \nName: Test \nHealth: 1000 \nWeapon Accuracy: 80 \nDodge: 40" 
				+ "\nHumans Planet Base:   testHumansPlanet", testHumans.toString());
	}
}
