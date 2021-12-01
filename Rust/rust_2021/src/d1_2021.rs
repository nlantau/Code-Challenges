use std::fs::{self, File};

pub fn read_data() {
    let fin = fs::read_to_string("assets/d1_2021.txt").unwrap();
    let lines = fin
        .lines()
        .collect::<Vec<_>>();

    lines.iter().for_each(|c| println!("element: {}", c));
}