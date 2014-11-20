use std::io;
use std::io::stdio;
use std::collections;

struct Difficulty {
    min: uint,
    max: uint
}

fn main() {

    start();
}

fn start() {
    println!("WELCOME TO HANGMAN");
    println!("Please enter a difficulty: easy, medium, or hard:");

    loop {
        io::print(">");
        let input = &stdio::stdin()
                            .read_line()
                            .ok()
                            .expect("Failed to read line.");

        let difficulty_opt = match input.as_slice() {
            "easy\n"   => Some(Difficulty { min: 3, max: 5 }),
            "medium\n" => Some(Difficulty { min: 5, max: 7 }),
            "hard\n"   => Some(Difficulty { min: 7, max: 9 }),
            _          => None
        };

        let difficulty = match difficulty_opt {
            Some(d) => d,
            None    => {
                println!("Invalid input.");
                println!("Please enter a difficulty: easy, medium, or hard:");
                continue
            }
        };

        println!("Minimum word length set to {}", difficulty.min);
        println!("Maximum word length set to {}", difficulty.max);
    
        let words = *get_words(&difficulty);

    }
}

fn get_words(difficulty: &Difficulty) -> Box<Vec<String>> {
    let mut words = Vec::new();
    let min = difficulty.min;
    let max = difficulty.max;

    let path = Path::new("/usr/share/dict/words");
    let words_file = io::File::open(&path).ok().expect("Error opening file.");
    let mut reader = io::BufferedReader::new(words_file);
    let mut counter = 0u;
    loop {
        match reader.read_line() {
            Ok(line) => {
                if min < line.len() && line.len() < max {
                    words.push(line
                               .as_slice()
                               .trim_right_chars('\n')
                               .to_string());
                    counter += 1;
                }
            }
            Err(why) => match why.kind {
                io::EndOfFile => break,
                _             => fail!("Error reading file: {}", why)
            }
        }
    }
    println!("Read in {} words.", counter);
    box words
}

