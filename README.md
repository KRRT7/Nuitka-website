# Nuitka Website

## Introduction

Welcome to the Nuitka Website repository. This repository contains the source code and documentation for the Nuitka website, which is built using Sphinx and other tools. Nuitka is a Python compiler that translates Python code into C or C++ code and then compiles it into standalone executables, extension modules, or accelerated programs.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Nuitka/Nuitka-website.git
   cd Nuitka-website
   ```

2. **Set up a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Build the site:**
   ```bash
   python -m invoke site
   ```

5. **Serve the site locally:**
   ```bash
   python -m invoke run -t serve-site
   ```

## Usage

After setting up the project, you can make changes to the documentation and see the results in real-time. The site will be served at `http://localhost:8080`.

## Contributing

We welcome contributions to the Nuitka website. To get started, please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute.

### Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project, you agree to abide by its terms.

### How to Contribute

1. **Fork the repository:**
   Click the "Fork" button at the top right corner of the repository page.

2. **Clone your fork:**
   ```bash
   git clone https://github.com/your-username/Nuitka-website.git
   cd Nuitka-website
   ```

3. **Create a new branch:**
   ```bash
   git checkout -b my-feature-branch
   ```

4. **Make your changes and commit them:**
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

5. **Push your changes to your fork:**
   ```bash
   git push origin my-feature-branch
   ```

6. **Create a pull request:**
   Go to the original repository and click the "New pull request" button. Select your branch and submit the pull request.

### Coding Standards

- Follow the PEP 8 style guide for Python code.
- Write clear and concise commit messages.
- Ensure that your code is well-documented with comments and docstrings.

## License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for more details.
