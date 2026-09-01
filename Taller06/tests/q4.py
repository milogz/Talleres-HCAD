OK_FORMAT = True

test = {   'name': 'q4',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> res4 = indexar_columnas_numericamente()\n'
                                               ">>> assert isinstance(res4, pd.DataFrame), 'Debe retornar un "
                                               "DataFrame.'\n"
                                               ">>> assert res4.shape == (230509, 107), f'Dimensiones incorrectas: "
                                               "{res4.shape}, esperado (230509, 107).'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
