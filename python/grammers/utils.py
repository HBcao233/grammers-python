import re


def parse_phone(phone: int | str) -> str:
  """Parses the given phone, or returns `None` if it's invalid."""
  if isinstance(phone, int):
    return str(phone)
  else:
    phone = re.sub(r'[+()\s-]', '', str(phone))
    if phone.isdigit():
      return phone
