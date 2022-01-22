use std::fs;

pub fn day1_2015b() -> (i32, usize) {
    let line: String = read_data();
    let mut score: i32 = 0;
    let mut res: usize = 0;
    let mut base: bool = false;

    for (i, ch) in line.chars().enumerate() {
        score = if ch == '(' { score + 1 } else { score - 1 };
        if score == -1 && !base {
            res = i + 1;
            base = true;
        }
    }
    (score, res)
}

// Don't really need this function.
// Keeping it for learning purposes
pub fn day1_2015a() -> i32 {
    let line = read_data();
    line
        .chars()
        .fold(0, |mut score, char| {
            match char {
                '(' => score += 1,
                ')' => score -= 1,
                _ => (),
            }
            score
        })
}

fn read_data() -> String {
    fs::read_to_string("assets/d1_2015.txt").unwrap()
}
