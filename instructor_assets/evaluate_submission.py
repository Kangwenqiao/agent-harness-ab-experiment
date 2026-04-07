from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import subprocess
import sys


INSTRUCTOR_ROOT = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Check:
    name: str
    points: int
    command: list[str]


def resolve_python_executable(repo_root: Path) -> str:
    venv_python = repo_root / ".venv" / "bin" / "python"
    if venv_python.exists():
        return str(venv_python)
    return sys.executable


def run_check(repo_root: Path, check: Check) -> tuple[bool, str]:
    result = subprocess.run(check.command, cwd=repo_root, capture_output=True, text=True)
    output = (result.stdout + result.stderr).strip()
    return result.returncode == 0, output


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python instructor_assets/evaluate_submission.py <repo_path>", file=sys.stderr)
        return 2

    repo_root = Path(sys.argv[1]).resolve()
    python_exec = resolve_python_executable(repo_root)

    checks = [
        Check("Visible tests", 4, [python_exec, "-m", "pytest", "tests/test_onboarding_visible.py", "-q"]),
        Check(
            "Hidden tests",
            6,
            [python_exec, "-m", "pytest", str(INSTRUCTOR_ROOT / "tests_hidden" / "test_onboarding_hidden.py"), "-q"],
        ),
        Check("Architecture check", 4, [python_exec, str(INSTRUCTOR_ROOT / "check_layer_rules.py"), str(repo_root)]),
        Check(
            "Visible test expansion",
            2,
            [python_exec, str(INSTRUCTOR_ROOT / "check_visible_test_expansion.py"), str(repo_root)],
        ),
    ]

    earned = 0
    automated_total = sum(check.points for check in checks)

    print("Automated scoring")
    print("=================")
    for check in checks:
        passed, output = run_check(repo_root, check)
        status = "PASS" if passed else "FAIL"
        if passed:
            earned += check.points
        print(f"{status} | {check.name} | {check.points if passed else 0}/{check.points}")
        if output:
            print(output)
        print()

    print(f"Automated subtotal: {earned}/{automated_total}")
    print("Manual review remaining: 4/20")
    print("- Change quality: 2 points")
    print("- Delivery explanation: 2 points")
    return 0 if earned == automated_total else 1


if __name__ == "__main__":
    raise SystemExit(main())
