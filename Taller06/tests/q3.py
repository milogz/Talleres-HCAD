OK_FORMAT = True

test = {   'name': 'q3',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> res3 = sin_columnas()\n'
                                               ">>> assert isinstance(res3, pd.DataFrame), 'Debe retornar un "
                                               "DataFrame.'\n"
                                               ">>> assert res3.shape == (230509, 125), f'Dimensiones incorrectas: "
                                               "{res3.shape}.'\n"
                                               '>>> assert \'country_name\' not in res3.columns, "La columna '
                                               '\'country_name\' no debe existir."\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
