def explore_module(name):
    """Explore available attributes inside a Python module."""
    try:
        module = __import__(name)
        attributes = [attr for attr in dir(module) if not attr.startswith("_")]
        print(f"\nAttributes in module '{name}':\n", attributes)
    except ModuleNotFoundError:
        print("Module not found!")
