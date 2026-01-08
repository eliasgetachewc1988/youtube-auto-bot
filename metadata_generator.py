with open("used_topic.txt", "r", encoding="utf-8") as f:
    topic = f.read().strip()

if "Psalm" in topic or ":" in topic:
    ending = "Bible verses for sleep"
else:
    ending = "Bible stories for sleep"

title = f"{topic} | {ending}"

description = f"""
This video is created to help you rest peacefully.

Listen as gentle Christian reflections, Bible verses,
and calm thoughts about Jesus guide you into sleep.

There are no sudden sounds or distractions.
You may close your eyes and simply listen.

May God grant you peaceful rest.
"""

with open("metadata.txt", "w", encoding="utf-8") as f:
    f.write(title + "\n\n" + description)

print("Metadata generated.")
