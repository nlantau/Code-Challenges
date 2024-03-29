use std::collections::hash_map::{Entry, VacantEntry};
use std::collections::HashMap;
use std::time;

pub fn d10_2021_solution() {
    bench(part1_and_2);
}

fn bench(f: fn()) {
    let t0 = time::Instant::now();
    let ret = f();
    println!("Time used {:?}", time::Instant::now().duration_since(t0));
    ret
}

fn part1_and_2() {
    let inp = get_data();
    let (error_pairs, incomplete) = syntax_checker(&inp);
    let err_sum: HashMap<char, Vec<u32>> = calculate_syntax_score(&error_pairs);
    let mut res = 0;
    for (k, v) in err_sum.iter() {
        res += v[0] * v.len() as u32;
    }
    println!("Part 1: {}", res);
    assert_eq!(res, 243939);

    let mut incomplete_missing = get_incomplete_vectors(&incomplete);
    let mut scores: Vec<u128> = calculate_incomplete_score(&mut incomplete_missing);
    scores.sort_unstable();
    let valve = scores[scores.len() / 2];
    println!("Part 2: {}", valve);
    assert_eq!(valve, 2421222841);
}

fn get_data() -> Vec<Vec<char>> {
    include_str!("../assets/d10_2021.txt").lines().collect::<Vec<&str>>()
        .iter()
        .map(|&v| v.chars().collect::<Vec<char>>())
        .collect()
}

fn calculate_incomplete_score(incomplete_missing: &mut Vec<Vec<char>>) -> Vec<u128> {
    let mut scores: Vec<u128> = Vec::new();
    for v in incomplete_missing.iter_mut() {
        let mut score: u128 = 0;
        while let Some(val) = v.pop() {
            match val {
                '(' => score = score * 5 + 1,
                '[' => score = score * 5 + 2,
                '{' => score = score * 5 + 3,
                '<' => score = score * 5 + 4,
                _ => panic!("At the disco"),
            }
        }
        scores.push(score);
    }
    scores
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

fn syntax_checker(inp: &[Vec<char>]) -> (Vec<(char, char)>, Vec<Vec<char>>) {
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
    let incomplete: Vec<Vec<char>> = copy_incomplete_lines(inp, &corrupted_lines);
    (error_pairs, incomplete)
}

fn copy_incomplete_lines(inp: &[Vec<char>], corrupted_lines: &[usize]) -> Vec<Vec<char>> {
    let mut incomplete: Vec<Vec<char>> = Vec::new();
    for (i, v) in inp.iter().enumerate() {
        let mut copy_line = true;
        for (j, n) in corrupted_lines.iter().enumerate() {
            if *n == i { copy_line = false; }
        }
        if copy_line { incomplete.push(v.clone()); }
    }
    incomplete
}

fn get_incomplete_vectors(incomplete: &[Vec<char>]) -> Vec<Vec<char>> {
    let mut incomplete_missing: Vec<Vec<char>> = Vec::new();
    for (i, v) in incomplete.iter().enumerate() {
        let mut stack: Vec<char> = Vec::new();

        for c in v.iter() {
            if is_opener(c) { stack.push(*c); } else if is_closer(c) { stack.pop(); }
        }
        incomplete_missing.push(stack);
    }
    incomplete_missing
}

fn is_opener(c: &char) -> bool {
    matches!(c, '(' | '[' | '{' | '<')
}

fn is_closer(c: &char) -> bool {
    matches!(c, ')' | ']' | '}' | '>')
}
