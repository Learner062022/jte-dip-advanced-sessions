from typing import List


class Model:

    def __init__(self):
        self._tasks: List[str] = []

    def add_task(self, task: str) -> None:
        self._tasks.append(task)

    @property
    def tasks(self) -> List[str]:
        return self._tasks
