use std::fs::File;
use std::io::Read;

fn main() {
    let raw_input = read_input();
    day1(&raw_input);
    day2(&raw_input);
}

/**
 * Read the input file
 */
fn read_input() -> String {
    let mut input_file = File::open("../input.txt").unwrap();
    let mut input = String::new();
    input_file.read_to_string(&mut input).unwrap();

    return input;
}

/**
 * Get the max caloric sum from the groups
 */
fn day1(raw_input: &String) {
    let mut max_calories = 0;
    let groups = raw_input.split("\n\n");
    for group in groups {
        let lines = group
            .lines()
            .map(|line| line.trim().parse::<i32>().unwrap());
        let sum = lines.reduce(|a, b| a + b).unwrap();
        if sum > max_calories {
            max_calories = sum;
        }
    }
    println!("Max calories: {}", max_calories);
}

/**
 * Get the sum of the top 3 groups
 */
fn day2(raw_input: &String) {
    let mut caloric_groups = Vec::new();
    let groups = raw_input.split("\n\n");

    for group in groups {
        let sum: i32 = group
            .lines()
            .map(|line| line.trim().parse::<i32>().unwrap())
            .sum();
        caloric_groups.push(sum);
    }

    caloric_groups.sort_by(|a, b| b.cmp(a));
    let top_3 = caloric_groups.iter().take(3).collect::<Vec<_>>();
    println!("Top 3: {:?}", top_3);

    let top_3_sum: i32 = top_3.iter().copied().sum();
    println!("Top 3 sum: {}", top_3_sum);
}
