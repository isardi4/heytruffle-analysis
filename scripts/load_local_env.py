"""Carga la configuración local sin dependencias ni sobrescribir el entorno."""
import os
import re
import shlex
from pathlib import Path


def load_local_env(path=None):
    path = Path(path) if path is not None else Path(__file__).resolve().parents[1] / ".env"
    if not path.is_file():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("export "):
            line = line[7:].strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", key):
            continue
        try:
            parts = shlex.split(value, comments=True, posix=True)
        except ValueError:
            continue
        os.environ.setdefault(key, " ".join(parts))
