def camel_case(s: str) -> str:
    words = iter(s.split("_"))
    return next(words) + "".join(i.title() for i in words)


def title_case(s: str) -> str:
    words = iter(s.split("_"))
    return " ".join(i.title() for i in words)
