"""Module just to test the api of pygradethis"""

from pygradethis.grade_result import python_grade_result
from pygradethis.grade_code import grade_code

from pygradethis.python_grader import grade
from pygradethis.conditions import python_pass_if, python_fail_if

# Output checking only

# correct
result = python_grade_result(
    python_pass_if(2, "You got the right output of 2!"),
    user_result=2
)
# this returns back a tuple (True|False, dict(message = str, correct = True|False, type = 'success|info|warning|error|custom'))
print(result)
# (True, {'x': 2, 'message': 'You got the right output of 2!', 'correct': True, 'type': 'value'})

# incorrect  
result = python_grade_result(
    python_pass_if(2, "You got the right output of 2!"),
    user_result=3
)
# in this None is returned for our tuple because we didn't match any conditions
print(result)
# (False, None)

# if we supply a `python_fail_if` however, we can get a dict back for fail condition match
result = python_grade_result(
    python_pass_if(2, "You got the right output of 2!"),
    python_fail_if(3, "We do not want 3!"),
    user_result=3
)
print(result)
# (True, {'x': 3, 'message': 'We do not want 3!', 'correct': False, 'type': 'value'})

# AST checking only

### Same types, incorrect value
print(grade_code("3", "2"))
# I expected 2, but you wrote 3 in 3 at line 1.

### Different types
print(grade_code("\"2\"", "2"))
# I expected 2, but what you wrote was interpreted as "2" at line 1.
print(grade_code("1 + 1", "2"))
# I expected 2, but what you wrote was interpreted as 1 + 1 at line 1.

### Expression vs expression, incorrect values
print(grade_code("2 + len([1,2])", "2 + len([1,1])"))
# I expected len(obj=[1, 1]), but what you wrote was interpreted as len(obj=[1, 2]) at line 1.
print(grade_code("sum([1,2])", "sum([1,1])"))
# I expected sum(iterable=[1, 1], start=0), but what you wrote was interpreted as sum(iterable=[1, 2], start=0) at line 1.
print(grade_code("2 + sqrt(log(2))", "2 + sqrt(log(1))"))
# I expected 1, but you wrote 2 in log(2) at line 1.

### Function calls are standardized as well
# so that this will not return any feedback because they are equivalent calls
print(grade_code(
        student_code="def foo(a, b=1): pass; foo(1)", 
        solution_code="def foo(a, b=1): pass; foo(1)"
    )
)
# None
# but, this will return a feedback message because the arguments are now different
print(grade_code(
        student_code="def foo(a, b=1): pass; foo(2)", 
        solution_code="def foo(a, b=1): pass; foo(1)"
    )
)
# I expected foo(a=1, b=1), but what you wrote was interpreted as foo(a=2, b=1) at line 1.

# AST + Output checking

# This is if you wanted to do a more complete grade (AST + code output)
result = grade(
            python_pass_if(2, "Woah, nice!"),
            user_code="2", 
            solution_code="2", 
        )
# in this case, we only get a dict back with results
print(result)
# {'message': 'Superb work! Woah, nice!', 'correct': True, 'type': 'success'}

