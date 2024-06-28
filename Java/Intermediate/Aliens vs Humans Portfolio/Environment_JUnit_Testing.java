package aliens_vs_humans_portfolio;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;
import aliens_vs_humans_portfolio.Environment;

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class TestEnvironment {
	
	private Environment testEnvironment;

	@BeforeAll
	public void testEnvironmentSetup() {
		testEnvironment = new Environment();
	}
	
	
	@Test
	void testCreateBattlefield() {
		testEnvironment.createBattlefield(50, 50);
		assertNotNull(testEnvironment.getEnvironment());
	}

}
