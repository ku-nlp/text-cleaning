from pathlib import Path


PROJECT_ROOT = Path(__file__).parent.parent
SOURCE_ROOT = PROJECT_ROOT / "jp_broom"
STATIC_ROOT = SOURCE_ROOT / "static"


print(PROJECT_ROOT)
print(SOURCE_ROOT)
print(STATIC_ROOT)