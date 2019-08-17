
#! /usr/bin/python3.5
"""
Process         : Execute Bash commands in a secure way by checking the output type
Author          : Suganth Mohan.
Created         : August 17 2019
Last Modified   : 


VERSION CONTROL :
_______________

NAME
    ast

MODULE REFERENCE
    https://docs.python.org/3.5/library/ast.html
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    ast
    ~~~
    
    The `ast` module helps Python applications to process trees of the Python
    abstract syntax grammar.  The abstract syntax itself might change with
    each Python release; this module helps to find out programmatically what
    the current grammar looks like and allows modifications of it.
    
    An abstract syntax tree can be generated by passing `ast.PyCF_ONLY_AST` as
    a flag to the `compile()` builtin function or by using the `parse()`
    function from this module.  The result will be a tree of objects whose
    classes all inherit from `ast.AST`.
    
    A modified abstract syntax tree can be compiled into a Python code object
    using the built-in `compile()` function.
    
    Additionally various helper functions are provided that make working with
    the trees simpler.  The main intention of the helper functions and this
    module in general is to provide an easy to use interface for libraries
    that work tightly with the python syntax (template engines for example).
    
    
    :copyright: Copyright 2008 by Armin Ronacher.
    :license: Python License.
"""

# IMPORT STATEMENTS HERE
from ast import literal_eval
import pandas as pd

# INPUT DATASTRUCTURE
string= "[{'Category':'Cool','Engine':'Cryo'},{'Category':'Hot','Engine':'Combust'},{'Category':'Neutral','Engine':'ElectroMag' }]"

# CONVERT THE STRING TO DATASTRUCUTRE
ds = literal_eval(string)

# CONVERT DATASTRUCTURE TO DATAFRAME
df = pd.DataFrame(ds)

print(df)
