formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4 ))
print(formatter.format("first", "second", "third", "fourth"))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(True, False, "test", 7))

print(formatter.format(
"line",
"line with space ",
"next line",
"last line"
))
