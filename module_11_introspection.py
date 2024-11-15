def introspection_info(obj):
    info = {
        "type": type(obj).__name__,
        "attributes": [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")],
        "methods": [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")],
        "module": getattr(obj, "__module__", None),
        "doc": getattr(obj, "__doc__", None)
    }
    return info

# Пример использования
number_info = introspection_info(42)
print(number_info)
