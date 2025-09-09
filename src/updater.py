import subprocess
import sys
import os
import platform

from .version import get_pip_version

def update(name: str, version: str|None = None,  force: bool = False) -> None:
    """ Starts the update pipeline """

    

def _launch_update_process(name: str, version: str|None = None) -> None:
    system = platform.system()

    if system == "Windows":
        # Windows: DETACHED_PROCESS
        DETACHED_PROCESS = 0x00000008
        subprocess.Popen(
            [sys.executable, "-m", "pkgupdater", ""],
            creationflags=DETACHED_PROCESS,
            close_fds=True
        )
    else:
        # Unix/Linux/macOS: preexec_fn=os.setpgrp trennt vom Terminal
        subprocess.Popen(
            [python_executable, script_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL,
            preexec_fn=os.setpgrp
        )