def missing_char(str, n):
    return str.replace(str[n], '', 1)


print(missing_char("jitendrad", 5))
missing_char('kitten', 1)
missing_char('kitten', 0)
missing_char('kitten', 4)