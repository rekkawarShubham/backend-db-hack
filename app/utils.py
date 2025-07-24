def deep_merge_dicts(original: dict, update: dict) -> dict:
    for key, value in update.items():
        if isinstance(value, dict) and key in original and isinstance(original[key], dict):
            original[key] = deep_merge_dicts(original[key], value)
        else:
            original[key] = value
    return original
