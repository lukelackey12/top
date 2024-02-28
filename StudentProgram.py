import StudentClass as s

me = s.student(89252099, 'Luke Lackey', '09-05-2001', 'Senior')

print()
print(f"My name is {me.name}. I am {me.calc_age()} years old.")
print(f"Since I am a {me.year}, I can register from {me.get_registration()}.")
print()
