use std::fs;
use std::error::Error;

pub fn d7_2021_solution() {
    part1();
}

fn part1() {
    let fin = include_str!("../assets/d7_2021.txt")
        .split(',')
        .map(|n| n.parse::<i32>().unwrap())
        .collect::<Vec<i32>>();

    let mut bs = 999999;
    for i in 0..fin.len() {
        let mut tups: Vec<(i32, i32)> = Vec::new();
        for j in 0..fin.len() {
            tups.push((fin[i], fin[j]));
        }
        let d = tups.iter().fold(0, |sum, v| {
            sum + (v.0 - v.1).abs()
        });
        if bs > d {
            bs = d;
        }
    }
    println!("Part 1: {}", bs);
    assert_eq!(bs, 356179);
}
















