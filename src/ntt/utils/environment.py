"""Functions to be used to get system environment informations.
"""

import subprocess
import sys


def is_windows_os():
    """Test if system OS is Windows or Cygwin.

    Returns:
        boolean: True if Windows, False otherwise
    """
    return sys.platform in ["win32", "cygwin"]


def has_ffmpeg_cmd():
    """Test ffmpeg command line existence.

    Returns:
        boolean: True if ffmpeg was found, False otherwise
    """
    try:
        cp = subprocess.run(
            ["ffmpeg", "-version"], capture_output=True, check=False, text=True
        )

        if cp.returncode == 0:
            return True

    except FileNotFoundError as e:
        print(f"ffmpeg not found {e=}")

    return False
