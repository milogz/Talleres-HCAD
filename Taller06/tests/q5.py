OK_FORMAT = True

test = {   'name': 'q5',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> res5 = trabajo_afuera_y_mayores()\n'
                                               ">>> assert isinstance(res5, pd.DataFrame), 'Debe retornar un "
                                               "DataFrame.'\n"
                                               ">>> assert res5.shape[0] == 14311, f'Cantidad de filas incorrecta: "
                                               "{res5.shape[0]}, esperado 14311.'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
