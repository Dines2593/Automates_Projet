# Automaton Project README

This project is an implementation of operations on finite automata. It provides functionalities to create, manipulate, and analyze deterministic and non-deterministic finite automata.

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Overview

The project is designed to perform various operations on finite automata, including creating new automata, importing existing ones, and applying operations such as determinization, completion, pruning, concatenation, and more. The main functionalities are organized into a user-friendly menu system.

## Project Structure

The project is structured into several modules:

- `classes.py`: Contains the definition of the `Automate` and `State` classes.
- `completion.py`: Implements functions for checking and making automata complete.
- `determinisation.py`: Provides functions for determinizing automata.
- `manipulate.py`: Includes functions for creating, editing, and printing automata.
- `otherOperations.py`: Contains additional operations like making automata complete, mirroring, Cartesian product, and concatenation.
- `pruned.py`: Implements the pruning operation on automata.
- `wordRecognize.py`: Contains functions for recognizing words in automata.
- `exp_language_check.py`: Implements functions to extract regular expressions and check language equivalence.

## Usage

To use the project, run the `menu()` function from the main script.

The script will guide you through the available options, allowing you to create, manipulate, and analyze finite automata.

## Features

The project provides the following features:

1. **Create and Import Automata:**
   - Create a new automaton.
   - Import an existing automaton from a JSON file.

2. **Automata Verifications:**
   - Word recognition in an automaton.
   - Check if the automaton is complete.
   - Check if the automaton is determinized.
   - Identify the language recognized by the automaton.
   - Check language equivalence with another automaton.
   - Extract a regular expression for the recognized language.

3. **Automata Operations:**
   - Modify an automaton.
   - Make an automaton complete.
   - Make an automaton deterministic.
   - Prune an automaton.
   - Concatenate two automata.
   - Compute the Cartesian product of two automata.
   - Create the mirror image of an automaton.
   - Create the complement of an automaton.

4. **Save and Delete:**
   - Save the automaton to a JSON file.
   - Delete the automaton.

## Dependencies

The project relies on the following dependencies:

- `json`: For handling JSON serialization/deserialization.
- `os`: For interacting with the file system.
  
## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the terms of the license.
