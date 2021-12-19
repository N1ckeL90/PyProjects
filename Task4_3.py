from requests import get, utils
from datetime import date


def currency_rates(currency):
    """
    currency converter in rubles

    :param currency: currency to convert
    :return: currency value in rubles and current data
    """

    # parsing
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    # date
    current_date = date(int(content[66:70]), int(content[63:65]), int(content[60:62]))
    # search
    currency = currency.upper()
    text = content.split('<CharCode>')
    for el in text:
        if el[:3] == currency:
            nominal = el.split('<Nominal>')
            nominal = nominal[1].split('</Nominal>')
            value = el.split('<Value>')
            value = value[1].split('</Value>')
            return f'{nominal[0]} {currency} = {float(value[0].replace(",", "."))} RUB, {current_date}'
    print("None")


print(currency_rates('eur'))
print(currency_rates('UsD'))
