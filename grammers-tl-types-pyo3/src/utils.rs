/// mask phone.
pub fn mask_phone(s: &str) -> String {
    let chars: Vec<char> = s.chars().collect();
    let len = chars.len();
    if len <= 8 {
        return s.to_string();
    }

    let first: String = chars[..4].iter().collect();
    let last: String = chars[len - 4..].iter().collect();

    format!("{}****{}", first, last)
}
