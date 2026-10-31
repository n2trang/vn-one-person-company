"""RULE 2: core/ không được có trade/finance leakage."""
import os
import shutil
import subprocess
from pathlib import Path


def _utf8_env():
    env = os.environ.copy()
    env.setdefault("PYTHONUTF8", "1")
    env.setdefault("PYTHONIOENCODING", "utf-8")
    return env


def test_no_trade_leakage_in_core():
    repo = Path(__file__).parent.parent.parent
    repo / "scripts/dev/check-domain-neutral.sh"

    # On Windows, ensure bash is available; skip if not
    if shutil.which("bash") is None:
        import pytest
        pytest.skip("bash not available on this platform")

    # Use a relative path so Git Bash on Windows can resolve it correctly
    # (bash on Windows can't open scripts via 'F:/...' absolute paths reliably)
    rel_script = "scripts/dev/check-domain-neutral.sh"
    result = subprocess.run(
        ["bash", rel_script],
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
