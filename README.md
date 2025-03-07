# FruityVice Task

This is a command-line tool that interacts with the FruityVice API to fetch fruit details. It supports both human-readable and machine-readable output formats.

## Features

- Fetches fruit details, more specifically:name, ID, family, sugar, and carbohydrates.
- Supports human-readable and machine-readable output formats.
- Gracefully handles errors, such as unrecognized fruit names or service unavailability.

## Installation

1. Clone the Repository:

- git clone https://github.com/D-K-T-T/RSE-Interview-Task.git
- cd fruity_vice_task

2. Install Dependencies

- pip install -r requirements.txt

## Usage

To fetch fruit details:

- python -m fruity_vice_task.fruity_vice_cli <fruit_name> --format <human|machine>
- Replace <fruit_name> with the name of the fruit you want to look up.
- Use --format human for human-readable output or --format machine for machine-readable output.
- e.g. python -m fruity_vice_task.fruity_vice_cli Tomato --format human


## Tests

1. To run tests use the following command:

- python -m unittest discover -v tests


## How to contribute

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Commit your changes (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature-branch).
5. Create a new Pull Request.


## Future Improvements 
- In the future, I plan to add a setup file to make it easier to install and distribute the project as a Python package. 
- For now, the dependencies can be installed using `requirements.txt`.