# Third-party notices

## Included code

Baseline files under `scene/`, `gaussian_renderer/`, `utils/`, and `arguments/__init__.py` are exported with whitespace normalization only from baseline revision `00d49f350c98e6f16b62862c0651ff34bdcbe705` of the existing E-3DGS-based project. Their original copyright headers and the complete Gaussian Splatting license (`LICENSE.md`) are retained. New names-only argument previews, entry-point placeholders, and release-boundary tests are distributed under the same license. These files do not implement this manuscript's research contributions. See `PUBLIC_CONTENTS.md` for the exact boundary.

## Research foundations and external dependencies

- E-3DGS, Sohaib Zahid, Viktor Rudnev, Eddy Ilg, and Vladislav Golyanik, 3DV 2025: [project](https://4dqv.mpi-inf.mpg.de/E3DGS/), [official code](https://github.com/sohaib023/E-3DGS).
- 3D Gaussian Splatting, Bernhard Kerbl, Georgios Kopanas, Thomas Leimkuehler, and George Drettakis, ACM TOG 2023: [project](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/), [official code](https://github.com/graphdeco-inria/gaussian-splatting).
- CUDA rasterizer: https://github.com/graphdeco-inria/diff-gaussian-rasterization
- Nearest-neighbor extension: https://gitlab.inria.fr/bkerbl/simple-knn

The CUDA extensions are not bundled or vendored here. Python/PyTorch and other environment dependencies retain their respective licenses. Consult each original project before redistributing or using its components. The presence of a citation does not replace a license or imply endorsement.
