# randlab

## What it does
Utilities to generate random numeric data for testing and learning.

## Motivation
This project emerged as a way to learn Python and good programming practices while developing useful tools for data generation.
It will also be used as a basis for future studies involving statistics, software testing, export, and interfaces.

## How to use

### Random integer list
`Inputer.intlist(a, b, c)`

Parameters:
- `a`: list length
- `b`: minimum value (inclusive)
- `c`: maximum value (inclusive)

Example:
Inputer.intlist(5, -2, 20)

        [-2, 0, 5, 12, 1]

-----

### Random float list
`Inputer.floatlist(a, b, c, d(optional))`

Parameters:
- `a`: list length
- `b`: minimum value (inclusive)
- `c`: maximum value (inclusive)
- `d`: decimal places (optional, default=2)

Example:

Inputer.floatlist(5, -2, 20)

        [-1.40, 0.01, -1.22, 19.99, 20.00]

## Roadmap
1. seeds
2. fixed lists
3. statistics
4. report
5. order/filer
6. export
7. cli
8. module
9. clean GUI

## License

MIT License — free to use, study, and modify. Do not remove the credit

## This is a test commit
## Contributio
Open for educational PRs.
