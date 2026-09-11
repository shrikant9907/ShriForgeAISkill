import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class ShriForgeAISkillTests(unittest.TestCase):
    def test_validator_passes(self):
        p=subprocess.run([sys.executable, str(ROOT/'scripts/validate_repo.py')], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(p.returncode,0,p.stdout+p.stderr)

    def test_skill_is_progressively_disclosed(self):
        text=(ROOT/'SKILL.md').read_text(encoding='utf-8')
        self.assertLessEqual(len(text.splitlines()),500)
        self.assertIn('Selective routing',text)
        self.assertIn('Do not load every module',text)

    def test_truth_model_blocks_invention(self):
        text=(ROOT/'core/project-truth.md').read_text(encoding='utf-8').lower()
        for term in ['fabricate','testimonials','ratings','affiliations','assumption']:
            self.assertIn(term,text)
        self.assertIn('never fabricate', text)

    def test_workflow_routing_targets_exist(self):
        text=(ROOT/'SKILL.md').read_text(encoding='utf-8')
        refs=re.findall(r'`(workflows/[^`]+?\.md)`',text)
        self.assertGreaterEqual(len(set(refs)),10)
        for rel in refs:
            self.assertTrue((ROOT/rel).exists(),rel)

    def test_adapters_are_separate_from_core(self):
        core='\n'.join(p.read_text(encoding='utf-8') for p in (ROOT/'core').glob('*.md'))
        self.assertNotIn('"use client"',core)
        self.assertIn('"use client"',(ROOT/'adapters/nextjs-app-router.md').read_text(encoding='utf-8'))

    def test_release_states_are_explicit(self):
        text=(ROOT/'core/release-gates.md').read_text(encoding='utf-8')
        for state in ['PASS','PASS_WITH_NOTES','BLOCKED','FAIL']:
            self.assertIn(state,text)

    def test_json_schemas_parse(self):
        for p in (ROOT/'schemas').glob('*.json'):
            data=json.loads(p.read_text(encoding='utf-8'))
            self.assertEqual(data.get('$schema'),'https://json-schema.org/draft/2020-12/schema')

    def test_school_profile_forbids_fake_facts(self):
        text=(ROOT/'profiles/school-india.md').read_text(encoding='utf-8').lower()
        for term in ['affiliation','awards','fees','testimonials']:
            self.assertIn(term,text)
        self.assertIn('verified-only',text)

if __name__=='__main__':
    unittest.main()
