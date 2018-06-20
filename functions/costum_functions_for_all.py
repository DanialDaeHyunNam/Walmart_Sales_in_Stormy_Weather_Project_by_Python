
"""
    포함된 함수 정보
    sendSlackDm : slack 메시지 보내기
    saveDataFrameToCsv : 넘겨준 df를 filename + 년월일시간분 의 format으로 이루어진 이름의 파일로 생성해준다.
"""

from datetime import datetime
import json
import requests

def sendSlackDm(url, text):
    """
        Parameter :
            각자 받은 url을 넣어준다.
            text에는 보낼 글 내용
    """
    webhook_url = url
    slack_data = {'text': text}
    response = requests.post(
        webhook_url,
        data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'%(response.status_code, response.text)
    )

def saveDataFrameToCsv(df, fileName, idx = False):
    """
        넘겨준 df를 filename + 년월일시간분 의 format으로 이루어진 이름의 파일로 생성해준다.
        index를 True로 넘겨주면 저장할 때 아규먼트로 index=True를 넣어주게 된다.
    """
    fileName += "_" + datetime.now().strftime("%Y%m%d%H%M") + ".csv"
    return df.to_csv(fileName, index = idx)
