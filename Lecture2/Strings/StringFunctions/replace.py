String = "\nHello! I am String — simple, slender, and often underestimated. I may appear fragile, but I can tie things together, hold memories in knots, and stretch across time to connect people and places. I come in many forms — silk, thread, wire — and each version of me tells a different story. Sometimes I unravel; other times, I pull things tight. In this tale, I may be small, but never useless. I'm the quiet hero behind the scenes, binding everything with strength and purpose."

print(String)
old = input("\nEnter the old word that you want to replace with :")
if old not in String:
   print("\nThere does not exist such word in the string! TRY AGAIN!")
else:
    new = input("\nEnter the new word that you want to put in the place of old one :")
    print(String.replace(old, new))
