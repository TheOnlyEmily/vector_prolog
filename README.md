# Goal
Build a vector-based version of prolog that searches a vector database.

# Purpose
This may be faster than the method swi-prolog uses. This may also make building AIs similar to LLMs much easier.

# Milestones
1. Implement a basic genetic algorithm for creating a specific vector.
1. Implement genetic algorithm for creating two vectors within a certain distance of eachother. 
1. Implement genetic algorithm for creating four vectors, two vector pairs. Where each pair consists of a starting vector and an ending vector. Subtracting an ending vector from the starting vector from the same pair creates a relation vector. Adding the relation vector two the starting vector in the other pair should get that pair's ending vector.