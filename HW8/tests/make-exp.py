test = {
  'name': 'make-exp',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (make-exp 2 4)
          16
          scm> (make-exp 'x 1)
          x
          scm> (make-exp 'x 0)
          1
          scm> x^2
          (^ x 2)
          scm> (base x^2)
          x
          scm> (exponent x^2)
          2
          scm> (exp? x^2) ; True or False
          #t
          scm> (exp? 1)
          #f
          scm> (exp? 'x)
          #f
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw08)
      scm> (define x^2 (make-exp 'x 2))
      scm> (define x^3 (make-exp 'x 3))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
