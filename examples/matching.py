"""
Structural Pattern Matching
"""


def http_error(status: int) -> str:
    """
    Function details
    :param status:
    :return:
    """
    match status:
        case 400:
            return "Bad Request"
        case 401:
            return "Unauthorized"
        case 403:
            return "Permission denied"
        case 500 | 503:
            return "Server error"
        case _:
            return "Unknown status type"


if __name__ == '__main__':
    res = http_error(500)
    print(res)
