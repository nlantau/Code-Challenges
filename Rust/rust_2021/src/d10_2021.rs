use std::collections::hash_map::{Entry, VacantEntry};
use std::collections::HashMap;
use std::time;

pub fn d10_2021_solution() {
    bench(part1);
    //bench(part2);
}

fn bench(f: fn()) {
    let t0 = time::Instant::now();
    let ret = f();
    println!("Time used {:?}", time::Instant::now().duration_since(t0));
    ret
}

fn get_data() -> Vec<Vec<char>> {
    include_str!("../assets/d10_2021_test.txt").lines().collect::<Vec<&str>>()
        .iter()
        .map(|&v| v.chars().collect::<Vec<char>>())
        .collect()
}

fn part2() {
    let inp = get_data();
    inp.iter().for_each(|l| println!("{:?}", l));
    let errs = syntax_repair(&inp);
}

fn part1() {
    let inp = get_data();
    let error_pairs: Vec<(char, char)> = syntax_checker(&inp);
    let err_sum: HashMap<char, Vec<u32>> = calculate_syntax_score(&error_pairs);
    let mut res = 0;
    for (k, v) in err_sum.iter() {
        res += v[0] * v.len() as u32;
    }
    println!("Part 1: {}", res);
    assert_eq!(res, 26397);
    //assert_eq!(res, 243939);
}

fn syntax_checker(inp: &[Vec<char>]) -> Vec<(char, char)> {
    let mut error_pairs: Vec<(char, char)> = Vec::new();
    let mut stack: Vec<char> = Vec::new();
    let mut corrupted_lines: Vec<usize> = Vec::new();

    for (i, v) in inp.iter().enumerate() {
        for c in v.iter() {
            if is_opener(c) {
                stack.push(*c);
            } else if is_closer(c) {
                let open_token = stack.pop().unwrap();

                if open_token == '(' && *c != ')' {
                    error_pairs.push((')', *c));
                    corrupted_lines.push(i);
                } else if open_token == '[' && *c != ']' {
                    error_pairs.push((']', *c));
                    corrupted_lines.push(i);
                } else if open_token == '{' && *c != '}' {
                    error_pairs.push(('}', *c));
                    corrupted_lines.push(i);
                } else if open_token == '<' && *c != '>' {
                    error_pairs.push(('>', *c));
                    corrupted_lines.push(i);
                }
            }
        }
    }
    /*
    TODO: remove corrupted_lines from input => incomplete lines
    TODO: new loop -> push if opener, pop if closer
    TODO: reverse list or deque (?) while awarding points
    TODO: Once solved, Rustify the solution (if let, while let, match)
     */
    corrupted_lines.iter().for_each(|c| print!("{},", c));
    println!();
    error_pairs
}

fn calculate_syntax_score(ep: &[(char, char)]) -> HashMap<char, Vec<u32>> {
    let mut err_sum: HashMap<char, Vec<u32>> = HashMap::new();
    for (_, token) in ep.iter() {
        match err_sum.entry(*token) {
            Entry::Vacant(e) => {
                match token {
                    ')' => e.insert(vec![3]),
                    ']' => e.insert(vec![57]),
                    '}' => e.insert(vec![1197]),
                    '>' => e.insert(vec![25137]),
                    _ => panic!(),
                };
            }
            Entry::Occupied(mut e) => {
                match token {
                    ')' => e.get_mut().push(3),
                    ']' => e.get_mut().push(57),
                    '}' => e.get_mut().push(1195),
                    '>' => e.get_mut().push(25137),
                    _ => panic!(),
                };
            }
        }
    }
    err_sum
}

#[allow(unused_mut)]
fn syntax_repair(inp: &[Vec<char>]) -> Vec<(char, char)> {
    let mut error_pairs: Vec<(char, char)> = Vec::new();
    let mut stack: Vec<char> = Vec::new();
    let mut missing: Vec<char> = Vec::new();

    for v in inp.iter() {
        for c in v.iter() {
            match c {
                '(' => stack.push(*c),
                '[' => stack.push(*c),
                '{' => stack.push(*c),
                '<' => stack.push(*c),
                _ => panic!(),
            }
        }
    }

    missing.push('-');
    missing.iter().for_each(|c| println!("{}", c));
    error_pairs
}

fn is_opener(c: &char) -> bool {
    matches!(c, '(' | '[' | '{' | '<')
}

fn is_closer(c: &char) -> bool {
    matches!(c, ')' | ']' | '}' | '>')
}






















