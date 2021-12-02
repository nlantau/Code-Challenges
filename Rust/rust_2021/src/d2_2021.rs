use std::fs::{self, File};
use itertools::Itertools;

pub fn d2_2021_improved_solution() {
    let fin = include_str!("../assets/d2_2021.txt");
    let l: Vec<(String, i32)> = fin
        .lines()
        .map(|c| c.split_whitespace().collect::<Vec<_>>())
        .map(|c| (c[0].to_string(), c[1].parse::<i32>().unwrap()))
        .collect();

    let (hora, deep, aima) = l
        .iter()
        .fold((0, 0, 0), |mut sum, (s, n)| {
            match s.as_str() {
                "forward" => {
                    sum.0 += n;
                    sum.1 += sum.2 * n;
                }
                "up" => sum.2 -= n,
                "down" => sum.2 += n,
                _ => ()
            };
            sum
        });


    println!("{}, {}, {}", hora, deep, aima);
    println!("Day 2b: {}", hora * deep);
}

pub fn d2_2021_first_solution() {
    let fin = fs::read_to_string("assets/d2_2021.txt").unwrap();

    let mut hor = 0;
    let mut dep = 0;
    let mut aim = 0;

    let l: Vec<_> = fin.split('\n').collect();

    for s in l.iter() {
        let x = s.split_at(s.find(' ').unwrap());
        let n = &x.1[1..].parse::<i32>().unwrap();
        match x.0 {
            "forward" => {
                hor += n;
                dep += aim * n;
            }
            "up" => {
                aim -= n;
            }
            "down" => {
                aim += n;
            }
            _ => ()
        };
    }

    println!("{}", hor);
    println!("Day 2b: {}", hor * dep);
}
