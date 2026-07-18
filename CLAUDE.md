# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Desafio Fotos** is a system for creating enriched flashcards for Spaced Repetition Systems (SRS) from photographic questions/scenarios. The primary workflow involves extracting multiple-choice questions from images, creating basic cards, then enriching them with Portuguese translations, technical explanations, and analysis of answer choices.

## Core Workflow

### Photo Preparation Phase
Place new question photos in the repository root directory with any filename pattern (Screenshots, Captures, etc.). The skill handles renaming automatically.

### Card Generation Phase
Invoke the custom skill:
```bash
/gerar-cards-enriquecidos
```

This skill automates the entire enrichment pipeline for each photo:
- Extracts question text and four answer options (A, B, C, D)
- Generates `NNN-card.md` (basic card with original English text and options)
- Generates `NNN-enriched-card.md` with:
  - Portuguese translation of question and options
  - Technical explanation section explaining the tested concept/pattern
  - Detailed analysis of why the correct answer is correct
  - Individual analysis of why each incorrect option is wrong
  - Pattern/concept guidance ("Dica importante")
  - Marked correct answer

## Card Formats

### Simple Card (NNN-card.md)
```markdown
[Original Question in English]
---
[ ] A - [Option A]
[ ] B - [Option B]
[ ] C - [Option C]
[ ] D - [Option D]
```

### Enriched Card (NNN-enriched-card.md)
- Original question (English)
- Separator (`---`)
- `### TRANSLATED QUESTION` section with Portuguese translation + translated options
- Separator (`---`)
- `### EXPLANATION (TECH LEAD)` section with:
  - Context and concept being tested
  - Deep technical analysis of why correct answer is best
  - Detailed breakdown of why each wrong option fails
  - Pattern insights and connection to broader topics
- Separator (`---`)
- `### SIMPLE EXPLANATION` section (accessible for learners/beginners) with:
  - Concept explained in plain language
  - Why the correct answer works (simple terms)
  - Why other options don't work (without jargon)
  - Key takeaway to remember
- Separator (`---`)
- `### CORRECT ANSWER` section with marked letter (A/B/C/D)

## Available Skills

### `/gerar-cards-enriquecidos`
Generates enriched flashcards from photos automatically.
- **Input**: Photos with any name (e.g., Screenshots)
- **Process**: Rename → Extract → Create simple + enriched cards
- **Output**: `NNN-card.md` and `NNN-enriched-card.md` files
- **Features**: Automatic renaming, dual-level explanations, structured format

**Documentation:**
- `.claude/skills/gerar-cards-enriquecidos/SKILL.md` — Overview
- `.claude/skills/gerar-cards-enriquecidos/README.md` — Detailed instructions

### `/exporta-cards-enriquecidos-para-pdf`
Consolidates all enriched cards into a single PDF deck.
- **Input**: All `NNN-enriched-card.md` files
- **Process**: Extract → Consolidate → Format → Export to PDF
- **Output**: `flashcards-deck-[DATE].pdf`
- **Features**: Deck-style formatting, numbered pages, indexed content

**Documentation:**
- `.claude/skills/exporta-cards-enriquecidos-para-pdf/SKILL.md` — Overview
- `.claude/skills/exporta-cards-enriquecidos-para-pdf/README.md` — Detailed instructions
- `.claude/skills/exporta-cards-enriquecidos-para-pdf/EXEMPLO-SAIDA.md` — Example output format

## Key References

- **README.md**: Complete workflow documentation
- **USAR_SKILL.md**: Interactive usage guide
- **`templates/`**: Example cards and deck format
- **`EXAMPLE-enriched-card-new-format.md`**: Card example with both explanation levels
- **`templates/deck-exemplo.md`**: PDF deck format template

## Certification Context

The skill is designed around patterns from **Claude Certified Architect – Foundations Certification**, testing knowledge of:
- Claude Models and capabilities
- Prompt engineering and advanced techniques
- Agentic systems and tool use
- Vision and document handling
- Best practices and design patterns
- Trade-offs in system architecture
- Practical use cases and applications

Cards focus on architecture decisions, design patterns, and engineering principles rather than trivia.

## Development Notes

### Skill Invocation
When the user runs `/gerar-cards-enriquecidos`:

**Phase 1: Photo Detection & Renaming**
1. Detect all image files (*.png, *.jpg) in the current directory
2. Rename non-standard files to `foto-001.png`, `foto-002.png`, etc. (sorted by modification date)
3. Report renamed files

**Phase 2: Card Generation** (for each photo in order)
4. Read the image and extract question + 4 options (A, B, C, D)
5. Create simple card (`NNN-card.md`) with English text only
6. Analyze the question and determine correct answer based on technical merit
7. Create enriched card (`NNN-enriched-card.md`) with:
   - Translated question and options in Portuguese
   - **EXPLANATION (TECH LEAD)**: Deep technical explanation using architecture patterns/design principles
   - **SIMPLE EXPLANATION**: Accessible explanation suitable for beginners/learners
   - **CORRECT ANSWER**: Marked letter

**Phase 3: Summary**
8. List all cards created
9. Confirm success

### Output Quality Standards

#### EXPLANATION (TECH LEAD)
- Reference architectural patterns, design principles, or engineering concepts
- Explain WHY each alternative is right/wrong, not just that it is
- Provide context on what concept/pattern is being tested
- Connect to broader topics when relevant
- Maintain technical precision and professional tone
- Structure: Context → Correct answer analysis → Wrong options analysis → Pattern insight

#### SIMPLE EXPLANATION
- Use plain language without sacrificing accuracy
- Explain concept as if teaching a beginner/learner (accessible but not childish)
- Focus on WHY the correct answer works
- Address common misconceptions in wrong options
- Use analogies and practical examples when helpful
- Structure: Simple concept → Why correct → Why others don't work → Key takeaway

#### General Standards
- Translations must be faithful to meaning (not literal)
- Keep technical terms in English when appropriately localized to Portuguese
- Cards are self-contained educational units for SRS
- Both explanation levels should complement each other (different audience, not repetition)

### Permissions Note
The `.claude/settings.local.json` file contains pre-approved permissions for file renaming operations with `chmod`, `mv`, and `rm` commands for the flashcard workflow.
