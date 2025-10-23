# Contributing to Blog-App

First off, thank you for considering contributing to Blog-App! It's people like you that make this project better.

## Code of Conduct

By participating in this project, you are expected to uphold our Code of Conduct:

- Use welcoming and inclusive language
- Be respectful of different viewpoints and experiences
- Accept constructive criticism gracefully
- Focus on what is best for the community
- Show empathy towards other community members

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* Use a clear and descriptive title
* Describe the exact steps which reproduce the problem
* Provide specific examples to demonstrate the steps
* Describe the behavior you observed after following the steps
* Explain which behavior you expected to see instead and why
* Include screenshots if possible

### Suggesting Enhancements

If you have a suggestion for the project, we'd love to hear about it! Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* A clear and descriptive title
* A detailed description of the proposed feature
* Any possible drawbacks
* Mock-ups or examples if applicable

### Pull Requests

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. If you've changed APIs, update the documentation
4. Ensure the test suite passes
5. Make sure your code follows the existing style
6. Issue that pull request!

## Development Process

1. Create a virtual environment and activate it:
```bash
python -m venv .venv
source .venv/bin/activate  # On Linux/Mac
# or
.venv\Scripts\activate     # On Windows
```

2. Install development dependencies:
```bash
pip install -r requirements.txt
```

3. Make your changes and test them:
```bash
python manage.py test
```

### Coding Style

* Follow PEP 8 guidelines
* Use meaningful variable and function names
* Add comments for complex logic
* Keep functions focused and single-purpose
* Write descriptive commit messages

## Project Structure

When adding new features, please maintain the existing project structure:

```
blog/               # Main project directory
├── blog/           # Project settings
├── members/        # User authentication app
│   ├── views.py    # Authentication views
│   └── templates/  # Auth templates
└── theblog/        # Blog functionality app
    ├── views.py    # Blog views
    ├── models.py   # Blog models
    └── templates/  # Blog templates
```

## Testing

* Write tests for new features
* Update tests for modified features
* Ensure all tests pass before submitting PR
* Include both unit and integration tests where appropriate

## Documentation

* Update README.md if you change functionality
* Comment your code where necessary
* Update docstrings for any modified functions
* Add type hints to function definitions

## Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters
* Reference issues and pull requests liberally after the first line

## Questions?

Feel free to open an issue with your question or contact the maintainers directly.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.