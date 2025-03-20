# Birthday Greeting Generator

A simple Python script that generates customizable birthday greeting messages with various styling options.

## Features

- Generate random birthday messages from a template collection
- Customize with the person's name and age
- Calculate age automatically from birth year
- Apply colorful formatting to messages
- Add emoji decorations
- Display all available greeting templates

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/diaotapha/birthday-greeting-generator.git
   cd birthday-greeting-generator
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

```bash
python birthday_generator.py "John Doe"
```

### Options

- `-a, --age` - Specify the person's age
- `-y, --birth-year` - Calculate age based on birth year
- `-c, --color` - Choose message color (red, green, blue, yellow, magenta, cyan, white)
- `-e, --no-emojis` - Disable emoji decorations
- `-t, --all-templates` - Show all greeting templates

### Examples

```bash
# Basic usage with name
python birthday_generator.py "John Doe"

# Specify age
python birthday_generator.py "John Doe" --age 30

# Calculate age from birth year
python birthday_generator.py "John Doe" --birth-year 1990

# Change message color
python birthday_generator.py "John Doe" --age 30 --color green

# Disable emoji decorations
python birthday_generator.py "John Doe" --no-emojis

# Show all available templates
python birthday_generator.py "John Doe" --all-templates
```

## License

MIT