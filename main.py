#!/usr/bin/env python3
"""
RxR Multilingual VLN Agent — Custom Map & Room Studio
Main Application Entrypoint (Launches backend & serves integrated frontend)
"""

import sys
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(ROOT_DIR, "backend")

if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

from server import run_server

if __name__ == "__main__":
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            pass
    run_server(port=port)
