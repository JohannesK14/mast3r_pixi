from pathlib import Path
from setuptools import setup

curope = Path(__file__).parent / "mast3r" / "croco" / "models" / "curope"

asmk = Path(__file__).parent / "asmk"
setup(
    install_requires=[
        "torch<2.6.0",
        "torchvision",
        "scikit-learn",
        "roma",
        "gradio",
        "matplotlib",
        "tqdm",
        "opencv-python",
        "scipy",
        "einops",
        "trimesh",
        "tensorboard",
        "pyglet",
        "huggingface-hub[torch]>=0.22",
        f"curope @ {curope.as_uri()}",
        f"asmk @ {asmk.as_uri()}",
    ],
)