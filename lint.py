"""Runs pylint over each file in this project"""


from pylint.lint import Run


def main():
    """Runs pylint over each file in this project"""
    files = ['LA.py',
             'test_LA.py',
             'QR.py',
             'test_QR.py',
             'LS.py',
             'test_LS.py',
             'pylint.py']
    for file_ in files:
        Run([file_])


if __name__ == '__main__':
    main()
