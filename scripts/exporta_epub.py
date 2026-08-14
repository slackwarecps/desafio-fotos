#!/usr/bin/env python3
"""
Wrapper para o script oficial de exportação de EPUB.
Delega para .agents/skills/exporta-cards-enriquecidos-para-epub/exporta.py
"""

import sys
import subprocess
from pathlib import Path

script_path = Path(__file__).parent.parent / ".agents" / "skills" / "exporta-cards-enriquecidos-para-epub" / "exporta.py"

if __name__ == "__main__":
    args = [sys.executable, str(script_path)] + sys.argv[1:]
    sys.exit(subprocess.call(args))
