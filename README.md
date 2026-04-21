# 💰 Investment Calculator

A tool that calculates the return on an investment over time using compound growth. Available as a CLI app, a deployed Streamlit webapp, and a Flask webapp (in progress).

## Versions

### 🖥️ CLI Version
A command-line tool that prompts for investment details, calculates your return, and saves results to `investments.txt` for future reference.

### 🌐 Streamlit Version
A simple web UI version of the calculator. Try it live: [calculate-investment.streamlit.app](https://calculate-investment.streamlit.app/)

### 🔧 Flask Version *(in progress)*
A Flask-based web version currently under development.

## How It Works

The program asks for four values:

- **Company name** — who you're investing with
- **Investment amount** — how much you're putting in
- **Years** — how long you're investing for
- **Annual growth rate** — the expected yearly percentage increase

It then calculates your projected return using the compound growth formula:

total = investment * (1 + rate) ** years

## Usage

### CLI
```bash
python CLI_version/main.py
```

### Streamlit
```bash
streamlit run streamlit_version/main.py
```

## Input Validation

All inputs are validated — the program will keep prompting until a valid value is entered.
