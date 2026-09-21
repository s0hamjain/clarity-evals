import json
import random
from collections.abc import Callable
from pathlib import Path

from clarity_evals.models import CaseResult, EvaluationCase

Adapter = Callable[[EvaluationCase], CaseResult]


def load_cases(path: Path) -> list[EvaluationCase]:
    raw_cases = json.loads(path.read_text())
    return [EvaluationCase(**case) for case in raw_cases]


def run(cases: list[EvaluationCase], adapter: Adapter) -> list[CaseResult]:
    return [adapter(case) for case in cases]


def mock_adapter(case: EvaluationCase) -> CaseResult:
    """Return deterministic sample data until the production adapter is connected."""
    rng = random.Random(case.id)
    valid_manim = rng.random() > 0.1
    rendered = valid_manim and rng.random() > 0.08
    failure_stage = None
    if not valid_manim:
        failure_stage = "code_generation"
    elif not rendered:
        failure_stage = "rendering"

    return CaseResult(
        case_id=case.id,
        category=case.category,
        valid_manim=valid_manim,
        rendered=rendered,
        latency_ms=rng.randint(45_000, 95_000),
        cache_hit=rng.random() > 0.7,
        estimated_cost_usd=round(rng.uniform(0.03, 0.11), 4),
        failure_stage=failure_stage,
    )

