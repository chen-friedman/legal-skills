"""Basic smoke tests for extract.py.

These tests verify the extractor handles each supported file type
without crashing and produces the expected output shape. All fixtures
are generated at runtime so the repo ships without bundled demo data.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
EXTRACT = REPO_ROOT / "skills" / "mapping-legal-cases" / "scripts" / "extract.py"
FIXTURES = REPO_ROOT / "tests" / "fixtures"


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


@pytest.fixture
def tmp_case_folder(tmp_path: Path) -> Path:
    """Create a minimal fictional case folder at runtime (not committed to repo)."""
    folder = tmp_path / "fictional-case"
    (folder / "notes").mkdir(parents=True)
    (folder / "notes" / "summary.md").write_text(
        "# Case summary\n\nFictional dispute. Hearing scheduled for 2026-04-15.\n",
        encoding="utf-8",
    )
    (folder / "ledger.csv").write_text(
        "date,amount,note\n2026-01-01,5000,fictional payment\n",
        encoding="utf-8",
    )
    (folder / "readme.txt").write_text(
        "Fictional notes, no real data.",
        encoding="utf-8",
    )
    return folder


def test_preflight_returns_ready():
    out = _run_extract("--preflight")
    assert out["ready"] is True
    assert "capabilities" in out
    assert out["capabilities"]["plain_text"] is True


def test_scan_folder(tmp_case_folder: Path):
    out = _run_extract("--scan", str(tmp_case_folder))
    assert out["total_files"] >= 3
    assert "by_category" in out
    cats = out["by_category"]
    assert cats.get("markdown", 0) >= 1
    assert cats.get("csv", 0) >= 1
    assert cats.get("text", 0) >= 1


def test_extract_markdown(tmp_case_folder: Path):
    md_file = tmp_case_folder / "notes" / "summary.md"
    out = _run_extract(str(md_file))
    assert out["success"] is True
    assert out["char_count"] > 20
    assert out["language_detected"] == "en"


def test_extract_csv(tmp_case_folder: Path):
    csv_file = tmp_case_folder / "ledger.csv"
    out = _run_extract(str(csv_file))
    assert out["success"] is True
    assert "amount" in out["text"]


def test_extract_plain_text(tmp_case_folder: Path):
    txt_file = tmp_case_folder / "readme.txt"
    out = _run_extract(str(txt_file))
    assert out["success"] is True
    assert "Fictional" in out["text"]


def test_extract_unknown_extension_handled_gracefully(tmp_path: Path):
    tmp = tmp_path / "tmp_unknown.xyz"
    tmp.write_text("some text content", encoding="utf-8")
    out = _run_extract(str(tmp))
    # Should either succeed via plain-text fallback or mark unsupported -- never crash
    assert "file" in out
    assert "warnings" in out
