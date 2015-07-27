"""Common code used by several test cases."""
from sys import version_info
# flake8:noqa
# pylint:disable=import-error,unused-import

if version_info < (3, 4):
    from unittest2 import TestCase
else:
    from unittest import TestCase

if version_info.major == 2:
    from urlparse import urlparse
    # The `__builtins__` module (note the "s") also provides the `open`
    # function. However, that module is an implementation detail for CPython 2,
    # so it should not be relied on.
    import __builtin__ as builtins
    import httplib as http_client
else:
    from urllib.parse import urlparse  # pylint:disable=no-name-in-module
    import builtins
    import http.client as http_client
