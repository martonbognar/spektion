def get_range(values: [(float, float)]) -> (float, float):
    min_x = min(elem[0] for elem in values)
    max_x = max(elem[0] for elem in values)
    return (min_x, max_x)


def get_max_value(values: [(float, float)]) -> float:
    return max(elem[1] for elem in values)


def stern_volmer(initial_intensity: float, q: float, values: [(float, float)]) -> float:
    max_intensity = get_max_value(values)
    return ((max_intensity / initial_intensity) - 1) / q
