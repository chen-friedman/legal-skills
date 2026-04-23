"""Basic smoke tests for extract.py.

These tests verify the extractor handles each supported file type
without crashing and produces the expected output shape.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
EXTRACT = REPO_ROOT / "skills" / "mapping-legal-cases" / "scripts" / "extract.py"
SAMPLE = REPO_ROOT / "examples" / "sample-case-folder"


def _run_extract(*args: str) -> dict:
    proc = subprocess.run(
        [sys.executable, str(EXTRACT), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if not proc.stdout.strip():
        pytest.fail(f"no stdout; stderr: {proc.stderr}")
    return json.loads(proc.stdout)


def test_preflight_returns_ready():
    out = _run_extract("--preflight")
    assert out["ready"] is True
    assert "capabilities" in out
    assert out["capabilities"]["plain_text"] is True


def test_scan_sample_folder():
    out = _run_extract("--scan", str(SAMPLE))
    assert out["total_files"] > 0
    assert "by_category" in out


def test_extract_markdown():
    md_file = SAMPLE / "pleadings" / "statement-of-claim.md"
    out = _run_extract(str(md_file))
    assert out["success"] is True
    assert out["char_count"] > 100
    assert out["language_detected"] == "en"


def test_extract_csv():
    csv_file = SAMPLE / "evidence" / "payment-history.csv"
    out = _run_extract(str(csv_file))
    assert out["success"] is True
    assert "amount" in out["text"]


def test_extract_unknown_extension_handled_gracefully():
    # Create a temp file with unknown extension
    tmp = REPO_ROOT / "tests" / "fixtures" / "tmp_unknown.xyz"
    tmp.parent.mkdir(parents=True, exist_ok=True)
    tmp.write_text("some text content", encoding="utf-8")
    try:
        out = _run_extract(str(tmp))
        # Should either succeed via plain-text fallback or mark unsupported — never crash
        assert "file" in out
        assert "warnings" in out
    finally:
        tmp.unlink(missing_ok=True)
