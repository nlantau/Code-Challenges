pub fn d13_2021_solution() {
    part1();
}

fn part1() {
    println!("Hello");
    find_fold_algo();
}

#[allow(unused_mut)]
fn find_fold_algo() {
    let mut v = vec![
        vec!["1", "1", "a", "a"],
        vec!["2", "2", "b", "b"],
        vec!["3", "3", "c", "c"],
        vec!["4", "4", "d", "d"],
    ];

    println!("{:?}", v);

    println!("> Fold left");

    // Only right to left fold (not down to up)
    for (idx, vect) in v.clone().iter().enumerate() {
        let fold_index = vect.len() / 2;
        for (idy, token) in vect.iter().enumerate() {

            // fold large to small (right to left)
            if idy < fold_index {
                //let s = [v[idx][idy], v[idx][vect.len() - idy - 1]].concat();
                v[idx][idy] = format!("{}{}", v[idx][idy].clone(), v[idx][vect.len() - idy - 1]).as_str();
            }
        }
    }
    println!("{:?}", v);
}






















