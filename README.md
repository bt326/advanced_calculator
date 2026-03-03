# Advanced Calculator Application

## Overview

The Advanced Calculator Application is a modular, command-line based Python system designed to demonstrate professional software engineering principles, object-oriented programming, and practical design pattern implementation.

This project extends beyond basic arithmetic by integrating state management, logging, configuration handling, persistent storage, automated testing, and CI/CD workflows. It was developed with scalability, maintainability, and clean architecture in mind.

---

## Key Capabilities

### Advanced Arithmetic Operations
- Addition
- Subtraction
- Multiplication
- Division
- Power
- Nth Root
- Modulus
- Integer Division
- Percentage Calculation
- Absolute Difference

### State & History Management
- Persistent calculation history
- Undo and Redo functionality (Memento Pattern)
- CSV-based history serialization using pandas
- Maximum history size enforcement

### Configuration Management
- Environment-based configuration using python-dotenv
- Configurable calculation precision
- Input validation constraints
- Customizable log and history directories

### Logging & Observability
- Structured logging using Python’s logging module
- Operation-level logging via Observer pattern
- Automatic history persistence through AutoSave observer

### Testing & Quality Assurance
- 51 unit tests
- 100% test coverage
- Edge-case and parameterized testing
- CI pipeline with minimum 90% coverage enforcement ..
- i achieved 100% coverage 

---

## Design Patterns Implemented

- Factory Pattern – Encapsulates arithmetic operation creation.
- Memento Pattern – Enables undo/redo via state snapshots.
- Observer Pattern – Decouples logging and auto-save from core logic.
- Decorator Pattern – Dynamically generates help menu content.

---

## Project Architecture

project_root/
│
├── app/
│   ├── calculator.py
│   ├── calculation.py
│   ├── operations.py
│   ├── history.py
│   ├── calculator_memento.py
│   ├── observer.py
│   ├── logging_observer.py
│   ├── autosave_observer.py
│   ├── logger.py
│   ├── calculator_config.py
│   ├── input_validators.py
│   └── exceptions.py
│
├── tests/
├── .github/workflows/
├── requirements.txt
└── README.md

The system follows a modular design with strong separation of concerns to ensure readability, maintainability, and scalability.

---

## Installation

Clone the repository:

git clone https://github.com/bt326/advanced_calculator.git  
cd advanced_calculator  

Create a virtual environment:

python3 -m venv venv  
source venv/bin/activate  

Install dependencies:

pip install -r requirements.txt  

---

## Configuration

Create a `.env` file in the project root (optional if defaults are sufficient).

Example configuration:

CALCULATOR_LOG_DIR=logs  
CALCULATOR_HISTORY_DIR=history  
CALCULATOR_MAX_HISTORY_SIZE=100  
CALCULATOR_AUTO_SAVE=true  
CALCULATOR_PRECISION=2  
CALCULATOR_MAX_INPUT_VALUE=1000000  
CALCULATOR_DEFAULT_ENCODING=utf-8  

If environment variables are not defined, default values are applied automatically.

---

## Running the Application

If using module execution:

python -m app  

If using an entry file:

python main.py  

---

## Command-Line Interface (REPL)

Supported Commands:

add <a> <b>  
subtract <a> <b>  
multiply <a> <b>  
divide <a> <b>  
power <a> <b>  
root <a> <b>  
modulus <a> <b>  
int_divide <a> <b>  
percent <a> <b>  
abs_diff <a> <b>  

history  
clear  
undo  
redo  
save  
load  
help  
exit  

---

## Running Tests

Run all tests:

pytest  

Check coverage:

pytest --cov=app --cov-report=term  

Current Coverage: 100%

---

## Continuous Integration

GitHub Actions automatically:

- Installs dependencies
- Runs unit tests
- Enforces minimum 90% coverage
- Fails the build if coverage drops

Workflow file location:

.github/workflows/python-app.yml  

---

## Technical Highlights

- Clean, modular architecture
- Strong application of OOP principles
- DRY principle applied
- Robust error handling with custom exceptions
- Persistent data management using pandas
- Automated CI/CD validation
- Production-style project structure

---
