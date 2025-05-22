#!/usr/bin/env bash
declare -A outline=(
  [01-welcome]="about-this-gitbook quick-start-tldr"
  [02-vision-and-mission]="guiding-principles identity-blurb"
  [03-concept-foundations]="why-a-dao web3-refi-basics bioregionalism feedback-first-design vertical-vs-horizontal three-tier-oracle"
  [04-strategic-roadmap]="phase-0 phase-1 phase-2 phase-3"
  [05-technical-architecture]="data-flow local-first-nodes climate-oracles identity-credentials hypercerts"
  [06-coop-producer-pathways]="roles-incentives participatory-mrv coffee-use-case"
  [07-esg-integration-track]="supply-chain-traceability pitch-deck case-studies"
  [08-funding-capital-stacks]="hypercerts gitcoin quadratic-funding blended-capital"
  [09-glossary]="vision-phrases acronyms"
  [10-resources-references]="partners transcripts research-library"
  [A-working-notes]="brainstorms meeting-logs todo"
)
for folder in "${!outline[@]}"; do
  mkdir -p "$folder"
  for page in ${outline[$folder]}; do
    file="$folder/$page.md"
    [[ -e $file ]] || printf "# %s\n\n_TODO_\n" "${page//-/ }" > "$file"
  done
done
