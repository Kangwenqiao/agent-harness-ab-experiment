from __future__ import annotations

from pathlib import Path
import sys


def collect_violations(root: Path, directory: Path) -> list[str]:
    forbidden_snippets = (
        ".strip(",
        ".lower(",
        ".replace(",
        "re.compile(",
        "re.sub(",
        "RESERVED_USERNAMES",
        "admin_",
        "root_",
        "system_",
        "USERNAME_PATTERN",
    )

    violations: list[str] = []
    for path in sorted(directory.rglob("*.py")):
        text = path.read_text()
        for snippet in forbidden_snippets:
            if snippet in text:
                relative_path = path.relative_to(root)
                violations.append(f"{relative_path}: found forbidden snippet {snippet!r}")
    return violations


def main() -> int:
    repo_root = Path(sys.argv[1]).resolve()
    api_dir = repo_root / "src" / "api"
    services_dir = repo_root / "src" / "services"

    violations = collect_violations(repo_root, api_dir) + collect_violations(repo_root, services_dir)
    if violations:
        print("Layer rule violations detected:")
        for violation in violations:
            print(f"- {violation}")
        return 1

    print("Layer rule check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
