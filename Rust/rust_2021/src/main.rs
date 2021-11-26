use rust_2021::d1_2015::day1_2015;
use rust_2021::day1::day1a;

fn main() {
    let args = std::env::args().collect::<Vec<String>>();
    let problem = args.get(1).map(|s| s.as_str()).unwrap_or("None");

    let result = match problem {
        "day1a" => day1a(),
        "d1_2015" => day1_2015().to_string(),
        _ => "What?".to_string(),
    };
    println!("{}", result);
}
