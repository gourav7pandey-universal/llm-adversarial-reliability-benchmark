def compute_failure_rates(results):
    """
    Compute failure rates per model and category.

    Parameters
    ----------
    results : list of dict
        Benchmark evaluation results

    Returns
    -------
    stats : list of dict
        Aggregated failure statistics
    """

    stats = {}

    for r in results:

        key = (r["model"], r["category"])

        if key not in stats:
            stats[key] = {"total": 0, "fail": 0}

        stats[key]["total"] += 1

        if r["verdict"] == "FAIL":
            stats[key]["fail"] += 1

    output = []

    for (model, category), v in stats.items():

        failure_rate = v["fail"] / v["total"]

        output.append({
            "model": model,
            "category": category,
            "failure_rate": round(failure_rate, 3)
        })

    return output
