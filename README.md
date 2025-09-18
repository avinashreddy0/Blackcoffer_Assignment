<p align="center">
  <img src="images/assigment.png" alt="Blackcoffer Assignment Thumbnail" width="720" />
</p>

## 🧠 Blackcoffer Assignment – Text Analytics Toolkit

Make text analysis easy and repeatable with a lightweight setup using dictionaries, stopwords, and an input workbook. This project structure is designed for Power BI/Excel workflows and can be adapted for Python/R as needed. ✨

### 📦 What's Inside
- **data/raw_data_excel/Input.xlsx**: Your input data file (articles, URLs, or text).
- **MasterDictionary/**: Contains `positive-words.txt` and `negative-words.txt` for polarity scoring 👍👎.
- **StopWords/Words.txt**: Stopwords list to clean the text 🧹.
- **answer/**: Put or generate your processed outputs here 📁.

### 🔍 Typical Metrics You Can Compute
- **Polarity Score** 🟥🟩
- **Subjectivity Score** 🎯
- **Average Sentence Length** ✍️
- **Complex Word Count / %** 📚
- **Fog Index** 🌫️
- **Syllable Count per Word** 🔤

### 🚀 How To Use
1. Place your raw input in `data/raw_data_excel/Input.xlsx`.
2. Review and update dictionaries in `MasterDictionary/` if needed.
3. Update `StopWords/Words.txt` to match your use case.
4. Process the input using your preferred tool:
   - Power BI (Power Query / custom functions) ⚡
   - Excel (Power Query / formulas) 📊
   - Python/R scripts (optional) 🐍📈
5. Save the final outputs to the `answer/` folder.

### 🗂️ Project Structure
```text
Blackcoffer_Assignment/
├─ answer/
├─ data/
│  └─ raw_data_excel/
│     └─ Input.xlsx
├─ MasterDictionary/
│  ├─ negative-words.txt
│  └─ positive-words.txt
├─ StopWords/
│  └─ Words.txt
└─ README.md
```

### 🧩 Integration Tips
- Keep dictionaries in simple UTF-8 text, one word per line.
- Normalize text to lowercase before matching.
- Strip punctuation and remove stopwords prior to scoring.
- For Power BI, consider caching dictionaries via `Enter Data` or `Web.Contents` to avoid path issues.

### 🛠️ Optional: Python Helper (snippet)
If you later add a Python script, this snippet shows how to load dictionaries:
```python
from pathlib import Path

root = Path('.')
pos_words = set(w.strip().lower() for w in (root / 'MasterDictionary' / 'positive-words.txt').read_text(encoding='utf-8').splitlines() if w.strip())
neg_words = set(w.strip().lower() for w in (root / 'MasterDictionary' / 'negative-words.txt').read_text(encoding='utf-8').splitlines() if w.strip())
stopwords = set(w.strip().lower() for w in (root / 'StopWords' / 'Words.txt').read_text(encoding='utf-8').splitlines() if w.strip())
```

### ✅ Checklist
- [ ] Input placed in `data/raw_data_excel/Input.xlsx`
- [ ] Dictionaries reviewed in `MasterDictionary/`
- [ ] Stopwords updated in `StopWords/Words.txt`
- [ ] Outputs exported to `answer/`

### 📣 Notes
- This repo is structured for the Blackcoffer text analytics assignment; adapt paths as needed for your environment.
- Feel free to extend with additional linguistic features (e.g., lemmatization, POS tagging) if you add Python/R processing.

Happy analyzing! 🚀