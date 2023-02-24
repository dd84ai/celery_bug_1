from django import db
from contextlib import contextmanager
from typing import Generator


@contextmanager
def empty_contextmanager() -> Generator[None, None, None]:
    try:
        yield
    except:
        pass
