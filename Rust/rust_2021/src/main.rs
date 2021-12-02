#![allow(unused_imports)]
#![allow(dead_code)]
#![allow(unused_variables)]

use rust_2021::d1_2015::*;
use rust_2021::d2_2015::*;
use rust_2021::day1::day1a;
use rust_2021::*;
use rust_2021::d1_2021::*;
use rust_2021::d2_2021::{d2_2021_solution, read_data_i32};


fn main() {
    //d2_2021_solution();
    read_data_i32();
}

fn prev_days() {
    println!("{}", solution_a());
    println!("{}", solution_b());
}

fn take_env_args() {
    let args: Vec<String> = std::env::args().collect::<Vec<String>>();
    let problem: &str = args.get(1).map(|s| s.as_str()).unwrap_or("None");

    let result: String = match problem {
        "day1a" => day1a(),
        "d1_2015a" => day1_2015a().to_string(),
        "d1_2015b" => day1_2015b().0.to_string()
            + ", "
            + &*day1_2015b().1.to_string(),
        "d2_2015" => day2(),
        _ => "What?".to_string(),
    };
    println!("{}", result);
}
