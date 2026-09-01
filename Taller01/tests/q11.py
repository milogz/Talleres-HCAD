OK_FORMAT = True

test = {   'name': 'q11',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> assert type(tupla_pedidos) == tuple\n'
                                               '>>> assert len(tupla_pedidos) == 3\n'
                                               '>>> for i in tupla_pedidos:\n'
                                               '...     assert type(i) == tuple\n'
                                               '>>> assert tupla_pedidos == (pedidos_semana_1, pedidos_semana_2, '
                                               'pedidos_semana_3)\n'
                                               ">>> print('Felicidades, realizaste este ejercicio correctamente.')\n"
                                               'Felicidades, realizaste este ejercicio correctamente.\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
