class TimeStamp private constructor(private val secondCount: Int) {
    fun getTimeInSeconds(): Int {
        return secondCount
    }

    companion object {
        fun of(timeString: String): TimeStamp {
            val secondsCount = secondsFromString(timeString)
            return TimeStamp(secondsCount)
        }

        private const val SECONDS_IN_MINUTE = 60
        private const val SECONDS_IN_HOUR = 60 * 60

        private fun secondsFromString(timeString: String): Int {
            val (hours, minutes, seconds) = getHoursMinutesSecondsFromString(timeString)

            val overallSeconds = hours * SECONDS_IN_HOUR +
                    minutes * SECONDS_IN_MINUTE +
                    seconds
            return overallSeconds
        }

        private fun getHoursMinutesSecondsFromString(timeString: String): IntArray {
            val (hours, minutes, seconds) = timeString.split(":").map { str -> str.toInt() }

            if (minutes >= 60 || seconds >= 60) {
                throw WrongInput(timeString)
            }

            return intArrayOf(hours, minutes, seconds)
        }
    }


    override fun toString(): String {
        val hours = getHours()
        val minutes = getMinutes()
        val seconds = getSeconds()
        return "%02d:%02d:%02d".format(hours, minutes, seconds)
    }

    private fun getHours(): Int {
        return secondCount / SECONDS_IN_HOUR
    }

    private fun getMinutes(): Int {
        val secondCountWithoutFullHours = secondCount % SECONDS_IN_HOUR
        return secondCountWithoutFullHours / SECONDS_IN_MINUTE
    }

    private fun getSeconds(): Int {
        return secondCount % SECONDS_IN_MINUTE
    }

    fun plus(s: String): TimeStamp {
        val difference = of(s)
        val newSecondsCount = secondCount + difference.secondCount
        return TimeStamp(newSecondsCount)
    }

    fun minus(s: String): TimeStamp {
        val difference = of(s)
        val newSecondsCount = secondCount - difference.secondCount
        return TimeStamp(newSecondsCount)
    }

}

class WrongInput(val illegalString: String) :
    IllegalArgumentException("\"$illegalString\" could not be parsed into time!") {
}
