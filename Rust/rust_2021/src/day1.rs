use std::fs;

pub fn day1a() -> String {
    let arr = read_data();

    println!("{:?}", arr);

    "> Day 1, OK".to_string()
}

fn read_data() -> Vec<i32> {
    let values = fs::read_to_string("assets/day1a.txt").expect("File error");

    let numbs: Vec<i32> =
        values
            .split('\n')
            .filter(|s| !s.is_empty())
            .map(|s| s.parse().unwrap()).collect();
    numbs
}