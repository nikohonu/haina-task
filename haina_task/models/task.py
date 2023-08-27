import json
from dataclasses import dataclass, field
from datetime import datetime
from typing import Callable


@dataclass
class Task:
    name: str
    chain: list[str] | None
    description: str | None
    schedule: datetime | None
    deadline: datetime | None
    recurrence: str | None
    project: str | None

    def as_tuple(
        self, project_name_to_id: Callable[[str | None], int | None]
    ) -> tuple[
        str,
        str | None,
        str | None,
        datetime | None,
        datetime | None,
        str | None,
        int | None,
    ]:
        chain = json.dumps(self.chain) if self.chain else None
        return (
            self.name,
            chain,
            self.description,
            self.schedule,
            self.deadline,
            self.recurrence,
            project_name_to_id(self.project),
        )
