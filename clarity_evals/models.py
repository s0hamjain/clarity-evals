from dataclasses import asdict, dataclass
from typing import Any


@dataclass(frozen=True)
class EvaluationCase:
    id: str
    category: str
    prompt: str


@dataclass(frozen=True)
class CaseResult:
    case_id: str
    category: str
    valid_manim: bool
    rendered: bool
    latency_ms: int
    cache_hit: bool
    estimated_cost_usd: float
    failure_stage: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

