use base64::{engine::general_purpose::STANDARD, Engine};
use hex::encode as hex_encode;
use num_bigint::BigUint;
use std::io::{self, Write};

const FERROUS_OXIDE_USERNAME: &str = "AdminFeroxide";
const ANIONIC_PASSWORD: &str = "NjQzMzcyNzUzNTM3MzE2Njc5MzE2ZTM2";
const ALKALINE_SECRET: &str = "4143454354467B34707072336E373163335F3634322C28010D3461302C392E";

fn ionic_bond(cation_input: &str, anion_input: &str) {
    let cation_hex = hex_encode(cation_input);
    let anion_hex = hex_encode(anion_input);

    let cation_value = BigUint::parse_bytes(cation_hex.as_bytes(), 16).unwrap();
    let anion_value = BigUint::parse_bytes(anion_hex.as_bytes(), 16).unwrap();

    let covalent_link = &cation_value ^ &anion_value;

    let alkaline_secret_value = BigUint::parse_bytes(ALKALINE_SECRET.as_bytes(), 16).unwrap();
    let metallic_alloy = &covalent_link ^ &alkaline_secret_value;

    let precipitate = format!("{:x}", metallic_alloy);

    let alloy_compound = (0..precipitate.len())
        .step_by(2)
        .map(|i| u8::from_str_radix(&precipitate[i..i + 2], 16).unwrap() as char)
        .collect::<String>();

    println!("Crystallized Flag (ASCII): {}", alloy_compound);
}

fn reaction_chamber() {
    let mut username = String::new();
    print!("Introduce the Catalyst: ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut username).unwrap();
    let username = username.trim();

    let mut password = String::new();
    print!("Introduce the Reagent: ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut password).unwrap();
    let password = password.trim();
    
    if username != FERROUS_OXIDE_USERNAME {
        println!("Reaction denied: Unstable molecule detected.");
        return;
    }
    
    let reagent_ion = STANDARD.encode(hex_encode(password).as_bytes());
    if reagent_ion != ANIONIC_PASSWORD {
        println!("Reaction denied: Unstable molecule detected.");
        return;
    }

    ionic_bond(username, password);
}

fn main() {
    reaction_chamber();
}
