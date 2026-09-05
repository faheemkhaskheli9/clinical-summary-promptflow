import argparse
import json
from pathlib import Path

from pydantic import ValidationError

from .schemas import VitalsSchema


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate synthetic patient vitals.")
    parser.add_argument("--input", required=True, type=Path, help="Path to a UTF-8 JSON object.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        raw = args.input.read_text(encoding="utf-8")
    except OSError as exc:
        raise SystemExit(f"Could not read explicit input path '{args.input}': {exc}") from exc

    try:
        payload = json.loads(raw)
        vitals = VitalsSchema.model_validate(payload)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Input is not valid JSON: {exc}") from exc
    except ValidationError as exc:
        raise SystemExit(f"Vitals validation failed:\n{exc}") from exc

    print(vitals.model_dump_json(indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
