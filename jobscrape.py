from lxml import html, etree
import requests, json
import sys

headers = {'Host': 'studentemployment.umich.edu', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36', 'DNT': '1', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Referer': 'https://studentemployment.umich.edu/JobX_FindaJob.aspx?ls=1',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9',
'Cookie': '_ga=GA1.2.1299378274.1519492210; gwlob=on; um_cookie_consent=na; CID=AgAAAIk45i8Wg5G7Dff6fBjm//Y=; visid_incap_496857=Sa4+AhhSSh6kvrHs8M1Y9BxJsVsAAAAAQUIPAAAAAACcXY8SZX/a/cTxYeL9kezp; nlbi_496857=WpYIUo8aCjkALCnDDOqUQgAAAADGzEuM9n/JV4qS327PUPOw; incap_ses_115_496857=xW9DLxRoEDmZ43Zje5CYATCsglwAAAAA+TFYH4lg00FqKA9ut5deDw==; __unam=85db7e4-16996cfc9d4-60900892-2; __utma=7269686.1299378274.1519492210.1553013394.1553013394.1; __utmc=7269686; __utmz=7269686.1553013394.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); ASP.NET_SessionId=mziq5kpdewbjrdrveeq3h02x; __utmc=172058721; Chm_Logins=duttar@umich.edu; _gid=GA1.2.1983775086.1556743181; __utma=172058721.1299378274.1519492210.1556763384.1556807503.7; __utmz=172058721.1556807503.7.4.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmb=172058721.10.10.1556807503'}

url = "https://studentemployment.umich.edu/JobX_FindAJob.aspx?t=qs&qs=21"
page = requests.get(url, headers=headers);
tree = html.fromstring(page.content);
titles = tree.xpath('//tr/descendant-or-self::*/text()');
#//h4/a/text()
#//div[@class="columns"]/div[@class="test_wrap"]
cleaned_up = [];
words = list(filter(None, [i.strip(' \n\t\r') for i in titles]));
for i in range(1,len(words)):
	if words[i] == "Job Title:":
		title = words[i+1];
		wage = words[i+6];
		openings = words[i+10][2:];
		hours = words[i+14][2:];
		cleaned_up.append({
				'Title:': title,
				'Wage:': wage,
				'Hours:': hours,
				'Openings:':openings
				});
cleaned_up = json.dumps(cleaned_up);
file = open('Jobs.json', 'w');
file.write(cleaned_up);

