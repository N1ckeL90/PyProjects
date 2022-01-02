import re


def email_parse(email_adress):
    pattern = re.compile(r'(?P<someone>\w+)@(?P<domain>\w+\.[ru|com]+$)', re.IGNORECASE)
    result = re.match(pattern, email_adress)
    if not result:
        raise ValueError(f'wrong email: {email_adress}')
    print(result.groupdict())


email_parse('someone@geekbrains.ru')
email_parse('someone@geekbrainsru')
