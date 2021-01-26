package controller

import model.TimeStamp
import kotlin.streams.toList


class Controller {
    fun pipeArgs(args: Array<String>) {
        // java -jar timeshifter.jar 00:00:13 "00:00:34,00:01:00,01:01:03"
        subtractAndPrintTimeStamps(args[0], args[1])
    }

    private fun subtractAndPrintTimeStamps(subtractedAmountInput: String, timeStampsInput: String) {
        val timeStamps = TimeStamp.getListOf(timeStampsInput)
        val subtractedTimeStamps = timeStamps
            .stream()
            .map { timeStamp -> timeStamp.minus(subtractedAmountInput) }
            .toList()
        println(subtractedTimeStamps.joinToString(","))
    }


}
