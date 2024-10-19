import json
import requests
import datetime

sign = ""
userCode = ""
unitCode = ""

def http(xq):
    headers = {
        "Host": "ktkq.hainanu.edu.cn",
        "Connection": "keep-alive",
        "Content-Length": "95",
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.50(0x1800323d) NetType/4G Language/zh_CN",
        "Referer": "https://servicewechat.com/wxa1e3abcd201139a2/28/page-frame.html"
    }
    data = {
        "sign": sign,
        "userType": "1",
        "userCode": userCode,
        "unitCode": unitCode
    }
    response = requests.post('https://ktkq.hainanu.edu.cn/app/getKbList', data=data, headers=headers)
    table = json.loads(response.text)
    total = table.pop('Total')
    to_week = table.pop('toWeek')

    for k, v in table.items():
        # 收集要删除的元素的索引
        to_remove = [i for i, e in enumerate(v) if len(e) == 85]
        # 反向删除,以避免索引变化导致的问题
        for index in reversed(to_remove):
            v.pop(index)
        # 删除0
        for a in v:
            to_remove = [i for i, j in a.items() if j == 0 or j == 0.0]
            for index in reversed(to_remove):
                del a[index]
    del table['day']
    del table['Rows']

    return table[xq]

def main():
    xhx = "=========================="
    today = datetime.date.today()
    day_of_week = today.weekday()
    weekdays = ['xq1', 'xq2', 'xq3', 'xq4', 'xq5', 'xq6', 'xq0']
    today_weekday = weekdays[day_of_week]
    table = http(today_weekday)
    print('今日课表')
    print(xhx)
    if not table:
        print('今天没有课:)')
    else:
        for course in table:
            print(course['skSj'])
            print(course['skDd'])
            print(course['kcMc'])
            print(course['skJs'])
            print(xhx)


if __name__ == '__main__':
    main()
