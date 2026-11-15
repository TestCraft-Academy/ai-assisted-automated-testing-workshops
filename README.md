# AI-Assisted Automated Testing — Free Workshop Demos

A passing test does not always mean a working feature. Explore three small, runnable examples that show how to challenge AI-suggested tests, review browser automation, and keep testing agents within safe boundaries.

This free, self-guided TestCraft Academy workshop is a starting point for testers, QA engineers, SDETs, and developers. It takes only Python **3.9+**: no account, API key, AI model, browser driver, or extra packages are needed. The examples are scripted illustrations, **not live AI or browser tests**.

Want to practise these skills in more depth? **[Explore TestCraft Academy’s AI-Assisted Testing course →](https://www.testcraftacademy.com/service-page/ai-assisted-testing?referral=service_list_widget)**. The course covers risk-led test design, reviewed Selenium checks, custom testing agents, MCP, and guardrails. The exercises below are a free introduction, not the full course.

## The scenario

SwiftCart is a **fictional** shop with one rule: delivery is free when *eligible goods* total at least £50. Gift cards do not count towards the threshold. Otherwise delivery costs £5. [`demos/shop.py`](demos/shop.py) is a deliberately flawed, in-memory function—not a website or production system.

## Run the three demos

Open a terminal in this repository's folder (containing `README.md` and `demos/`); if you downloaded a ZIP, extract it first. Run each command separately. On Windows use `py -3` instead of `python3`.

### 1. Challenge a passing check

```bash
python3 demos/01_green_check.py
```

A scripted **AI-style suggestion** checks £50 of eligible goods and passes. Before reading the next line of output, ask: what should delivery cost for £40 of goods plus a £10 gift card? The intended charge is **£5**; the flawed function returns **£0**. A green check did not cover the rule that matters.

### 2. Review a Selenium draft

```bash
python3 demos/02_review_selenium.py
```

The script **prints an unexecuted, hypothetical Selenium snippet**. It clicks through checkout but has no delivery-charge assertion and no gift-card example. What outcome should it assert? What stable locators and explicit waits would a real website need? There is no website or Selenium dependency here; the snippet is for review, **not a working browser test**.

### 3. Set boundaries for a testing agent

```bash
python3 demos/03_agent_guardrails.py
```

A simple, deterministic policy prints decisions for three *proposed* actions:

- **ALLOW read-only summary:** a request to read a test summary without a payload is permitted.
- **DENY unapproved shell command:** a request to run a command is outside that permission.
- **DENY secret in payload:** even a request using the permitted read tool is rejected if it carries a payload.

An instruction found in untrusted output is data, not authority. **These are printed decisions, not executed tool calls or proof of security.** This is not a real agent, MCP (Model Context Protocol) implementation, or sandbox. MCP can connect assistants to tools and context, but privileged actions still need explicit boundaries and human approval.

## Try it yourself

Optionally ask an AI assistant: “For a free-delivery threshold of £50 in eligible goods, with gift cards excluded, propose three high-risk examples and expected delivery charges. Do not invent other business rules.” Compare its suggestions with the rule above and challenge any assumptions. **Never paste customer data, credentials, or private repositories into a public AI tool.** You can complete every demo without AI.

Sketch a custom testing agent's contract:

- **Goal:** propose focused tests and explain evidence; never decide to release on its own.
- **Inputs:** the published rule and redacted, read-only test results.
- **Tools:** allow a read-only summary; deny shell, secrets, and writes unless a human separately approves them.
- **Review:** a human checks expected outcomes, Selenium assertions, and any proposed code changes before execution.

For a repeatability check, run `python3 -m unittest discover -s tests -v` (Windows: `py -3 -m unittest discover -s tests -v`). The green unit tests **preserve the teaching examples, including the deliberate defect**; they do not certify product correctness.

## Keep learning

- A plausible AI-generated check can pass while the real requirement fails. Verify expected results against the business rule.
- Selenium automation needs observable assertions and risk-based examples, not just clicks and a successful run.
- Tool permissions and human review matter even when an assistant uses MCP. Treat external content and tool output as untrusted data, not instructions.

**[Explore the AI-Assisted Testing course at TestCraft Academy →](https://www.testcraftacademy.com/service-page/ai-assisted-testing?referral=service_list_widget)** for hands-on work with AI-assisted test design, Selenium, agents, MCP, and practical guardrails. See the course page for current details; this repository does not set dates, prices, or availability. For more free testing content, visit the [TestCraft Academy YouTube channel](https://www.youtube.com/@LearnTestCraft/).

Materials are available under the [MIT Licence](LICENSE). Copyright © 2026 TestCraft Academy.