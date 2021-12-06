use itertools::{Itertools};

pub fn d5_2021_solution() {
    part1();
    part2();
}

#[allow(clippy::comparison_chain)]
fn part2() {
    let mut grid: [[i32; 1000]; 1000] = [[0; 1000]; 1000];
    let data = include_str!("../assets/d5_2021.txt");
    let sample = include_str!("../assets/d5_2021_test.txt");

    let pdata: Vec<Vec<(i32, i32)>> = data
        .lines()
        .map(|line| {
            let h = line.split_whitespace().collect::<Vec<&str>>();
            let (x1, y1) = h[0].split_once(',').unwrap();
            let (x2, y2) = h[2].split_once(',').unwrap();
            let x: Vec<(i32, i32)> = vec![(x1.parse().unwrap(), y1.parse().unwrap()),
                                          (x2.parse().unwrap(), y2.parse().unwrap())];
            x
        })
        .collect();

    for (i, line) in pdata.iter().enumerate() {
        let dx = (line[0].0 - line[1].0).abs();
        let dy = (line[0].1 - line[1].1).abs();
        let x1 = line[0].0;
        let x2 = line[1].0;
        let y1 = line[0].1;
        let y2 = line[1].1;

        if x1 == x2 {
            for j in 0..dy + 1 {
                if y1 < y2 {
                    grid[x1 as usize][y1 as usize + j as usize] += 1;
                } else {
                    grid[x1 as usize][y1 as usize - j as usize] += 1;
                }
            }
        } else if y2 == y1 {
            for j in 0..dx + 1 {
                if x1 < x2 {
                    grid[x1 as usize + j as usize][y1 as usize] += 1;
                } else { grid[x1 as usize - j as usize][y1 as usize] += 1; }
            }
        } else if dx == dy {
            for row in 0..dy + 1 {
                if y1 < y2 && x1 < x2 {
                    grid[x1 as usize + row as usize][y1 as usize + row as usize] += 1;
                } else if y1 > y2 && x1 < x2 {
                    grid[x1 as usize + row as usize][y1 as usize - row as usize] += 1;
                } else if y2 < y1 && x2 < x1 {
                    grid[x2 as usize + row as usize][y2 as usize + row as usize] += 1;
                } else if y2 > y1 && x2 < x1 {
                    grid[x2 as usize + row as usize][y2 as usize - row as usize] += 1;
                }
            }
        }
    }

    let mut counter = 0;
    for i in 0..1000 {
        for j in 0..1000 {
            if grid[j][i] >= 2 {
                counter += 1;
            }
        }
    }
    println!("counter: {}", counter);
    assert_eq!(counter, 19081);
}

fn part1() {
    /*
    x1,y1 -> x2,y2
    0,9 -> 5,9
    8,0 -> 0,8
    Data structure: [ [(0,9), (5,9)], [(8,0), (0,8)] ], list of tuples
    only horizontal and vertical lines; x1 = x2 or y1 = y2

    if y1 == y2 { fill up x-vals between x1 and x2 }
    else if x1 == x2 { fill up y-vals between y1 and y2 }

     */
    let mut grid: [[i32; 1000]; 1000] = [[0; 1000]; 1000];
    let data = include_str!("../assets/d5_2021.txt");
    let sample = include_str!("../assets/d5_2021_test.txt");

    let pdata: Vec<Vec<(i32, i32)>> = data
        .lines()
        .map(|line| {
            let h = line.split_whitespace().collect::<Vec<&str>>();
            let (x1, y1) = h[0].split_once(',').unwrap();
            let (x2, y2) = h[2].split_once(',').unwrap();
            let x: Vec<(i32, i32)> = vec![(x1.parse().unwrap(), y1.parse().unwrap()),
                                          (x2.parse().unwrap(), y2.parse().unwrap())];
            x
        }).collect();

    for (i, line) in pdata.iter().enumerate() {
        let dx = (line[0].0 - line[1].0).abs();
        let dy = (line[0].1 - line[1].1).abs();
        let x1 = line[0].0;
        let x2 = line[1].0;
        let y1 = line[0].1;
        let y2 = line[1].1;

        if x1 == x2 {
            for j in 0..dy + 1 {
                if y1 < y2 {
                    grid[x1 as usize][y1 as usize + j as usize] += 1;
                } else {
                    grid[x1 as usize][y1 as usize - j as usize] += 1;
                }
            }
        } else if y2 == y1 {
            for j in 0..dx + 1 {
                if x1 < x2 {
                    grid[x1 as usize + j as usize][y1 as usize] += 1;
                } else {
                    grid[x1 as usize - j as usize][y1 as usize] += 1;
                }
            }
        }
    }

    let mut counter = 0;
    for i in 0..1000 {
        for j in 0..1000 {
            if grid[j][i] >= 2 {
                counter += 1;
            }
        }
    }
    println!("counter: {}", counter);
    assert_eq!(counter, 6666);
}
