from typing import Any
import warnings

class CompileWarning(Warning):
    ...

class RelationError(Exception):
    ...


class PrologVectorbase:
    def __init__(self) -> None:
        self._can_compile: bool = False

    def add_relationship(self, name: str, *atoms: Any):
        if len(atoms) == 0:
            raise RelationError("relationship must have at least one atom")
        self._can_compile = True

    def compile(self):
        if not self._can_compile:
            warnings.warn("nothing to compile", CompileWarning)