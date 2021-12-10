use std::collections::hash_map::Entry;
use std::collections::HashMap;
use std::time;

pub fn d10_2021_solution() {
    //bench(part1);
    bench(part2);
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

fn part2() {
    let inp = get_data();
    let errs = syntax_repair2(&inp);
}

#[derive(Debug)]
struct Token {
    token: char,
    expected_closer: char,
    found_closer: char,
    complete: bool,
    position: i32,
}

impl Token {
    fn new() -> Token {
        Token {
            token: '=',
            expected_closer: '?',
            found_closer: '!',
            complete: false,
            position: -1,
        }
    }

    fn set_complete(&mut self) {
        let b = self.expected_closer == self.found_closer;
        self.complete = b;
    }
}

fn syntax_repair2(inp: &[Vec<char>]) -> Vec<(char, char)> {
    let mut error_pairs: Vec<(char, char)> = Vec::new();
    let mut stack: Vec<char> = Vec::new();
    let mut missing: Vec<char> = Vec::new();

    for v in inp.iter() {
        for c in v.iter() {
            if is_opener(c) {
                stack.push(*c);
            } else if is_closer(c) {
                let open_token = stack.pop().unwrap();

                if open_token == '(' && *c != ')' {
                    //error_pairs.push((')', *c));
                    missing.push(')');
                } else if open_token == '[' && *c != ']' {
                    //error_pairs.push((']', *c));
                    missing.push(']');
                } else if open_token == '{' && *c != '}' {
                    //error_pairs.push(('}', *c));
                    missing.push('}');
                } else if open_token == '<' && *c != '>' {
                    //error_pairs.push(('>', *c));
                    missing.push('>');
                }
            }
        }
    }
    missing.push('-');
    missing.iter().for_each(|c| println!("{}", c));
    error_pairs
}

#[allow(unused_mut)]
fn syntax_repair(inp: &[Vec<char>]) -> Vec<Token> {
    let mut stack: Vec<char> = Vec::new();
    let mut tokens: Vec<Token> = Vec::new();

    for v in inp.iter() {
        for (idx, opener) in v.iter().enumerate() {
            if is_opener(opener) {
                let mut boken: Token = Token::new();
                boken.token = *opener;
                tokens.push(boken);
            }
        }
    }
    dbg!(&tokens);
    tokens
}

fn syntax_checker(inp: &[Vec<char>]) -> Vec<(char, char)> {
    let mut error_pairs: Vec<(char, char)> = Vec::new();
    let mut stack: Vec<char> = Vec::new();
    for v in inp.iter() {
        for c in v.iter() {
            if is_opener(c) {
                stack.push(*c);
            } else if is_closer(c) {
                let open_token = stack.pop().unwrap();
                if open_token == '(' && *c != ')' {
                    error_pairs.push((')', *c));
                    break;
                } else if open_token == '[' && *c != ']' {
                    error_pairs.push((']', *c));
                    break;
                } else if open_token == '{' && *c != '}' {
                    error_pairs.push(('}', *c));
                    break;
                } else if open_token == '<' && *c != '>' {
                    error_pairs.push(('>', *c));
                    break;
                }
            }
        }
    }
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

fn is_opener(c: &char) -> bool {
    matches!(c, '(' | '[' | '{' | '<')
}

fn is_closer(c: &char) -> bool {
    matches!(c, ')' | ']' | '}' | '>')
}






















