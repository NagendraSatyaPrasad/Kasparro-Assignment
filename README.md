# Kasparro – Multi-Agent Content Generation System

## Overview
Kasparro is a modular, agent-based content generation system designed to automatically convert a small structured product dataset into multiple machine-readable content pages.

The primary focus of this project is **system design and agent orchestration**, rather than content writing or domain expertise. A monolithic approach was intentionally avoided. Instead, the system is built using **independent agents**, where each agent is responsible for a single task and all agents are coordinated through a central **Orchestrator Agent**.

---

## What the System Does
The system takes a single structured product input (JSON) and automatically generates the following outputs:

- An **FAQ page**
- A **Product Description page**
- A **Comparison page**

All outputs are generated as **clean, structured JSON files**, making them suitable for automation, pipelines, or downstream integrations.

---

## Design Approach
The system follows an **agent-oriented architecture**, where each agent has:

- A single responsibility
- Clearly defined inputs and outputs
- No shared global state

The entire workflow is controlled by an **Orchestrator Agent**, which ensures that agents execute in the correct order and communicate **only through explicit data passing**.

This approach keeps the system:
- Easy to understand
- Easy to extend
- Easy to debug

---

## High-Level Flow

```text
Product Input
   ↓
Product Parser Agent
   ↓
Question Generation Agent
   ↓
Content Logic Agent
   ↓
Page Generation Agents
   ↓
JSON Outputs
```
## Agents and Their Responsibilities

### Product Parser Agent
This agent is responsible for reading the raw product input and converting it into a clean, normalized internal data model.

Its purpose is to ensure that all downstream agents work with consistent and predictable data, reducing complexity and edge cases later in the pipeline.

---

### Question Generation Agent
This agent automatically generates categorized user questions based on the product data.

Question categories include:
- Informational  
- Usage  
- Safety  
- Purchase  
- Comparison  

All questions are structured and reusable across different page types.

---

### Content Logic Agent
The Content Logic Agent acts as a shared logic layer across the entire system.

It contains reusable content blocks for:
- Product summary generation  
- Benefits formatting  
- Usage steps  
- Safety information  
- Pricing structure  

By centralizing this logic, duplication across page generators is avoided and consistency is maintained.

---

### FAQ Page Agent
This agent uses the generated questions together with the content logic to produce a structured FAQ page.

It ensures that:
- A minimum number of question–answer pairs are generated  
- All output follows a strict JSON structure  

---

### Product Page Agent
This agent assembles a complete product description page by combining:
- Product summary  
- Ingredients  
- Benefits  
- Usage instructions  
- Safety details  
- Price information  

All fields are generated in a strictly structured JSON format suitable for machine consumption.

---

### Comparison Page Agent
This agent generates a comparison between the main product and a fictional **Product B**.

Key characteristics:
- The fictional product is intentionally structured  
- No external facts or research are introduced  
- The comparison follows clear, deterministic, rule-based logic  

---

### Orchestrator Agent
The Orchestrator Agent manages the entire execution flow of the system.

Responsibilities include:
- Invoking each agent in the correct sequence  
- Passing data explicitly between agents  
- Writing final outputs to JSON files  

No agent directly calls another agent, keeping dependencies clean, explicit, and easy to reason about.

---

## Templates and Reusable Logic
Content logic is separated from page structure using lightweight templates.

- Templates define **what** a page should contain  
- Logic defines **how** the data is transformed  

This separation improves:
- Consistency  
- Reusability  
- Extensibility  

---

## Output Structure
The system generates the following machine-readable outputs:

```text
outputs/faq.json
outputs/product_page.json
outputs/comparison_page.json
```

Each output:
- Strictly follows a structured format  
- Avoids free-form text blobs  
- Is suitable for automation and downstream processing  

---

## Scope and Assumptions

### Assumptions
- Only the provided product dataset is used  
- No external research or additional product facts are introduced  
- Content generation is deterministic and rule-based  
- The system is designed to be easily extended for new products or page types  

### Out of Scope
- UI rendering  
- Databases  
- Real-time APIs  
- LLM prompting or fine-tuning  

---

## Conclusion
This project demonstrates how a production-style agentic system can be built using clear abstractions, reusable logic, and controlled orchestration.

By separating parsing, logic, templating, and page generation into independent agents, the system remains:
- Scalable  
- Maintainable  
- Easy to reason about  

The overall design closely mirrors real-world automation pipelines used in modern content generation platforms.
