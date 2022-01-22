use std::time;

pub fn d12_2021_solution() {
    bench(part1);
}

fn bench(f: fn()) {
    let t0 = time::Instant::now();
    let ret = f();
    println!("Time used {:?}", time::Instant::now().duration_since(t0));
    ret
}

#[allow(unused_mut)]
fn part1() {
    /*
    A path begins at 'start' and finished at 'end'
     */
    let rmap: Vec<(&str, &str)> = include_str!("../assets/d12_2021_test_2.txt")
        .lines()
        .map(|line| line.split_once('-').unwrap()).collect();

    println!("{:?}", rmap);
    /*
    TODO: For each 'start' find all paths to 'end'
    TODO: For each tuple
     */
    let mut paths: Vec<Vec<(&str, &str)>> = Vec::new();
    let mut path: Vec<(&str, &str)> = Vec::new();

    for (index, &(left, right)) in rmap.iter().enumerate() {
        match (left, right) {
            ("start", _) => {
                println!("1: {} {}", left, right);
                path.push((left, right));
            },
            (_, "start") => {
                println!("2: {} {}", left, right);
                path.push((right, left));
            },
            _ => println!(),
        }

    }
}