# Reference environment

The research implementation targets Linux with Python 3.7.13, PyTorch 1.12.1, torchvision 0.13.1, torchaudio 0.12.1, and CUDA toolkit 11.6. These are the project's declared compatibility versions, not a new claim that this pre-release has been trained or reproduced on a fresh environment.

The included `environment.yml` is adapted from the project's environment specification. Local-path CUDA extension installations have been omitted because the extension source and training code are not part of this pre-release. It is a reference environment rather than a complete reproducibility lockfile. Unpinned dependencies and availability of historical packages may affect resolution.

Optional environment preparation on Linux:

```bash
conda env create -f environment.yml
conda activate compact-event-preview
```

This environment file has not been installed or validated on a fresh Linux/CUDA system for this pre-release. Installing it alone does not enable training. A compatible NVIDIA driver, CUDA compiler/toolkit, C++ build toolchain, and the upstream `diff-gaussian-rasterization` and `simple-knn` extensions are required by the eventual full training release. CUDA runtime packages alone do not provide every extension build requirement. Exact build and reproduction instructions will accompany the full release.

The public `utils/system_utils.py` helper can be used with Python alone. `mkdir_p(path)` creates a directory idempotently. `searchForMaxIteration(path)` expects a nonempty directory containing only entries whose final underscore-separated component is an integer, such as `iteration_100`; it returns the largest integer. The unchanged upstream helper does not filter unrelated filenames.
