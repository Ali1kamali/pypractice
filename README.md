
# PyPractice

**PyPractice** is an offline Python practice library designed to help developers improve their programming skills through categorized coding questions and automated answer evaluation.

The library provides a structured collection of programming exercises organized by difficulty level, along with an evaluation engine for checking answers.

## Features

- Fully offline — no internet connection required.
- Three difficulty levels: Easy, Medium, and Hard.
- Categorized programming questions.
- Automated answer calculation and evaluation.
- Lightweight with minimal external dependencies.
- Easy integration into Python projects.
- Open Source under the MIT License.

## Installation

Install PyPractice using pip:

```bash
pip install pypractice
```

## Quick Start

```python
from pypractice import PracticeEngine

practice = PracticeEngine()

# Get available questions
questions = practice.get_questions("easy")

# Evaluate an answer
result = practice.evaluate("easy-001", 4)

print(result)
```

## Difficulty Levels

PyPractice organizes questions into three difficulty levels:

| Level | Description |
| --- | --- |
| Easy | Basic programming concepts and simple exercises. |
| Medium | Intermediate problems requiring logical thinking. |
| Hard | Advanced problems involving complex logic and problem-solving. |

## Project Structure

```text
pypractice/
├── src/
│   └── pypractice/
│       ├── core/
│       ├── questions/
│       │   ├── easy/
│       │   ├── medium/
│       │   └── hard/
│       ├── evaluator/
│       └── models/
│
├── tests/
├── README.md
├── LICENSE
└── pyproject.toml
```

## Usage

### Get Questions

Retrieve questions based on their difficulty level.

```python
questions = practice.get_questions("medium")
```

### Get a Specific Question

```python
question = practice.get_question("easy-001")
```

### Evaluate Answers

Submit an answer and receive an evaluation result.

```python
result = practice.evaluate("easy-001", 4)
```

## Contributing

Contributions are welcome!

If you want to improve PyPractice, add new questions, fix bugs, or introduce new features:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Add or update tests.
5. Submit a Pull Request.

Please make sure that new questions follow the existing question structure and difficulty classification.

## Roadmap

- [x] Initial project structure
- [ ] Question management system
- [ ] Easy, Medium, and Hard question collections
- [ ] Answer calculation engine
- [ ] Automated answer evaluation
- [ ] Comprehensive test coverage
- [ ] Command-line interface (CLI)
- [ ] Expand the question database
- [ ] PyPI release

## License

PyPractice is released under the [MIT License](LICENSE).

You are free to use, modify, and distribute this software according to the license terms.

## Author

**PyPractice Contributors**

---

If you find this project useful, consider giving it a star on GitHub!