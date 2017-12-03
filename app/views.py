from flask import render_template, request
from app import app
from .sudopy import Sudoku


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/solution', methods=['POST'])
def solution():
    data = request.form.getlist('cell-input')
    print(data)
    data = clean_puzzle(data)
    S = Sudoku(data)
    T = S.solve()
    print(T.to_list())
    return render_template('solution.html', solved_puzzle=T.puzzle)


def clean_puzzle(puzzle):
    """
    converts input from request.form to a string format readable by Sudoku
    """
    output = ''
    for val in puzzle:
        if val == '':
            output += '.'
        elif int(val) in range(1, 10):
            output += val
    return output
