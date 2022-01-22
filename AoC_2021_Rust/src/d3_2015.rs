//! nlantau, 2021-12-02
use itertools::Itertools;

pub fn d3_2015_solution() {
    let fin = include_str!("../assets/d3_2015.txt");
    let mut pos = (0, 0);
    let coordinates: Vec<(i32, i32)> = fin
        .chars()
        .map(|c| {
            match c {
                '^' => pos = (pos.0, pos.1 + 1),
                'v' => pos = (pos.0, pos.1 - 1),
                '>' => pos = (pos.0 + 1, pos.1),
                '<' => pos = (pos.0 - 1, pos.1),
                _ => {}
            };
            pos
        }).collect();

    // coordinates.iter().for_each(|(x, y)| println!("{},{}", x, y));

    let x = coordinates.into_iter().unique().count() + 1;
    println!("Day 3a: {}", x);
    assert_eq!(x, 2081);
}

















