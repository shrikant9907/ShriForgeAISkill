import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class ShriForgeAISkillTests(unittest.TestCase):
    def test_validator_passes(self):
        p = subprocess.run([sys.executable, str(ROOT / 'scripts/validate_repo.py')], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)

    def test_skill_is_progressively_disclosed(self):
        text = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        self.assertLessEqual(len(text.splitlines()), 500)
        self.assertIn('Selective routing', text)
        self.assertIn('Do not load every module', text)

    def test_truth_model_blocks_invention(self):
        text = (ROOT / 'core/project-truth.md').read_text(encoding='utf-8').lower()
        for term in ['fabricate', 'testimonials', 'ratings', 'affiliations', 'assumption']:
            self.assertIn(term, text)
        self.assertIn('never fabricate', text)

    def test_workflow_routing_targets_exist(self):
        text = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        refs = re.findall(r'`(workflows/[^`]+?\.md)`', text)
        self.assertGreaterEqual(len(set(refs)), 10)
        for rel in refs:
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_adapters_contain_production_recipes(self):
        next_adapter = (ROOT / 'adapters/nextjs-app-router.md').read_text(encoding='utf-8')
        self.assertIn('Dynamic Sitemap', next_adapter)
        self.assertIn('Safe Server Action Pattern', next_adapter)
        self.assertIn('Performance-Safe Responsive Image', next_adapter)

    def test_release_states_are_explicit(self):
        text = (ROOT / 'core/release-gates.md').read_text(encoding='utf-8')
        for state in ['PASS', 'PASS_WITH_NOTES', 'BLOCKED', 'FAIL']:
            self.assertIn(state, text)

    def test_json_schemas_parse(self):
        for p in (ROOT / 'schemas').glob('*.json'):
            data = json.loads(p.read_text(encoding='utf-8'))
            self.assertEqual(data.get('$schema'), 'https://json-schema.org/draft/2020-12/schema')

    def test_school_profile_forbids_fake_facts(self):
        text = (ROOT / 'profiles/school-india.md').read_text(encoding='utf-8').lower()
        for term in ['affiliation', 'awards', 'fees', 'testimonials']:
            self.assertIn(term, text)
        self.assertIn('verified-only', text)

    def test_slash_commands_exist(self):
        commands = ['shri-plan.md', 'truth-check.md', 'shri-audit.md', 'release-gate.md']
        for cmd in commands:
            p = ROOT / 'commands' / cmd
            self.assertTrue(p.exists(), f"Missing command: {cmd}")
            content = p.read_text(encoding='utf-8')
            self.assertTrue(content.startswith('# /'), f"Command {cmd} missing '# /' title")

    def test_subagents_exist(self):
        agents = ['truth-auditor.md', 'web-architect.md', 'release-evaluator.md']
        for agent in agents:
            p = ROOT / 'agents' / agent
            self.assertTrue(p.exists(), f"Missing agent: {agent}")
            content = p.read_text(encoding='utf-8')
            self.assertTrue(content.startswith('# Subagent:'), f"Agent {agent} missing '# Subagent:' title")

    def test_domain_profiles_expanded(self):
        profiles = ['ecommerce-store.md', 'healthcare-clinic.md', 'developer-docs.md']
        for prof in profiles:
            p = ROOT / 'profiles' / prof
            self.assertTrue(p.exists(), f"Missing profile: {prof}")

    def test_plugin_manifest_valid(self):
        p = ROOT / '.claude-plugin' / 'plugin.json'
        self.assertTrue(p.exists())
        data = json.loads(p.read_text(encoding='utf-8'))
        self.assertEqual(data['name'], 'shriforge-ai-skill')
        self.assertEqual(data['commands'], './commands')
        self.assertEqual(data['agents'], './agents')

    def test_audit_content_truth_tool_detects_placeholders(self):
        sys.path.insert(0, str(ROOT / 'scripts'))
        import audit_content_truth
        match_lorem = audit_content_truth.PATTERNS["LOREM_IPSUM"][0].search("This has Lorem Ipsum text")
        self.assertIsNotNone(match_lorem)
        match_phone = audit_content_truth.PATTERNS["DUMMY_PHONE"][0].search("Call 123-456-7890 today")
        self.assertIsNotNone(match_phone)
        match_clean = audit_content_truth.PATTERNS["LOREM_IPSUM"][0].search("Clean factual description")
        self.assertIsNone(match_clean)

    def test_visual_design_tokens(self):
        content = (ROOT / 'disciplines/visual-design.md').read_text(encoding='utf-8')
        self.assertIn('Design Token Vault', content)
        self.assertIn('44×44px', content)
        self.assertIn('Space Grotesk', content)
        self.assertIn('--bg-canvas', content)

    def test_aeo_geo_citability(self):
        content = (ROOT / 'disciplines/aeo-geo.md').read_text(encoding='utf-8')
        self.assertIn('130–170 Word', content)
        self.assertIn('BLUF', content)
        self.assertIn('Definition-First', content)
        self.assertIn('llms.txt', content)

    def test_seo_vatm_rubric(self):
        content = (ROOT / 'disciplines/seo.md').read_text(encoding='utf-8')
        self.assertIn('VATM 100-Point Quality Rubric', content)
        self.assertIn('VALUE (25 pts)', content)
        self.assertIn('ACCESS (25 pts)', content)
        self.assertIn('TRUST (25 pts)', content)
        self.assertIn('MEASUREMENT (25 pts)', content)

    def test_falsifiability_protocol(self):
        content = (ROOT / 'workflows/audit.md').read_text(encoding='utf-8')
        self.assertIn('Falsifiability Protocol', content)
        self.assertIn('Falsifiable Verification Test', content)

if __name__ == '__main__':
    unittest.main()
