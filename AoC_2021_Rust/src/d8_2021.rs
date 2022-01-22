use std::time;

pub fn d8_2021_solution() {
    bench(part1);
}

fn bench(f: fn()) {
    let t0 = time::Instant::now();
    let ret = f();
    println!("Time used {:?}", time::Instant::now().duration_since(t0));
    ret
}

fn part1() {
    let ls2 = include_str!("../assets/d8_2021.txt")
        .lines()
        .collect::<Vec<&str>>()
        .iter()
        .map(|&line| {
            let (l, r) = line
                .trim()
                .split_once('|').unwrap();
            r
                .split_whitespace()
                .collect::<Vec<&str>>()
        })
        .flatten()
        .filter(|&l| {
            l.len() == 2 || l.len() == 3 || l.len() == 4 || l.len() == 7
        }).count();
    println!("Part 1: {:?}", ls2);
    assert_eq!(ls2, 369);
}