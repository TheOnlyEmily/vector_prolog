from typing import Any

class RelationError(Exception):
    ...


class PrologVectorbase:
    def add_relationship(self, name: str, *atoms: Any):
        if len(atoms) == 0:
            raise RelationError("relationship must have at least one atom")