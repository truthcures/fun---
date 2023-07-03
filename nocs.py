#tested on python 3.10.6

import re

"""
Напишите на вашем любимом скриптовом языке программирования (Ruby, Perl, PHP, Python, Groovy, . . . )  программу,
которая считывает файл и выводит число событий NOK за каждую минуту. Ответ пришлите ссылкой на GitHub.
"""

logs = open("events.log", "r")
logs = logs.readlines()
noks = {}

for status in logs:
	matches = re.search(r"(\d+-\d+-\d+)[ \t]+(\d+:\d+).*[ \t]+([NOK]+)", status)
	
	if \
	matches is not None and \
	matches.group(1) is not None and \
	matches.group(2) is not None and \
	matches.group(3) == "NOK":
		
		minute = matches.group(1) + " " + matches.group(2) + " NOKs"
		noks[minute] = noks.get(minute, 0) + 1
		
print(noks)
