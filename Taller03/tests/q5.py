OK_FORMAT = True

test = {   'name': 'q5',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> assert callable(modulo_del_minimo), 'modulo_del_minimo debe ser "
                                               "una funcion.'\n"
                                               '>>> fn = modulo_del_minimo([3, 4, 2, 5, 5, 6, 3])\n'
                                               ">>> assert str(fn).find('lambda') > -1, 'modulo_del_minimo debe "
                                               "retornar una funcion lambda.'\n"
                                               ">>> assert fn(2) == 1, 'En [3,4,2,5,5,6,3], el minimo repetido es 3. 3 "
                                               "% 2 debe ser 1.'\n"
                                               ">>> assert fn(3) == 0, '3 % 3 debe ser 0.'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
