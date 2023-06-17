from vector_prolog.vectorbase import PrologVectorbase


def test_init_should_take_no_arguments():
    PrologVectorbase()


def test_should_have_attribute_add_relationship():
    assert hasattr(PrologVectorbase(), "add_relationship")