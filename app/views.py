from flask import render_template, request, flash
from app import app
from .sudopy import Sudoku, InvalidInputError


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/solution', methods=['POST'])
def solution():
    data = request.form
    data = clean_puzzle(data)
    S = Sudoku(data)
    T = S.solve()
    return render_template('solution.html', solved_puzzle=T.puzzle)
    # try:
    #     S = Sudoku(data)
    #     T = S.solve()
    #     return render_template('solution.html', solved_puzzle=T.puzzle)
    # except InvalidInputError:
    #     flash('Invalid Sudoku')
    #     render_template('index.html')
    # else:
    #     flash('An error occured')
    #     render_template('index.html')


def clean_puzzle(puzzle):
    """
    converts input from request.form to a string format readable by Sudoku
    """
    output = ''
    for val in puzzle.values():
        if val == '':
            output += '.'
        elif int(val) in range(1, 10):
            output += val
    return output
