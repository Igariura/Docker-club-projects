import random, datetime

notes = [
    "🌟 Every expert was once a beginner. Keep going!",
    "🔥 Small steps every day lead to big results.",
    "🚀 You don't have to be great to start, but you have to start to be great.",
    "💡 The best time to learn something new is right now.",
    "🎯 Focus on progress, not perfection.",
    "🐳 You just ran your first Docker container. Legend!",
    "⚡ Code today, inspire tomorrow.",
    "🌱 Growth happens outside your comfort zone.",
]

today = datetime.date.today()
note  = random.choice(notes)

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f"  📋 Lucky Notes  |  {today}")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print()
print(f"  {note}")
print()
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")