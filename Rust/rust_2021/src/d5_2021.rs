use itertools::{Itertools};

pub fn d5_2021_solution() {
    part1();
}

#[allow(unused_mut)]
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

    let pdata: Vec<Vec<(i32, i32)>> = sample
        .lines()
        .map(|line| {
            let h = line.split_whitespace().collect::<Vec<&str>>();
            let (x1, y1) = h[0]
                .split_once(',')
                .unwrap();
            let (x2, y2) = h[2]
                .split_once(',')
                .unwrap();
            let x: Vec<(i32, i32)> = vec![(x1.parse().unwrap(), y1.parse().unwrap()),
                                          (x2.parse().unwrap(), y2.parse().unwrap())];
            x
        })
        .collect();

    println!("{:?}", pdata);


    //println!("{:?}", grid);
}