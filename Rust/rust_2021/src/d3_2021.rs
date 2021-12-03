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

    let gamma = usize::from_str_radix(&occurs, 2).unwrap();
    let epsilon = 0b1111_1111_1111 ^ gamma;


    println!("Gamma rate: {}", occurs);
    println!("Gamma rate: {}", gamma);
    println!("Epsilon rate: {}", epsilon);
    println!("Res: {}", gamma * epsilon);
    assert_eq!(gamma * epsilon, 3958484);

    part2(gamma, epsilon, &occurs);
}

fn part2(gamma: usize, epsilon: usize, str_gamma: &str) {
    println!("Part 2");
    let fin = include_str!("../assets/d3_2021.txt");
    let data: Vec<Vec<u32>> = fin
        .lines()
        .map(|l| l.chars().map(|c| c.to_digit(2).unwrap()).collect())
        .collect();

    let data_b: Vec<_> = data
        .iter()
        .map(|v| v.iter().join(""))
        .collect();

    data_b.iter().for_each(|s| println!("{}", s));

    let mut matched_vecs: Vec<&str> = Vec::new();

    for r in data_b.iter() {
       todo!();
    }

    /*
    oxygen generator rating: most common value
    CO2 scrubber rating:     least common value


     */












    /*
    loop {
        for v in data.iter() {
            s = v.iter().join("").parse::<usize>().unwrap() & shifter;
            let g = gamma & shifter;

            if s == g {
                matching_vecs += 1;
            }
            println!("{}", v.iter().join(""));
            panic!("TESTING");
        }
        if matching_vecs == 1 {
            println!("matching vec: {}", s);
            break;
        } else {
            matching_vecs = 0;
        }
        shifter = shifter >> 1;
        if shifter == 11 || shifter < 1{
            println!("Bad algo");
            break
        }
    }

     */

    /*
    let res = 0;
    for v in data.iter() {
        v.iter().for_each(|x| print!("{}", x));
        println!();
    }
     */
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