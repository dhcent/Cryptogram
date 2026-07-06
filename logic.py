import random

def sattolo_cycle(items) -> None:
    """Sattolo's algorithm."""
    i = len(items)
    while i > 1:
        i = i - 1
        j = random.randrange(i)  # 0 <= j <= i-1
        items[j], items[i] = items[i], items[j]

