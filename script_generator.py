import random

TARGET_MINUTES = 2        # 2.5 hours
WORDS_PER_MINUTE = 80       # very slow narration

def pick_topic():
    with open("topic.txt", "r", encoding="utf-8") as f:
        topics = [t.strip() for t in f if t.strip()]
    return random.choice(topics)

def generate_sleep_paragraph(topic):
    templates = [
        f"Let us rest peacefully while reflecting on {topic}.",
        "These words are calm and gentle.",
        "They were written to bring peace to the heart.",
        "Imagine Jesus sitting quietly, teaching the people with kindness.",
        "There is nothing you need to do.",
        "Allow your breathing to slow.",
        "God is near, watching over you.",
        "You are safe to rest."
    ]
    return " ".join(random.sample(templates, k=6))

def generate_long_script(topic):
    target_words = TARGET_MINUTES * WORDS_PER_MINUTE
    words = []

    while len(words) < target_words:
        paragraph = generate_sleep_paragraph(topic)
        words.extend(paragraph.split())
        words.append("\n\n")

    return " ".join(words)

if __name__ == "__main__":
    topic = pick_topic()
    script = generate_long_script(topic)

    with open("script.txt", "w", encoding="utf-8") as f:
        f.write(script)

    with open("used_topic.txt", "w", encoding="utf-8") as f:
        f.write(topic)

    print("Sleep script generated.")
    print("Topic:", topic)

