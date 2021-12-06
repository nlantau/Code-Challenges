use std::collections::HashMap;

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