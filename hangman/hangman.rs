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
    let mut hangman = Hangman::new();
    hangman.start()
}

impl Hangman {
    fn new() -> Hangman {
        println!("WELCOME TO HANGMAN");
        println!("Type 'bye' at any time to quit.");
        println!("Please enter a difficulty: easy, medium, or hard.");


        let difficulty = Hangman::get_difficulty();

        
        println!("Minimum word length set to {}", difficulty.min);
        println!("Maximum word length set to {}", difficulty.max);

        let words: Box<Vec<String>> = Hangman::get_words(&difficulty);

        // pick a word

        let mut rng = task_rng();
        let rand_word = rng.choose(words.as_slice()).expect("No word found.").clone();
        let mut letters: collections::HashSet<char> = collections::HashSet::new();
        println!("{}", rand_word);
        for letter in rand_word.as_slice().chars() {
            letters.insert(letter.clone());
        }

        Hangman {
            state: 0,
            word: rand_word,
            letters: letters.clone(),
            matched: collections::HashSet::new()
        }
    }

    fn get_difficulty() -> Difficulty {
        let mut difficulty: Option<Difficulty> = None;
        while difficulty.is_none() {
            print!(">");
            let input = &stdio::stdin()
                .read_line()
                .ok()
                .expect("Failed to read line.");

            match input.as_slice().trim_right_chars('\n') {
                "easy"   => difficulty = Some(Difficulty { min: 3, max: 5 }),
                "medium" => difficulty = Some(Difficulty { min: 5, max: 7 }),
                "hard"   => difficulty = Some(Difficulty { min: 7, max: 9 }),
                _          => continue
            }
        }
        difficulty.expect("No difficulty set.")
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

    fn start(&mut self) {
        let mut reader = stdio::stdin();
        
        self.print_state();
        println!("");
        print!(">");
        for line in reader.lock().lines() {
            if !self.is_over() {
                let input = line.ok().expect("Unable to read input."); // change this

                if input.as_slice().trim_right_chars('\n') == "bye" {
                    break
                } else {
                    match &input.as_slice().char_at(0) {
                        x if self.letters.contains(x) => {
                            self.matched.insert(x.clone());
                            self.print_state();
                            println!("");
                            print!(">");
                        },
                        _                             => {
                            self.state += 1;
                            self.print_state();
                            println!("");
                            print!(">");
                        }
                    }
                }
            } else {
                break
            }
        }

    }
    
    fn is_over(&self) -> bool {
        // do we have all the letters?
        if self.state == 6 {
            true
        } else if self.letters == self.matched {
            true
        } else {
            false
        }
    }

    fn print_state(&self) {
        println!("State: {}", self.state);

        for letter in self.word.as_slice().chars() {
            if self.matched.contains(&letter) {
                print!("{} ", letter)
            } else {
                print!("_ ")
            }
        }
    }
}
