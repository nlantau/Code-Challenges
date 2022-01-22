use std::fs::{self, File};
use itertools::Itertools;

pub fn solution_a() -> String {
    let d1a = read_data().iter()
        .tuple_windows()
        .filter(|(a, b)| a < b)
        .count();
    format!("Day 1a: {}", d1a)
}

pub fn solution_b() -> String {
    let d1b = read_data().iter()
        .tuple_windows::<(_, _, _)>()
        .map(|(a, b, c)| a + b + c)
        .tuple_windows()
        .filter(|(a, b)| a < b)
        .count();
    format!("Day 1b: {}", d1b)
}

fn read_data() -> Vec<i32> {
    let fin = fs::read_to_string("assets/d1_2021.txt").unwrap();
    let lines = fin
        .lines()
        .map(|c| c.parse().unwrap())
        .collect::<Vec<i32>>();
    lines
}