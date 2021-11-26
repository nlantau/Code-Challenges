use std::fs;

pub fn day1_2015() -> i32 {
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
