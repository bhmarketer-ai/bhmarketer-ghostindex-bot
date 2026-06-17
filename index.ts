#!/usr/bin/env node

interface GhostIndexInput {
  url: string;
  violationType: "expired" | "misinformation" | "policy" | "violent" | "compliance";
  expiredContent: number;
  misinformation: number;
  policyViolation: number;
  violentContent: number;
  complianceRisk: number;
}

interface GhostIndexOutput {
  url: string;
  violationType: string;
  expiredContentScore: number;
  misinformationScore: number;
  policyViolationScore: number;
  violentContentScore: number;
  complianceRiskScore: number;
  deindexPriorityScore: number;
  deindexRecommendation: string;
  estimatedProcessing: string;
}

function getStatus(score: number): string {
  if (score <= 30) return "Low Risk";
  if (score <= 60) return "Medium Risk";
  if (score <= 80) return "High Risk";
  return "Critical Risk";
}

function getDeindexRecommendation(score: number): string {
  if (score <= 30) return "LOW — Monitor only";
  if (score <= 60) return "MEDIUM — Review and optimize";
  if (score <= 80) return "HIGH — Submit removal request immediately";
  return "CRITICAL — Immediate removal required";
}

function getProcessingTime(violationType: string): string {
  const times: Record<string, string> = {
    expired: "3-7 days",
    misinformation: "1-5 days",
    policy: "2-5 days",
    violent: "1-3 days",
    compliance: "3-7 days",
  };
  return times[violationType] ?? "3-7 days";
}

export function detectDeindex(input: GhostIndexInput): GhostIndexOutput {
  const scores = [
    input.expiredContent,
    input.misinformation,
    input.policyViolation,
    input.violentContent,
    input.complianceRisk,
  ];
  const deindexPriorityScore = Math.round(
    scores.reduce((a, b) => a + b, 0) / scores.length
  );

  return {
    url: input.url,
    violationType: input.violationType.charAt(0).toUpperCase() + input.violationType.slice(1),
    expiredContentScore: input.expiredContent,
    misinformationScore: input.misinformation,
    policyViolationScore: input.policyViolation,
    violentContentScore: input.violentContent,
    complianceRiskScore: input.complianceRisk,
    deindexPriorityScore,
    deindexRecommendation: getDeindexRecommendation(deindexPriorityScore),
    estimatedProcessing: getProcessingTime(input.violationType),
  };
}

const args = process.argv.slice(2);
const url = args[0] || "https://example.com/page";
const violationType = (args[1] as GhostIndexInput["violationType"]) || "expired";
const expiredContent = parseInt(args[2]) || 85;
const misinformation = parseInt(args[3]) || 72;
const policyViolation = parseInt(args[4]) || 90;
const violentContent = parseInt(args[5]) || 65;
const complianceRisk = parseInt(args[6]) || 78;

const result = detectDeindex({
  url, violationType, expiredContent,
  misinformation, policyViolation, violentContent, complianceRisk,
});

console.log(`URL: ${result.url}`);
console.log(`Violation Type: ${result.violationType} Content`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Expired Content Score:       ${result.expiredContentScore}/100  [${getStatus(result.expiredContentScore)}]`);
console.log(`Misinformation Score:        ${result.misinformationScore}/100  [${getStatus(result.misinformationScore)}]`);
console.log(`Policy Violation Score:      ${result.policyViolationScore}/100  [${getStatus(result.policyViolationScore)}]`);
console.log(`Violent Content Score:       ${result.violentContentScore}/100  [${getStatus(result.violentContentScore)}]`);
console.log(`Compliance Risk Score:       ${result.complianceRiskScore}/100  [${getStatus(result.complianceRiskScore)}]`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Deindex Priority Score:      ${result.deindexPriorityScore}/100`);
console.log(`Deindex Recommendation:      ${result.deindexRecommendation}`);
console.log(`Estimated Processing:        ${result.estimatedProcessing}`);
