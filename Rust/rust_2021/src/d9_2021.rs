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

    let res = locate_low_points(&populate_grid(&inp))
        .iter()
        .map(|&v| v + 1).sum::<u32>();
    println!("{:?}", res);
    assert_eq!(res, 528);
    // assert_eq!(res, 15);
}

fn locate_low_points(grid: &[[u32; 102]; 102]) -> Vec<u32> {
    let mut low_points: Vec<u32> = Vec::new();

    (1..grid.len() - 1).for_each(|x| {
        (1..grid[0].len() - 1).for_each(|y| {
            if neighbors_are_smaller(&x, &y, grid) {
                let cp = grid[x][y];
                low_points.push(cp);
            }
        })
    });
    low_points
}

fn neighbors_are_smaller(x: &usize, y: &usize, grid: &[[u32; 102]; 102]) -> bool {
    let up = grid[*x][y - 1];
    let dn = grid[*x][y + 1];
    let rp = grid[*x + 1][*y];
    let lp = grid[*x - 1][*y];
    let cp = grid[*x][*y];
    cp < up && cp < dn && cp < rp && cp < lp
}

fn populate_grid(s: &[Vec<u32>]) -> [[u32; 102]; 102] {
    let mut grid = [[9u32; 102]; 102];

    for x in 0..s.len() {
        for y in 0..s[0].len() {
            grid[x + 1][y + 1] = s[x][y];
        }
    }
    grid
}