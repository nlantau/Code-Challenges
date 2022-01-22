//! nlantau, 2021-12-03
use std::cmp::max;
use itertools::{Itertools};
use transpose::*;

pub fn d3_2021_solution() {
    part1();
    part2();
}

fn test_partition() {
    let mut oxygen: Vec<&str> = include_str!("../assets/d3_2021_test.txt").lines().collect();

    for i in 0..12 {
        if oxygen.len() == 1 { break; }
        let (ox1, ox0): (Vec<&str>, Vec<&str>) = oxygen
            .iter()
            .partition(|&line| {
                line.chars().nth(i).unwrap() == '1'
            });
        println!(" - New iteration -");
        ox1.iter().for_each(|&c| print!("{},", c));
        println!();
        ox0.iter().for_each(|&c| print!("{},", c));
        println!();

        oxygen = if ox1.len() >= ox0.len() { ox1 } else { ox0 }
    }
}

fn part1() {
    let data_t: Vec<Vec<u32>> = transpose2(include_str!("../assets/d3_2021.txt")
        .lines()
        .map(|l| l.chars().map(|c| c.to_digit(2).unwrap()).collect())
        .collect());

    let occurs = data_t
        .iter()
        .map(|v| {
            let zero = v.iter().join("").matches('0').count();
            let one = v.iter().join("").matches('1').count();
            if zero > one { '0' } else { '1' }
        }).join("");

    let gamma = usize::from_str_radix(&occurs, 2).unwrap();
    let epsilon = 0b1111_1111_1111 ^ gamma;

    println!("Part 1: {}", gamma * epsilon);
    assert_eq!(gamma * epsilon, 3958484);
}

fn part2() {
    let mut oxygen: Vec<&str> = include_str!("../assets/d3_2021.txt").lines().collect();
    let mut co2: Vec<&str> = oxygen.clone();

    for i in 0..12 {
        if oxygen.len() == 1 { break; }
        let (ox1, ox0): (Vec<&str>, Vec<&str>) = oxygen
            .iter()
            .partition(|&line| {
                line.chars().nth(i).unwrap() == '1'
            });
        oxygen = if ox1.len() >= ox0.len() { ox1 } else { ox0 }
    }
    for i in 0..12 {
        if co2.len() == 1 { break; }
        let (co0, co1): (Vec<&str>, Vec<&str>) = co2
            .iter()
            .partition(|&line| {
                line.chars().nth(i).unwrap() == '0'
            });
        co2 = if co0.len() <= co1.len() { co0 } else { co1 }
    }

    let oxy = isize::from_str_radix(oxygen[0], 2).unwrap();
    let co2 = isize::from_str_radix(co2[0], 2).unwrap();

    println!("Part 2: {}", oxy * co2);
    assert_eq!(oxy * co2, 1613181);
}

fn transpose2<T>(v: Vec<Vec<T>>) -> Vec<Vec<T>> {
    assert!(!v.is_empty());
    let len = v[0].len();
    let mut iters: Vec<_> = v.into_iter().map(|n| n.into_iter()).collect();
    (0..len)
        .map(|_| {
            iters
                .iter_mut()
                .map(|n| n.next().unwrap())
                .collect::<Vec<T>>()
        })
        .collect()
}

fn part1_unreadable() {
    let gamma = usize::from_str_radix(&transpose2(include_str!("../assets/d3_2021.txt")
        .lines()
        .map(|l| l.chars().map(|c| c.to_digit(2).unwrap()).collect())
        .collect()).iter().map(|v| {
        let zero = v.iter().join("").matches('0').count();
        let one = v.iter().join("").matches('1').count();
        if zero > one { '0' } else { '1' }
    }).join(""), 2).unwrap();

    println!("Part 1: {}", gamma * (0b1111_1111_1111 ^ gamma));
    assert_eq!(gamma * (0b1111_1111_1111 ^ gamma), 3958484);
}


