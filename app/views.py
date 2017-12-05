from flask import render_template, request, flash, redirect, url_for
from app import app
from .sudopy import Sudoku


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/solution', methods=['POST'])
def solution():
    data = request.form
    data = clean_puzzle(data)
    S = Sudoku(data)
    if S.validate():
        T = S.solve()
        return render_template('solution.html', solved_puzzle=T.puzzle)
    else:
        flash('Invalid Sudoku')
        return redirect(url_for('index'))


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
