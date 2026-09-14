# Python Learning

This folder contains my Python learning notes, exercises, experiments, practical
work, and engineering lessons as I build my software engineering foundation.

The goal is not simply to watch Python tutorials or memorize syntax. I want to
understand Python well enough to write programs independently, solve problems,
work with files and data, use packages and environments, write tests, and
eventually apply Python to backend engineering and application security.

## Learning Approach

My Python learning follows the Engineering Learning Journal cycle:

**Roadmap → Learn → Practice → Build → Test → Document → Review**

I use roadmap.sh to understand what I should learn, learning resources such as
Corey Schafer to understand concepts, exercises to practice them, and small
projects to prove that I can apply them.

A topic is not considered complete simply because I watched a video. I should be
able to explain the concept, implement it without blindly copying, practice it,
and demonstrate what I learned through my notes or code.

---

# Core Topics

The Python learning path is organized into 10 core topics.

## 1. Python Fundamentals

Foundational Python concepts and the basic structure of Python programs.

### Topics

- Python syntax
- Writing and running Python programs
- Statements and expressions
- Comments
- Variables
- Basic program structure
- Python interpreter
- Basic input and output
- Type casting
- Basic built-in functionality

### Roadmap Alignment

- Learn the Basics
- Basic Syntax
- Variables and Data Types
- Type Casting

---

## 2. Variables, Data Types & Operators

Understanding how Python represents and manipulates different kinds of data.

### Topics

- Variables
- Integers
- Floats
- Strings
- Booleans
- Lists
- Tuples
- Sets
- Dictionaries
- Operators
- Comparison operators
- Logical operators
- Membership and identity
- Type conversion

### Roadmap Alignment

- Variables and Data Types
- Type Casting
- Lists, Tuples and Sets
- Dictionaries

---

## 3. Control Flow & Loops

Learning how programs make decisions and repeat operations.

### Topics

- Conditional statements
- `if`
- `elif`
- `else`
- Boolean expressions
- `for` loops
- `while` loops
- Loop control
- `break`
- `continue`
- Nested loops

### Roadmap Alignment

- Conditionals
- Loops

---

## 4. Functions & Scope

Understanding how to organize reusable logic and manage variable scope.

### Topics

- Defining functions
- Parameters
- Arguments
- Return values
- Default arguments
- Keyword arguments
- Built-in functions
- Lambda functions
- Variable scope
- LEGB rule
- `global`
- `nonlocal`
- Writing reusable functions

### Roadmap Alignment

- Functions
- Built-in Functions
- Lambdas
- Variable Scope
- LEGB

---

## 5. Modules & Packages

Learning how to organize Python code and work with reusable functionality.

### Topics

- Import statements
- Python modules
- Standard library
- Creating custom modules
- Packages
- Package structure
- PyPI
- `pip`
- Package installation
- Dependency management
- Common Python packages
- Regular expressions

### Roadmap Alignment

- Modules
- Package Managers
- PyPI
- Pip
- Conda
- Poetry
- Regular Expressions
- Common Packages

---

## 6. Exception Handling

Learning how to handle errors and unexpected situations safely.

### Topics

- Exceptions
- `try`
- `except`
- `else`
- `finally`
- Raising exceptions
- Handling specific exceptions
- Understanding common Python errors
- Writing safer programs
- Debugging errors

### Roadmap Alignment

- Exceptions

---

## 7. File Handling & Data Processing

Learning how Python works with files and structured data.

### Topics

- Reading files
- Writing files
- File objects
- File paths
- Context managers
- CSV files
- Parsing data
- Processing structured data
- Automating file operations
- Working with text data
- Regular expressions for data processing

### Practical Work

Examples of practical work may include:

- Reading and writing text files
- Processing CSV files
- Renaming multiple files
- Extracting information from data
- Generating output from structured data

### Roadmap Alignment

The roadmap provides related material through:

- Context Managers
- Regular Expressions
- Common Packages

File handling will therefore be developed through practical Python work
alongside the roadmap material.

---

## 8. Object-Oriented Programming

Learning how to structure larger Python programs using objects and classes.

### Topics

- Object-oriented programming
- Classes
- Objects
- Attributes
- Methods
- Constructors
- Inheritance
- Encapsulation
- Special methods
- Dunder methods
- Object relationships

### Roadmap Alignment

- Object-Oriented Programming
- Classes
- Inheritance
- Methods
- Dunder Methods

---

## 9. Virtual Environments & Dependency Management

Learning how to create isolated Python environments and manage project
dependencies.

### Topics

- Python environments
- Virtual environments
- `venv`
- `virtualenv`
- `pip`
- Dependency management
- Package installation
- Requirements files
- Project configuration
- Python version management
- `pyenv`
- `Pipenv`
- Poetry
- `pyproject.toml`

### Roadmap Alignment

- Package Managers
- Pip
- Pipenv
- virtualenv
- pyenv
- Configuration
- `pyproject.toml`
- Poetry

---

## 10. Type Hints & Testing

Learning how to make Python code easier to understand, maintain, and verify.

### Topics

- Type hints
- Python typing
- Static typing
- Pydantic
- Type checking
- `mypy`
- `pyright`
- Unit testing
- Test cases
- Assertions
- `unittest`
- `pytest`
- Test-driven thinking
- Testing normal and failure cases

### Roadmap Alignment

- Static Typing
- Pydantic
- mypy
- pyright
- pyre
- Testing
- pytest
- unittest
- typing

---

# Additional Python Topics

The 10 topics above form the main learning structure.

The roadmap.sh Python roadmap also contains more advanced subjects. These
will be introduced when they become relevant rather than creating unnecessary
additional sections.

### Advanced / Supplementary Topics

- Data Structures & Algorithms
- Recursion
- Sorting Algorithms
- List Comprehensions
- Generator Expressions
- Decorators
- Iterators
- Context Managers
- Concurrency
- Threading
- Multiprocessing
- Asynchronous programming
- The Global Interpreter Lock (GIL)
- Code formatting
- Ruff
- Black
- Documentation
- Sphinx
- Python configuration
- `pyproject.toml`

These subjects may appear inside dated learning entries or be connected to
later backend, testing, DevOps, or security work.

Frameworks such as FastAPI, Django, and Flask will primarily be documented in
the **Backend Engineering** section of the learning journal rather than being
treated as core Python topics.

---

# Learning Entries

Dated Markdown files record what I actually studied and practiced.

A learning entry should be created after meaningful study and practice rather
than being created in advance.

### Example

```text
python/
├── README.md
├── 2026-09-15-functions-and-modules.md
├── 2026-09-17-exceptions.md
├── 2026-09-19-file-handling.md
└── ...
```

Each entry should document useful evidence from the learning session.

Typical sections include:

- What I learned
- What I understand
- What confused me
- What I practiced
- What I built
- Errors or problems encountered
- How I solved them
- Engineering or security lessons
- What I can now explain without notes
- What I will learn next

## Learning Progress

| Topic | Status | Evidence |
|---|---|---|
| Python Fundamentals | ✅ Complete |[Learning Entry](./2026-09-14-python-fundamentals.md) |
| Variables, Data Types & Operators | ✅ Complete | [Learning Entry](./2026-09-14-variables-data-types-and-operators.md) |
| Control Flow & Loops | ✅ Complete | [Learning Entry](./2026-09-14-control-flow-and-loops.md) |
| Functions & Scope | 🟡 In Progress  | — |
| Modules & Packages | ⬜ Not started | — |
| Exception Handling | ⬜ Not started | — |
| File Handling & Data Processing | ⬜ Not started | — |
| Object-Oriented Programming | ⬜ Not started | — |
| Virtual Environments & Dependency Management | ⬜ Not started | — |
| Type Hints & Testing | ⬜ Not started | — |

Status should be updated based on actual understanding and practice, not
simply because a tutorial or video has been watched.

---

# Practice

Python concepts will be reinforced through hands-on exercises and small
programs.

Practice may include:

- Python exercises
- Coding challenges
- Small scripts
- File-processing programs
- Data-processing exercises
- Error-handling exercises
- Object-oriented programs
- Testing exercises
- Small automation tasks

The purpose of practice is to move from:

"I understand the explanation"

to:

"I can write it myself."

---

# Projects & Engineering Application

Python knowledge will eventually be applied to larger software engineering
projects.

Planned applications include:

- Student Management API
- Secure Student Management Application
- Web Vulnerability Scanner
- Secure Cloud Application

Python will therefore become a foundation for later work in:

- Backend Engineering
- Application Security
- Testing
- Docker
- Cloud
- DevSecOps

The project repositories themselves will contain the complete project code and
project-specific documentation. This folder is primarily for the learning
process, experiments, and evidence of how my understanding developed.

---

# Learning Resources

### Primary Python Teacher

**Corey Schafer**

Used primarily for clear explanations and practical Python demonstrations.

### Secondary Resource

**freeCodeCamp.org**

Used when additional explanations, longer courses, or alternative teaching
approaches are useful.

### Roadmap

**roadmap.sh — Python Roadmap**

Used as a learning map to understand the broader Python ecosystem and the
order in which major concepts can be explored.

### Important

No single resource is treated as proof that a topic is complete.

The learning process is:

**Roadmap → Learn → Practice → Build → Test → Document**

---

# AI Usage

AI may be used as a learning assistant, but not as a replacement for
understanding.

Useful ways to use AI include:

- Asking for explanations of difficult concepts
- Asking why an error occurs
- Getting debugging guidance
- Asking for practice questions
- Generating additional test cases
- Reviewing code for mistakes
- Reviewing code for security problems
- Challenging design decisions
- Preparing interview questions
- Improving documentation

After using AI-generated code, I should understand the important parts,
rewrite or explain them where appropriate, and test the result myself.

I will not use AI simply to generate large amounts of code that I cannot
explain.

I will also never put passwords, private keys, API secrets, or other sensitive
credentials into AI prompts.

---

# Engineering Evidence

The purpose of this folder is to create evidence of real technical growth.

Useful evidence includes:

- Dated learning entries
- Working Python programs
- Exercises
- Tests
- Debugging notes
- Git commits
- Project implementations
- Engineering decisions
- Security considerations
- Reflections on mistakes and improvements

The goal is not to produce the largest number of Markdown files or commits.

The goal is to create a truthful record of consistent learning and practical
engineering work.

---

# Reference Material

## Python Roadmap

The Python learning path is guided by the roadmap.sh Python roadmap.

[View Python Roadmap](./python.pdf)

The roadmap is used as a reference for identifying concepts and understanding
the broader Python ecosystem. It is not treated as a checklist that must be
completed blindly.

---

# Current Focus

Python fundamentals and core language development.

The immediate focus is to strengthen the fundamentals before moving deeper
into object-oriented programming, dependency management, typing, and testing.

