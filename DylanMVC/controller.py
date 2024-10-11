from model import Model
from view import View


class Controller:
    def __init__(self, model: Model, view: View):
        self._model = model
        self._view = view

    def run(self) -> None:
        while True:
            self._view.print_menu()
            choice = self._view.get_input("Choose an option: ")
            if choice == '1':
                new_task = self._view.get_input("Enter a new task: ")
                self._model.add_task(new_task)
                self._view.print_message("Task added!")
            elif choice == '2':
                self._view.list_tasks(self._model.tasks, "\nYour Tasks:")
            elif choice == '3':
                self._view.print_message("Goodbye!")
                break
            else:
                self._view.print_message("Invalid option. Try again.")


if __name__ == "__main__":
    controller = Controller(Model(), View())
    controller.run()

