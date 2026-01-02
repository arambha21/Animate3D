"""
Compatibility shims for running Animate3D in Colab with modern packages
"""
import warnings
import sys
import os

# PyTorch Version Check
try:
    import torch
    major, minor = torch.__version__.split('.')[:2]
    if int(major) >= 2:
        warnings.warn(f"Using PyTorch {torch.__version__} - Animate3D was originally tested with < 2.0. "
                      "Some features might require adaptation.")
except ImportError:
    pass

# Optional Dependency: nvdiffrast
try:
    import nvdiffrast
    HAS_NVDIFFRAST = True
except ImportError:
    HAS_NVDIFFRAST = False
    # Mock or warn if needed, but usually we just check this flag
    warnings.warn("nvdiffrast not available - advanced mesh rendering features may be disabled.")

# Optional Dependency: nerfacc
try:
    import nerfacc
    HAS_NERFACC = True
except ImportError:
    HAS_NERFACC = False
    warnings.warn("nerfacc not available - NeRF acceleration features may be disabled.")

# Optional Dependency: tiny-cuda-nn
try:
    import tinycudann
    HAS_TINYCUDANN = True
except ImportError:
    HAS_TINYCUDANN = False
    warnings.warn("tiny-cuda-nn not available - some features may be disabled.")

# Helper to suppress common Colab warnings for demo purposes
def suppress_warnings():
    warnings.filterwarnings("ignore", category=UserWarning, module="torch.functional")
    warnings.filterwarnings("ignore", category=FutureWarning, module="diffusers")
