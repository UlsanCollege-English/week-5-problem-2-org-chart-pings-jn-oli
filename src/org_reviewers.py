# src/org_reviewers.py

def count_senior(node, min_level):
    """Recursively count how many people have level >= min_level in an org chart."""
    if not node or not isinstance(node, dict):
        return 0

    # Get this person's level and reports
    level = node.get("level", 0)
    reports = node.get("reports", [])

    # Count this person if they meet the minimum level
    count = 1 if level >= min_level else 0

    # Recurse for all reports
    for report in reports:
        count += count_senior(report, min_level)

    return count
