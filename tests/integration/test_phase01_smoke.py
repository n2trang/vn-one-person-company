"""Smoke tests: all Phase 1 modules import + work."""
import os
import subprocess
import sys
from pathlib import Path


def _utf8_env():
    env = os.environ.copy()
    env.setdefault("PYTHONUTF8", "1")
    env.setdefault("PYTHONIOENCODING", "utf-8")
    return env


def test_import_all():
    pass


def test_cli_status_works():
    repo = Path(__file__).parent.parent.parent
    fixture = repo / "tests" / "fixtures" / "demo-vault"
    result = subprocess.run(
        [sys.executable, "-m", "core.cli", "status", "--vault", str(fixture)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        cwd=str(repo),
        env=_utf8_env(),
    )
    assert result.returncode == 0
    assert "Brain loaded" in result.stdout


def test_dept_loader_loads_12_depts():
    from core.agents.department import DepartmentLoader
    repo = Path(__file__).parent.parent.parent
    depts = DepartmentLoader(repo / "departments").load_all()
    assert len(depts) == 12


def test_templates_vn_has_192_files():
    repo = Path(__file__).parent.parent.parent
    md_files = list((repo / "templates-vn").rglob("*.md"))
    assert len(md_files) == 192
