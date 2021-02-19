fn main() {
    let t: Vec<usize> = generate_range(2, 10, 2);
    println!("Vec t: {:?}", t);

    println!("Is divide by: {}", is_divide_by(8,3,4));

    println!("bin to dec: {}", bin_to_decimal("1001001"));
}

fn bin_to_decimal(inp: &str) -> i32 {
    i32::from_str_radix(inp, 2).unwrap()
}


// Completed
fn is_divide_by(n: i32, a: i32, b: i32) -> bool {
    (n % a == 0) & (n % b == 0)
}

// Completed
fn generate_range(min: usize, max: usize, step: usize) -> Vec<usize> {
    let mut vec: Vec<usize> = Vec::new();
    let mut i: usize = min;

    while i <= max {
        vec.push(i);
        i += step;
    }
    vec
}