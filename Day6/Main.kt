import java.nio.file.Files
import java.nio.file.Paths
import kotlin.streams.toList

fun solution(input: String, segmentLength: Int) {
    var solution: Int = -1
    for (i in 0 until input.length - segmentLength) {
        val str = input.substring(i, i + segmentLength)
        val set = HashSet(str.chars().toList())
        if (set.size == str.length) {
            solution = i+segmentLength
            break
        }
    }
    println("Solution: $solution")
}

object Main {
    @JvmStatic
    fun main(args: Array<String>) {
        val input = Files.readString(Paths.get("./input.txt"))
        val startSegmentLength = 4
        val messageSegmentLength = 14
        solution(input, startSegmentLength)
        solution(input, messageSegmentLength)
    }
}
