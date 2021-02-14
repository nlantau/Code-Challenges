// nlantau, 2021-02-14

fun points(games: List<String>): Int {
    var sum = 0
    games.forEach { scoreTable -> 
            if (scoreTable[0].toInt() > scoreTable[2].toInt()) {
                sum += 3
            } else if (scoreTable[0].toInt() == scoreTable[2].toInt()) {
                sum += 1
            } else {
                sum = sum
            }
        }
    return sum
}
