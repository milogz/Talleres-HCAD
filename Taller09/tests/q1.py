OK_FORMAT = True

test = {   'name': 'q1',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> assert isinstance(datos, pd.DataFrame), 'datos debe ser un "
                                               "DataFrame.'\n"
                                               '>>> assert \'Name\' in datos.columns, "Debe contener la columna '
                                               '\'Name\'."\n'
                                               ">>> assert len(datos) > 0, 'El DataFrame no debe estar vacio.'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
