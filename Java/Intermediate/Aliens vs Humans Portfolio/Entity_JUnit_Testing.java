package aliens_vs_humans_portfolio;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;
import aliens_vs_humans_portfolio.Entity;

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class TestEntity {
	
	private Entity testEntity;
	
	@BeforeAll
	public void testEntityGear() {
		this.testEntity = new Entity("test");
	}

	@Test
	public void testEntityName() {
		this.testEntity.setEntityName("name");
		assertEquals("name", this.testEntity.getEntityName());
	}

	@Test
	public void testHealth() {
		this.testEntity.setHealth(90);
		assertEquals(90, this.testEntity.getHealth());
		
		this.testEntity.removeHealth(70);
		assertEquals(20 , this.testEntity.getHealth());
		
		this.testEntity.removeHealth(1000);
		assertEquals(0 , this.testEntity.getHealth());
	}
	
	@Test
	public void testWeaponAccuracy() {
		int currentAccuracy = 0;
		
		for (int i = 0; i < 500; i++) {
			this.testEntity.setWeaponAccuracy(this.testEntity.defaultStat(100, 500));
			currentAccuracy = this.testEntity.getWeaponAccuracy();
			
			assertTrue((currentAccuracy >= 100) && (currentAccuracy <= 500));
		}		
	}
	
	@Test
	public void testDeflection() {
		int currentDeflection = 0;
		
		for (int i = 0; i < 500; i++) {
			this.testEntity.setDeflection(this.testEntity.defaultStat(10, 60));
			currentDodge = this.testEntity.getDeflection();
			
			assertTrue((currentDeflection >= 10) && (currentDeflection <= 60));
		}		
	}
	
	@Test
	public void testDefaultStat() {
		int currentDefaultStat = 0;
		
		for (int i = 0; i < 500; i++) {
			currentDefaultStat = this.testEntity.DefaultStat(-100, 500);
			
			assertTrue((currentDefaultStat >= 0) && (currentDefaultStat <= 100));
		}
	}
	
	@Test
	public void testAreYouAlive() {
		this.testEntity.deleteHealth(300);
		assertEquals(false, this.testEntity.isEntityExistence());
		
		this.testEntity.setEntityExistence(true);
		assertEquals(true, this.testEntity.isEntityExistence());
	}
	
	@Test
	void testToString() {
		testEntity.battlefieldID("TestField");
		testEntity.setHealth(1000);
		testEntity.setWeaponAccuracy(90);
		testEntity.setDeflection(70);
		assertEquals("ID: TestField \nName: Test \nHealth: 1000 \nWeapon Accuracy: 90\nDeflection: 70"
		, testEntity.toString());
	}
}
