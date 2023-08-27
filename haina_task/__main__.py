from haina_task.controller import Controller
from haina_task.model import Model
from haina_task.typer_view import TyperView


def main() -> None:
    controller = Controller(Model(), TyperView())
    controller.start()


if __name__ == "__main__":
    main()
