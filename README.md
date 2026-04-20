# 💰 Investment Calculator

A simple CLI tool that calculates the return on an investment over time using compound growth.

## How It Works

The program prompts you for three values:

- **Years** — how long you're investing for
- **Investment amount** — how much you're putting in
- **Annual growth rate** — the expected yearly percentage increase

It then calculates and displays your projected return using the compound growth formula:

total = investment * (1 + rate) ** years

## Usage

```bash
python main.py
```

Example output:

The total profit for a 10 year investment of 5000 at 7% is: 9835.76

## Input Validation

All inputs are validated — the program will keep prompting until a valid number is entered.
