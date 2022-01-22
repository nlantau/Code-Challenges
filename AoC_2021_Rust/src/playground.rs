
pub fn pass_reference_update_val() {
    let mut val = 13;
    println!("val: {}", val);
    change_val_of_reference(&mut val);
    println!("val: {}", val);


}

fn change_val_of_reference(v: &mut i32) {
    *v += 3;
}