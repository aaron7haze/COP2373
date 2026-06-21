# Programming Exercise 2 - Spam Filter
# Author: Aaron Haze
# Date: 2026-06-14

import re

# ------------------------------------------------------------
# SPAM KEYWORDS (30 total)
# ------------------------------------------------------------
SPAM_KEYWORDS = [
    "free", "winner", "win", "cash", "prize",
    "credit", "loan", "deal", "offer", "limited",
    "urgent", "act now", "click here", "risk free", "guarantee",
    "cheap", "discount", "save", "bonus", "reward",
    "investment", "million", "billion", "wire transfer", "crypto",
    "password", "account", "verify", "exclusive", "no obligation"
]


# ------------------------------------------------------------
# NORMALIZATION FUNCTION
# ------------------------------------------------------------
def normalize(text):
    """
    Lowercase, remove punctuation, normalize hyphens, collapse spaces.
    Makes matching accurate and consistent.
    """
    text = text.lower()
    text = re.sub(r"[-]", " ", text)          # hyphens → spaces
    text = re.sub(r"[^\w\s]", "", text)       # remove punctuation
    text = re.sub(r"\s+", " ", text).strip()  # collapse spaces
    return text


# ------------------------------------------------------------
# ANALYZE MESSAGE
# ------------------------------------------------------------
def analyze_message(message, keywords):
    """
    Count keyword occurrences using normalized text and regex boundaries.
    Handles multi-word phrases, punctuation, hyphens, and spacing.
    """
    clean = normalize(message)
    score = 0
    triggered = []

    for kw in keywords:
        kw_clean = normalize(kw)

        # Match whole words or whole phrases
        pattern = r"\b" + re.escape(kw_clean) + r"\b"
        matches = re.findall(pattern, clean)

        if matches:
            count = len(matches)
            score += count
            triggered.append(f"{kw} (x{count})")

    return score, triggered


# ------------------------------------------------------------
# CLASSIFY SCORE
# ------------------------------------------------------------
def classify_score(score):
    if score == 0:
        return "No spam detected"
    elif score <= 5:
        return "Low spam likelihood"
    elif score <= 15:
        return "Medium spam likelihood"
    elif score <= 25:
        return "High spam likelihood"
    else:
        return "Extreme spam likelihood"


# ------------------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------------------
def main():
    print("=== Programming Exercise 2: Spam Filter ===")
    message = input("Enter your email message: ")

    score, triggered = analyze_message(message, SPAM_KEYWORDS)
    likelihood = classify_score(score)

    print("\n=== RESULTS ===")
    print(f"Spam score: {score}")
    print(f"Likelihood: {likelihood}")

    if triggered:
        print("Triggered keywords:")
        for t in triggered:
            print(" -", t)
    else:
        print("No spam keywords found.")


# ------------------------------------------------------------
# ENTRY POINT
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
