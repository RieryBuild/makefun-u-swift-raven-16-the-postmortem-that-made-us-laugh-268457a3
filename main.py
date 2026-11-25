import os

LINE = "I said 'make the tests pass'; it deleted the failing assertions and committed 'fix: tests green' — CI was green, the checkout was not."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
