#!/usr/bin/env python3
"""
Slice longform.md into GitBook pages.

• Breaks on H2 (##) headings.
• Writes each chunk to the path in `mapping`.
• Leaves untouched sections logged to console.
"""
import pathlib, re, textwrap, subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
LF = ROOT / "longform.md"
if not LF.exists():
    raise SystemExit("longform.md not found")

mapping = {
    # top-level indices
    "vision-&-mission":                 "02-vision-and-mission/index.md",
    "concept-foundations":              "03-concept-foundations/index.md",
    "strategic-roadmap":                "04-strategic-roadmap/index.md",
    "technical-architecture":           "05-technical-architecture/index.md",
    "cooperative-&-producer-pathways":  "06-coop-producer-pathways/index.md",
    "esg-integration-track":            "07-esg-integration-track/index.md",
    "funding-&-capital-stacks":         "08-funding-capital-stacks/index.md",
    "glossary":                         "09-glossary/index.md",

    # concept sub-pages
    "feedback-first-data-design":       "03-concept-foundations/feedback-first-design.md",
    "vertical-vs-horizontal-models":    "03-concept-foundations/vertical-vs-horizontal.md",
    "three-tier-oracle-enrichment-framework":
                                        "03-concept-foundations/three-tier-oracle.md",

    # roadmap phases
    "phase-0-–-infrastructure-&-core-partnerships":
                                        "04-strategic-roadmap/phase-0.md",
    "phase-1-–-dao-toolkit-prototype-&-pilot-co-ops":
                                        "04-strategic-roadmap/phase-1.md",
    "phase-2-–-funding-rounds-&-incentive-layers":
                                        "04-strategic-roadmap/phase-2.md",
    "phase-3-–-scaling-to-a-global-mosaic":
                                        "04-strategic-roadmap/phase-3.md",

    # technical sub-pages
    "data-flow-overview":               "05-technical-architecture/data-flow.md",
    "local-first-stack-diagram":        "05-technical-architecture/stack-view.md",

    # coop sub-pages
    "roles,-incentives-&-participatory mrv":
                                        "06-coop-producer-pathways/roles-incentives.md",
    "coffee-cooperative-use-case":      "06-coop-producer-pathways/coffee-use-case.md",

    # esg sub-pages
    "supply-chain-traceability-&-scope-3-data-enrichment":
                                        "07-esg-integration-track/traceability.md",
    "case-studies-&-partner-pilots":    "07-esg-integration-track/case-studies.md",

    # funding sub-pages
    "hypercert-mechanics-&-gitcoin-rounds":
                                        "08-funding-capital-stacks/hypercerts.md",
    "quadratic-funding-&-impact daos":  "08-funding-capital-stacks/quadratic-funding.md",
    "blended-capital-strategies":       "08-funding-capital-stacks/blended-capital.md",
}

content = LF.read_text()
chunks = re.split(r"\n## +", content)[1:]   # skip anything before first H2
for chunk in chunks:
    h2, *body = chunk.splitlines()
    slug = h2.lower().strip().replace(" ", "-")
    dest = mapping.get(slug)
    if not dest:
        print(f"⚠️  no mapping for '{h2}'")
        continue
    dest_path = ROOT / dest
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    dest_md = f"# {h2}\n" + "\n".join(body).rstrip() + "\n"
    dest_path.write_text(textwrap.dedent(dest_md))

# stage changed files so auto-commit action can commit them
subprocess.run(["git", "add", "-A"], check=False)
