use std::io;
use std::io::stdio;
use std::collections;
use std::rand::{Rng, task_rng};

struct Difficulty {
    min: uint,
    max: uint
}

struct Hangman {
    state: int,
    word: String,
    letters: collections::HashSet<char>,
    matched: collections::HashSet<char>
}

fn main() {
    let hangman = Hangman::new();
}

impl Hangman {
    fn new() -> Hangman {
        println!("WELCOME TO HANGMAN");
        println!("Type 'bye' at any time to quit.");
        println!("Please enter a difficulty: easy, medium, or hard.");


        let difficulty = Hangman::get_difficulty();

        
        println!("Minimum word length set to {}", difficulty.min);
        println!("Maximum word length set to {}", difficulty.max);

        let words = Hangman::get_words(&difficulty);

        // pick a word

        let mut rng = task_rng();
        let rand_word: &String = rng.choose(&*words.as_slice()).expect("No word.");
        let mut letters = collections::HashSet::new();
        println!("{}", rand_word);
        for letter in rand_word.as_slice().chars() {
            letters.insert(letter);
        }

        Hangman {
            state: 0,
            word: *rand_word,
            letters: letters,
            matched: collections::HashSet::new()
        }

    }

    fn get_difficulty() -> Difficulty {
        let mut difficulty: Difficulty;
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

            match input.as_slice() {
                "easy\n"   => difficulty = Difficulty { min: 3, max: 5 },
                "medium\n" => difficulty = Difficulty { min: 5, max: 7 },
                "hard\n"   => difficulty = Difficulty { min: 7, max: 9 },
                _          => continue
            }

//            difficulty = match difficulty_opt {
//                Some(d) => d,
//                None    => {
//                    println!("Invalid input.");
//                    println!("Please enter a difficulty: easy, medium, or hard:");
//                    continue
//                }
//            };
        }
        difficulty
    }

    fn get_words(difficulty: &Difficulty) -> Box<Vec<String>> {
        let mut words = Vec::new();

        let path = Path::new("/usr/share/dict/words");
        let words_file = io::File::open(&path).ok().expect("Error opening file.");
        let mut reader = io::BufferedReader::new(words_file);
        let mut counter = 0u;
        loop {
            match reader.read_line() {
                Ok(line) => {
                    if difficulty.min < line.len() && line.len() < difficulty.max {
                        words.push(line
                                   .as_slice()
                                   .trim_right_chars('\n')
                                   .to_string());
                        counter += 1;
                    }
                }
                Err(why) => match why.kind {
                    io::EndOfFile => break,
                    _             => panic!("Error reading file: {}", why)
                }
            }
        }
        println!("Read in {} words.", counter);
        box words
    }
}

