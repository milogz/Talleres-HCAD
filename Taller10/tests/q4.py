OK_FORMAT = True

test = {   'name': 'q4',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> preds = predecir(modelo, datos)\n'
                                               '>>> assert isinstance(preds, np.ndarray)\n'
                                               '>>> assert len(preds) == 5\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
