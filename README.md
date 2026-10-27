# Compact Event-based 3D Gaussian Reconstruction

Public pre-release materials for **Compact event-based 3D Gaussian reconstruction: log-intensity appearance and event-domain sensitivity pruning**.

## Code availability

**The complete source code will be made publicly available in this repository upon acceptance of the associated manuscript.**

The current pre-release contains only a non-core filesystem utility, a reference environment configuration, citation information, and third-party notices. The core reconstruction methods, training and rendering pipelines, checkpoints, and experimental outputs are not included. This snapshot is not sufficient to reproduce the manuscript results.

中文：本仓库目前仅公开非核心辅助代码、参考环境和引用信息。论文录用后，将在本仓库公开完整源代码。当前版本不包含核心算法，不能用于复现论文结果。

## Current contents

| File | Purpose |
| --- | --- |
| `utils/system_utils.py` | Upstream directory creation and iteration-directory lookup helpers |
| `environment.yml` | Reference Python/PyTorch environment, excluding unpublished code and CUDA extensions |
| `ENVIRONMENT.md` | Environment scope and verification limits |
| `CITATION.bib` | Provisional manuscript citation and upstream references |
| `THIRD_PARTY_NOTICES.md` | Provenance, attribution, and dependency links |
| `LICENSE.md` | Original Gaussian Splatting license retained for the upstream utility |

## Environment

The research code targets Linux, Python 3.7.13, PyTorch 1.12.1, and CUDA toolkit 11.6. See [ENVIRONMENT.md](ENVIRONMENT.md) for details. The included filesystem utility uses only the Python standard library and does not require a GPU.

## Citation

If you refer to this project, cite the associated manuscript using the provisional entry in [CITATION.bib](CITATION.bib). Its title and author order follow the current manuscript. Publication venue, DOI, and final bibliographic details will be added after acceptance. The manuscript is not represented here as an accepted or published article.

Please also credit the original E-3DGS and 3D Gaussian Splatting work when using their methods or code. Their citation entries are included separately; they are not authors of this project's manuscript.

## Data and third-party components

No datasets or model weights are distributed in this pre-release. E-3DGS datasets are available through the [upstream project page](https://4dqv.mpi-inf.mpg.de/E3DGS/), subject to the original providers' terms. This repository does not grant rights to third-party data or software.

## License and acknowledgments

The included `utils/system_utils.py` is an unchanged upstream utility with its original copyright header. Its use is governed by [LICENSE.md](LICENSE.md). See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Public visibility does not replace the applicable license terms. The license and component notices for the complete release will be provided with that release.
