"""CPU-only argument preview; never executes reconstruction or reads checkpoints."""
from argparse import ArgumentParser
from . import ModelParams, OptimizationParams, PipelineParams
from .core_parameters import CORE_PARAMETER_NAMES


def build_preview_parser():
    """Return an argparse parser with baseline options and names-only reserved options."""
    parser = ArgumentParser(description='Public interface preview; core code is unreleased.',
                            allow_abbrev=False)
    ModelParams(parser)
    OptimizationParams(parser)
    PipelineParams(parser)
    group = parser.add_argument_group('Reserved names (implementation not released)')
    for name in CORE_PARAMETER_NAMES:
        group.add_argument('--' + name, default=None, nargs='?', const='', metavar='VALUE',
                           help='Reserved name only; no algorithm or default is provided.')
    return parser


def main(argv=None):
    """Show --help, otherwise fail before importing GPU modules or producing outputs."""
    parser = build_preview_parser()
    parser.parse_args(argv)
    parser.exit(2, 'Core reconstruction code is not included in this public preview. '
                   'The complete code will be released upon manuscript acceptance.\n')
