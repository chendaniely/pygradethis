
"""This module contains utilities for generating a friendly message for feedback"""
import random

def praise() -> str:
  """Returns a random praise message"""
  return random.choice([
      "Absolutely fabulous!",
      "Amazing!",
      "Awesome!",
      "Beautiful!",
      "Bravo!",
      "Cool job!",
      "Delightful!",
      "Excellent!",
      "Fantastic!",
      "Great work!",
      "I couldn't have done it better myself.",
      "Impressive work!",
      "Lovely job!",
      "Magnificent!",
      "Nice job!",
      "Out of this world!",
      "Resplendent!",
      "Smashing!",
      "Someone knows what they're doing :)",
      "Spectacular job!",
      "Splendid!",
      "Success!",
      "Super job!",
      "Superb work!",
      "Swell job!",
      "Terrific!",
      "That's a first-class answer!",
      "That's glorious!",
      "That's marvelous!",
      "Very good!",
      "Well done!",
      "What first-rate work!",
      "Wicked smaht!",
      "Wonderful!",
      "You aced it!",
      "You rock!",
      "You should be proud.",
      ":)"
    ]
  )

def encourage() -> str:
  """Returns a random encouragement message"""
  return random.choice([
      "Please try again.",
      "Give it another try.",
      "Let's try it again.",
      "Try it again; next time's the charm!",
      "Don't give up now, try it one more time.",
      "But no need to fret, try it again.",
      "Try it again. I have a good feeling about this.",
      "Try it again. You get better each time.",
      "Try it again. Perseverence is the key to success.",
      "That's okay: you learn more from mistakes than successes. Let's do it one more time."
    ]
  )