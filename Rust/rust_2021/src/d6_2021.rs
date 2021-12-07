use std::collections::HashMap;
use std::fs::File;
use std::io::{BufReader, Lines};
use cached::proc_macro::cached;

pub fn d6_2021_solution() {
    part1();
    part2();
}

fn part1() {
    let data = include_str!("../assets/d6_2021.txt")
        .split(',').map(|d| d.parse::<usize>().unwrap()).collect::<Vec<usize>>();
    let sample = include_str!("../assets/d6_2021_test.txt")
        .split(',').map(|d| d.parse::<usize>().unwrap()).collect::<Vec<usize>>();

    let ages = data.clone();
    let days = 80 + 1;

    let mut fishes: HashMap<usize, Vec<usize>> = HashMap::new();
    fishes.insert(0, ages);

    for day in 1..days {
        let temp = fishes[&(day - 1)].clone();
        let mut new_timers = temp.clone();

        for (i, timer) in temp.iter().enumerate() {
            if *timer == 0 {
                new_timers.push(8);
                new_timers[i] = 6;
            } else {
                new_timers[i] -= 1;
            }
        }
        fishes.insert(day, new_timers);
    }

    println!("Part 1: {}", fishes[&(days - 1)].len());
    assert_eq!(fishes[&(days - 1)].len(), 380612);
}


fn part2() {
    let data = include_str!("../assets/d6_2021.txt");
    let sample = include_str!("../assets/d6_2021_test.txt");


    let mut fishes = [0usize; 9];
    for fish in data.split(',').map(|s| s.parse::<usize>().unwrap()) {
        fishes[fish] += 1;
    }
    let days = 256;

    for day in 0..days {
        fishes[(day + 7) % 9] += fishes[day % 9];
    }
    println!("Part 2: {}", fishes.into_iter().sum::<usize>());
    assert_eq!(fishes.into_iter().sum::<usize>(), 1710166656900);
}

/*
Other people's solutions
 */
fn rounds(lines: Lines<BufReader<File>>, rounds: usize) -> Result<u128, Box<dyn std::error::Error>> {
    let mut new;

    let mut old = vec![0u128; 9];
    // reads file, splits on ',', and increments position 0 through 8.
    lines.for_each(|x| x.unwrap().split(',').filter_map(|x| x.parse::<usize>().ok()).for_each(|x| old[x] += 1));

    for _ in 0..rounds {
        new = vec![0; 9];
        // .rev() is important, as it needs to do 0 last.
        for (i, &val) in old.iter().enumerate().rev() {
            match i {
                1..=8 => new[i - 1] = val,
                0 => {
                    new[6] += val;
                    new[8] += val;
                }
                _ => unreachable!()
            }
        }
        // i love ownership
        old = new;
    }
    Ok(old.iter().fold(0, |tot, x| tot + x))
}


#[cached]
fn fish(days: u64, state: u32) -> u64 {
    if days == 0 {
        1
    } else if state == 0 {
        fish(days - 1, 6) + fish(days - 1, 8)
    } else {
        fish(days - 1, state - 1)
    }
}

fn solve_v2(input: &str, days: u64) -> u64 {
    input
        .trim()
        .split(',')
        .map(str::parse::<u32>)
        .map(Result::unwrap)
        .map(|age| fish(days, age))
        .sum()
}