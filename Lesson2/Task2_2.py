text_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_text_list = []
for i in range(len(text_list)):
    if text_list[i].isdigit():
        text_list[i] = ['"', f'{int(text_list[i]):02d}', '"']
    elif text_list[i][1:].isdigit():
        text_list[i] = ['"', text_list[i][:1] + f'{int(text_list[i][1:]):02d}', '"']
for el in text_list:
    if isinstance(el, list):
        new_text_list.extend(el)
    else:
        new_text_list.append(el)
print(new_text_list)
text = " ".join(new_text_list)
i = 0
finish_text = ''
while i < len(text):
    if text[i] == '"' and text[i + 1] == ' ' \
            and (text[i + 2].isdigit() or text[i + 3].isdigit()):
        finish_text += '"'
        i += 1
    elif text[i] == ' ' and text[i - 1].isdigit():
        finish_text += '"'
        i += 1
    else:
        finish_text += text[i]
    i += 1
print(finish_text)
