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
__-Basic Arithmetic Operations__: The calculator can solve equations involving any combination of the following operations: addition, subtraction, multiplication, or division.

The following symbols can be used to represent these operations:

Addition: +

Subtraction: -

Multiplication: * or x

Division: /

__-Brackets__: 
   -The calculator supports the use of parentheses () for grouping operations.

   -Other bracket types such as [] and {} are not accepted.

   -When two adjacent bracket elements or a number followed by a bracket element are present,       the calculator interprets the computation as the product of the two elements.

__-Positive & Negative Handling__: 
   -The calculator recognizes + or - before a number or bracket element as an indication of a       positive or negative element.

   -It can simplify multiple adjacent + or - signs into a single + or - sign.
   Example:
   5 + -3 is simplified to 5 - 3.
   5 -- 3 is simplified to 5 + 3.

__-Space & Error Handling__: Is capable of handling whether spaces are included, not included, or a combination of both. Arithemtic-Calculator also produces error message if unclosed bracket, random string, invalid operation detected.
## License
This project is licensed under MIT license.

### Acknowledgements
Thanks to the os library for providing backend framework.
