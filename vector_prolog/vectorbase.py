from typing import Any
import warnings

class CompileError(Exception):
    ...

class CompileWarning(Warning):
    ...

class RelationError(Exception):
    ...


class PrologVectorbase:
    def __init__(self) -> None:
        self._can_compile: bool = False
        self._can_query: bool = False

    def add_relationship(self, name: str, *atoms: Any):
        if type(name) is not str:
            raise RelationError("relationship name must have type string")
        if len(atoms) == 0:
            raise RelationError("relationship must have at least one atom")
        self._can_compile = True
        self._can_query=False

# TODO change CompileWarning to CompileError
    def compile(self) -> None:
        if not self._can_compile:
            warnings.warn("nothing to compile", CompileWarning)
        self._can_query = True

    def query(self, name: str, *atoms: list[Any]) -> int:
        if not self._can_query:
            raise CompileError("vectorbase must be compiled before query is called")