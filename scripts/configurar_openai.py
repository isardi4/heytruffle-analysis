#!/usr/bin/env python3
"""Guarda una clave de OpenAI localmente sin mostrarla ni agregarla a Git."""
import getpass
import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENV_FILE = ROOT / ".env"
DEFAULT_MODEL = "gpt-6-luna"


def main():
    key = getpass.getpass("Pegá tu clave de OpenAI (no se mostrará): ").strip()
    if not key:
        raise SystemExit("No se guardó nada: la clave está vacía.")

    lines = ENV_FILE.read_text(encoding="utf-8").splitlines() if ENV_FILE.exists() else []
    values = {"OPENAI_API_KEY": key}
    found = set()
    output = []
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith("#") and "=" in stripped:
            name = stripped.split("=", 1)[0].strip()
            if name in values:
                output.append(f"{name}={values[name]}")
                found.add(name)
                continue
        output.append(line)
    output.extend(f"{name}={value}" for name, value in values.items() if name not in found)
    if not any(line.strip().startswith("OPENAI_MODEL=") for line in output):
        output.append(f"OPENAI_MODEL={DEFAULT_MODEL}")

    temporary = ENV_FILE.with_suffix(".env.tmp")
    temporary.write_text("\n".join(output) + "\n", encoding="utf-8")
    os.chmod(temporary, 0o600)
    temporary.replace(ENV_FILE)
    print(f"Configuración guardada en {ENV_FILE.name}; clave oculta y archivo excluido de Git.")
    print(f"Modelo inicial: {DEFAULT_MODEL}. Si tu proyecto no tiene acceso a ese modelo, cambia OPENAI_MODEL en .env.")


if __name__ == "__main__":
    try:
        main()
    except (OSError, EOFError) as exc:
        print(f"No se pudo guardar la configuración: {exc}", file=sys.stderr)
        raise SystemExit(1)
