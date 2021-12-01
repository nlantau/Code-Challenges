use std::fs::{self, File};
use itertools::Itertools;

pub fn read_data() {
    let fin = fs::read_to_string("assets/d1_2021.txt").unwrap();
    let lines = fin
        .lines()
        .map(|c| c.parse().unwrap())
        .collect::<Vec<i32>>();

    //lines.iter().for_each(|c| println!("element: {}", c));

    let mut inc = 0;

    for n in 0..2000 {
        if lines.get(n) < lines.get(n + 1) {
            inc += 1;
        }
    }
    println!("{}", inc);

    let sum = lines.iter()
        .tuple_windows()
        .filter(|(a, b)| a < b)
        .count();

    println!("Day 1a: {}", sum);

    let sum2 = lines.iter()
        .tuple_windows::<(_, _, _)>()
        .map(|(a, b, c)| a + b + c)
        .tuple_windows()
        .filter(|(a, b)| a < b)
        .count();
    println!("Day 1b: {}", sum2);
    //dbg!(&sum2);


    let mut temp: i32 = 0;
    let mut inc2 = 0;

    for n in 0..2000 - 2 {
        let a = lines.get(n).unwrap()
            + lines.get(n + 1).unwrap() + lines.get(n + 2).unwrap();
        if a > temp {
            inc2 += 1;
        }
        temp = a;
    }
    println!("{}", inc2 - 1);
}