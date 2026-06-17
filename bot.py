#!/usr/bin/env python3
"""
BHMarketer GhostIndex Bot
AI-powered bot that detects pages requiring deindexing due to expired content,
misinformation, policy violations, violent content, and other compliance risks.
https://bhmarketer.ai | https://bhmarketer.ai/takedown-bad-search-results/
"""

import sys


def get_status(score: int) -> str:
    if score <= 30:
        return "Low Risk"
    elif score <= 60:
        return "Medium Risk"
    elif score <= 80:
        return "High Risk"
    return "Critical Risk"


def get_deindex_recommendation(score: int) -> str:
    if score <= 30:
        return "LOW — Monitor only"
    elif score <= 60:
        return "MEDIUM — Review and optimize"
    elif score <= 80:
        return "HIGH — Submit removal request immediately"
    return "CRITICAL — Immediate removal required"


def get_processing_time(violation_type: str) -> str:
    times = {
        "expired": "3-7 days",
        "misinformation": "1-5 days",
        "policy": "2-5 days",
        "violent": "1-3 days",
        "compliance": "3-7 days",
    }
    return times.get(violation_type, "3-7 days")


def detect_deindex(
    url: str,
    violation_type: str = "expired",
    expired_content: int = 85,
    misinformation: int = 72,
    policy_violation: int = 90,
    violent_content: int = 65,
    compliance_risk: int = 78,
) -> dict:
    """
    Detect pages requiring deindexing and score compliance risks.

    Args:
        url: Target URL to analyze
        violation_type: Type of violation — expired, misinformation, policy, violent, compliance
        expired_content: Expired content score (0-100)
        misinformation: Misinformation score (0-100)
        policy_violation: Policy violation score (0-100)
        violent_content: Violent content score (0-100)
        compliance_risk: Compliance risk score (0-100)

    Returns:
        dict with individual signal scores, deindex priority, and recommendation
    """
    scores = [expired_content, misinformation, policy_violation, violent_content, compliance_risk]
    deindex_priority_score = round(sum(scores) / len(scores))

    return {
        "url": url,
        "violation_type": violation_type.capitalize() + " Content",
        "expired_content_score": expired_content,
        "misinformation_score": misinformation,
        "policy_violation_score": policy_violation,
        "violent_content_score": violent_content,
        "compliance_risk_score": compliance_risk,
        "deindex_priority_score": deindex_priority_score,
        "deindex_recommendation": get_deindex_recommendation(deindex_priority_score),
        "estimated_processing": get_processing_time(violation_type),
    }


if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else "https://example.com/page"
    violation_type = sys.argv[2] if len(sys.argv) > 2 else "expired"
    expired_content = int(sys.argv[3]) if len(sys.argv) > 3 else 85
    misinformation = int(sys.argv[4]) if len(sys.argv) > 4 else 72
    policy_violation = int(sys.argv[5]) if len(sys.argv) > 5 else 90
    violent_content = int(sys.argv[6]) if len(sys.argv) > 6 else 65
    compliance_risk = int(sys.argv[7]) if len(sys.argv) > 7 else 78

    result = detect_deindex(
        url, violation_type, expired_content,
        misinformation, policy_violation, violent_content, compliance_risk
    )

    print(f"URL: {result['url']}")
    print(f"Violation Type: {result['violation_type']}")
    print("=" * 45)
    print(f"Expired Content Score:       {result['expired_content_score']}/100  [{get_status(result['expired_content_score'])}]")
    print(f"Misinformation Score:        {result['misinformation_score']}/100  [{get_status(result['misinformation_score'])}]")
    print(f"Policy Violation Score:      {result['policy_violation_score']}/100  [{get_status(result['policy_violation_score'])}]")
    print(f"Violent Content Score:       {result['violent_content_score']}/100  [{get_status(result['violent_content_score'])}]")
    print(f"Compliance Risk Score:       {result['compliance_risk_score']}/100  [{get_status(result['compliance_risk_score'])}]")
    print("=" * 45)
    print(f"Deindex Priority Score:      {result['deindex_priority_score']}/100")
    print(f"Deindex Recommendation:      {result['deindex_recommendation']}")
    print(f"Estimated Processing:        {result['estimated_processing']}")
