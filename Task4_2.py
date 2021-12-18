from requests import get, utils


def currency_rates(currency):
    """
    currency converter in rubles

    :param currency: currency to convert
    :return: currency value in rubles
    """

    # parsing
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    # search
    currency = currency.upper()
    text = content.split('<CharCode>')
    for el in text:
        if el[:3] == currency:
            value = el.split('<Value>')
            value = value[1].split('</Value>')
            return float(value[0].replace(",", "."))
    print("None")


print(currency_rates('EUR'))
print(currency_rates('UsD'))
