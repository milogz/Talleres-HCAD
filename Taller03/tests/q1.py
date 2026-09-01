OK_FORMAT = True

test = {   'name': 'q1',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> assert callable(suma_lista), 'suma_lista debe ser una funcion.'\n"
                                               ">>> assert round(suma_lista([20, 12, 21.3, 34]), 2) == 87.3, 'Falla "
                                               "con la lista del enunciado.'\n"
                                               ">>> assert suma_lista([1, 2, 3, 4, 5]) == 15, 'Falla con lista [1, 2, "
                                               "3, 4, 5].'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
