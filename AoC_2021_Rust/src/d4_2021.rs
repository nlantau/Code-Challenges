use itertools::Itertools;

pub fn d4_2021_solution() {
    part1();
}

fn part1() {
    let (draw, boards) = parse_input();
    //println!("{:?}", boards);
    //println!("{:?}", draw);
    let b2 = mark(draw, boards);
    println!("{:?}", b2);
}

#[allow(unused_assignments)]
fn mark(draw: Vec<usize>, boards: Vec<Vec<Vec<(usize, bool)>>>) -> Vec<Vec<Vec<(usize, bool)>>> {
    for (i, board) in boards.iter().enumerate() {
        for (j, row) in board.iter().enumerate() {
            for (k, &(value, mut state)) in row.iter().enumerate() {
                for (h, &d) in draw.iter().enumerate() {
                    if d == value {
                        state = true;
                        todo!("Complete me....!")
                    }
                }
            }
        }
    }
    boards
}

#[allow(clippy::type_complexity)]
fn parse_input() -> (Vec<usize>, Vec<Vec<Vec<(usize, bool)>>>) {
    let data = include_str!("../assets/d4_2021.txt");
    let (draw, boards) = include_str!("../assets/d4_2021_test.txt").split_once("\n\n").unwrap();
    let draw: Vec<usize> = draw.split(',').map(|c| c.parse().unwrap()).collect();
    let boards: Vec<Vec<(usize, bool)>> = boards
        .split("\n\n")
        .map(|row| {
            row.split_whitespace()
                .map(|i| (i.parse().unwrap(), false))
                .collect()
        }).collect();

    let mut board2: Vec<Vec<Vec<(usize, bool)>>> = Vec::new();
    let mut b_5x5: Vec<Vec<(usize, bool)>> = Vec::new();
    let mut b_5: Vec<(usize, bool)> = Vec::new();

    for (e, v) in boards.iter().enumerate() {
        for i in 1..26 {
            b_5.push((v[i - 1].0, v[i - 1].1));
            if i % 5 == 0 {
                b_5x5.push(b_5.clone());
                b_5 = Vec::new();
            }
        }
        board2.push(b_5x5.clone());
        b_5x5 = Vec::new();
    }
    (draw, board2)
}

fn part1_old() {
    println!("Part 1");

    let data = include_str!("../assets/d4_2021.txt");
    let sample: Vec<&str> = include_str!("../assets/d4_2021_test.txt").lines().collect();

    dbg!(&sample);

    let draw: Vec<usize> = sample.get(0).unwrap().split(',')
        .map(|n| n.parse::<usize>().unwrap())
        .collect();

    dbg!(&draw);

    let boards: Vec<Vec<i32>> = sample.iter().skip(1)
        .filter(|line| !line.is_empty())
        .map(|line| {
            line.split_whitespace().map(|numb| numb.parse::<i32>().unwrap()).collect::<Vec<i32>>()
        }).collect();

    dbg!(&boards);
    println!("{:?}", boards);

    let mut boards_3d: Vec<Vec<Vec<i32>>> = Vec::new();

    for (i, row) in boards.iter().enumerate() {
        let mut b: Vec<Vec<i32>> = Vec::new();
        for j in 0..5 {
            println!("i:{} j:{}", i, j);
            if i + j < boards.len() {
                b.push(boards[i + j].clone());
            }
        }
        boards_3d.push(b);
    }

    dbg!(&boards_3d);
    println!("{:?}", boards_3d);
}