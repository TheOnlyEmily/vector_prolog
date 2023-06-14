# Goal
Build a vector-based version of prolog that searches a vector database.

# Purpose
This may be faster than the method swi-prolog uses. This may also make building AIs similar to LLMs much easier.

# Milestones
1. Implement a basic genetic algorithm for creating a specific vector.
1. Implement genetic algorithm for creating two vectors within a certain distance of eachother. 
1. Implement genetic algorithm for creating four vectors, two vector pairs. Where each pair consists of a starting vector and an ending vector. Subtracting an ending vector from the starting vector from the same pair creates a relation vector. Adding the relation vector two the starting vector in the other pair should get that pair's ending vector.

# Example Use
```python
from vector_prolog.vectorbase import PologVectorbase
from vector_prolog import vector_rule

pvb = PrologVectorbase()

pvb.add_relationship("safety inspector", "Homer")
pvb.add_relationship("homemaker", "Marge")
pvb.add_relationship("student", "Bart")
pvb.add_relationship("student", "Lisa")

pvb.add_relationship("parent", "Homer", "Bart")
pvb.add_relationship("parent", "Homer", "Lisa")
pvb.add_relationship("parent", "Marge", "Bart")
pvb.add_relationship("parent", "Marge", "Lisa")
pvb.add_relationship("parent", "Homer", "Maggie")
pvb.add_relationship("parent", "Marge", "Maggie")

pvb.add_rule(
    name="siblings",
    arguments=["x", "y"],
    variables=["z"]
    body=vector_rule.intersect(
        vector_rule.do_query("parent", "z", "x"),
        vector_rule.do_query("parent", "z", "y"),
        vector_rule.not_equal("x", "y"),
    ),
)

pvb.compile()

pvb.query("safety inspector", "Homer").as_int() # should return 1
pvb.query("safety inspector", "Marge").as_int() # should return 0
pvb.query("student").as_list() # should return ['Bart', 'Lisa']
pvb.query("parent").as_list() # should return [['Homer', 'Bart'], ['Homer', 'Lisa'], etc.]
pvb.query("siblings", "Bart").as_list() # should return ['Lisa', 'Maggie'] 
```