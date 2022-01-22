use std::cmp::min;
use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;
use std::path::Path;

pub fn day2() -> String {
    let lines: Vec<String> = read_data_d2();
    let res: i32 = lines
        .iter()
        .map(|s| str_vec_to_int(s))
        .map(wrapping_paper)
        .sum();

    res.to_string()
}

fn wrapping_paper(numbs: Vec<i32>) -> i32 {
    let lw = numbs[0] * numbs[1];
    let lh = numbs[0] * numbs[2];
    let wh = numbs[1] * numbs[2];
    2 * lw + 2 * wh + 2 * lh + min(lw, min(lh, wh))
}

fn str_vec_to_int(line: &str) -> Vec<i32> {
    line.split('x')
        .map(|d| d.parse())
        .map(|d| d.unwrap())
        .collect()
}

fn read_data_d2() -> Vec<String> {
    let inp = File::open(Path::new("assets/d2_2015.txt")).unwrap();
    let reader = BufReader::new(&inp);
    let lines: Vec<String> = reader
        .lines()
        .collect::<Result<_, _>>()
        .unwrap();
    lines
}