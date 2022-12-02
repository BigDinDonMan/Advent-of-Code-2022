use std::fs::File;
use std::io::prelude::*;
use std::path::Path;
use std::collections::HashMap;

#[derive(Copy, Clone)]
enum MatchResult {
    Win = 6,
    Lose = 0,
    Draw = 3
}

struct CombinationData {
    wins_with: String,
    loses_with: String
}

fn readlines(path: &String) -> Vec<String> {
    let fpath = Path::new(&path);
    let mut file = match File::open(&fpath) {
        Err(why) => panic!("Could not open {}: {}", fpath.display(), why),
        Ok(file) => file,
    };

    let mut result_str = String::new();
    file.read_to_string(&mut result_str).ok().expect("Failed to read the file");

    return result_str.split("\n").map(|s: &str| s.to_string()).collect();
}

fn part1(lines: &Vec<String>, shapes: &HashMap<String, i32>, responses: &HashMap<String, i32>, combinations: &HashMap<String, CombinationData>) -> i32 {
    let mut points = 0;
    for line in lines {
        let parts: Vec<String> = line.split(" ").map(|s: &str| s.trim().to_string()).collect();
        let elf_selection = &parts[0];
        let my_selection = &parts[1];

        let gained_points = responses.get(my_selection).unwrap();
        let elf_points = shapes.get(elf_selection).unwrap();
        let result: MatchResult;
        if (elf_points == gained_points) {
            result = MatchResult::Draw;
        } else {
            let data = combinations.get(my_selection).unwrap();
            if (data.wins_with == parts[0]) {
                result = MatchResult::Win;
            } else {
                result = MatchResult::Lose;
            }
        }
        points += result as i32;
        points += gained_points;
    }

    return points;
}

fn part2(lines: &Vec<String>, shapes: &HashMap<String, i32>, responses: &HashMap<String, i32>) -> i32 {
    let match_results = HashMap::from([
        (String::from("Z"), MatchResult::Win),
        (String::from("Y"), MatchResult::Draw),
        (String::from("X"), MatchResult::Lose)
    ]);
    let combinations = HashMap::from([
        (String::from("A"), CombinationData { wins_with: String::from("C"), loses_with: String::from("B") }),
        (String::from("B"), CombinationData { wins_with: String::from("A"), loses_with: String::from("C") }),
        (String::from("C"), CombinationData { wins_with: String::from("B"), loses_with: String::from("A") }),
    ]);

    let mut points = 0;
    for line in lines {
        let parts: Vec<String> = line.split(" ").map(|s: &str| s.trim().to_string()).collect();
        let elf_selection = &parts[0];
        let target_match_result = &parts[1];

        let match_result = match_results.get(target_match_result).unwrap();
        let data = combinations.get(elf_selection).unwrap();
        let key = &match match_result {
            MatchResult::Win => data.loses_with.to_string(),
            MatchResult::Lose => data.wins_with.to_string(),
            MatchResult::Draw => elf_selection.to_string()
        };
        let gained_points = shapes.get(key).unwrap();

        points += *match_result as i32 + gained_points;
    }
    return points;
}

fn main() {
    let file_path = String::from("./input.txt");
    let lines = readlines(&file_path);
    let shapes = HashMap::from([
        ("A".to_string(), 1), //Rock
        ("B".to_string(), 2), //Paper
        ("C".to_string(), 3)  //Scissors
    ]);
    let responses = HashMap::from([
        ("X".to_string(), 1),
        ("Y".to_string(), 2),
        ("Z".to_string(), 3)
    ]);
    let combinations = HashMap::from([
        ("X".to_string(), CombinationData {wins_with: "C".to_string(), loses_with: "B".to_string()}),
        ("Y".to_string(), CombinationData {wins_with: "A".to_string(), loses_with: "C".to_string()}),
        ("Z".to_string(), CombinationData {wins_with: "B".to_string(), loses_with: "A".to_string()})
    ]);
    
    // let points = part1(&lines, &shapes, &responses, &combinations);
    let points = part2(&lines, &shapes, &responses);

    println!("Result: {}", points);
}