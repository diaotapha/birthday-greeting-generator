#!/usr/bin/env python3

import random
import argparse
from datetime import datetime
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Template birthday messages
BIRTHDAY_TEMPLATES = [
    "Happy Birthday, {name}! Wishing you a fantastic day filled with joy and laughter!",
    "Happy {age}th Birthday, {name}! May your day be as special as you are!",
    "Congratulations on turning {age}, {name}! Hope your birthday is absolutely amazing!",
    "Many happy returns, {name}! {age} looks good on you!",
    "Happy Birthday to the wonderful {name}! Enjoy your {age}th trip around the sun!",
    "Wishing you the happiest {age}th birthday, {name}! May all your dreams come true!",
    "It's {name}'s special day! Happy {age}th Birthday!",
    "Here's to another amazing year, {name}! Happy {age}th Birthday!",
    "Happy Birthday, {name}! {age} years of awesome!",
    "Cheers to {age} wonderful years, {name}! Happy Birthday!"
]

# Emoji decorations
EMOJIS = [
    "🎂", "🎉", "🎊", "🎁", "🎈", "🥳", "✨", "🎇", "🎆", "🍰"
]

# Color options
COLORS = {
    "red": Fore.RED,
    "green": Fore.GREEN,
    "blue": Fore.BLUE,
    "yellow": Fore.YELLOW,
    "magenta": Fore.MAGENTA,
    "cyan": Fore.CYAN,
    "white": Fore.WHITE
}

def calculate_age(birth_year):
    """Calculate age based on birth year."""
    current_year = datetime.now().year
    return current_year - birth_year

def generate_birthday_message(name, age=None, birth_year=None, color="cyan", emojis=True, all_templates=False):
    """Generate a customized birthday message."""
    
    # Calculate age if birth_year is provided
    if birth_year and not age:
        age = calculate_age(birth_year)
    
    # Use a default age if none is provided
    if not age:
        age = "special"
    
    selected_color = COLORS.get(color.lower(), Fore.CYAN)
    
    if all_templates:
        messages = [template.format(name=name, age=age) for template in BIRTHDAY_TEMPLATES]
        result = "\n\n".join(messages)
    else:
        # Select a random template
        template = random.choice(BIRTHDAY_TEMPLATES)
        result = template.format(name=name, age=age)
    
    # Add emoji decorations if enabled
    if emojis:
        emoji_decoration = " ".join(random.sample(EMOJIS, k=3))
        result = f"{emoji_decoration} {result} {emoji_decoration}"
    
    # Apply color
    return f"{selected_color}{result}{Style.RESET_ALL}"

def main():
    parser = argparse.ArgumentParser(description="Generate a customized birthday greeting")
    parser.add_argument("name", help="Name of the birthday person")
    parser.add_argument("-a", "--age", type=int, help="Age of the birthday person")
    parser.add_argument("-y", "--birth-year", type=int, help="Birth year of the birthday person")
    parser.add_argument("-c", "--color", choices=list(COLORS.keys()), default="cyan", 
                        help="Color of the greeting message")
    parser.add_argument("-e", "--no-emojis", action="store_true", 
                        help="Disable emoji decorations")
    parser.add_argument("-t", "--all-templates", action="store_true", 
                        help="Show all greeting templates")
    
    args = parser.parse_args()
    
    message = generate_birthday_message(
        name=args.name,
        age=args.age,
        birth_year=args.birth_year,
        color=args.color,
        emojis=not args.no_emojis,
        all_templates=args.all_templates
    )
    
    print("\n")
    print(message)
    print("\n")

if __name__ == "__main__":
    main()