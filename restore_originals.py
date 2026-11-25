#!/usr/bin/env python3
"""Restore the two original CIQ ZIP archives; never change SHA256SUMS.txt."""
from pathlib import Path
import hashlib
import os
import tempfile
import zipfile
import gdown

ROOT = Path(__file__).resolve().parent
FILES = {
    "Quellen/CIQ_Rechen_Startpaket_2026-11-24_FULLCODE.zip": ("1_U4fgu9wmbs-bIoFaQQF0ujHRSqujvwH", "823d9c8076bda4f423ff2f78d85b2d853f2953085e10c0e3aa713dd4dfbe1761"),
    "Quellen/Operator_sortiert_nummeriert.zip": ("1Gk1xESrXY7oK41xOyAAKPyu3WGNOnAsU", "584719c1e59ec972e8e499ddd8e5059644c10146d616edc599ea744f97782b99"),
}
def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def verify_zip(path, expected):
    if digest(path) != expected:
        raise RuntimeError(f"SHA-256 mismatch: {path}")
    with zipfile.ZipFile(path) as z:
        bad = z.testzip()
        if bad is not None:
            raise RuntimeError(f"ZIP CRC failure: {bad}")

def main():
    manifest = {}
    for line in (ROOT / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
        if line.strip():
            sha, name = line.split(maxsplit=1)
            manifest[name.lstrip("*")] = sha
    for name, (drive_id, expected) in FILES.items():
        if manifest.get(name) != expected:
            raise RuntimeError(f"Original manifest mismatch: {name}")
        target = ROOT / name
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            verify_zip(target, expected)
            print(f"Already verified: {name}")
            continue
        fd, tmp = tempfile.mkstemp(prefix=".ciq-download-", dir=target.parent)
        os.close(fd)
        temp = Path(tmp)
        try:
            if gdown.download(id=drive_id, output=str(temp), quiet=False) is None:
                raise RuntimeError(f"Download failed: {name}")
            verify_zip(temp, expected)
            os.replace(temp, target)
            print(f"SHA-256 and CRC OK: {name}")
        finally:
            temp.unlink(missing_ok=True)
    for name, expected in manifest.items():
        if digest(ROOT / name) != expected:
            raise RuntimeError(f"Manifest verification failed: {name}")
        print(f"{name}: OK")
    print(f"PASS: {len(manifest)}/{len(manifest)} original files")

if __name__ == "__main__":
    main()
