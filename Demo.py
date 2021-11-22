"""Demos the functions in this package"""


import LA
import QR
import LS
import test_LA
import test_QR
import test_LS


Test = tuple[tuple, object]


def main():
    """Demos the functions in this package"""
    # Sometimes the desire to not type as much leads a programmer (me,
    # in this case) to learn a lot about the language they're using
    code_mods: dict = {'LA':LA,
                       'QR':QR,
                       'LS':LS}
    test_mods: dict = {'test_LA':test_LA,
                       'test_QR':test_QR,
                       'test_LS':test_LS}
    for m_name, m_val in code_mods.items():
        # Module header
        print(f'Module {m_name}: {m_val.__doc__}')
        # Build a dictionary of all functions in the current module
        m_fun = {obj:m_val.__getattribute__(obj)
                for obj in dir(m_val) if obj[0] != '_' and str.islower(obj[0])}
        # The test module for the current code module
        t_mod = test_mods['test_' + m_name]
        # Iterate over each of these functions and print docstring and test
        for f_name, f_val in m_fun.items():
            shortdoc = f_val.__doc__[:f_val.__doc__.index('\n')]
            print(f'  Function {m_name}.{f_name}: {shortdoc}')
            # The test function for the current code function
            try:
                t_fun = t_mod.__getattribute__('test_' + f_name)  # The test function
                test = t_fun()  # The test function returns a test case, so use that
                print('    Example use case:')
                print(f'    {m_name}.{f_name}({", ".join(map(str, test[0]))}) = {test[1]}')
            except AssertionError:
                print("    Actually that function is broken don't use it")
            except AttributeError:
                continue


if __name__ == '__main__':
    main()
