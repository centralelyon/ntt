======================
ntt pipeline example 1
======================

Here is a beginning of a Flowchart made with `mermaid`_.

.. mermaid::

    flowchart TD
        A[Start] -->|extract_first_frame| B{flash}
        B -- Yes --> C[detect_peak_video right]
        B -- No --> D[detect_peak_video left]
        C --> E[extract]
        D --> E
        E -- extract_nth_frame --> F[and so on]

.. _mermaid: https://mermaid.js.org/
