# Security

## Protecting Secrets

This project uses API keys for OpenAI, OpenRouter, and Telegram. These credentials **must never be committed to version control**.

### Why .env Must Not Be Pushed

The `.env` file contains sensitive values such as `OPENAI_API_KEY` and `TELEGRAM_BOT_TOKEN`. If committed, anyone with access to the repository can:

- Use your OpenAI / OpenRouter API key and incur charges on your account
- Send messages via your Telegram bot
- Access your Telegram chat history

### How We Protect Secrets

1. **`.env` is in `.gitignore`** – Git will never track or stage `.env` by default.
2. **`.env.example` is the template** – It contains placeholder values only and is safe to commit.
3. **Secrets are read at runtime** – The application reads credentials from environment variables via `python-dotenv`, never from source code.
4. **GitHub Actions uses Secrets** – The CI/CD workflow reads all credentials from GitHub Secrets, not from the repository.

### Best Practices

- **Never** hardcode an API key or token in any Python file.
- **Never** paste a real key in issue comments, pull requests, or discussions.
- **Rotate keys regularly** – Generate new keys on OpenAI / OpenRouter / Telegram every few months.
- **Use separate keys per project** – If a key is compromised, revoke only that one.

### What to Do If You Accidentally Push a Secret

1. **Revoke the compromised key immediately** on the provider's dashboard.
2. Remove the secret from the git history:
   ```bash
   git filter-branch --force --index-filter \
     "git rm --cached --ignore-unmatch .env" \
     --prune-empty --tag-name-filter cat -- --all
   ```
3. Force-push the cleaned history:
   ```bash
   git push origin --force --all
   ```
4. Generate a new key and update your local `.env`.
5. Consider the key compromised and rotate anything that depended on it.

> **Note:** `git filter-branch` rewrites history. Coordinate with collaborators before force-pushing.
