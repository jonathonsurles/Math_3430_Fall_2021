"""Runs pylint over each file in this project"""


from pylint.lint import Run


def main():
    """Runs pylint over each file in this project"""
    args = ['-j 0']
    files = ['LA.py',
             'test_LA.py',
             'QR.py',
             'test_QR.py',
             'LS.py',
             'test_LS.py',
             'lint.py']
    Run(args + files)


if __name__ == '__main__':
    main()
