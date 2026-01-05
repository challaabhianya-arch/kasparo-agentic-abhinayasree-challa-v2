# Multi-Agent Content Generation System

## Problem Statement
The objective of this project is to design and implement a modular, agent-based AI system that generates structured, machine-readable content pages from a single product input. The system must simulate a multi-agent architecture where each agent is responsible for a specific task in the content generation pipeline, such as data parsing, question generation, templating, and page assembly.

The system should only use the provided product data and output clean JSON files suitable for downstream consumption.

---

## Solution Overview
This solution implements a multi-agent content generation pipeline orchestrated by a central controller. Each agent performs a well-defined role and communicates through structured data objects.

The pipeline starts with product data ingestion and ends with the generation of multiple structured JSON pages such as a product page, FAQ page, and comparison page. The system is fully modular, extensible, and follows separation of concerns.

---

## Scopes & Assumptions
- Only the provided product data (GlowBoost Vitamin C Serum) is used as input.
- No external APIs or databases are used.
- Outputs are generated as machine-readable JSON files.
- Each agent operates independently and performs a single responsibility.
- The system is designed for clarity, extensibility, and maintainability rather than UI rendering.

---

## System Design
The system follows a multi-agent architecture coordinated by an orchestrator.

### Agents and Responsibilities

1. **Data Parser Agent**
   - Reads and structures raw product data into a normalized format.
   - Acts as the single source of truth for product information.

2. **Question Generator Agent**
   - Generates relevant customer questions based on product attributes.
   - Produces structured question lists for FAQ and comparison use cases.

3. **Logic Blocks Agent**
   - Applies rule-based logic to determine responses and content flow.
   - Ensures deterministic behavior for content decisions.

4. **Template Engine Agent**
   - Converts structured data into predefined content templates.
   - Ensures consistency across different page formats.

5. **Page Assembler Agent**
   - Aggregates templated content into final JSON pages.
   - Writes output files such as product_page.json, faq.json, and comparison_page.json.

6. **Orchestrator**
   - Controls execution order of all agents.
   - Manages data flow between agents and triggers output generation.

### Data Flow
1. Product data is parsed by the Data Parser.
2. Parsed data is passed to the Question Generator.
3. Logic Blocks determine content rules.
4. Template Engine formats structured content.
5. Page Assembler generates final JSON outputs.
6. Orchestrator coordinates the full pipeline.

This modular design ensures scalability, easy debugging, and clear separation of responsibilities across agents.
