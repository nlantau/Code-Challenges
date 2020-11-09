# nlantau, 2020-11-09

import re


def validate_code(code):
    return True if (re.match(r"[123]", str(code))) else False


print(validate_code(123))