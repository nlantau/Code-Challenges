use std::time;
use std::cmp;

pub fn d7_2021_solution() {
    bench(part1);
    bench(part2);
    bench(part2_other);
}

fn bench(f: fn()) {
    let t0 = time::Instant::now();
    let ret = f();
    println!("Time used {:?}", time::Instant::now().duration_since(t0));
    ret
}

fn part2_other() {
    let fin = include_str!("../assets/d7_2021.txt")
        .split(',')
        .map(|n| n.parse::<i32>().unwrap())
        .collect::<Vec<i32>>();

    let (min, max) = fin
        .iter()
        .fold((i32::MAX, i32::MIN), |(min, max), pos| {
            (*pos.min(&min), *pos.max(&max))
        });

    println!("min: {}, max: {}", min, max);

    let mut best_cost = i32::MAX;
    for i in min..=max {
        let cost = fin.iter().fold(0, |accum, pos| {
            let n = (pos - i).abs();
            let c = n * (n + 1) / 2;
            //println!("{}", accum + c);
            accum + c
        });
        best_cost = best_cost.min(cost);
    }

    println!("{}", best_cost);
}

fn part2() {
    let fin = include_str!("../assets/d7_2021.txt")
        .split(',')
        .map(|n| n.parse::<i32>().unwrap())
        .collect::<Vec<i32>>();

    let mut bs = i32::MAX;
    for i in 0..fin.len() {
        let mut tups: Vec<(i32, i32)> = Vec::new();
        for j in 0..fin.len() {
            tups.push((fin[i], fin[j]));
        }
        let d = tups.iter().fold(0, |sum, v| {
            let t = (v.0 - v.1).abs() * ((v.0 - v.1).abs() + 1) / 2;
            sum + t
        });
        bs = bs.min(d);
    }
    println!("Part 2: {}", bs);
    //assert_eq!(bs, 356179);
}

fn part1() {
    let fin = include_str!("../assets/d7_2021.txt")
        .split(',')
        .map(|n| n.parse::<i32>().unwrap())
        .collect::<Vec<i32>>();

    let mut bs = i32::MAX;
    for i in 0..fin.len() {
        let mut tups: Vec<(i32, i32)> = Vec::new();
        for j in 0..fin.len() {
            tups.push((fin[i], fin[j]));
        }
        let d = tups.iter().fold(0, |sum, v| {
            sum + (v.0 - v.1).abs()
        });
        bs = bs.min(d);
    }
    println!("Part 1: {}", bs);
    assert_eq!(bs, 356179);
}
















