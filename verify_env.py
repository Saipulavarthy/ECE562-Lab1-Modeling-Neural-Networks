"""Quick environment sanity check for the ECE562/662 assignment1 repo.

Run: python verify_env.py
Does not modify or import any assignment code.
"""
import sys

CHECKS = [
    "numpy",
    "scipy",
    "matplotlib",
    "Cython",
    "PIL",
    "imageio",
    "sklearn",
    "future",
    "PyPDF2",
    "torch",
    "torchvision",
    "tensorflow",
]

print(f"Python: {sys.version}")

failed = []
for mod in CHECKS:
    try:
        m = __import__(mod)
        version = getattr(m, "__version__", "unknown")
        print(f"  OK  {mod:<12} {version}")
    except ImportError as e:
        failed.append(mod)
        print(f"FAIL  {mod:<12} {e}")

if failed:
    print(f"\n{len(failed)} package(s) missing: {', '.join(failed)}")
    sys.exit(1)
else:
    print("\nAll dependencies importable.")
