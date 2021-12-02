use std::fs::{self, File};
use itertools::Itertools;

pub fn d2_2021_solution() {
    let solution = String::from("Hej");
    let v = read_data_i32();
    let s = read_data_string();
    println!("{}", solution);
}


fn read_data_string() -> String {
    fs::read_to_string("assets/d2_2021.txt").unwrap()
}

pub fn read_data_i32() {
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

    println!("Day 2b: {}", hor * dep);
}
