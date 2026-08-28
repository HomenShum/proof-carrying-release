import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "proof-carrying-release" / "SKILL.md"
REFERENCES = SKILL.parent / "references"


class PublicSkillPackageTests(unittest.TestCase):
    def test_manifest_and_skill_identity_are_one_versioned_plugin(self) -> None:
        manifest = json.loads(
            (ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8")
        )
        skill = SKILL.read_text(encoding="utf-8")
        self.assertEqual(manifest["name"], "proof-carrying-release")
        self.assertEqual(manifest["version"], "0.1.0")
        self.assertIn("name: proof-carrying-release", skill)
        self.assertLess(len(skill.splitlines()), 500)

    def test_every_reference_is_progressively_disclosed(self) -> None:
        skill = SKILL.read_text(encoding="utf-8")
        references = sorted(path.name for path in REFERENCES.glob("*.md"))
        self.assertEqual(len(references), 6)
        for name in references:
            self.assertIn(f"references/{name}", skill)

    def test_state_machine_covers_release_and_recovery(self) -> None:
        state_machine = (REFERENCES / "release-state-machine.md").read_text(
            encoding="utf-8"
        )
        for state in (
            "FROZEN",
            "PREFLIGHTED",
            "DARK",
            "SEMANTIC_PASS",
            "OBSERVED",
            "BACKEND_PROMOTED",
            "WEB_CANDIDATE_PASS",
            "CANONICAL_PASS",
            "EVIDENCE_FINAL",
            "MERGED",
            "ARCHIVED",
            "CLEAN",
            "INCIDENT",
            "ROLLED_BACK",
            "BLOCKED",
        ):
            self.assertIn(state, state_machine)

    def test_public_package_contains_no_private_release_material(self) -> None:
        patterns = {
            "email": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
            "windows_user_path": re.compile(r"[A-Za-z]:\\Users\\", re.I),
            "unix_user_path": re.compile(r"/(?:Users|home)/[^/\s]+"),
            "api_key": re.compile(r"(?:sk_(?:test|prod|live)_|github_pat_|gho_)[A-Za-z0-9_-]{12,}"),
            "jwt": re.compile(r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}"),
            "private_fixture": re.compile(r"trialscope|cheiron|hshum2018", re.I),
        }
        findings = []
        for path in ROOT.rglob("*"):
            if not path.is_file() or ".git" in path.parts:
                continue
            if path.resolve() == Path(__file__).resolve():
                continue
            if path.suffix.lower() not in {"", ".json", ".md", ".py", ".yml", ".yaml"}:
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            for label, pattern in patterns.items():
                if pattern.search(text):
                    findings.append(f"{path.relative_to(ROOT)}:{label}")
        self.assertEqual(findings, [])


if __name__ == "__main__":
    unittest.main()
