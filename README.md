# Emoji Sentiment Analyzer
A command-line Python tool that analyzes the emotional tone of text by extracting emojis and scoring them against positive and negative keyword lists.

---

## How to Use
1. Run the script from the terminal
2. Enter as many sentences as you want, one at a time
3. Type `STOP` when you are done
4. The tool displays a positive, negative, and neutral score along with an overall sentiment

---

## Features
- Accepts multiple sentences in one session
- Extracts emojis and reads their descriptions using `demoji`
- Scores emojis against positive and negative keyword lists
- Tracks per-sentence sentiment and running totals
- Handles ties and mixed sentiment results

---

## Example Output
```
Positive Score: 3
Negative Score: 2
Neutral Score: 1
Overall Sentiment: Positive
```

---

## Tech Stack
| Technology | Purpose |
|---|---|
| Python | Core logic |
| `demoji` | Emoji extraction and description lookup |

---

## Getting Started

### Prerequisites
- Python 3 installed
- demoji installed

```bash
py -m pip install demoji
```

### Installation
```bash
# Clone the repository
git clone https://github.com/kevvvvvz/emoji-sentiment-analyzer.git

# Navigate into the project
cd emoji-sentiment-analyzer

# Run the tool
python emojisentiment.py
```

---
