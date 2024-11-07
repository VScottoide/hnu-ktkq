import json
import requests

userBindInfo = {
    "sign": "",
    "userType": "",
    "userCode": "",
    "unitCode": "",
    "userName": "",
    "syMc": "",
    "syBjMc": "",
    "dsZgh": "",
    "dsXm": "",
    "fdyZgh": "",
    "fdyXm": "",
    "bjMc": "",
    "zyMc": "",
    "xyMc": "",
}

#获取今日签到列表
def get_qd_list():
    url = "https://ktkq.hainanu.edu.cn/app/getQdKbList"
    headers = {
        "Host": "ktkq.hainanu.edu.cn",
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.52(0x18003426) NetType/4G Language/zh_CN",
        "Referer": "https://servicewechat.com/wxa1e3abcd201139a2/28/page-frame.html"
    }
    data = {
        "sign": userBindInfo["sign"],
        "userType": userBindInfo["userType"],
        "userCode": userBindInfo["userCode"],
        "unitCode": userBindInfo["unitCode"],
        "userName": userBindInfo["userName"],
        "roleCode": "0",
        "bm": "null",
        "xyMc": userBindInfo["xyMc"],
        "zy": userBindInfo["zyMc"],
        "bj": userBindInfo["bjMc"],
        "xsCc": "2",
        "scene": "1",
        "key": "1"
    }
    response = requests.post(url, headers=headers, data=data)
    data = json.loads(response.text)
    print(data['today']+' 今日课表')
    sorted(data['Rows'],key = lambda item:item['isDjj1'] )
    
    return data['Rows']

# 获取课程签到信息
def get_qd_info(qd_kc):
    url = "https://ktkq.hainanu.edu.cn/app/getXsQdInfo"
    headers = {
        "Host": "ktkq.hainanu.edu.cn",
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.52(0x18003426) NetType/4G Language/zh_CN",
        "Referer": "https://servicewechat.com/wxa1e3abcd201139a2/28/page-frame.html"
    }
    data = {
        "sign": userBindInfo["sign"],
        "userType": userBindInfo["userType"],
        "userCode": userBindInfo["userCode"],
        "unitCode": userBindInfo["unitCode"],
        "userName": userBindInfo["userName"],
        "xkKh": qd_kc['xkKh'],
        "qdRq": qd_kc['qdRq'],
        "xqj": qd_kc['xqj'],
        "djj": qd_kc['isDjj1'],
        "djz": qd_kc['djz'],
        "qdId": qd_kc['qdId'],
        "isFz": 0,
        "fzMc": '全部'
    }
    response = requests.post(url, headers=headers, data=data)
    data = json.loads(response.text)
    if data['Rows']['klHm']:
        print("当前课程签到码为：" + data['Rows']['klHm'])
    return data['Rows']

# 签到
def save_qd_info(info,qd_kc):
    # print(info)
    # print(qd_kc)
    url = "https://ktkq.hainanu.edu.cn/app/saveXsQdInfo"
    headers = {
        "Host": "ktkq.hainanu.edu.cn",
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.52(0x18003426) NetType/4G Language/zh_CN",
        "Referer": "https://servicewechat.com/wxa1e3abcd201139a2/28/page-frame.html"
    }
    data = {
        "sign": userBindInfo["sign"],
        "unitCode": userBindInfo["unitCode"],
        "userCode": userBindInfo["userCode"],
        "userName": userBindInfo["userName"],
        "syMc": userBindInfo["syMc"],
        "syBjMc": userBindInfo["syBjMc"],
        "dsZgh": userBindInfo["dsZgh"],
        "dsXm": userBindInfo["dsXm"],
        "fdyZgh": userBindInfo["fdyZgh"],
        "fdyXm": userBindInfo["fdyXm"],
        "bjMc": userBindInfo["bjMc"],
        "zyMc": userBindInfo["zyMc"],
        "xyMc": userBindInfo["xyMc"],
        "wzJd": info['wzJd'],
        "wzWd": info['wzWd'],
        "qdId": info['uniqueCode'],
        "xkKh": qd_kc['xkKh'],
        "skDd": qd_kc['skDd'],
        "xqj": qd_kc['xqj'],
        "djj": qd_kc['isDjj1'],
        "djz": qd_kc['djz'],
        "isFace": "undefined",
        "wzAcc": "62.42532468953859",#位置精度
        "bqMode": qd_kc['bqMode'],
        "isFz": qd_kc['isFz'],
        "fzMc": qd_kc['fzMc'],
        "djc": qd_kc['djc'],
        "qdJc": qd_kc['qdJc'],
        "kcMc": qd_kc['kcMc'],
        "jsXm": qd_kc['skJs'],
        "skCd": qd_kc['skCd']
    }
    response = requests.post(url, headers=headers, data=data)
    data = json.loads(response.text)
    print(data)

def main():
    # 获取签到列表
    qd_list = get_qd_list()
    # 从签到列表中获取需要签到的课程
    qd_kc = {}
    for i in range(len(qd_list)):
        print("================================")
        print(qd_list[i]["skSj"])
        print(qd_list[i]["skDd"])
        print('[' + qd_list[i]["kcMc"] +']  '+ qd_list[i]["qdQkMc"] + ',' + qd_list[i]["xsQdQkMc"])
        print(qd_list[i]["skJs"])
        if qd_list[i]["qdQkMc"] == '签到中' and qd_list[i]["xsQdQkMc"] == '未签':
            qd_kc = qd_list[i]
    print("================================")
    if not qd_kc:
        print('当前没有需要签到的课程')
        return

    # 获取需要签到的课程详情
    qd_info = get_qd_info(qd_kc)

    # 签到
    save_qd_info(qd_info,qd_kc)

if __name__ == '__main__':
    main()

