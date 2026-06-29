# Lessons Learned

**Tags:** #lessons #python #architecture

## 1. Start with the Interface, Not the Implementation

Defining the `LLMProvider` abstract class first forced every provider to implement the same contract. Adding OpenRouter and Ollama later required zero changes to the summariser.

## 2. Deduplication Is Trickier Than It Looks

MD5-hashing titles seemed clean, but different feeds sometimes publish the same story with minor differences (trailing spaces, punctuation). Lowercase `.strip()` dedup works better in practice.

## 3. Keep Prompts Separate from Code

Moving the system prompt and `build_summarizer_prompt` into `prompts/summarizer_prompt.py` made it much easier to tweak the briefing format without touching any service logic.

## 4. Logging vs Print

Early versions used `print` everywhere. Switching to Python's `logging` module gave us timestamps, log levels, and the ability to silence noise in tests. Worth the early investment.

## 5. GitHub Actions Secrets Are the Right Place for Config

Hardcoding would have been a disaster. Using Secrets forced clean separation between code and credentials from day one, and made the CI/CD workflow trivial to set up.

## 6. Test Deduplication First

The deduplicator is simple enough that a single test file caught a regression immediately (empty titles being counted as duplicates). Even "obviously correct" code benefits from tests.
