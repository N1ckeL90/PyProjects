import re


def parse_log(file):
    pattern = re.compile(r'(?P<remote_addr>[\w+\.\:].+)'
                         r' - - \[(?P<request_datetime>\d+\/\w+\/\d+\:\d+\:\d+\:\d+\s\+\d+)\]'
                         r' "(?P<request_type>\w+)'
                         r' (?P<requested_resource>[\/\w+].+)'
                         r' HTTP/1.1" (?P<response_code>\d+)'
                         r' (?P<response_size>\d+)')
    with open(file, encoding='utf-8') as f:
        for line in f.readlines():
            result = re.search(pattern, line)
            if result:
                print(result.groups())


parse_log('nginx_logs.txt')
