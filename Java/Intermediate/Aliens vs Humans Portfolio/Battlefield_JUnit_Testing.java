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
import aliens_vs_humans_portfolio.Battlefield;

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class TestBattlefield {
	
	private Battlefield testBattlefield;

	@BeforeAll
	void testBattlefieldGear() {
		testBattlefield = new Battlefield("Test");
	}

	@Test
	void testBattlefieldName() {
		testBattlefield.setEntityName("Name");
		assertEquals("Name", testBattlefield.getEntityName());
	}
	
	@Test
	void testToString() {
		testBattlefield.setBattlefieldID("Test");
		assertEquals("ID: Test \nName: test", testBattlefield.toString());
	}
}
