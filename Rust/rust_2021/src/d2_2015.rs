use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;
use std::path::Path;


pub fn day2() -> String {
    let lines: Vec<String> = read_data_d2();
    lines.get(0).unwrap().to_string()
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