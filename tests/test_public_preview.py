"""Public-release boundary checks; no CUDA or private research code required."""
import ast
from pathlib import Path
import subprocess
import sys
import unittest
from arguments.core_parameters import CORE_PARAMETER_NAMES
from arguments.preview import build_preview_parser

ROOT = Path(__file__).resolve().parents[1]


class PublicPreviewTests(unittest.TestCase):
    def test_reserved_names_have_no_defaults(self):
        args = build_preview_parser().parse_args([])
        self.assertTrue(CORE_PARAMETER_NAMES)
        self.assertEqual(len(CORE_PARAMETER_NAMES), len(set(CORE_PARAMETER_NAMES)))
        for name in CORE_PARAMETER_NAMES:
            self.assertIsNone(getattr(args, name))

    def test_names_cover_research_modules(self):
        for name in ('init_method', 'appearance_mode', 'event_log_loss',
                     'cooperative_control', 'event_post_pruning'):
            self.assertIn(name, CORE_PARAMETER_NAMES)

    def test_parameter_file_contains_only_names(self):
        tree = ast.parse((ROOT / 'arguments/core_parameters.py').read_text())
        self.assertEqual(len(tree.body), 2)
        names = ast.literal_eval(tree.body[1].value)
        self.assertEqual(names, CORE_PARAMETER_NAMES)
        self.assertTrue(all(isinstance(name, str) and name.isidentifier() for name in names))

    def test_help_works_without_gpu_imports(self):
        for entry in ('train.py', 'render.py'):
            run = subprocess.run([sys.executable, str(ROOT / entry), '--help'],
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            self.assertEqual(run.returncode, 0, run.stderr)
            self.assertIn('--appearance_mode', run.stdout)

    def test_execution_fails_explicitly(self):
        for entry in ('train.py', 'render.py'):
            for options in ([], ['--appearance_mode', 'elog_sg'], ['--event_log_loss']):
                run = subprocess.run([sys.executable, str(ROOT / entry)] + options,
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                self.assertEqual(run.returncode, 2)
                self.assertIn('not included', run.stderr)

    def test_unknown_option_is_rejected(self):
        run = subprocess.run([sys.executable, str(ROOT / 'train.py'), '--unknown_private_option'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self.assertEqual(run.returncode, 2)
        self.assertIn('unrecognized arguments', run.stderr)

    def test_no_core_implementation_paths(self):
        for path in ('scene/appearance', 'scene/initialization', 'scene/event_support',
                     'losses', 'optimization', 'experiments', 'diagnostics'):
            self.assertFalse((ROOT / path).exists(), path)


if __name__ == '__main__':
    unittest.main()
