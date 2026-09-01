OK_FORMAT = True

test = {   'name': 'q2',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> assert callable(primera_letra), 'primera_letra debe ser una "
                                               "funcion.'\n"
                                               ">>> assert primera_letra([23, '2', 46, 'l', 8.3, 'm']) == 'l', 'Falla "
                                               "con la lista del enunciado.'\n"
                                               ">>> assert primera_letra([1, 2, '3', 4.5]) == '', 'Falla cuando no hay "
                                               "letras.'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
