OK_FORMAT = True

test = {   'name': 'q2',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> res2 = indice_sencillo_a_multiple()\n'
                                               ">>> assert isinstance(res2, pd.DataFrame), 'Debe retornar un "
                                               "DataFrame.'\n"
                                               ">>> assert isinstance(res2.index, pd.MultiIndex), 'El indice debe ser "
                                               "un MultiIndex.'\n"
                                               ">>> assert res2.shape == (230509, 127), f'Dimensiones incorrectas: "
                                               "{res2.shape}.'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
