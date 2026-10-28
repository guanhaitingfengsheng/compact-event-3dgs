# Public preview scope

This snapshot contains reusable baseline infrastructure and a names-only interface preview.
It does not contain the manuscript's research implementation.

## Included baseline code

- `scene/`: baseline camera handling, event/dataset readers, scene loading, and SH Gaussian model.
- `gaussian_renderer/`: baseline rasterizer wrapper and optional upstream GUI transport.
- `utils/`: filesystem, camera conversion, geometry, image metrics, conventional losses, SH and general helpers.
- `arguments/__init__.py`: baseline argument definitions.

These files were exported from the project's pre-module baseline revision
`00d49f350c98e6f16b62862c0651ff34bdcbe705`, not from the modified research implementation.
Only trailing whitespace and final newlines were normalized. They retain their original headers and are attributed to the E-3DGS / 3DGS code lineage.
The baseline's conventional losses and Gaussian densification routines are existing upstream infrastructure,
not this manuscript's event-log loss, event-sensitive pruning, or appearance implementation.

## Names only

`arguments/core_parameters.py` lists additional parameter names extracted from the project.
Their defaults, suggested values, formulas, schedules, and implementation bodies are omitted.
The list also includes reserved diagnostic and integration options; inclusion is not a promise
that every option will appear in the final paper release.

`train.py` and `render.py` are explicit interface placeholders. `--help` works on CPU with the
Python standard library. Any attempted execution exits with status 2 and an availability message.
No training, rendering, checkpoint loading, fallback model, or fabricated output is performed.

```bash
python train.py --help
python render.py --help
python -m unittest discover -s tests -v
```

## Withheld until acceptance

ESBI; SG/ELog-SG appearance and lifecycle integration; event log-intensity loss;
staged optimization; cooperative control; event geometry auditing; event-sensitive post-pruning;
research training/rendering integration; tuned configurations; ablation runners and outputs;
datasets, checkpoints, and internal design/derivation documents.

The included baseline files still require their original third-party dependencies when imported.
CUDA extension sources are not bundled. GPU import, rendering and training have not been validated
for this partial release. Passing interface tests does not establish reproduction of paper results.
