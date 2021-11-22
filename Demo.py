"""Demos the functions in this package"""


import LA
import QR
import LS
import test_LA
import test_QR
import test_LS


Case = tuple[tuple, object]


def main():
    """Demos the functions in this package"""
    # Sometimes the desire to not type as much leads a programmer (me,
    # in this case) to learn a lot about the language they're using
    # These dictionaries allow us to find modules based on their names
    code_mods: dict = {'LA':LA,
                       'QR':QR,
                       'LS':LS}
    test_mods: dict = {'test_LA':test_LA,
                       'test_QR':test_QR,
                       'test_LS':test_LS}
    # m_name is a string, m_val is a module
    for m_name, m_val in code_mods.items():
        # Print module header
        print(f'Module {m_name}: {m_val.__doc__}')
        # The test module for the current code module
        # Note: to properly annotate would have to import types module
        t_mod = test_mods['test_' + m_name]
        # Build a dictionary of all functions in the current module
        m_fun: dict = {obj:getattr(m_val, obj)
                for obj in dir(m_val) if obj[0] != '_' and str.islower(obj[0])}
        # Iterate over each of these functions and print docstring and test
        for f_name, f_val in m_fun.items():
            # Grab and print the one-line documentation for the function
            shortdoc: str = f_val.__doc__[:f_val.__doc__.index('\n')]
            print(f'  Function {m_name}.{f_name}: {shortdoc}')
            # Print an example of function usage
            try:
                # Find the test function for the current code function
                # Note: to properly annotate would have to import types module
                t_fun = getattr(t_mod, 'test_' + f_name)
                # Tests have been written to return an example test case,
                # so grab it and print it.
                case: Case = t_fun()
                args: str = ', '.join(map(str, case[0]))
                rslt: str = str(case[1])
                print('    Example use case:')
                print(f'    {m_name}.{f_name}({args}) = {rslt}')
            except AssertionError:
                print("    ERROR: Failed test. Do not use.")
            except AttributeError:
                continue


if __name__ == '__main__':
    main()
