from pathlib import Path
import shutil

def main() -> None:
    Path("data/generated/reference").mkdir(parents=True, exist_ok=True)
    for name in ["partners.csv", "programs.csv", "products.csv", "historical_cases.csv"]:
        src = Path("data/seeds") / name
        dst = Path("data/generated/reference") / name
        if src.exists():
            shutil.copy(src, dst)

if __name__ == "__main__":
    main()
