import pytest
from hypothesis import given, assume, strategies as st
from vector_prolog.vectorbase import PrologVectorbase, RelationError, CompileWarning

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

@given(name=st.text(), atoms=st.lists(elements=st.one_of(st.integers(), st.floats(), st.text())))
def test_add_relationship_returns_none(name, atoms):
    assume(len(atoms) > 0)
    vectorbase = PrologVectorbase()
    assert vectorbase.add_relationship(name, *atoms) == None

def test_has_attribute_compile():
    vectorbase = PrologVectorbase()
    assert hasattr(vectorbase, "compile")

def test_attribute_compile_is_callable():
    vectorbase = PrologVectorbase()
    assert callable(vectorbase.compile)

@pytest.mark.filterwarnings("ignore:nothing to compile")
def test_compile_takes_no_arguments():
    vectorbase = PrologVectorbase()
    vectorbase.compile() 

@pytest.mark.filterwarnings("ignore:nothing to compile")
def test_compile_returns_none():
    vectorbase = PrologVectorbase()
    assert vectorbase.compile() == None 

def test_compile_issues_warning_when_no_relationships_are_added():
    vectorbase = PrologVectorbase()
    with pytest.warns(CompileWarning, match="nothing to compile"):
        vectorbase.compile()

@pytest.mark.filterwarnings("error:nothing to compile")
@given(name=st.text(), atoms=st.lists(elements=st.one_of(st.integers(), st.floats(), st.text())))
def test_calling_compile_after_add_relationship_should_not_produce_warning(name, atoms):
    assume(len(atoms) > 0)
    vectorbase = PrologVectorbase()
    vectorbase.add_relationship(name, *atoms)
    vectorbase.compile()