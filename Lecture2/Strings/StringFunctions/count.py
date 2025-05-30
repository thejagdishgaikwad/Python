string_story = "\nHello! I am String — simple, slender, and often underestimated. I may appear fragile, but I can tie things together, hold memories in knots, and stretch across time to connect people and places. I come in many forms — silk, thread, wire — and each version of me tells a different story. Sometimes I unravel; other times, I pull things tight. In this tale, I may be small, but never useless. I'm the quiet hero behind the scenes, binding everything with strength and purpose."

print(string_story)
word = input("\nEnter the word that needs to keep count :")

if word not in string_story:
    print("\nThere exist no such word in the string! TRY AGAIN!")
else:
    print("The count of the word :", word, ":", string_story.count(word))

