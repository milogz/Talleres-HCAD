OK_FORMAT = True

test = {   'name': 'q3',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> mod = crear_modelo(datos)\n'
                                               '>>> assert isinstance(mod, LinearRegression)\n'
                                               ">>> assert hasattr(mod, 'coef_')\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
