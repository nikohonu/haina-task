from haina_task.controllers.controller import Controller
from haina_task.models.model import Model
from haina_task.views.typer_view import TyperView


def main() -> None:
    controller = Controller(Model(), TyperView())
    controller.start()


if __name__ == "__main__":
    main()
