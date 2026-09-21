from collections import Counter
from statistics import median

from clarity_evals.models import CaseResult


def summarize(results: list[CaseResult]) -> dict[str, object]:
    if not results:
        raise ValueError("Cannot summarize an empty evaluation run")

    total = len(results)
    failures = Counter(
        result.failure_stage for result in results if result.failure_stage is not None
    )

    return {
        "total_cases": total,
        "valid_manim_rate": sum(result.valid_manim for result in results) / total,
        "render_success_rate": sum(result.rendered for result in results) / total,
        "median_latency_ms": int(median(result.latency_ms for result in results)),
        "cache_hit_rate": sum(result.cache_hit for result in results) / total,
        "estimated_cost_usd": round(
            sum(result.estimated_cost_usd for result in results), 4
        ),
        "failures_by_stage": dict(sorted(failures.items())),
    }

