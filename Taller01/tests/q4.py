OK_FORMAT = True

test = {   'name': 'q4',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> import math as _math\n'
                                               '>>> assert type(primera_mitad) == list\n'
                                               '>>> assert type(segunda_mitad) == list\n'
                                               '>>> assert len(primera_mitad) == _math.ceil(len(nombres) / 2)\n'
                                               '>>> assert len(segunda_mitad) == len(nombres) // 2\n'
                                               ">>> assert primera_mitad == sorted(primera_mitad), 'primera_mitad no "
                                               "esta en orden alfabetico.'\n"
                                               ">>> assert segunda_mitad == sorted(segunda_mitad), 'segunda_mitad no "
                                               "esta en orden alfabetico.'\n"
                                               ">>> print('Felicidades, realizaste este ejercicio correctamente.')\n"
                                               'Felicidades, realizaste este ejercicio correctamente.\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
