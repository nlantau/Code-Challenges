use std::fs::{self, File};




pub fn d2_2021_solution() {
    let solution = String::from("Hej");
    let v = read_data_i32();
    println!("{}", solution);
}




fn read_data_i32() -> Vec<i32> {
    let fin = fs::read_to_string("assets/d2_2021.txt").unwrap();
    let lines = fin
        .lines()
        .map(|c| c.parse().unwrap())
        .collect::<Vec<i32>>();
    lines
}
