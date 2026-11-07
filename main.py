"""Мини-проект: список задач в терминале."""


def main():
    tasks = []
    print("Список задач. Введите задачу или 'выход'.")

    while True:
        task = input("> ").strip()
        if task.lower() == "выход":
            print("До встречи!")
            break
        if task:
            tasks.append(task)
            print(f"Добавлено: {task}")
            print("Текущие задачи:")
            for number, item in enumerate(tasks, start=1):
                print(f"{number}. {item}")


if __name__ == "__main__":
    main()
