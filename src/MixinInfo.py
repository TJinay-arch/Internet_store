class CreationInfoMixin:
    """Миксин-класс, который выводит информацию о создании объекта в отладочном режиме."""

    debug_mode = False  # Переменная для включения/отключения отладочного режима

    def __init__(self, *args, **kwargs):
        if self.debug_mode:
            class_name = type(self).__name__
            args_repr = ", ".join(repr(arg) for arg in args)
            kwargs_repr = ", ".join(f"{k}={repr(v)}" for k, v in kwargs.items())
            params = f'({args_repr}{", " if args_repr and kwargs_repr else ""}{kwargs_repr})'
            print(f"Создан объект класса '{class_name}' с параметрами {params}")
        # Здесь нет вызова super().__init__(), так как выше нет смысла продолжать
