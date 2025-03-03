# Arithemtic-Calculator
Arithemtic-Calculator is a calculator that performs the following operations: addition, subtraction, multiplication, and division. It also supports brackets, negative numbers, and some more awkard inputs such as multiple + and - signs.
##Table of contents
1. [Installation](#installation)
2. [Usage](#usage)
4. [License](#license)
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/johnblessmbunga/Arithemtic-Calculator.git
   cd Arithemtic-Calculator
   npm install
## Usage
To strat application ,run:

npm start
### Features
__-Basic Arithmetic Operations__: Input an equation to with any combination of the follwoing operations; addition, subtraction, multiplication or division using user input.To represent these operations the follwoing symbols can be used +,-,*,x,/. 

__-Brackets__: Can use brackets in equations with symbols \(\) other brackets such as \[\] and \{\} are not accepted. When two adjacent bracket elements or a number element follwed by a bracket element the result of the commputation is the product of the two elements.

__-Positive & Negative Handling__: Recognises + or - before a number or bracket element as  an indication of a positive or negative element. Additionaly Arithemtic-Calculator can simplify multiple adjacent + or/and - signs into a single + or - sign.

__-Space & Error Handling__: Is capable of handling whether spaces are included, not included, or a combination of both. Arithemtic-Calculator also produces error message if unclosed bracket, random string, invalid operation detected.
## License
This project is licensed under MIT license.

### Acknowledgements
Thanks to the os library for providing backend framework.
