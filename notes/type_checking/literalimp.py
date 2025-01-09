from typing import Literal

def set_status(status: Literal["online", "offline", "busy"]) -> str:
    return f"Status set to {status}"

# Valid usage:
print(set_status("online"))  # Status set to online

# failed when running `mypy literalimp.py`
print(set_status("random"))
