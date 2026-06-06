def add(a: int, b: int) -> int:
    return a + b

# Исправлено: ранее было add(2, "3"), что вызывало ошибку mypy
result: int = add(2, 3) 