/**
 * This is JUnit that tests the methods of the Clock.
 * This contains 2 testcases.
 * 
 * Please don't run this file.
 * You can add your own test cases to this file by just copy and 
 * paste the last three lines of the code (TestCase2).
 * 
 * @author: Deepak
 */

import org.junit.Test;
import static org.junit.Assert.assertEquals;

import java.beans.Transient;

public class TestJUnit {

   @Test
   public void testCase1() {
      EggCartons s = new EggCartons();
      assertEquals("1.", 0, s.eggCartons(0));
      assertEquals("2.", 1, s.eggCartons(12));
      assertEquals("3.", 3, s.eggCartons(25));
    }

   @Test
   public void testCase2() {
      EggCartons s = new EggCartons();
      assertEquals("1.", 1, s.eggCartons(10));
      assertEquals("2.", 2, s.eggCartons(13));
      assertEquals("3.", 2, s.eggCartons(24));  
   }
}