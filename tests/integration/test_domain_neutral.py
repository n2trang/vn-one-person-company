"""RULE 2: core/ không được có trade/finance leakage."""
import os
import subprocess
from pathlib import Path


def _utf8_env():
    env = os.environ.copy()
    env.setdefault("PYTHONUTF8", "1")
    env.setdefault("PYTHONIOENCODING", "utf-8")
    return env


def test_no_trade_leakage_in_core():
    repo = Path(__file__).parent.parent.parent
    result = subprocess.run(
        ["python", str(repo / "scripts" / "dev" / "check_domain_neutral.py")],
        cwd=str(repo),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env=_utf8_env(),
    )
    assert result.returncode == 0, (
        f"Domain-neutral check failed:\n"
        f"STDOUT:\n{result.stdout}\n"
        f"STDERR:\n{result.stderr}"
    )
