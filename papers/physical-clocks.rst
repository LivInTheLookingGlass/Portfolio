Achieving Causality with Physical Clocks
++++++++++++++++++++++++++++++++++++++++

`arXiv link <https://arxiv.org/abs/2104.15099>`__

Abstract:

  Physical clocks provide more precision than applications can use. For example, a 64 bit NTP clock allows a precision of 233 picoseconds. In this paper, we focus on whether the least significant bits that are not useful to the applications could be used to track (one way) causality among events. We present PWC (Physical clock With Causality) that uses the extraneous bits in the physical clock. We show that PWC is very robust to errors in clock skew and transient errors. We show that PWC can be used as both a physical and logical clock for a typical distributed application even if just 6-9 extraneous bits (corresponding to precision of 15-120 nanoseconds) are available. Another important characteristic of PWC is that the standard integer < operation can be used to compare timestamps to deduce (one-way) causality among events. Thus, PWC is significantly more versatile than previous approaches for using the physical clock to provide causality information. 

.. tags:: Research, Paper Writing, Python, Python3, Mathematics, Distributed Systems, Networking, Communication Protocol
