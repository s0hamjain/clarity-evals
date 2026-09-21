import pytest

from clarity_evals.metrics import summarize
from clarity_evals.models import CaseResult


def test_summarize_results() -> None:
    results = [
        CaseResult("a", "code", True, True, 60_000, True, 0.04),
        CaseResult("b", "code", False, False, 90_000, False, 0.06, "code_generation"),
    ]

    summary = summarize(results)

    assert summary["valid_manim_rate"] == 0.5
    assert summary["render_success_rate"] == 0.5
    assert summary["median_latency_ms"] == 75_000
    assert summary["failures_by_stage"] == {"code_generation": 1}


def test_empty_results_are_rejected() -> None:
    with pytest.raises(ValueError, match="empty"):
        summarize([])

