fn main() {
    let t: Vec<usize> = generate_range(2, 10, 2);
    println!("Vec t: {:?}", t);
}

fn generate_range(min: usize, max: usize, step: usize) -> Vec<usize> {
    let mut vec: Vec<usize> = Vec::new();
    let mut i: usize = min;

    while i <= max {
        vec.push(i);
        i += step;
    }
    vec
}