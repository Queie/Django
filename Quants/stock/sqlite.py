import sqlite3
import pandas as pd


# DB의 table 이름 추출
def sqlite_table(db):
	con = sqlite3.connect(db)
	table_list = pd.read_sql("SELECT name FROM sqlite_master WHERE type = 'table';", con)
	con.commit()
	con.close()
	return table_list.to_html(index=None)
	# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_html.html
	# 숫자 자료형의 thousand comma 를 표시할 때
	# return table_list.to_html(float_format=lambda x: '{:,}'.format(x))



# 38공모 사이트 테이블 자료 가져오기
def stocks_38new():
    import requests, re
    import pandas as pd
    from lxml.html import fromstring, tostring
    url = "http://www.38.co.kr/html/fund/?o=nw"
    response = requests.get(url)
    html_code = fromstring(response.text)

    # 해당 기업의 내부 URL의 정보 크롤링
    comp_text = html_code.xpath('//table[@summary="신규상장종목"]//tr/td/a//text()')
    # 가장 가까운 테이블의 속성으로 구분
    text = html_code.xpath('//table[@summary="신규상장종목"]//tr/td/a/@href')
    comp_text = [txt  for txt in comp_text  if txt not in '(유가)']
    url_link = [url[:-6] + txt[1:]  for txt in text  if txt[:8] in './?o=v&n']

    codes ,markets = [], []
    print('www.38.co.kr 사이트 자료 수집중...')
    for i in range(len(url_link)):
        response = requests.get(url_link[i])
        html_code = fromstring(response.text)

        # 상장코드 번호 찾기
        text = html_code.xpath('//table[@summary="기업개요"]')
        inner_html = tostring(text[0],encoding='unicode')
        inner_html = fromstring(inner_html)
        text = inner_html.xpath('//tr/td[@bgcolor="#FFFFFF"]/text()')
        code = re.sub('\xa0', '',text[4])
        code = re.sub(' ', '',code)
        codes.append(code)
        market = re.sub('\xa0', '',text[3])
        market = re.sub(' ', '',market)
        markets.append(market)

    krxcode, result = [], []
    for mkt in markets:
        if mkt == '코스닥': krxcode.append('.KQ')
        else:               krxcode.append('.KS')
    markets = krxcode

    for i in range(len(comp_text)):
        new = [comp_text[i], codes[i]+markets[i]]
        result.append(new)
    result = pd.DataFrame(result)
    result = result.rename(columns={0:'기업명', 1:'Code'})#, 2:'Shares'})
    return result.to_html(index=None)