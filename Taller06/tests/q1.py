OK_FORMAT = True

test = {   'name': 'q1',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> res = importar_e_indexar()\n'
                                               ">>> assert isinstance(res, pd.DataFrame), 'Debe retornar un "
                                               "DataFrame.'\n"
                                               ">>> assert res.shape == (230509, 128), f'Dimensiones incorrectas: "
                                               "{res.shape}, esperado (230509, 128).'\n"
                                               '>>> assert res.index.name == \'id\', "El indice debe ser la columna '
                                               '\'id\'."\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
