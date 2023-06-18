import pytest
from hypothesis import given, assume, strategies as st
from vector_prolog.vectorbase import PrologVectorbase, RelationError

def test_init_should_take_no_arguments():
    PrologVectorbase()

def test_should_have_attribute_add_relationship():
    assert hasattr(PrologVectorbase(), "add_relationship")

def test_add_relationship_should_be_callable():
    assert callable(PrologVectorbase().add_relationship)

@given(name=st.text(), atoms=st.lists(elements=st.one_of(st.integers(), st.floats(), st.text())))
def test_add_relationship_takes_a_string_and_multiple_atoms(name, atoms):
    assume(len(atoms) > 0)
    vectorbase = PrologVectorbase()
    vectorbase.add_relationship(name, *atoms)

@given(name=st.text())
def test_add_relationship_raises_relation_error_when_0_atoms_given(name):
    vectorbase = PrologVectorbase()
    with pytest.raises(RelationError, match="relationship must have at least one atom"):
        vectorbase.add_relationship(name)