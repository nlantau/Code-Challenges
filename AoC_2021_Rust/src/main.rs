#![allow(unused_imports)]
#![allow(dead_code)]
#![allow(unused_variables)]

use rust_2021::d1_2015::*;
use rust_2021::d2_2015::*;
use rust_2021::day1::day1a;
use rust_2021::*;
use rust_2021::d10_2021::d10_2021_solution;
use rust_2021::d12_2021::d12_2021_solution;
use rust_2021::d13_2021::d13_2021_solution;
use rust_2021::d1_2021::*;
use rust_2021::d2_2021::{d2_2021_improved_solution, d2_2021_first_solution};
use rust_2021::d3_2015::d3_2015_solution;
use rust_2021::d3_2021::d3_2021_solution;
use rust_2021::d4_2021::d4_2021_solution;
use rust_2021::d5_2021::d5_2021_solution;
use rust_2021::d6_2021::d6_2021_solution;
use rust_2021::d7_2021::d7_2021_solution;
use rust_2021::d8_2021::d8_2021_solution;
use rust_2021::d9_2021::d9_2021_solution;
use rust_2021::playground::pass_reference_update_val;


fn main() {
    d13_2021_solution();
}

fn prev_days() {
    println!("{}", solution_a());
    println!("{}", solution_b());
    d2_2021_first_solution();
    d2_2021_improved_solution();
    d3_2015_solution();
    d3_2021_solution();
    //d4_2021_solution(); // Not finished part 1 nor 2
    d5_2021_solution();
    d6_2021_solution();
    d7_2021_solution();
    d8_2021_solution();
    d9_2021_solution();
    d10_2021_solution();
    // No d11 yet
    d12_2021_solution(); // Not completed
    pass_reference_update_val();
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
