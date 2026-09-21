# Clarity Evals

Clarity Evals is a reproducible evaluation harness and dashboard for [Clarity](https://github.com/s0hamjain/Clarity), a macOS-native AI app that turns problems and code into Manim animations.

The project measures whether changes to Clarity improve reliability without increasing latency or cost. Each evaluation run stores structured results that can be compared across releases and rendered in a lightweight dashboard.

## Metrics

- Valid Manim code rate
- Successful render rate
- End-to-end latency
- Pipeline-stage failures
- Cache hit rate
- Estimated model cost

## Quick start

```bash
python scripts/run_evals.py --adapter mock
python -m http.server 8000 --directory dashboard
```

Open `http://localhost:8000` to view the dashboard.

The mock adapter makes the repository runnable without production credentials. A future Clarity adapter will invoke the real pipeline and record its output using the same schema.

## Repository structure

```text
benchmarks/        Versioned evaluation cases
clarity_evals/     Runner, adapters, and metrics
dashboard/         Static results dashboard
data/results/      Timestamped evaluation runs
scripts/           Command-line entry points
tests/             Metric and schema tests
```

## Evaluation philosophy

The benchmark suite stays stable so results remain comparable over time. Automated runs should commit only verified evaluation data. Product changes belong in the main Clarity repository.

