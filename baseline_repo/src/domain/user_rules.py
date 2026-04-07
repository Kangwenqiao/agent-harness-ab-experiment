import re

USERNAME_PATTERN = re.compile(r"^[a-z0-9_]+$")
RESERVED_USERNAMES = {"admin", "root", "system"}


def validate_username(username: str) -> str:
    if len(username) < 3 or len(username) > 20:
        raise ValueError("username must be between 3 and 20 characters")
    if not USERNAME_PATTERN.fullmatch(username):
        raise ValueError("username may only contain lowercase letters, numbers, and underscores")
    return username
