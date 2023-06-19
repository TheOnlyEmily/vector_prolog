import pytest
from hypothesis import given, assume, strategies as st
from vector_prolog.vectorbase import PrologVectorbase, RelationError, CompileWarning, CompileError

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

@given(name=st.one_of(st.integers(), st.floats()), atoms=st.lists(elements=st.one_of(st.integers(), st.floats(), st.text())))
def test_add_relationship_raises_relation_error_when_name_is_not_a_string(name, atoms):
    assume(len(atoms) > 0)
    vectorbase = PrologVectorbase()
    with pytest.raises(RelationError, match="relationship name must have type string"):
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

def test_has_property_query():
    vectorbase = PrologVectorbase()
    assert hasattr(vectorbase, "query")

def test_attribute_query_is_callable():
    vectorbase = PrologVectorbase()
    assert callable(vectorbase.query)

@given(relation_name=st.text(), atom=st.one_of(st.integers(), st.floats(), st.text()))
def test_calling_query_before_compile_causes_a_compile_error(relation_name, atom):
    vectorbase = PrologVectorbase()
    with pytest.raises(CompileError, match="vectorbase must be compiled before query is called"):
        vectorbase.query(relation_name, atom)

@given(relation_name=st.text())
def test_query_takes_at_least_one_argument(relation_name):
    vectorbase = PrologVectorbase()
    vectorbase.add_relationship("test", "test")
    vectorbase.compile()
    vectorbase.query(relation_name)

@given(relation_name=st.text(), atoms=st.lists(elements=st.one_of(st.integers(), st.floats(), st.text())))
def test_query_takes_2_or_more_arguments(relation_name, atoms):
    vectorbase = PrologVectorbase()
    vectorbase.add_relationship("test", "test")
    vectorbase.compile()
    vectorbase.query(relation_name, *atoms)

@given(relation_name=st.text())
def test_query_raises_compile_error_if_add_relationship_is_called_after_compile(relation_name):
    vectorbase = PrologVectorbase()
    vectorbase.add_relationship("test", "test")
    vectorbase.compile()
    vectorbase.add_relationship("test", 1)
    with pytest.raises(CompileError, match="vectorbase must be compiled before query is called"):
        vectorbase.query(relation_name)