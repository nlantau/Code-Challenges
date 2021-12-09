use std::time;

pub fn d9_2021_solution() {
    bench(part1);
}

fn bench(f: fn()) {
    let t0 = time::Instant::now();
    let ret = f();
    println!("Time used {:?}", time::Instant::now().duration_since(t0));
    ret
}

fn part1() {
    let inp: Vec<Vec<_>> = include_str!("../assets/d9_2021.txt")
        .lines()
        .map(|line| line.chars().collect::<Vec<char>>()
            .iter()
            .map(|c| {
                c.to_string().parse::<u32>().unwrap()
            }).collect()
        )
        .collect();


    let mut grid = [[9u32; 102]; 102];

    for x in 0..inp.len() {
        for y in 0..inp[0].len() {
            grid[x + 1][y + 1] = inp[x][y];
        }
    }

    let mut low_points: Vec<u32> = Vec::new();

    for x in 1..grid.len() - 1 {
        for y in 1..grid[0].len() - 1 {
            let up = grid[x][y - 1];
            let dn = grid[x][y + 1];
            let rp = grid[x + 1][y];
            let lp = grid[x - 1][y];
            let cp = grid[x][y];

            if cp < up && cp < dn && cp < rp && cp < lp {
                low_points.push(cp);
            }
        }
    }
    let res = low_points.iter().map(|&v| v + 1).sum::<u32>();
    println!("{:?}", res);
    assert_eq!(res, 528);
}





































