from typing import List


class View:

    def print_menu(self):
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Exit")

    def get_input(self, prompt: str) -> str:
        return input(prompt)

    def print_message(self, message: str) -> None:
        print(message)

    def list_tasks(self, tasks: List, message: str) -> None:
        self.print_message(message)
        for idx, task in enumerate(tasks, start=1):
            self.print_message(f"{idx}. {task}")
