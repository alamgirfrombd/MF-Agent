# MF Agent — আপডেট নোট

## কী পরিবর্তন করা হয়েছে
- পুরোনো তিনটি বিচ্ছিন্ন কাঠামোর পরিবর্তে একক modular project structure তৈরি করা হয়েছে।
- সাতটি বিদ্যমান Dataset Registry `registry/datasets/`-এ রাখা হয়েছে এবং Master Registry-র path ঠিক করা হয়েছে।
- সব Dataset `draft` রাখা হয়েছে; প্রকৃত SQL Server schema যাচাই না হওয়া পর্যন্ত এগুলো execute করা যাবে না।
- `.env.example`, `.gitignore`, `pyproject.toml`, `requirements.txt` এবং Windows setup নির্দেশনা যোগ করা হয়েছে।
- Configuration, SQL Server connection, metadata-only schema discovery, registry loader/validator, read-only SQL guard, query executor, Ollama adapter, audit helper, starter UI এবং tests যোগ করা হয়েছে।
- Empty/invalid legacy Python files-কে executable হিসেবে কপি করা হয়নি।

## Validation ফলাফল
- Python compile check: PASS
- Registry load: 7 datasets
- Registry structural validation: PASS (0 errors)
- Pytest: 3 passed, 1 skipped
- SQL Guard test skipped কারণ এই build environment-এ `sqlglot` install করা যায়নি (network unavailable)।
- SQL Server connectivity ও ODBC driver test: NOT RUN; এই environment-এ আপনার SQL Server/Windows ODBC access নেই।
- LLM connectivity test: NOT RUN; Ollama service/model access নেই।

## গুরুত্বপূর্ণ সীমাবদ্ধতা
এটি একটি কার্যকর starter infrastructure, সম্পূর্ণ production-ready Agent নয়। Deterministic plan-to-SQL compiler, Registry-based table/column allowlist, OpenAI adapter, authentication, branch-level authorization, এবং অনুমোদিত MRA/PKSF metric formulas পরবর্তী কাজ। Production ব্যবহারের আগে dedicated SQL read-only login এবং database-side access control বাধ্যতামূলক।

## চালু করার নিয়ম
README.md এবং instruction.md অনুসরণ করুন। প্রথমে `.env.example` থেকে `.env` তৈরি করে SQL Server settings দিন; তারপর requirements install, offline tests, database health check এবং schema discovery চালান।
