# AI-Assisted Automated Testing — Free Workshop Demos

> **AI wrote a green check. What did it miss—and what should it be allowed to do next?**

Follow three short demos in a self-guided workshop designed for a future TestCraft Academy video. Practise reviewing AI-suggested tests, challenging a Selenium draft, and setting boundaries for a custom testing agent. **No account, API key, AI model, browser driver, or packages are needed.** This is a small preview of the planned course, not the course itself.

## The story

SwiftCart is a **fictional** shop with one rule: delivery is free when *eligible goods* total at least £50. Gift cards do not count towards the threshold. Otherwise delivery costs £5. [`demos/shop.py`](demos/shop.py) is a deliberately flawed, in-memory function—not a website or production system.

## Follow the three steps

Use Python **3.9+**. Open a terminal in this repository's folder (the one containing `README.md` and `demos/`); extract the ZIP first if necessary. Run the commands separately. On Windows use `py -3` instead of `python3`.

### 1. Challenge the suggested check

```bash
python3 demos/01_green_check.py
```

The scripted **AI-style suggestion** checks a £50 basket of goods; it passes. Then try £40 of goods plus a £10 gift card. **Pause:** what should delivery cost? Why did a green check miss this? The output compares the intended rule with the deliberate defect.

### 2. Review a Selenium draft

```bash
python3 demos/02_review_selenium.py
```

This prints a short, **unexecuted Selenium example** and review questions. Find the missing assertion and the missing gift-card example. What locator and wait strategy would you ask for if this were a real website? There is no website or Selenium dependency here: **do not present the snippet as a working browser test.**

### 3. Bound the agent's tools

```bash
python3 demos/03_agent_guardrails.py
```

A deterministic policy permits a read-only test summary but rejects a proposed command and an attempt to pass a secret. It models the *idea* of approving tools for a custom agent; it is **not an AI agent or an MCP implementation**. MCP (Model Context Protocol) can connect an assistant to tools and context, but a connection alone does not make a tool safe. Who approves writes, and what should happen when untrusted test output tells the agent to ignore its rules?

## Try it yourself

Ask an AI assistant (optional): “For a free-delivery threshold of £50 in eligible goods, with gift cards excluded, propose three high-risk examples and expected delivery charges. Do not invent other business rules.” **Do not paste customer data, credentials, or private repositories into a public AI tool.** Compare its suggestions with the rule above, challenge assumptions, and run the local demos yourself. No AI service is required to complete the workshop.

Sketch a custom testing agent's contract:

- **Goal:** propose focused tests and explain evidence; never decide to release on its own.
- **Inputs:** the published rule and redacted, read-only test results.
- **Tools:** allow a read-only summary; deny shell, secrets, and writes unless a human separately approves them.
- **Review:** a human checks expected outcomes, Selenium assertions, and any proposed code changes before execution.

Optional repeatability check: `python3 -m unittest discover -s tests -v` (or `py -3 -m unittest discover -s tests -v` on Windows). The green unit tests **preserve the teaching examples and policy**, not product correctness: the shipping defect is intentionally still present.

## What did you learn?

- A plausible AI-generated check can pass while the real requirement fails. Verify expected results against the business rule.
- Selenium automation needs observable assertions and risk-based examples, not just clicks and a successful run.
- Tool permissions and human review matter even when an assistant uses MCP. Treat external content and tool output as untrusted data, not instructions.

For more practical testing content, visit the [TestCraft Academy YouTube channel](https://www.youtube.com/@LearnTestCraft/). The **AI-Assisted Automated Testing course is planned but not yet published**; this free workshop does not imply that dates, bookings, pricing, or a course page are available. See [TestCraft Academy](https://www.testcraftacademy.com/) for current information.

Recording this workshop? Use the [video walkthrough guide](VIDEO_GUIDE.md); the video link can be added here after publication.

Materials are available under the [MIT Licence](LICENSE). Copyright © 2026 TestCraft Academy.