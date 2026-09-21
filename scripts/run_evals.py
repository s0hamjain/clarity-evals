import argparse
import json
import sys
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from clarity_evals.metrics import summarize
from clarity_evals.runner import load_cases, mock_adapter, run


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the Clarity benchmark suite")
    parser.add_argument("--adapter", choices=["mock"], default="mock")
    args = parser.parse_args()

    cases = load_cases(ROOT / "benchmarks" / "cases.json")
    results = run(cases, mock_adapter)
    timestamp = datetime.now(UTC)
    report = {
        "schema_version": 1,
        "run_id": timestamp.strftime("%Y%m%dT%H%M%SZ"),
        "created_at": timestamp.isoformat(),
        "adapter": args.adapter,
        "summary": summarize(results),
        "results": [result.to_dict() for result in results],
    }

    output_dir = ROOT / "data" / "results"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{report['run_id']}.json"
    output_path.write_text(json.dumps(report, indent=2) + "\n")
    (ROOT / "dashboard" / "latest.json").write_text(
        json.dumps(report, indent=2) + "\n"
    )
    print(f"Wrote {output_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

