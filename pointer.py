def pointer(id):
    import ctypes
    return ctypes.cast(id, ctypes.py_object).value
