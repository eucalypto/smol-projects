import org.junit.jupiter.api.DisplayName
import org.junit.jupiter.api.Nested
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.assertThrows
import kotlin.test.assertEquals

class TimeStampTest {

    @Test
    internal fun `create from string returns correct time in seconds`() {
        val timeStamp = TimeStamp.of("00:01:10")
        assertEquals(70, timeStamp.getTimeInSeconds())
    }

    @Test
    internal fun `create from different string returns correct time in seconds`() {
        val timeStamp = TimeStamp.of("01:00:01")
        val expectedSecondCount = 60 * 60 + 1
        assertEquals(expectedSecondCount, timeStamp.getTimeInSeconds())
    }

    @Test
    internal fun `create maximal valued TimeStamp`() {
        val timeStamp = TimeStamp.of("59:59:59")
        val secondCount = 59 * 60 * 60 + 59 * 60 + 59
        assertEquals("59:59:59", timeStamp.toString())
        assertEquals(secondCount, timeStamp.getTimeInSeconds())
    }

    @Test
    internal fun `throw WrongInput for illegal input`() {
        assertThrows<WrongInput> {
            TimeStamp.of("00:00:60")
        }
    }

    @Test
    internal fun `WrongInput check message and member string`() {
        val exception = assertThrows<WrongInput> {
            TimeStamp.of("00:00:60")
        }

        assert(exception.message!!.contains("00:00:60"))
        assertEquals("00:00:60", exception.illegalString)
    }

    @Test
    internal fun `shows correct formatted representation string with hours`() {
        val timeStamp = TimeStamp.of("02:00:00")
        assertEquals("02:00:00", timeStamp.toString())
    }

    @Test
    internal fun `shows correct formatted representation string with hours, and minutes`() {
        val timeStamp = TimeStamp.of("02:02:00")
        assertEquals("02:02:00", timeStamp.toString())
    }

    @Test
    internal fun `shows correct formatted representation string with hours, minutes, and seconds`() {
        val timeStamp = TimeStamp.of("02:02:02")
        assertEquals("02:02:02", timeStamp.toString())
    }

    @Nested
    @DisplayName("When time is added")
    inner class WhenTimeAdded {
        @Test
        internal fun `seconds are incremented`() {
            val timeStamp = TimeStamp.of("00:00:10")
            val laterTimeStamp = timeStamp.plus("00:00:03")

            assertEquals("00:00:13", laterTimeStamp.toString())
        }

        @Test
        internal fun `minutes are incremented when enough seconds add up`() {
            val timeStamp = TimeStamp.of("00:00:59")
            val laterTimeStamp = timeStamp.plus("00:00:01")

            assertEquals("00:01:00", laterTimeStamp.toString())
        }

        @Test
        internal fun `hours are incremented when enough minutes sum up`() {
            val timeStamp = TimeStamp.of("00:59:00")
            val laterTimeStamp = timeStamp.plus("00:01:00")

            assertEquals("01:00:00", laterTimeStamp.toString())
        }
    }

    @Nested
    @DisplayName("When time is subtracted")
    inner class WhenTimeSubtracted {
        @Test
        internal fun `seconds are decremented`() {
            val timeStamp = TimeStamp.of("00:00:13")
            val earlierTimeStamp = timeStamp.minus("00:00:03")
            assertEquals("00:00:10", earlierTimeStamp.toString())
        }
    }
}
