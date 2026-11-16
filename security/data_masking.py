"""Basic masking helpers; production masking rules must follow organizational policy."""
def mask_identifier(value, keep_last: int = 4):
    if value is None:
        return None
    text = str(value)
    if len(text) <= keep_last:
        return "*" * len(text)
    return "*" * (len(text) - keep_last) + text[-keep_last:]
