# Third-party notices

## Included code

`utils/system_utils.py` is copied unchanged from the existing E-3DGS-based project. Its header identifies Copyright (C) 2023, Inria, GRAPHDECO research group. The original header and complete Gaussian Splatting license are retained in this distribution (`LICENSE.md`). This file contains filesystem helpers only and does not implement this manuscript's research contributions.

## Research foundations and external dependencies

- E-3DGS, Sohaib Zahid, Viktor Rudnev, Eddy Ilg, and Vladislav Golyanik, 3DV 2025: [project](https://4dqv.mpi-inf.mpg.de/E3DGS/), [official code](https://github.com/sohaib023/E-3DGS).
- 3D Gaussian Splatting, Bernhard Kerbl, Georgios Kopanas, Thomas Leimkuehler, and George Drettakis, ACM TOG 2023: [project](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/), [official code](https://github.com/graphdeco-inria/gaussian-splatting).
- CUDA rasterizer: https://github.com/graphdeco-inria/diff-gaussian-rasterization
- Nearest-neighbor extension: https://gitlab.inria.fr/bkerbl/simple-knn

The CUDA extensions are not bundled or vendored here. Python/PyTorch and other environment dependencies retain their respective licenses. Consult each original project before redistributing or using its components. The presence of a citation does not replace a license or imply endorsement.
