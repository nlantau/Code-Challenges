//! nlantau, 2021-12-03
use std::cmp::max;
use itertools::{Itertools};
use transpose::*;

pub fn d3_2021_solution() {
    let fin = include_str!("../assets/d3_2021.txt");

    /*
    1. Most common for each bit = gamma rate
    2. Least common for each bit = epsilon rate
    3. gamma * epsilon = power consumption

    12-bit
     */

    let data: Vec<Vec<u32>> = fin
        .lines()
        .map(|l| l.chars().map(|c| c.to_digit(2).unwrap()).collect())
        .collect();

    let data_t: Vec<Vec<u32>> = transpose2(data);

    let ox: Vec<usize> = Vec::new();

    let occurs = data_t
        .iter()
        .map(|v| {
            let zero = v.iter().join("").matches('0').count();
            let one = v.iter().join("").matches('1').count();
            if zero > one {
                '0'
            } else {
                '1'
            }
        }
        ).join("");

    let gamma = isize::from_str_radix(&occurs, 2).unwrap();
    let epsilon = 0b1111_1111_1111 ^ gamma;




    println!("Gamma rate: {}", occurs);
    println!("Gamma rate: {}", gamma);
    println!("Epsilon rate: {}", epsilon);
    println!("Res: {}", gamma * epsilon);



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