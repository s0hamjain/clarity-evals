const percent = value => `${Math.round(value * 100)}%`;

fetch("latest.json")
  .then(response => response.json())
  .then(report => {
    const summary = report.summary;
    const metrics = [
      ["Render success", percent(summary.render_success_rate)],
      ["Valid Manim", percent(summary.valid_manim_rate)],
      ["Median latency", `${(summary.median_latency_ms / 1000).toFixed(1)}s`],
      ["Estimated cost", `$${summary.estimated_cost_usd.toFixed(2)}`],
    ];

    document.querySelector("#metrics").innerHTML = metrics
      .map(([label, value]) => `<article class="metric"><span>${label}</span><strong>${value}</strong></article>`)
      .join("");
    document.querySelector("#run-id").textContent = report.run_id;
    document.querySelector("#run-meta").textContent = `${summary.total_cases} cases · ${report.adapter} adapter`;
    document.querySelector("#results").innerHTML = report.results
      .map(result => `<tr><td>${result.case_id}</td><td>${result.category}</td><td class="${result.rendered ? "success" : "failure"}">${result.rendered ? "Passed" : "Failed"}</td><td>${(result.latency_ms / 1000).toFixed(1)}s</td></tr>`)
      .join("");
  })
  .catch(() => {
    document.querySelector("#run-id").textContent = "Run the evaluation script to generate results.";
  });

