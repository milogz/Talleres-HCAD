OK_FORMAT = True

test = {   'name': 'q13',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> assert type(dicc_meses) == dict\n'
                                               ">>> assert len(dicc_meses) == 12, 'Tu diccionario no tiene los 12 "
                                               "meses.'\n"
                                               ">>> for mes in ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', "
                                               "'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', "
                                               "'Diciembre']:\n"
                                               "...     assert mes in dicc_meses, f'Falta el mes {mes}.'\n"
                                               ">>> print('Felicidades, realizaste este ejercicio correctamente.')\n"
                                               'Felicidades, realizaste este ejercicio correctamente.\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
