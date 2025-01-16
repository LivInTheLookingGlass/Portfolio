CPython Contributions
+++++++++++++++++++++

I `added support <https://github.com/python/cpython/pull/14258>`__ for `UDPLite <https://en.wikipedia.org/wiki/UDP-Lite>`__ to CPython, the most common implementation of the Python language. This communication protocol is a variant on UDP, except that it allows for data corruption to non-important sections. This is particularly useful in applications like video streaming, where data correction is already a part of the higher level protocol, and dropped packets are more problematic than corrupted data.

.. tags:: C, Software Testing, Python, Networking, Linux
