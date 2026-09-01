OK_FORMAT = True

test = {   'name': 'q4',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> assert callable(funcion_interactiva), 'funcion_interactiva debe "
                                               "ser callable.'\n"
                                               ">>> fig_test = funcion_interactiva('Casos', 'Historico')\n"
                                               ">>> assert isinstance(fig_test, go.Figure), 'Debe retornar un "
                                               "go.Figure.'\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
