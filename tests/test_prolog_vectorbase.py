from hypothesis import given, assume, strategies as st
from vector_prolog.vectorbase import PrologVectorbase

def test_init_should_take_no_arguments():
    PrologVectorbase()

def test_should_have_attribute_add_relationship():
    assert hasattr(PrologVectorbase(), "add_relationship")

def test_add_relationship_should_be_callable():
    assert callable(PrologVectorbase().add_relationship)

@given(name=st.text(), atoms=st.lists(elements=st.one_of(st.integers(), st.floats(), st.text())))
def test_add_relationship_takes_a_string_and_multiple_atoms(name, atoms):
    vectorbase = PrologVectorbase()
    vectorbase.add_relationship(name, *atoms)