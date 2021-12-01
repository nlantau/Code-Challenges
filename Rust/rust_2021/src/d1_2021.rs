use std::fs::{self, File};
use itertools::Itertools;

pub fn read_data() {
    let fin = fs::read_to_string("assets/d1_2021.txt").unwrap();
    let lines = fin
        .lines()
        .map(|c| c.parse().unwrap())
        .collect::<Vec<i32>>();

    let d1a = lines.iter()
        .tuple_windows()
        .filter(|(a, b)| a < b)
        .count();

    let d1b = lines.iter()
        .tuple_windows::<(_, _, _)>()
        .map(|(a, b, c)| a + b + c)
        .tuple_windows()
        .filter(|(a, b)| a < b)
        .count();

    println!("Day 1a: {}", d1a);
    println!("Day 1b: {}", d1b);
}