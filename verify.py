import hashlib
import json
from pathlib import Path


def main():
    root = Path(__file__).resolve().parent
    source_map = json.loads((root / "SOURCE_MAP.json").read_text(encoding="utf-8"))
    records = source_map["sources"]
    names = [record["file"] for record in records]
    if len(set(names)) != len(names):
        raise SystemExit("FAIL duplicate baseline path")
    present = {
        path.relative_to(root).as_posix()
        for path in (root / "baseline").rglob("*")
        if path.is_file()
    }
    expected = set(names)
    if present != expected:
        raise SystemExit(
            f"FAIL missing={sorted(expected - present)} extra={sorted(present - expected)}"
        )
    for record in records:
        raw = (root / record["file"]).read_bytes()
        blob = hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()
        sha256 = hashlib.sha256(raw).hexdigest()
        if (len(raw), blob, sha256) != (
            record["bytes"], record["git_blob"], record["sha256"]
        ):
            raise SystemExit(f"FAIL identity mismatch {record['file']}")
    print(f"PASS {len(records)} whole files verified, {len(source_map['unrecovered_git_versions'])} staged Git versions unresolved")


if __name__ == "__main__":
    main()
