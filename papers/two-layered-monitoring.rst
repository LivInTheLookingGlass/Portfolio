Efficient Two-Layered Monitor for Partially Synchronous Distributed Systems (Technical Report)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

`arXiv link <https://arxiv.org/abs/2007.13030>`__

Abstract:
.. quote::

    Monitoring distributed systems to ensure their correctness is a challenging and expensive but essential problem. It is challenging because while execution of a distributed system creates a partial order among events, the monitor will typically observe only one serialization of that partial order. This means that even if the observed serialization is consistent with the system specifications, the monitor cannot assume that the system is correct because some other unobserved serialization can be inconsistent with the system specifications. Existing solutions that guarantee identification of all such unobserved violations require some combination of lots of time and large clocks, e.g. O(n) sized Vector Clocks.
    We present a new, efficient two-layered monitoring approach that overcomes both the time and space limitations of earlier monitors. The first layer is imprecise but efficient and the second layer is precise but (relatively) inefficient. We show that the combination of these two layers reduces the cost of monitoring by 85-95%. Furthermore, the two-layered monitor permits the use of O(1) sized Hybrid Logical Clocks. 

.. tags:: Research, Paper Writing, Mathematics, Distributed Systems, Networking, Communication Protocol
