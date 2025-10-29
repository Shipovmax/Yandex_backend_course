not_uniq_str = 'съешь же ещё этих мягких французских булок да выпей чаю'

stri = not_uniq_str.replace(' ', '')
set_stri = set(stri)
print(len(set_stri))
# print(count_char)