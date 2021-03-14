# 2021.03.04 고려 사항
# 1. 생산 능력: 제품을 쪼개기 : 2개 설비로...
# 2. 마스터 파일 관련: Goods 분류: 1.반자동, 2.로터리, 3.고주파, 4.수동, 5.874, 6.374 ===> 최소 조립품만은 [874,374] 구분???

# 2021.03.01 To Do List
# *. 생산 진도 관리: ppp_current
# 1. javascript: 조회 기간 제한: 사용자가 선택한 [fromDate]를 기준으로 해당월의 [1일]부터 [말일]까지 [1개월간]만의 자료로 제한.
#   ===> [sideBar.html] [월도] 표시 <태그> 추가...

# 1. ERP : 마스터 폐기품 원상 회복
# 2. 조립 라인 Machine.Language1,2,3,4 명칭 정리: 설비명만 기록, 제품명은 제외한다.
# 3. 그래프 Y 좌표 출발을 [0]부터...
# 4. 생산 실적 레전드 Sorting 한 후에 뿌리기...
# 5. 생산 실적 레전드 : 특정 제품 선택에서는 페이지 합이 잘 나옴, 특정 제품 선택 해제시에는 ???

# 1. 생산 능력 분석
#   1) 각 데이터윈도우의 Title : dw 이름 표시
#   2) 중국어 번역
#   3) 설비명을 [반자동] ===> [반자] 까지만 입력... 2글자만...
# 2. w_Machine
#   1) 중국어 번역
# 3. 공정별 전체 가동률
# 4. 설비별 생산 제품 현황 뿌리기.


# 2021.02.28 파워빌더는 처음 실행시, DB에 5개의 테이블을 만드는데, MySql 또는 MariaDB 사용시,
#            잘 생성이 안 되는 경우가 있다. 그냥 직접 만들어 준다.

# 2020.12.31 ??? 강두원
# 1. 내가 서버를 구동하기도 하고, 죽이기도 하는데, 그것은 어떻게 하나? 새로 구동해야 될 때가 있는데...
# 2. Python3 가상 환경이 아니라면... Python3 으로 구동을 하는데, 그게 어디있는지...
#    어떤 Python3.exe 환경으로 Project 생성했는지... 라이브러리를 계속 추가해야 되는데...
#    즉, django도 라이브러리인데, 어디에 설치를 했는지...



# - 웹 디버깅 ???
# - style_com.css 파일 안 먹네???
# - 웹싸이트를 오래 켜 두고, 다시 [새로 고침]하면 싸이트에서 [MSSQL] 접속 에러가 나네..
#   : 꼭 웹서버를 죽이고, 다시 웹서버를 가동해야, 브라우저에서 [새로 고침] ???

# 0. 웹서버가 죽으면... 어떠한 이유로든 웹서버가 죽으면... 누가 다시 실행해 주지???
# 1. 클릭해서 자료를 가져오고 있는 중에, 다시 클릭하면, 완전 서버 에러 발생하여, refresh도 안 먹네???
# 2. 자료를 전부 가져와서, javascript로 정리하는게 속도가 빠르겠지? 그라프 그리는 것도...
# 3. 세션과 쿠키: db 연결? 221.195.223.104에서 192.168.3.170로 전환시, 바로 적용이 안 되네???


# 2021.02.24 IDEA
# 1. Flutter, Django : OpenCV 육안 검사 앱.
# 2. 가족 가업 앱 : 정부 지원 연동.


# 2021.02.19 To Do List
############################################################## 생산 Volume - (음수.마이너스 수량) 확인...
# 0. 공정을 선택하면, 선택한 공정을 [navbar] 뿌려준다.
# 0. navbar 정리: navbar 숨기기: 마우스 그쪽으로 가면 보이기
# 20200115  1) 달력 넣기
#           2) 달을 선택하면, 해당 월의 1일부터 말일까지 자동 선택...
#   2) 공정 넣기
#   3) 제품 구분 넣기
#   4) 제품 넣기 ???
# 20200202 1. navbar CSS
# 20200126 2. pagination CSS
# 20200119 3. sidebar CSS
# 20200121 4. 월간 생산 목표 대비 실적 대비 불량 : 가동율 및 불량율
# 4-2. 년간 생산 목표 대비 실적 대비 불량 : 가동율 및 불량율
# 5. 생산 계획 대비 실적 : 달성율 : 이건 의미가 없나???
# 6. 차종 합계
# 2020103 7. 우클릭 : 전체 레전드 밑줄...
# 8. 모든 공정에 374, 874 구분...
# 9. table 추가 : 날짜별 차종별 생산 총괄표 : 맨 우측 컬럼에 개별 그라프 뿌리기...
#10. 화면 줄일 때, 스마트폰 화면에서, table 컬럼 조정 : [제품 규격,1,10], [양품량] : 요래 2개만 뿌리기.
#12. 생산 진도 관리 : (생산 계획량: 월간 계획 엑셀표 업로드) / (생산 실적 누계량) / 생산 잔량
#13. 안 해도 무방: 그라프에서 제품 선택시, 아래 표에서 해당 제품만 필터...


# 2020.11.02 체크 사항
# 1. 생산 실적 수량 확인: 정상 or Not: 목표 수량 초과 품목
# 2. 불량 수량 확인: ?%.지정 % 이상 발생 품목
# 3. 생산 품절 확인: 생산 진도 관리 표에서.
# 4. 인당 가동율
# 5. 설비당 가동율


# 2020.11.01 To Do List
# 20201130 1. 생산 실적 검색 기간 설정
# 20201209 2. 서버 데이터베이스 변경 : Ms Sql ===> MySql
# 20201215 3. 서버로 데이터 상시 전송 프로그램
# 20201229 4. process.html : 함수를 활용한 javascript 단에서 data 정리...


# # Semy colon's
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.contrib.auth.models import User
# from django.core.paginator import Paginator
# import json
# from django.http import JsonResponse
# from userpreferences.models import UserPreference

# from .api.sudokus import Sudoku

# import jsonify as jsonify
# from flask import Flask, render_template

from django.contrib import messages
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views import View
from .models import ProductionActual, Customer, GoodsMaster, Log, Count, Student, ProductionPerformance, Process
from django.db.models import Sum

from ppp.processor import getGlobal

from django.core import serializers
from django.views.generic.list import ListView
# from rest_app.models import Repository
from django.http.response import HttpResponse

from ppp.f_common import connectDB, connectRemoteDB, connectWebDB, test

import pyautogui
# import pyodbc
# import pymssql
import pandas as pd
import json
# import pandas.io.sql as pdsql  # 이것도 안 되네...
import numpy as np

import pytz

from datetime import time, date, datetime, timedelta
from django.utils import timezone
from dateutil import relativedelta
from collections import defaultdict

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # csrf_exempt 사용을 위해...
import re

from django.db import connection  # 테이블 존재 여부 확인용.
from django.db.models.functions import TruncMonth, TruncDate  # 일별, 월별 데이터 뽑기
from decimal import Decimal  # decimao('문자')를 넣어 줌에 특히 주의.

import locale
import ctypes

windll = ctypes.windll.kernel32
LANGUAGE_NO = windll.GetUserDefaultUILanguage()  # 1033, 1042 : int 숫자형...
LANGUAGE_CODE = locale.windows_locale[windll.GetUserDefaultUILanguage()]  # "en_US", "ko_KR" : 문자형
print("LANGUAGE_NO: ", LANGUAGE_NO, ", LANGUAGE_NO: ", LANGUAGE_NO)
print("type(LANGUAGE_NO): ", type(LANGUAGE_NO), ", type(LANGUAGE_NO): ", type(LANGUAGE_NO))

# for Debugging...
# rtnString = pyautogui.alert("현재 여기까지 실행되었음을 확인함!!!!!!!!!!!", "Info", "OK")
# rtnString = pyautogui.confirm(text="현재 여기까지 실행되었음을 확인함!!!!!!!!!!!", title="Info", buttons=["OK","Cancel"])
# rtnString = pyautogui.password('password', '비밀 번호를 입력하시오!')

# 1. 오늘 날짜, 이번달 첫 날, 다음달 첫 날, 이번달 마지막 날
today = timezone.now()
first_date_this_month = today.replace(day=1)
first_date_next_month = first_date_this_month + relativedelta.relativedelta(months=1)
print("today: ", today, ", first_date_next_month: ", first_date_next_month)

last_date_this_month = first_date_next_month - timedelta(days=1)
print("first_date_this_month: ", first_date_this_month, ", last_date_this_month: ", last_date_this_month)

period_days = (last_date_this_month - first_date_this_month).days + 1  # 한편 넣기...
print("period_days: ", period_days)

# 2021.02.06 Conclusion. 결론적으로, 사용자가 싸이트에 처음 접속하면, 여기 [Public] 부분을 먼저 실행하게 되는데,
# 그렇기 때문에, 여기서 [global] 변수로 세팅하면 안 되고,
# 사용자가 선택한 [fromDate, toDate, processCode] 값을 활용해야 하기 때문에,
# 우선은 각각의 함수 내부에서, 사용토록 한다???????

fromDateDefault = first_date_this_month.strftime("%Y-%m-%d")  #.split("-")
toDateDefault = last_date_this_month.strftime("%Y-%m-%d")  #.split("-")
print("fromDateDefault: ", fromDateDefault)
print("toDateDefault: ", toDateDefault)

# # 2021.01.20 Conclusion. urls.py 내부에,
# # path('process/<str:process_code>/', views.process_code, name='process-code'), 요래 [process_code] 함수가 있는
# # 상태에서, 아래와 같이 같은 이름으로 변수를 지정하면, 절대 안 된다. 변수 값을 얻지 못하네요... 함수명을 변경한다.
# process_code = "all"  # "all"  # "2100"

beInUse = 1  # 현재 사용중인 공정만...
CONNECTEDSERVER = False
CONNECTEDWEB = False


def productionPerformance(request):
    labels = []
    data = []
    queryset = []
    querysets = ProductionPerformance.objects.all()
    for j in len(querysets):
        code = querysets.code
        print("code: ", code)
        for i in range(1, 31):
            queryset[code] = ProductionPerformance.objects.values('code').annotate(d1=Sum('d' + str(i))).order_by('-code')
            print("queryset[code]: ", queryset[code])

    for i in range(1, 31):
        labels.append(labels['d' + str(i)])

    print("labels: ", labels)
    print("code: ", code)


def __getProductionPerformance(fromDate, toDate, ProcessCode):
    global msSqlServerDb, cursArrayServer, CONNECTEDSERVER, CONNECTEDWEB

    # print("view.py __getProductionPerformance type(fromDate): ", type(fromDate))
    # print("view.py __getProductionPerformance fromDate: ", fromDate)
    # print("view.py __getProductionPerformance toDate: ", toDate)
    # print("view.py __getProductionPerformance ProcessCode: ", ProcessCode)
    # print("view.py __getProductionPerformance timezone.now(): ", timezone.now())

    # 2021.02.18 Conclusion. 아래는 다음과 같은 에러가 발생한다. [workdate_lte] 요기 때문...
    # RuntimeWarning: DateTimeField ProductionActual.workdate received a naive datetime (2020-12-31 08:00:00) while time zone support is acti
    # ve.   RuntimeWarning)
    # qrProductionPerformance = ProductionActual.objects\
    #     .values('workdate', 'productionactualno', 'code', 'goodness', 'badness', 'daywork')\
    #     .filter(workdate_lte=fromDateDate, workdate__gte=toDateDate)

    if CONNECTEDWEB == False:
        # 2021.03.01 Conclusion. WEB DB 웹 Database 또한 [MS SQL]로 최종 결정되었다.
        # mySqlLocalDb, cursArray, cursDict, \
        # COMPANY_CODE, HOST3, USER3, PASS3, DBNAME3, BOUNCE_TIME, SLEEP_TIME, \
        # TIME_GAP, NIGHT_CLOSING_HHMMSS, DAY_CLOSING_HHMMSS, \
        # FORPRODUCINGORDERDATA, PROCESS, GROUPS, DESCRIPTION_TEXT, LINE_CODE, \
        # WORK_DATE, DAY_NIGHT, GOODS, CODE, CAVITY, GOODSRIGHT, CODERIGHT, CAVITYRIGHT, TO_WAREHOUSE, \
        # FACODE, PRODUCTSELECTION, PLCBIT, FRONTJISNO, TRADE, UI, BAUDRATE = connectWebDB()
        # if mySqlLocalDb:

        msSqlServerDb, cursArrayServer, HOST3, USER3, PASS3, DBNAME3 = connectWebDB()
        # print("__getProductionPerformance msSqlServerDb: ", msSqlServerDb, "type(msSqlServerDb):", type(msSqlServerDb))

        if msSqlServerDb:
            CONNECTEDWEB = True
            # print("3 __getProductionPerformance Database 연결 성공!")
        else:
            CONNECTEDWEB = False
            # print("3 __getProductionPerformance Database 연결을 확인하시오!")
        # print("__getProductionPerformance mySqlLocalDb: ", mySqlLocalDb, "type(mySqlLocalDb):", type(mySqlLocalDb))
        # print("__getProductionPerformance cursArray: ", cursArray, "type(cursArray):", type(cursArray))
        # print("__getProductionPerformance cursDict: ", cursDict, "type(cursDict):", type(cursDict))
        # print("__getProductionPerformance HOST3: ", HOST3, "type(HOST3):", type(HOST3))
        # print("__getProductionPerformance USER3: ", USER3, "type(USER3):", type(USER3))
        # print("__getProductionPerformance DBNAME3: ", DBNAME3, "type(DBNAME3):", type(DBNAME3))

    # 2021.02.21 Added. 자료를 가져오기 전에, 먼저 [Mp.작업 시간]을 찍어준다. [Mp] 컬럼은 임시로 사용한다.
    # 아니다... 그냥 [DataFrame]에서 처리하자...
    # sql = "UPDATE ProductionActual Set Mp = WorkTo - WorkFrom WHERE WorkDate BETWEEN %s AND %s ORDER BY WorkDate DESC "

    # 2021.03.21 Conclusion. 컬럼 정리.
    # 1. [pa.Ap = 생산 계획 수량] : 나중에 사용할 컬럼
    # 2. [pa.Mp = 생산 능력 수량] 컬럼은 [pa.WorkTo], [pa.WorkFrom], [t_Product.StandardTime] 컬럼으로 계산하여,
    #    [pandas.DataFrame]에서 [pa.Mp=volume] 컬럼에 정리.
    if str(processCode).lower() == 'all' or str(processCode) == '0000':
        print("1 __getProductionPerformance() Database 선택한 공정 코드가 없습니다. 전체 공정 자료를 뿌려줍니다.")
        values = (fromDate, toDate)
        # 2021.03.01 Conclusion. WEB DB 웹 Database 또한 [MS SQL]로 최종 결정되었다.
        # sql = "Select pa.WorkDate, pa.ProductionActualNo, pa.Code, ma.Step9, pa.Goodness, pa.Badness, pa.Mp, pa.Ap, pd.CodeTwins, " \
        #       "ma.Process, pr.Language2, pr.Language3, pa.Machine, pa.Groups, pa.WorkFrom, pa.WorkTo, pd.StandardTime "\
        #       "From ProductionActual AS pa LEFT JOIN GoodsMaster AS ma ON TRIM(pa.Code) = TRIM(ma.Code) " \
        #       "LEFT JOIN t_Product AS pd ON TRIM(ma.Code) = TRIM(pd.Code) " \
        #       "LEFT JOIN Process AS pr ON TRIM(ma.Process) = TRIM(pr.Code) " \
        #       "WHERE (pa.Goodness > 0 AND (pa.WorkDate BETWEEN %s AND %s)) ORDER BY pa.WorkDate DESC "
        sql = "Select pa.WorkDate, pa.ProductionActualNo, pa.Code, ma.Step9, pa.Goodness, pa.Badness, pa.Mp, pa.Ap, pd.CodeTwins, " \
              "ma.Process, pr.Language2, pr.Language3, pa.Machine, pa.Groups, pa.WorkFrom, pa.WorkTo, pd.StandardTime " \
              "From ProductionActual AS pa INNER JOIN GoodsMaster AS ma ON pa.Code = ma.Code " \
              "INNER JOIN Process AS pr ON ma.Process = pr.Code INNER JOIN t_Product AS pd ON ma.Code = pd.Code " \
              "WHERE pa.WorkDate BETWEEN %s AND %s AND pa.Goodness <> 0 ORDER BY pa.WorkDate DESC "
    else:
        print("__getProductionPerformance processCode: ", processCode, "에 대한 자료만 필터합니다.")
        values = (fromDate, toDate, processCode)
        # 2021.03.01 Conclusion. WEB DB 웹 Database 또한 [MS SQL]로 최종 결정되었다.
        # sql = "Select pa.WorkDate, pa.ProductionActualNo, pa.Code, ma.Step9, pa.Goodness, pa.Badness, pa.Mp, pa.Ap, pd.CodeTwins, " \
        #       "ma.Process, pr.Language2, pr.Language3, pa.Machine, pa.Groups, pa.WorkFrom, pa.WorkTo, pd.StandardTime "\
        #       "From ProductionActual AS pa LEFT JOIN GoodsMaster AS ma ON TRIM(pa.Code) = TRIM(ma.Code) " \
        #       "LEFT JOIN t_Product AS pd ON TRIM(ma.Code) = TRIM(pd.Code) " \
        #       "LEFT JOIN Process AS pr ON TRIM(ma.Process) = TRIM(pr.Code) " \
        #       "WHERE (pa.Goodness > 0 AND (pa.WorkDate BETWEEN %s AND %s) AND LEFT(ma.Process,4) = %s) ORDER BY pa.WorkDate DESC "
        sql = "Select pa.WorkDate, pa.ProductionActualNo, pa.Code, ma.Step9, pa.Goodness, pa.Badness, pa.Mp, pa.Ap, pd.CodeTwins," \
              "ma.Process, pr.Language2, pr.Language3, pa.Machine, pa.Groups, pa.WorkFrom, pa.WorkTo, pd.StandardTime " \
              "From ProductionActual AS pa INNER JOIN GoodsMaster AS ma ON pa.Code = ma.Code " \
              "INNER JOIN Process AS pr ON ma.Process = pr.Code INNER JOIN t_Product AS pd ON ma.Code = pd.Code " \
              "WHERE pa.WorkDate BETWEEN %s AND %s AND ma.Process = %s AND pa.Goodness <> 0 ORDER BY pa.WorkDate DESC "

    try:
        # print("view.py __getProductionPerformance 디버깅... 1")
        print("===========================================================================================")
        # print("sql: \n", sql)
        # print("values: ", values)
        print("__getProductionPerformance views.cursArrayServer() 접속을 시도합니다. 시간이 오래 걸릴수도 있습니다 잠시만 기다려 주세요...", values)
        print("===========================================================================================")
        cursArrayServer.execute(sql, values)  # 우측은 에러 발생함에 주의. cursArrayServer.execute(sql, from_date, to_date)
        print("view.py __getProductionPerformance 디버깅... 2")
    except:  # DB 연결을 한 번 더 시도...
        if CONNECTEDSERVER == False:
            msSqlServerDb, cursArrayServer, HOST3, USER3, PASS3, DBNAME3 = connectWebDB()
            if msSqlServerDb:
                CONNECTEDWEB = True
                print("3 __getProductionPerformance Database 연결 성공!")
            else:
                CONNECTEDWEB = False
                print("3 __getProductionPerformance Database 연결을 확인하시오!")
            # print("__getProductionPerformance msSqlServerDb: ", msSqlServerDb, "type(msSqlServerDb):", type(msSqlServerDb))
            # print("__getProductionPerformance cursArray: ", cursArrayServer, "type(cursArrayServer):", type(cursArrayServer))
            # print("__getProductionPerformance cursDict: ", cursDict, "type(cursDict):", type(cursDict))
            # print("__getProductionPerformance HOST3: ", HOST3, "type(HOST3):", type(HOST3))
            # print("__getProductionPerformance USER3: ", USER3, "type(USER3):", type(USER3))
            # print("__getProductionPerformance DBNAME3: ", DBNAME3, "type(DBNAME3):", type(DBNAME3))

        # print("view.py __getProductionPerformance 디버깅... 1-1")
        # print("sql: \n", sql)
        # print("__getProductionPerformance values: ", values)
        if values == '':
            cursArrayServer.execute(sql)  # 우측은 에러 발생함에 주의. cursArrayServer.execute(sql, from_date, to_date)
        else:
            cursArrayServer.execute(sql, values)  # 우측은 에러 발생함에 주의. cursArrayServer.execute(sql, from_date, to_date)
        # print("view.py __getProductionPerformance 디버깅... 2-1")

    try:
        CONNECTEDSERVER = True
        # print("view.py __getProductionPerformance 디버깅... 3")
        sqlQuerySets = cursArrayServer.fetchall()  # Dictionary based cursor, 선택한 "로우"가 1개 이상일 때.
        # print("view.py __getProductionPerformance 디버깅... 4")
        # print("sqlQuerySets: ", sqlQuerySets)
        # print("type(sqlQuerySets): ", type(sqlQuerySets))
        # for i, data in enumerate(sqlQuerySets):
        #     if i == 11314:
        #         print("i: ", i, ", data: ", data)

        dfSets = pd.DataFrame(sqlQuerySets)  # <class 'pandas.core.frame.DataFrame'>
        # print("view.py __getProductionPerformance dfSets: \n", dfSets)
        # print("view.py __getProductionPerformance type(dfSets): ", type(dfSets))
        # print("view.py __getProductionPerformance len(dfSets): ", len(dfSets))
        # print("view.py __pp_data_period_process 디버깅... 6")
        # print("\n\n")

        # 2021.02.06 Added. 빈 dfSets 확인.
        if len(dfSets) == 0:  # len(dfSets.index) == 0: 또는 dfSets.shape[0] == 0: 같은 구문이다.
            print("__getProductionPerformance 조건에 맞는 자료가 없습니다. 다시 확인하시오!")
        else:
            # 2021.02.21 Conclusion. ProductionActual.Mp 컬럼인 생산 능력 수량 ['volumn'] 값은, DataFrame에서 추가한다.
            # 아니다... 여기서 가져오고, [DataFrame]에서는 그 값을 정리만 한다.
            dfSets.columns = ['workdate', 'productionactualno', 'code', 'step9', 'goodness', 'badness', 'volume', 'schedule', 'codetwins',
                          'process', 'process_kor', 'process_loc', 'machine', 'groups', 'workfrom', 'workto', 'standardtime']
            # dfSets.columns = ['workdate', 'productionactualno', 'code', 'step9', 'goodness', 'badness', 'schedule',
            #               'process', 'process_kor', 'process_loc', 'machine', 'groups', 'workfrom', 'workto', 'standardtime']
            # print("컬럼명 변경 후 dfSets: \n", dfSets)

            # 2021.01.31 Added. workdate.작업일자 컬럼은 TimeStamp.시간 정보는 전혀 필요가 없기에, [문자형 타입]으로 변환...
            dfSets['workdate'] = dfSets['workdate'].astype(str)
            # print("__getProductionPerformance::type(dfSets): ", type(dfSets))
            # print("__getProductionPerformance::len(dfSets): ", len(dfSets))
            # print("__getProductionPerformance::dfSets: \n", dfSets)

            # print("view.py __getProductionPerformance 디버깅... 7")
            # dfSets['codespec'] = dfSets['code'] + " " + dfSets['step9']
            # print("__getProductionPerformance codespec 추가 후 dfSets: \n", dfSets)
            # print("view.py __getProductionPerformance 디버깅... 8")

            if LANGUAGE_NO == 1042:
                dfSets['processinfo'] = dfSets['process'] + " " + dfSets['process_kor']
            else:
                dfSets['processinfo'] = dfSets['process'] + " " + dfSets['process_loc']
            # print("__getProductionPerformance processinfo 추가 후 dfSets: \n", dfSets)
            # print("view.py __getProductionPerformance 디버깅... 8")

            # if len(dfSets) > 0:
            #     if ProcessCode == 'all':
            #         processInfoCurrent = 'ALL'
            #     else:
            #         processInfoCurrent = dfSets.at[0, 'processinfo']
            # print("__getProductionPerformance processInfoCurrent 추가 후 processInfoCurrent: \n", processInfoCurrent)

    except:
        CONNECTEDSERVER = False
        # # [dfSets = pd.DataFrame()] 이 문장을 실행하지 않더라도,
        # # 아래 [if dfSets is None and isinstance(dfSets, pd.DataFrame) and not dfSets.empty] 여기서 걸러진다.
        # # 그렇지만, 프로그램 오류 없이 걸러지기 위해, retrun 값 [dfSets] 변수는 정의해 준다.
        # dfSets = ""
        # dfSets = pd.DataFrame(np.nan, index=[0, 1, 2, 3], columns=['A'])
        dfSets = pd.DataFrame(columns=['index', 'number'])
        # dfSets = pd.DataFrame(index=range(0, 0), columns=['index', 'number'])
        print("경고, __getProductionPerformance [callMainData]에서 치명적 에러가 발생하였습니다. 관리자에게 문의하시오!")
        print("경고 dfSets: \n", dfSets)

    return sqlQuerySets, dfSets


def __getProductionCapacity(fromDate, toDate, ProcessCode):
    global msSqlServerDb, cursArrayServer, CONNECTEDSERVER, CONNECTEDWEB

    print("view.py __getProductionCapacity type(fromDate): ", type(fromDate))
    print("view.py __getProductionCapacity fromDate: ", fromDate)
    print("view.py __getProductionCapacity toDate: ", toDate)
    # print("view.py __getProductionCapacity ProcessCode: ", ProcessCode)
    # print("view.py __getProductionCapacity timezone.now(): ", timezone.now())

    year = fromDate[:4]
    month = fromDate[5:7]
    # serial = "0001"  # 사업 계획 Revision은 필요 없고, 그냥 [달]을 4자리로 하여 처리...
    revision = year + "00" + month
    print("view.py __getProductionCapacity year: ", year)
    print("view.py __getProductionCapacity month: ", month)
    print("view.py __getProductionCapacity revision: ", revision)

    # 해당 월도의 마지막 날짜를 찾는다.
    maxDate = getMaxDate(year, month)
    print("__getProductionCapacity 55 maxDate: ", maxDate)

    # [ppp_current.생산 Capa 관리]는 반드시 1개월 단위로만 관리해야 하므로, 기간의 종료 날짜를 이번달 말일로 새로 넣어준다.
    toDate = datetime.strptime(year + "-" + month + "-" + maxDate, "%Y-%m-%d")

    if CONNECTEDWEB == False:
        msSqlServerDb, cursArrayServer, HOST3, USER3, PASS3, DBNAME3 = connectWebDB()
        # print(" msSqlServerDb: ", msSqlServerDb, "type(msSqlServerDb):", type(msSqlServerDb))

        if msSqlServerDb:
            CONNECTEDWEB = True
            print("3 __getProductionCapacity Database 연결 성공!")
        else:
            CONNECTEDWEB = False
            print("3 __getProductionCapacity Database 연결을 확인하시오!")
    if str(processCode).lower() == 'all' or str(processCode) == '0000':
        # print("1 __getProductionCapacity() Database 선택한 공정 코드가 없습니다. 전체 공정 자료를 뿌려줍니다.")
        # mc.Language2: 설비명 korea
        # mc.Language3: 설비명 local
        # fo.Duduction: 근무 일수: 해당 월 + 해당 공정
        # fo.Coefficient: Cycle Time (초)
        # fo.PoBal: 소요 일수
        # fo.Minimum: 소요 시간
        # fo.Tmp: UPH
        # fo.ClassMonth: 생산 라인 코드 3자리: String, (LineCode.라인 번호는 중복이 있어 사용 불가)
        # ma.Good2: 구분: 용접이면, 1.로타리, 2.반자동, 3.고주파, 4.수동
        # fo.WorkBaseDay: UPD
        # fo.Stock: 월초 재고: 월말 재고 조사 수량을 차월초 재고로 등록...
        # fo.Dpt: 생산 계획 합
        # fo.Dst: 생산 계획 잔량 합
        # fo.Nmt: 달성률
        # fo.Nst: 현재 재고

        # dfSets.columns = ['revision', 'code', 'step9', 'workingdays', 'ct', 'needsday', 'needshour', 'uph',
        #               'division', 'upd', 'stockfirst', 'dpt', 'dft', 'dmt', 'dst', 'npt', 'nft', 'nst',
        #               'machine', 'machine_kor', 'machine_loc', 'process', 'process_kor', 'process_loc']

        values = (revision)
        sql = "Select fo.Revision, fo.Code, ma.Step9, fo.Deduction, fo.Coefficient, fo.PoBal, fo.Minimum, fo.Tmp, " \
              "ma.Goods2, fo.WorkBaseDay, fo.Stock, fo.Dpt, fo.Dft, fo.Dmt, fo.Dst, fo.Npt, fo.Nft, fo.Nst, " \
              "fo.ClassMonth, mc.Language2, mc.Language3, ma.Process, pr.Language2, pr.Language3 " \
              "From ForecastHistoryDay AS fo INNER JOIN GoodsMaster AS ma ON fo.Code = ma.Code AND fo.Dpt <> 0 " \
              "INNER JOIN Process AS pr ON ma.Process = pr.Code  INNER JOIN Machine AS mc ON fo.ClassMonth = mc.Code " \
              "WHERE fo.Revision = %s " \
              "ORDER BY fo.Revision Desc, ma.Process Desc, fo.ClassMonth, ma.Step9 "

    else:
        # print("__getProductionCapacity processCode: ", processCode, "에 대한 자료만 필터합니다.")
        values = (revision, processCode)
        sql = "Select fo.Revision, fo.Code, ma.Step9, fo.Deduction, fo.Coefficient, fo.PoBal, fo.Minimum, fo.Tmp, " \
              "ma.Goods2, fo.WorkBaseDay, fo.Stock, fo.Dpt, fo.Dft, fo.Dmt, fo.Dst, fo.Npt, fo.Nft, fo.Nst, " \
              "fo.ClassMonth, mc.Language2, mc.Language3, ma.Process, pr.Language2, pr.Language3 " \
              "From ForecastHistoryDay AS fo INNER JOIN GoodsMaster AS ma ON fo.Code = ma.Code " \
              "INNER JOIN Process AS pr ON ma.Process = pr.Code INNER JOIN Machine AS mc ON fo.ClassMonth = mc.Code " \
              "WHERE fo.Revision = %s AND ma.Process = %s AND fo.Dpt <> 0 " \
              "ORDER BY fo.Revision Desc, ma.Process Desc, fo.ClassMonth, ma.Step9 "

    try:
        print("===========================================================================================")
        print("__getProductionCapacity views.cursArrayServer() 접속을 시도합니다. 시간이 오래 걸릴수도 있습니다 잠시만 기다려 주세요...", values)
        print("===========================================================================================")
        cursArrayServer.execute(sql, values)  # 우측은 에러 발생함에 주의. cursArrayServer.execute(sql, from_date, to_date)
    except:  # DB 연결을 한 번 더 시도...
        if CONNECTEDSERVER == False:
            msSqlServerDb, cursArrayServer, HOST3, USER3, PASS3, DBNAME3 = connectWebDB()
            if msSqlServerDb:
                CONNECTEDWEB = True
                print("3 __getProductionCapacity Database 연결 성공!")
            else:
                CONNECTEDWEB = False
                print("3 __getProductionCapacity Database 연결을 확인하시오!")

        # print("view.py __getProductionCapacity 디버깅... 1-1")
        if values == '':
            cursArrayServer.execute(sql)  # 우측은 에러 발생함에 주의. cursArrayServer.execute(sql, from_date, to_date)
        else:
            cursArrayServer.execute(sql, values)  # 우측은 에러 발생함에 주의. cursArrayServer.execute(sql, from_date, to_date)
        # print("view.py __getProductionCapacity 디버깅... 2-1")

    try:
        CONNECTEDSERVER = True
        # print("view.py __getProductionCapacity 디버깅... 3")
        sqlQuerySets = cursArrayServer.fetchall()  # Dictionary based cursor, 선택한 "로우"가 1개 이상일 때.

        dfSets = pd.DataFrame(sqlQuerySets)  # <class 'pandas.core.frame.DataFrame'>
        # print("view.py __getProductionCapacity dfSets: \n", dfSets)
        # print("view.py __getProductionCapacity type(dfSets): ", type(dfSets))
        # print("view.py __getProductionCapacity len(dfSets): ", len(dfSets))
        # print("view.py __getProductionCapacity 디버깅... 6")

        # 2021.02.06 Added. 빈 df 확인.
        # if len(dfSets) == 0:  # len(dfSets.index) == 0: 또는 dfSets.shape[0] == 0: 같은 구문이다.
        #     print("__getProductionCapacity 조건에 맞는 자료가 없습니다. 다시 확인하시오!")
        #     dfSets.columns = ['revision', 'code', 'step9', 'workingdays', 'ct', 'needsday', 'needshour', 'uph',
        #                       'division', 'upd', 'stockfirst', 'dpt', 'dft', 'dmt', 'dst', 'npt', 'nft', 'nst',
        #                       'machine', 'machine_kor', 'machine_loc', 'process', 'process_kor', 'process_loc']
        # else:
        dfSets.columns = ['revision', 'code', 'step9', 'workingdays', 'ct', 'needsday', 'needshour', 'uph',
                          'division', 'upd', 'stockfirst', 'dpt', 'dft', 'dmt', 'dst', 'npt', 'nft', 'nst',
                          'machine', 'machine_kor', 'machine_loc', 'process', 'process_kor', 'process_loc']
        # print("컬럼명 변경 후 __getProductionCapacity dfSets: \n", dfSets)

        # print("view.py __getProductionCapacity 디버깅... 7")
        # dfSets['codespec'] = dfSets['code'] + " " + dfSets['step9']
        # print("__getProductionCapacity codespec 추가 후 dfSets: \n", dfSets)
        # print("view.py __getProductionCapacity 디버깅... 8")

        if LANGUAGE_NO == 1042:
            dfSets['processinfo'] = dfSets['process'] + " " + dfSets['process_kor']
        else:
            dfSets['processinfo'] = dfSets['process'] + " " + dfSets['process_loc']
        # print("__getProductionCapacity processinfo 추가 후 dfSets: \n", dfSets)
        # print("view.py __getProductionCapacity 디버깅... 8")

        # if len(dfSets) > 0:
        #     if ProcessCode == 'all':
        #         processInfoCurrent = 'ALL'
        #     else:
        #         processInfoCurrent = dfSets.at[0, 'processinfo']
        # print("__getProductionCapacity processInfoCurrent 추가 후 processInfoCurrent: \n", processInfoCurrent)

    except:
        CONNECTEDSERVER = False
        # dfSets = pd.DataFrame(np.nan, index=[0, 1, 2, 3], columns=['A'])
        dfSets = pd.DataFrame(columns=['index', 'number'])
        # dfSets = pd.DataFrame(index=range(0, 0), columns=['index', 'number'])
        print("경고, __getProductionCapacity processinfo dfSets: \n", dfSets)
        print("경고, __getProductionCapacity [callMainData]에서 치명적 에러가 발생하였습니다. 관리자에게 문의하시오!")

    return sqlQuerySets, dfSets, revision, toDate


def __getProductionCurrent(fromDate, toDate, ProcessCode):
    global msSqlServerDb, cursArrayServer, CONNECTEDSERVER, CONNECTEDWEB

    year = fromDate[:4]
    month = fromDate[5:7]
    # serial = "0001"  # 사업 계획 Revision은 필요 없고, 그냥 [달]을 4자리로 하여 처리...
    revision = year + "00" + month
    # print("view.py     # print("view.py __getProductionCurrent month: ", month) revision: ", revision)

    # 해당 월도의 마지막 날짜를 찾는다.
    maxDate = getMaxDate(year, month)
    print("__getProductionCurrent 55 maxDate: ", maxDate)

    # [ppp_current.생산 진도 관리]는 반드시 1개월 단위로만 관리해야 하므로, 기간의 종료 날짜를 이번달 말일로 새로 넣어준다.
    toDate = datetime.strptime(year + "-" + month + "-" + maxDate, "%Y-%m-%d")

    if CONNECTEDWEB == False:
        msSqlServerDb, cursArrayServer, HOST3, USER3, PASS3, DBNAME3 = connectWebDB()
        # print("__getProductionCurrent msSqlServerDb: ", msSqlServerDb, "type(msSqlServerDb):", type(msSqlServerDb))

        if msSqlServerDb:
            CONNECTEDWEB = True
            print("3 __getProductionCurrent Database 연결 성공!")
        else:
            CONNECTEDWEB = False
            print("3 __getProductionCurrent Database 연결을 확인하시오!")

    if str(processCode).lower() == 'all' or str(processCode) == '0000':
        print("1 __getProductionCurrent() Database 선택한 공정 코드가 없습니다. 전체 공정 자료를 뿌려줍니다.")

        # 1. fo.Revision: 관리 번호
        # 2. fo.Code: 제품 코드
        # mc.Language2: 설비명 korea
        # mc.Language3: 설비명 local
        # fo.Duduction: 근무 일수: 해당 월 + 해당 공정
        # 3. fo.Coefficient: Cycle Time (초)
        # 4. fo.PoBal: 소요 일수
        # fo.Minimum: 소요 시간
        # fo.Tmp: UPH
        # 5. ma.Goods2: 구분: 용접이면, 1.로타리, 2.반자동, 3.고주파, 4.수동, 조립이면, 1.?, 2.?
        # fo.WorkBaseDay: UPD
        # 6. fo.Stock: 월초 재고: 월말 재고 조사 수량을 차월초 재고로 등록...
        # 7. fo.Dpt: 생산 계획 합
        # 8. fo.Dst: 생산 계획 잔량 합
        # 9. fo.Nmt: 달성률
        # 10. fo.Nst: 현재 재고
        # fo.ClassMonth: 생산 라인 코드 3자리: String, (LineCode.라인 번호는 중복이 있어 사용 불가)
        # 11. fo.Dm01 - Dm31: 생산 실적 수량
        # 12. fo.Nf01 - Nf31: 생산 실적 누계 수량

        # dfSets.columns = ['revision', 'code', 'step9', 'ct', 'needsday',
        #               'division', 'stockfirst', 'dpt', 'dft', 'dmt', 'dst', 'npt', 'nft', 'nst',
        #               'machine', 'machine_kor', 'machine_loc', 'process', 'process_kor', 'process_loc']
        #
        # values = (revision)
        # sql = "Select fo.Revision, fo.Code, ma.Step9, fo.Coefficient, fo.PoBal, " \
        #       "ma.Goods2, fo.Stock, fo.Dpt, fo.Dft, fo.Dmt, fo.Dst, fo.Npt, fo.Nft, fo.Nst, " \
        #       "fo.ClassMonth, mc.Language2, mc.Language3, ma.Process, pr.Language2, pr.Language3, " \
        #       "fo.Dm1, fo.Dm2, fo.Dm3, fo.Dm4, fo.Dm5, fo.Dm6, fo.Dm7, fo.Dm8, fo.Dm9, fo.Dm10, " \
        #       "fo.Dm11, fo.Dm12, fo.Dm13, fo.Dm14, fo.Dm15, fo.Dm16, fo.Dm17, fo.Dm18, fo.Dm19, fo.Dm20, " \
        #       "fo.Dm21, fo.Dm22, fo.Dm23, fo.Dm24, fo.Dm25, fo.Dm26, fo.Dm27, fo.Dm28, fo.Dm29, fo.Dm30, fo.Dm31, " \
        #       "fo.Nf1, fo.Nf2, fo.Nf3, fo.Nf4, fo.Nf5, fo.Nf6, fo.Nf7, fo.Nf8, fo.Nf9, fo.Nf10, " \
        #       "fo.Nf11, fo.Nf12, fo.Nf13, fo.Nf14, fo.Nf15, fo.Nf16, fo.Nf17, fo.Nf18, fo.Nf19, fo.Nf20, " \
        #       " fo.Nf21, fo.Nf22, fo.Nf23, fo.Nf24, fo.Nf25, fo.Nf26, fo.Nf27, fo.Nf28, fo.Nf29, fo.Nf30, fo.Nf31 " \
        #       "From ForecastHistoryDay AS fo INNER JOIN GoodsMaster AS ma ON fo.Code = ma.Code " \
        #       "INNER JOIN Process AS pr ON ma.Process = pr.Code  INNER JOIN Machine AS mc ON fo.ClassMonth = mc.Code " \
        #       "WHERE fo.Revision = %s " \
        #       "ORDER BY fo.Revision Desc, ma.Process Desc, fo.ClassMonth, ma.Step9 "

        # 2021.032.08 Conclusion. 위의 방식은 문제가 좀 있다. 생산 실적 등록을 완료하였음에도,
        # 생산 능력에서 [실적 자료] 버튼을 클릭하지 않으면, ForecastHistoryDay.NFxx 컬럼이 정리가 안 되어,
        # [생산 진도 관리]를 볼 수가 없다.
        # 그러므로 ProductionActual.생산 실적 자료를 직접 가져와서 처리한다.
        values = (fromDate, toDate)
        sql = "Select pa.WorkDate, pa.ProductionActualNo, pa.Code, ma.Step9, pa.Goodness, pa.Badness, pa.Mp, pa.Ap, pd.CodeTwins, " \
              "ma.Process, pr.Language2, pr.Language3, pa.Machine, pa.Groups, pa.WorkFrom, pa.WorkTo, pd.StandardTime " \
              "From ProductionActual AS pa INNER JOIN GoodsMaster AS ma ON pa.Code = ma.Code AND pa.Goodness <> 0 " \
              "INNER JOIN Process AS pr ON ma.Process = pr.Code INNER JOIN t_Product AS pd ON ma.Code = pd.Code " \
              "WHERE pa.WorkDate BETWEEN %s AND %s ORDER BY pa.WorkDate DESC "
    else:
        print("__getProductionCurrent processCode: ", processCode, "에 대한 자료만 필터합니다.")
        values = (fromDate, toDate, processCode)
        sql = "Select pa.WorkDate, pa.ProductionActualNo, pa.Code, ma.Step9, pa.Goodness, pa.Badness, pa.Mp, pa.Ap, pd.CodeTwins," \
              "ma.Process, pr.Language2, pr.Language3, pa.Machine, pa.Groups, pa.WorkFrom, pa.WorkTo, pd.StandardTime " \
              "From ProductionActual AS pa INNER JOIN GoodsMaster AS ma ON pa.Code = ma.Code AND pa.Goodness <> 0 " \
              "INNER JOIN Process AS pr ON ma.Process = pr.Code INNER JOIN t_Product AS pd ON ma.Code = pd.Code " \
              "WHERE pa.WorkDate BETWEEN %s AND %s AND ma.Process = %s ORDER BY pa.WorkDate DESC "

        # values = (revision, processCode)
        # sql = "Select fo.Revision, fo.Code, ma.Step9, fo.Coefficient, fo.PoBal, " \
        #       "ma.Goods2, fo.Stock, fo.Dpt, fo.Dft, fo.Dmt, fo.Dst, fo.Npt, fo.Nft, fo.Nst, " \
        #       "fo.ClassMonth, mc.Language2, mc.Language3, ma.Process, pr.Language2, pr.Language3, " \
        #       "fo.Dm1, fo.Dm2, fo.Dm3, fo.Dm4, fo.Dm5, fo.Dm6, fo.Dm7, fo.Dm8, fo.Dm9, fo.Dm10, " \
        #       "fo.Dm11, fo.Dm12, fo.Dm13, fo.Dm14, fo.Dm15, fo.Dm16, fo.Dm17, fo.Dm18, fo.Dm19, fo.Dm20, " \
        #       "fo.Dm21, fo.Dm22, fo.Dm23, fo.Dm24, fo.Dm25, fo.Dm26, fo.Dm27, fo.Dm28, fo.Dm29, fo.Dm30, fo.Dm31, " \
        #       "fo.Nf1, fo.Nf2, fo.Nf3, fo.Nf4, fo.Nf5, fo.Nf6, fo.Nf7, fo.Nf8, fo.Nf9, fo.Nf10, " \
        #       "fo.Nf11, fo.Nf12, fo.Nf13, fo.Nf14, fo.Nf15, fo.Nf16, fo.Nf17, fo.Nf18, fo.Nf19, fo.Nf20, " \
        #       " fo.Nf21, fo.Nf22, fo.Nf23, fo.Nf24, fo.Nf25, fo.Nf26, fo.Nf27, fo.Nf28, fo.Nf29, fo.Nf30, fo.Nf31 " \
        #       "From ForecastHistoryDay AS fo INNER JOIN GoodsMaster AS ma ON fo.Code = ma.Code " \
        #       "INNER JOIN Process AS pr ON ma.Process = pr.Code  INNER JOIN Machine AS mc ON fo.ClassMonth = mc.Code " \
        #       "WHERE fo.Revision = %s AND ma.Process = %s " \
        #       "ORDER BY fo.Revision Desc, ma.Process Desc, fo.ClassMonth, ma.Step9 "

    try:
        print("===========================================================================================")
        print("__getProductionCurrent views.cursArrayServer() 접속을 시도합니다. 시간이 오래 걸릴수도 있습니다 잠시만 기다려 주세요...", values)
        print("===========================================================================================")
        cursArrayServer.execute(sql, values)  # 우측은 에러 발생함에 주의. cursArrayServer.execute(sql, from_date, to_date)
    except:  # DB 연결을 한 번 더 시도...
        if CONNECTEDSERVER == False:
            msSqlServerDb, cursArrayServer, HOST3, USER3, PASS3, DBNAME3 = connectWebDB()
            if msSqlServerDb:
                CONNECTEDWEB = True
                print("3 __getProductionCurrent Database 연결 성공!")
            else:
                CONNECTEDWEB = False
                print("3 __getProductionCurrent Database 연결을 확인하시오!")

        # print("view.py __getProductionCurrent 디버깅... 1-1")
        if values == '':
            cursArrayServer.execute(sql)  # 우측은 에러 발생함에 주의. cursArrayServer.execute(sql, from_date, to_date)
        else:
            cursArrayServer.execute(sql, values)  # 우측은 에러 발생함에 주의. cursArrayServer.execute(sql, from_date, to_date)
        # print("view.py __getProductionCurrent 디버깅... 2-1")

    try:
        CONNECTEDSERVER = True
        # print("view.py __getProductionCurrent 디버깅... 3")

        sqlQuerySets = cursArrayServer.fetchall()  # Dictionary based cursor, 선택한 "로우"가 1개 이상일 때.
        # print("view.py __getProductionCurrent sqlQuerySets: \n", sqlQuerySets)
        # print("view.py __getProductionCurrent type(sqlQuerySets): ", type(sqlQuerySets))
        # print("view.py __getProductionCurrent len(sqlQuerySets): ", len(sqlQuerySets))
        # print("view.py __getProductionCurrent 디버깅... 4")

        dfSets = pd.DataFrame(sqlQuerySets)  # <class 'pandas.core.frame.DataFrame'>
        # print("view.py __getProductionCurrent dfSets: \n", dfSets)
        # print("view.py __getProductionCurrent type(dfSets): ", type(dfSets))
        # print("view.py __getProductionCurrent len(dfSets): ", len(dfSets))
        # print("view.py __getProductionCurrent 디버깅... 6")

        # 2021.02.06 Added. 빈 dfSets 확인.
        # if len(dfSets) == 0:  # len(dfSets.index) == 0: 또는 dfSets.shape[0] == 0: 같은 구문이다.
        #     print("__getProductionCurrent 조건에 맞는 자료가 없습니다. 다시 확인하시오!")
        # else:
        #     # 2021.02.21 Conclusion. ProductionActual.Mp 컬럼인 생산 능력 수량 ['volumn'] 값은, DataFrame에서 추가한다.
        #     # 아니다... 여기서 가져오고, [DataFrame]에서는 그 값을 정리만 한다.
        dfSets.columns = ['workdate', 'productionactualno', 'code', 'step9', 'goodness', 'badness', 'volume',
                          'schedule', 'codetwins',
                          'process', 'process_kor', 'process_loc', 'machine', 'groups', 'workfrom', 'workto',
                          'standardtime']
        # print("__getProductionCurrent 컬럼명 변경 후 dfSets: \n", dfSets)

        # 2021.01.31 Added. workdate.작업일자 컬럼은 TimeStamp.시간 정보는 전혀 필요가 없기에, [문자형 타입]으로 변환...
        dfSets['workdate'] = dfSets['workdate'].astype(str)
        # print("__getProductionCurrent::type(dfSets): ", type(dfSets))
        # print("__getProductionCurrent::len(dfSets): ", len(dfSets))
        # print("__getProductionCurrent::dfSets: \n", dfSets)

        # print("view.py __getProductionCurrent 디버깅... 7")
        # dfSets['codespec'] = dfSets['code'] + " " + dfSets['step9']
        # print("__getProductionCurrent codespec 추가 후 dfSets: \n", dfSets)
        # print("view.py __getProductionCurrent 디버깅... 8")

        if LANGUAGE_NO == 1042:
            dfSets['processinfo'] = dfSets['process'] + " " + dfSets['process_kor']
        else:
            dfSets['processinfo'] = dfSets['process'] + " " + dfSets['process_loc']
        # print("__getProductionCurrent processinfo 추가 후 dfSets: \n", dfSets)
        # print("view.py __getProductionCurrent 디버깅... 8")

        # if len(dfSets) > 0:
        #     if ProcessCode == 'all':
        #         processInfoCurrent = 'ALL'
        #     else:
        #         processInfoCurrent = dfSets.at[0, 'processinfo']
        # print("__getProductionCurrent processInfoCurrent 추가 후 processInfoCurrent: \n", processInfoCurrent)

    except:
        CONNECTEDSERVER = False
        # dfSets = pd.DataFrame(np.nan, index=[0, 1, 2, 3], columns=['A'])
        # dfSets = pd.DataFrame(index=range(0, 0), columns=['index', 'number'])
        dfSets = pd.DataFrame(columns=['index', 'number'])
        print("경고, __getProductionCurrent processinfo dfSets: \n", dfSets)
        print("경고, __getProductionCurrent [callMainData]에서 치명적 에러가 발생하였습니다. 관리자에게 문의하시오!")

    return sqlQuerySets, dfSets, toDate


def __getProcess(beInUse):
    # qrProcess = Process.objects.filter(beInUse=beInUse)
    qrProcess = Process.objects.all().order_by('-code')  # 조립 공정이 맨 위로 오게, 내림차순(-code)으로 정렬...
    # print("__getProcess qrProcess: \n", qrProcess)

    processList = []  # 여기서는 의미가 없다. 다만, 이전 __process()와 동일한 파라메터를 맟추기 위함이다.
    for p in qrProcess:
        # print("__getProcess p[0]: ", p[0])  # [Queryset 자료]는, 이렇게 하면, 에러 난다. Queryset type = Object 임에 주의.
        # print("__getProcess p.code: ", p.code)
        # print("__getProcess p.language1: ", p.language1)
        # print("__getProcess p.language2: ", p.language2)
        # print("__getProcess p.language3: ", p.language3)
        processList.append(p)

    # print("__getProcess processList: ", processList)  # processList 리스트 내부에 각각의 공정 Obejct가 있다.

    # dfProcess = pd.DataFrame(qrProcess)  # Queryset 자료는 이런식으로 [DataFrame]을 만들 수 없다. 이것은 SQL 쿼리 결과 자료만 가능함에 주의.
    # print("__getProcess dfProcess: \n", dfProcess)
    #
    # if LANGUAGE_NO == 1042:
    #     if processCode == 'all':
    #         processList = [data for data in dfProcess]
    #     else:
    #         processList = [data for data in dfProcess if data[0] == processCode]
    # print("__getProcess processList: \n", processList)

    total_process_count = len(qrProcess)
    # print("process_selected total_process_count: ", total_process_count)

    return qrProcess, processList, total_process_count

    # dfProcess = pd.DataFrame(process)
    # print("__getProcess dfProcess: \n", dfProcess)

    # options = [{'label': x, 'value': x} for x in sorted(dfProcess.codespec.unique())],


@csrf_exempt
def home(request):
    global fromDate, toDate, processCode

    print("\n\n\n\n\nhome*******************************************************************************************")

    data = dict()
    data['is_valid_post'] = False
    data['is_valid_get'] = False

    if request.method == "POST":
        if len(request.POST) > 0:
            data['is_valid_post'] = True
            fromDate = request.POST['fromDate']
            toDate = request.POST['toDate']
            processCode = request.POST['processCode']
            print("views.py home() POST fromDate: ", fromDate)
            print("views.py home() POST toDate: ", toDate)
            print("views.py home() POST processCode: ", processCode)
        else:
            fromDate = fromDateDefault  # "2020.12.01"
            toDate = toDateDefault  # "2020.12.31"
            processCode = "all"  # "all"  # "2100"
            print("views.py home() POST 0 fromDate: ", fromDate)
            print("views.py home() POST 0 toDate: ", toDate)
            print("views.py home() POST 0 processCode: ", processCode)
    elif request.method == "GET":
        if len(request.GET) > 0:
            data['is_valid_get'] = True
            fromDate = request.GET['fromDate']
            toDate = request.GET['toDate']
            processCode = request.GET['processCode']
            print("views.py home() GET fromDate: ", fromDate)
            print("views.py home() GET toDate: ", toDate)
            print("views.py home() GET processCode: ", processCode)
        else:
            fromDate = fromDateDefault  # "2020.12.01"
            toDate = toDateDefault  # "2020.12.31"
            processCode = "all"  # "all"  # "2100"
            print("views.py home() GET 0 fromDate: ", fromDate)
            print("views.py home() GET 0 toDate: ", toDate)
            print("views.py home() GET 0 processCode: ", processCode)

        # print("views.py home() fromDate: ", fromDate)
        # print("views.py home() toDate: ", toDate)
        # print("views.py home() processCode: ", processCode)

    # qr_process, df_process = __process(beInUse)  # Process.objects.get(code=process_code_selected)
    qrProcess, processList,  total_process_count = __getProcess(beInUse)  # Process.objects.get(code=process_code_selected)

    # print("home qrProcess: ", qrProcess)
    # print("home processList: ", processList)
    # print("home total_process_count: ", total_process_count)

    # sqlQuerySets, dfSets = __pp_data_period_process(from_date, to_date, process_code)
    # sqlQuerySets, dfSets = __pp_data_period_process(fromDate, toDate, processCode)

    sqlQuerySets, dfSets = __getProductionPerformance(fromDate, toDate, processCode)
    # sqlQuerySets, dfSets = __getProductionPerformance(fromDate, toDate, processCode)

    # 2021.02.06 Added. 빈 dfSets 확인.
    if len(sqlQuerySets) == 0:  # len(dfSets.index) == 0: 또는 dfSets.shape[0] == 0: 같은 구문이다.
        print("views.py home 조건에 맞는 자료가 없습니다. 다시 확인하시오!")
        print("views.py home 현재 자료를 정리하지 못 했습니다. 관리자에게 문의하시오!", fromDate, " ", toDate, " ", processCode)
        print("views.py home 해당 자료가 전혀 없습니다!")
        # context = {'process': process, 'ppData': [], 'total_pp_data_count': 0,
        #            'sqlQuerySets': sqlQuerySets, 'LANGUAGE_NO': LANGUAGE_NO}
        context = {"qrProcess": qrProcess, "products": [], "productsCount": 0,
                   "ppDataPeriodProcessList": [], "ppDataPeriodProcessList2": [],
                   "sqlQuerySets": sqlQuerySets,
                   'fromDate': fromDate, 'toDate': toDate, 'processCode': processCode,
                   "LANGUAGE_NO": LANGUAGE_NO, "goodnessTotal": 0, "volumesTotal": 0}
        return render(request, 'ppp/index.html', context)
        # return redirect("home")

    ppDataPeriodProcessList, products, productsCount, ppDataPeriod, ppDataPeriodProcessList2, \
    goodnessTotal, volumesTotal = makingProduction(sqlQuerySets, dfSets)
    # print("home::type(ppDataPeriod): ", type(ppDataPeriod))
    # print("home::ppDataPeriod: \n", ppDataPeriod)
    # print("home::type(process): ", type(process))
    # print("home::process: \n", process)
    # print("home::type(rsDictSum): ", type(ppData))
    # print("home::rsDictSum: \n", ppData)
    # print("home::type(rsDictSum): ", type(rsDictSum))
    # print("home::rsDictSum: \n", rsDictSum)
    # print("home::type(rsListSum): ", type(rsListSum))
    # print("home::rsListSum: \n", rsListSum)
    # print("home::type(rsTupleSum): ", type(rsTupleSum))
    # print("home::rsTupleSum: \n", rsTupleSum)
    # print("home::type(sqlQuerySets): ", type(sqlQuerySets))
    # print("home::sqlQuerySets: \n", sqlQuerySets)

    # windll = ctypes.windll.kernel32
    # LANGUAGE_NO = windll.GetUserDefaultUILanguage()  # 1033, 1042
    # LANGUAGE_CODE = locale.windows_locale[windll.GetUserDefaultUILanguage()]  # en_US, ko_KR
    # print("process_selected LANGUAGE_NO: ", LANGUAGE_NO, ", LANGUAGE_CODE: ", LANGUAGE_CODE)

    context = {"qrProcess": qrProcess, "products": products,
               "ppDataPeriodProcessList": ppDataPeriodProcessList, "ppDataPeriodProcessList2": ppDataPeriodProcessList2,
               "productsCount": productsCount, "sqlQuerySets": sqlQuerySets,
               "ppDataPeriod": ppDataPeriod, 'fromDate': fromDate, 'toDate': toDate, 'processCode': processCode,
               "LANGUAGE_NO": LANGUAGE_NO, "goodnessTotal": goodnessTotal, "volumesTotal": volumesTotal}
    print("views.py home() request: ", request)
    print("views.py home() request.POST: ", request.POST)
    print("views.py home() len(request.POST): ", len(request.POST))
    print("views.py home() request.method: ", request.method)
    print("views.py home() fromDate: ", fromDate)
    print("views.py home() toDate: ", toDate)
    print("views.py home() processCode: ", processCode)

    # return HttpResponse('Customer page')  # [127.0.0.1:8000/about]으로 연결 시, 바로 뿌려준다. ===> 아래 : path('about/', contact),
    return render(request, 'ppp/index.html', context)
    # return JsonResponse(render(request, 'ppp/process.html', context), safe=False)  # 여긴 에러 나네...

    # data['context'] = render_to_string("ppp/process.html", context, request=request)
    # return JsonResponse(data, safe=False)


# 2021.03.04 Added. 일단 [ppp_process.날짜별 기간]을 그대로...
# 여기서는 [월간] 단위로 1년의 기간을 뿌려준다. 굳이 1월부터 12월로 고정시킬 필요는 없다.
@csrf_exempt
def ppp_month(request):
    global fromDate, toDate, processCode

    print("\n\n\n\n\nhome*******************************************************************************************")

    data = dict()
    data['is_valid_post'] = False
    data['is_valid_get'] = False

    if request.method == "POST":
        if len(request.POST) > 0:
            data['is_valid_post'] = True
            fromDate = request.POST['fromDate']
            toDate = request.POST['toDate']
            processCode = request.POST['processCode']
            print("views.py ppp_month() POST fromDate: ", fromDate)
            print("views.py ppp_month() POST toDate: ", toDate)
            print("views.py ppp_month() POST processCode: ", processCode)
        else:
            fromDate = fromDateDefault  # "2020.12.01"
            toDate = toDateDefault  # "2020.12.31"
            processCode = "all"  # "all"  # "2100"
            print("views.py ppp_month() POST 0 fromDate: ", fromDate)
            print("views.py ppp_month() POST 0 toDate: ", toDate)
            print("views.py ppp_month() POST 0 processCode: ", processCode)
    elif request.method == "GET":
        if len(request.GET) > 0:
            data['is_valid_get'] = True
            fromDate = request.GET['fromDate']
            toDate = request.GET['toDate']
            processCode = request.GET['processCode']
            print("views.py ppp_month() GET fromDate: ", fromDate)
            print("views.py ppp_month() GET toDate: ", toDate)
            print("views.py ppp_month() GET processCode: ", processCode)
        else:
            fromDate = fromDateDefault  # "2020.12.01"
            toDate = toDateDefault  # "2020.12.31"
            processCode = "all"  # "all"  # "2100"
            print("views.py ppp_month() GET 0 fromDate: ", fromDate)
            print("views.py ppp_month() GET 0 toDate: ", toDate)
            print("views.py ppp_month() GET 0 processCode: ", processCode)

        # print("views.py ppp_month() fromDate: ", fromDate)
        # print("views.py ppp_month() toDate: ", toDate)
        # print("views.py ppp_month() processCode: ", processCode)

    # qr_process, df_process = __process(beInUse)  # Process.objects.get(code=process_code_selected)
    qrProcess, processList, total_process_count = __getProcess(
        beInUse)  # Process.objects.get(code=process_code_selected)

    print("ppp_month qrProcess: ", qrProcess)
    print("ppp_month processList: ", processList)
    print("ppp_month total_process_count: ", total_process_count)

    # sqlQuerySets, dfSets = __pp_data_period_process(from_date, to_date, process_code)
    # sqlQuerySets, dfSets = __pp_data_period_process(fromDate, toDate, processCode)

    sqlQuerySets, dfSets = __getProductionPerformance(fromDate, toDate, processCode)
    # sqlQuerySets, dfSets = __getProductionPerformance(fromDate, toDate, processCode)

    # 2021.02.06 Added. 빈 dfSets 확인.
    if len(sqlQuerySets) == 0:  # len(dfSets.index) == 0: 또는 dfSets.shape[0] == 0: 같은 구문이다.
        print("views.py ppp_month 조건에 맞는 자료가 없습니다. 다시 확인하시오!")
        print("views.py ppp_month 현재 자료를 정리하지 못 했습니다. 관리자에게 문의하시오!", fromDate, " ", toDate, " ", processCode)
        print("views.py ppp_month 해당 자료가 전혀 없습니다!")
        # context = {'process': process, 'ppData': [], 'total_pp_data_count': 0,
        #            'sqlQuerySets': sqlQuerySets, 'LANGUAGE_NO': LANGUAGE_NO}
        context = {"qrProcess": qrProcess, "products": [], "productsCount": 0,
                   "ppDataPeriodProcessList": [], "ppDataPeriodProcessList2": [],
                   "sqlQuerySets": sqlQuerySets,
                   'fromDate': fromDate, 'toDate': toDate, 'processCode': processCode,
                   "LANGUAGE_NO": LANGUAGE_NO, "goodnessTotal": 0, "volumesTotal": 0}
        return render(request, 'ppp/index.html', context)
        # return redirect("home")

    ppDataPeriodProcessList, products, productsCount, ppDataPeriod, ppDataPeriodProcessList2, \
    goodnessTotal, volumesTotal = makingProduction(sqlQuerySets, dfSets)
    # print("ppp_month::type(ppDataPeriod): ", type(ppDataPeriod))
    # print("ppp_month::ppDataPeriod: \n", ppDataPeriod)
    # print("ppp_month::type(process): ", type(process))
    # print("ppp_month::process: \n", process)
    # print("ppp_month::type(rsDictSum): ", type(ppData))
    # print("ppp_month::rsDictSum: \n", ppData)
    # print("ppp_month::type(rsDictSum): ", type(rsDictSum))
    # print("ppp_month::rsDictSum: \n", rsDictSum)
    # print("ppp_month::type(rsListSum): ", type(rsListSum))
    # print("ppp_month::rsListSum: \n", rsListSum)
    # print("ppp_month::type(rsTupleSum): ", type(rsTupleSum))
    # print("ppp_month::rsTupleSum: \n", rsTupleSum)
    # print("ppp_month::type(sqlQuerySets): ", type(sqlQuerySets))
    # print("ppp_month::sqlQuerySets: \n", sqlQuerySets)

    # windll = ctypes.windll.kernel32
    # LANGUAGE_NO = windll.GetUserDefaultUILanguage()  # 1033, 1042
    # LANGUAGE_CODE = locale.windows_locale[windll.GetUserDefaultUILanguage()]  # en_US, ko_KR
    # print("process_selected LANGUAGE_NO: ", LANGUAGE_NO, ", LANGUAGE_CODE: ", LANGUAGE_CODE)

    context = {"qrProcess": qrProcess, "products": products,
               "ppDataPeriodProcessList": ppDataPeriodProcessList, "ppDataPeriodProcessList2": ppDataPeriodProcessList2,
               "productsCount": productsCount, "sqlQuerySets": sqlQuerySets,
               "ppDataPeriod": ppDataPeriod, 'fromDate': fromDate, 'toDate': toDate, 'processCode': processCode,
               "LANGUAGE_NO": LANGUAGE_NO, "goodnessTotal": goodnessTotal, "volumesTotal": volumesTotal}
    print("views.py ppp_month() request: ", request)
    print("views.py ppp_month() request.POST: ", request.POST)
    print("views.py ppp_month() len(request.POST): ", len(request.POST))
    print("views.py ppp_month() request.method: ", request.method)
    print("views.py ppp_month() fromDate: ", fromDate)
    print("views.py ppp_month() toDate: ", toDate)
    print("views.py ppp_month() processCode: ", processCode)

    # return HttpResponse('Customer page')  # [127.0.0.1:8000/about]으로 연결 시, 바로 뿌려준다. ===> 아래 : path('about/', contact),
    return render(request, 'ppp/ppp_process.html', context)
    # return JsonResponse(render(request, 'ppp/process.html', context), safe=False)  # 여긴 에러 나네...

    # data['context'] = render_to_string("ppp/process.html", context, request=request)
    # return JsonResponse(data, safe=False)


@csrf_exempt
def ppp_process(request):
    global fromDate, toDate, processCode

    print("\n\n\n\n\nhome*******************************************************************************************")

    data = dict()
    data['is_valid_post'] = False
    data['is_valid_get'] = False

    if request.method == "POST":
        if len(request.POST) > 0:
            data['is_valid_post'] = True
            fromDate = request.POST['fromDate']
            toDate = request.POST['toDate']
            processCode = request.POST['processCode']
            print("views.py ppp_process() POST fromDate: ", fromDate)
            print("views.py ppp_process() POST toDate: ", toDate)
            print("views.py ppp_process() POST processCode: ", processCode)
        else:
            fromDate = fromDateDefault  # "2020.12.01"
            toDate = toDateDefault  # "2020.12.31"
            processCode = "all"  # "all"  # "2100"
            print("views.py ppp_process() POST 0 fromDate: ", fromDate)
            print("views.py ppp_process() POST 0 toDate: ", toDate)
            print("views.py ppp_process() POST 0 processCode: ", processCode)
    elif request.method == "GET":
        if len(request.GET) > 0:
            data['is_valid_get'] = True
            fromDate = request.GET['fromDate']
            toDate = request.GET['toDate']
            processCode = request.GET['processCode']
            print("views.py ppp_process() GET fromDate: ", fromDate)
            print("views.py ppp_process() GET toDate: ", toDate)
            print("views.py ppp_process() GET processCode: ", processCode)
        else:
            fromDate = fromDateDefault  # "2020.12.01"
            toDate = toDateDefault  # "2020.12.31"
            processCode = "all"  # "all"  # "2100"
            print("views.py ppp_process() GET 0 fromDate: ", fromDate)
            print("views.py ppp_process() GET 0 toDate: ", toDate)
            print("views.py ppp_process() GET 0 processCode: ", processCode)

        # print("views.py ppp_process() fromDate: ", fromDate)
        # print("views.py ppp_process() toDate: ", toDate)
        # print("views.py ppp_process() processCode: ", processCode)

    # qr_process, df_process = __process(beInUse)  # Process.objects.get(code=process_code_selected)
    qrProcess, processList,  total_process_count = __getProcess(beInUse)  # Process.objects.get(code=process_code_selected)

    # print("ppp_process qrProcess: ", qrProcess)
    # print("ppp_process processList: ", processList)
    # print("ppp_process total_process_count: ", total_process_count)

    # sqlQuerySets, dfSets = sqlQuerySets(from_date, to_date, process_code)
    # sqlQuerySets, dfSets = sqlQuerySets(fromDate, toDate, processCode)

    sqlQuerySets, dfSets = __getProductionPerformance(fromDate, toDate, processCode)
    # sqlQuerySets = __getProductionPerformance(fromDate, toDate, processCode)

    # 2021.02.06 Added. 빈 dfSets 확인.
    if len(sqlQuerySets) == 0:  # len(dfSets.index) == 0: 또는 dfSets.shape[0] == 0: 같은 구문이다.
        print("views.py ppp_process 조건에 맞는 자료가 없습니다. 다시 확인하시오!")
        print("views.py ppp_process 현재 자료를 정리하지 못 했습니다. 관리자에게 문의하시오!", fromDate, " ", toDate, " ", processCode)
        print("views.py ppp_process 해당 자료가 전혀 없습니다!")
        # context = {'process': process, 'ppData': [], 'total_pp_data_count': 0,
        #            'sqlQuerySets': sqlQuerySets, 'LANGUAGE_NO': LANGUAGE_NO}
        context = {"qrProcess": qrProcess, "products": [], "productsCount": 0,
                   "ppDataPeriodProcessList": [], "ppDataPeriodProcessList2": [],
                   "sqlQuerySets": sqlQuerySets,
                   'fromDate': fromDate, 'toDate': toDate, 'processCode': processCode,
                   "LANGUAGE_NO": LANGUAGE_NO, "goodnessTotal": 0, "volumesTotal": 0}
        return render(request, 'ppp/ppp_process.html', context)
        # return redirect("home")

    ppDataPeriodProcessList, products, productsCount, ppDataPeriod, ppDataPeriodProcessList2, \
    goodnessTotal, volumesTotal = makingProduction(sqlQuerySets, dfSets)
    # print("ppp_process::type(ppDataPeriod): ", type(ppDataPeriod))
    # print("ppp_process::ppDataPeriod: \n", ppDataPeriod)
    # print("ppp_process::type(process): ", type(process))
    # print("ppp_process::process: \n", process)
    # print("ppp_process::type(rsDictSum): ", type(ppData))
    # print("ppp_process::rsDictSum: \n", ppData)
    # print("ppp_process::type(rsDictSum): ", type(rsDictSum))
    # print("ppp_process::rsDictSum: \n", rsDictSum)
    # print("ppp_process::type(rsListSum): ", type(rsListSum))
    # print("ppp_process::rsListSum: \n", rsListSum)
    # print("ppp_process::type(rsTupleSum): ", type(rsTupleSum))
    # print("ppp_process::rsTupleSum: \n", rsTupleSum)
    # print("ppp_process::type(sqlQuerySets): ", type(sqlQuerySets))
    # print("ppp_process::sqlQuerySets: \n", sqlQuerySets)

    # windll = ctypes.windll.kernel32
    # LANGUAGE_NO = windll.GetUserDefaultUILanguage()  # 1033, 1042
    # LANGUAGE_CODE = locale.windows_locale[windll.GetUserDefaultUILanguage()]  # en_US, ko_KR
    # print("process_selected LANGUAGE_NO: ", LANGUAGE_NO, ", LANGUAGE_CODE: ", LANGUAGE_CODE)

    context = {"qrProcess": qrProcess, "products": products,
               "ppDataPeriodProcessList": ppDataPeriodProcessList, "ppDataPeriodProcessList2": ppDataPeriodProcessList2,
               "productsCount": productsCount, "sqlQuerySets": sqlQuerySets,
               "ppDataPeriod": ppDataPeriod, 'fromDate': fromDate, 'toDate': toDate, 'processCode': processCode,
               "LANGUAGE_NO": LANGUAGE_NO, "goodnessTotal": goodnessTotal, "volumesTotal": volumesTotal}
    print("views.py ppp_process() request: ", request)
    print("views.py ppp_process() request.POST: ", request.POST)
    print("views.py ppp_process() len(request.POST): ", len(request.POST))
    print("views.py ppp_process() request.method: ", request.method)
    print("views.py ppp_process() fromDate: ", fromDate)
    print("views.py ppp_process() toDate: ", toDate)
    print("views.py ppp_process() processCode: ", processCode)

    # print("views.py ppp_process() products: \n", products)
    # print("views.py ppp_process() ppDataPeriodProcessList2: \n", ppDataPeriodProcessList2)  # [['날짜', 123.0, 456.0, ...], ...[]]

    # return HttpResponse('Customer page')  # [127.0.0.1:8000/about]으로 연결 시, 바로 뿌려준다. ===> 아래 : path('about/', contact),
    return render(request, 'ppp/ppp_process.html', context)
    # return JsonResponse(render(request, 'ppp/process.html', context), safe=False)  # 여긴 에러 나네...

    # data['context'] = render_to_string("ppp/process.html", context, request=request)
    # return JsonResponse(data, safe=False)


def goodsmasters(request):
    global process_code_selected
    goodsmasters = GoodsMaster.objects.all()

    print("goodsmasters process_code: ", processCode)
    # if process_code_selected is None or len(process_code_selected) == 0:  # 이것도 에러...
    if "process_code_selected" not in globals():  # 로컬 변수일 경우에는, [not in locals()]
        process_code_selected = processCode
        print("goodsmasters process_code_selected: ", process_code_selected)

    goodsmasters = GoodsMaster.objects.all().filter(process=process_code_selected)

    # return HttpResponse('Products page')  # [127.0.0.1:8000/about]으로 연결 시, 바로 뿌려준다. ===> 아래 : path('about/', contact),
    # return render(request, 'accounts/products.html')
    return render(request, 'ppp/goodsmasters.html', {'goodsmasters': goodsmasters})


def customers(request):
    # return HttpResponse('Customer page')  # [127.0.0.1:8000/about]으로 연결 시, 바로 뿌려준다. ===> 아래 : path('about/', contact),
    return render(request, 'ppp/customer.html')


# ***** 엄청 중요 ***** # 원래 위와 같은 [class]에서, 사용자가 customer.html 뿌려진 화면에서, 특정 customer를 클릭했을 때, 특정한 customer만 화면에 뿌려주는 방법...
def customer(request, pk):
    customer = Customer.objects.get(id=pk)  # urls.py : path('customer/<str:pk>/', views.customer), 이쪽과 연동...

    # ***** 여기서 또한 엄청 중요한 것은, ***** : customer.html 화면의 아래 부분에, Order 정보를 뿌려 주는 화면이 있으므로,
    # customer를 클릭하면, 해당 customer가 주문한 order 정보를 같이 가져다가, Order 정보 부분에 뿌려줘야 한다.
    orders = customer.order_set.all()
    # 또한, 같은 화면 customer.html에서, Total Orders 수량을 찍어줘야 하므로,
    order_count = 1  #orders.count()

    context = {'customer': customer, 'orders': orders, 'order_count': order_count}

    # return HttpResponse('Customer page')  # [127.0.0.1:8000/about]으로 연결 시, 바로 뿌려준다. ===> 아래 : path('about/', contact),
    # return render(request, 'accounts/customer.html')
    return render(request, 'ppp/customer.html', context)


def pp_process_analysis(request):
    return render(request, 'ppp/pp_process_analysis.html')
    # return render(request, 'ppp/index.html')


def pp_product_summary(request):
    # 2021.01.27 Conclusion. 아래와 같은 방법으로는 처리 불가...
    rsDictSum = {}
    # rs = process_selected(request, process_code)
    # print("pp_product_summary type(rs): ", type(rs))  # <class 'django.http.response.HttpResponse'>
    # print("pp_product_summary rs: ", rs)  #  <HttpResponse status_code=200, "text/html; charset=utf-8">

    # for key, val in rs.items():
    #     print("pp_product_summary key: ", key)
    #     print("pp_product_summary val: ", val)

    return JsonResponse({'rsDictSum': rsDictSum}, safe=False)

    # return render(request, 'ppp/process.html', context)



def pp_product_analysis(request):
    return render(request, 'ppp/pp_product_analysis.html')


@csrf_exempt
# 2021.02.10 Added. 조건에 맞는 자료만을 만들어서 도로 보낸다.
def makingProduction(sqlQuerySets, dfSets):
    rsDictSum = {}
    rsListSum = []

    ##########################################################################################################
    # 2021.02.21 Added. 생산 Volumn 수량 vs 실적 수량 같이 뿌리기 : t_Product.StandardTime
    processorGlobals = getGlobal(request=1)
    # dayWorkStartTime = time(8, 0)
    # nightWorkStartTime = time(20, 0)
    dayWorkStartTime = processorGlobals['DAY_WORK_START_TIME']
    nightWorkStartTime = processorGlobals['NIGHT_WORK_START_TIME']
    # print("dayWorkStartTime: ", dayWorkStartTime)
    print("nightWorkStartTime: ", nightWorkStartTime)

    ''' 2021.02.21 Conclusion. 아래 at() 사용보다 5~10배 느리다네...
    for i, v in dfSets.iterrows():  # 아래 보다 10배 느리다...
        workFrom = v["workfrom"]
        # if str(workFrom.time()) == "00:00:00":
        if workFrom.time() < dayWorkStartTime:
            workFrom = datetime.combine(workFrom.date(), dayWorkStartTime)
        workTo = v["workto"]
        if workTo.time() > nightWorkStartTime:
            workTo = datetime.combine(workTo.date(), nightWorkStartTime)
        workingSeconds = (workTo - workFrom).seconds
        # print("fromTime.time(), workTo.time(): ", workFrom.time(), " ", workTo.time())
        # print("fromTime, toTime: ", workFrom, " ", workTo)
        # print("type(fromTime), type(toTime): ", type(workFrom), " ", type(workTo))
        # print("workingSeconds: ", workingSeconds)
        # print("type(workingSeconds): ", type(workingSeconds))
        if workingSeconds > 7200 and workingSeconds < 14400:
            workingSeconds = workingSeconds - 600  # 10분 휴식 시간 공제
        elif workingSeconds > 14400 and workingSeconds < 25200:
            workingSeconds = workingSeconds - 600 - 3600  # 10분 휴식, 점심 시간 공제
        elif workingSeconds > 25200 and workingSeconds < 32400:
            workingSeconds = workingSeconds - 600 - 3600 - 600  # 10분 휴식, 점심 시간, 10분 휴식 공제
        elif workingSeconds > 32400 and workingSeconds < 39600:
            workingSeconds = workingSeconds - 600 - 3600 - 600 - 600  # 10분 휴식, 점심 시간, 10분 휴식, 10분 저녁 공제
        elif workingSeconds > 39600 and workingSeconds < 46800:
            workingSeconds = workingSeconds - 600 - 3600 - 600 - 600  # 10분 휴식, 점심 시간, 10분 휴식, 10분 저녁, 10분 휴식 공제
        else:
            workingSeconds = workingSeconds - 600 - 3600 - 600 - 600  # 10분 휴식, 점심 시간, 10분 휴식, 10분 저녁, 10분 휴식 공제

        standardSeconds = v['standardtime']
        # print("standardSeconds: ", standardSeconds)
        # print("type(standardSeconds): ", type(standardSeconds))
        if standardSeconds is None or standardSeconds == 0:
            standardSeconds = 10  # 아무리 안 걸려도 [10초]는 걸리게 한다???

        volume = int(workingSeconds / standardSeconds)
        v["volume"] = volume  # 여기서 세팅이 안 되네...
        # print("volume: ", volume)

    # print("dfSets: \n", dfSets[['step9', 'goodness', 'volume', 'codespec']])
    print("dfSets: \n", dfSets[['step9', 'goodness', 'volume']])
    '''

    # 2021.02.21 Added. 먼저 값이 [Null]인 것들을 한방에 모두 [0]으로 치환한다. 원본 데이터도 변경 : inplace=True
    # dfSets.replace({'standardtime': {'np.nan': 0}})  # 이건 에러는 안 나는데, 치환이 제대로 안 되네...
    # dfSets.replace({'codetwins': {'np.nan': ""}})  # 이건 에러는 안 나는데, 치환이 제대로 안 되네...
    # dfSets = dfSets.standardtime.fillna(0, inplace=True)  # 여기는 에러...
    dfSets.standardtime.fillna(0, inplace=True)  # [True]이면, 원본을 변경한다.
    dfSets.codetwins.fillna("", inplace=True)  # [True]이면, 원본을 변경한다.
    # dfSets = dfSets.standardtime.fillna(0, inplace=False)  # 여기가 작동...
    # dfSets = dfSets.standardtime.fillna(0)  # 여기도 작동되고...

    volumes = []
    # print("dfSets: \n", dfSets[['step9', 'goodness', 'standardtime']])
    # print("dfSets: \n", dfSets[['step9', 'codetwins', 'standardtime']])
    # print("dfSets.index: ", dfSets.index)
    for i in dfSets.index:
        # print("i: ", i)
        workFrom = dfSets.at[i, 'workfrom']
        workTo = dfSets.at[i, 'workto']
        if workFrom.time() < dayWorkStartTime:
            workFrom = datetime.combine(workFrom.date(), dayWorkStartTime)
        if workTo.time() > nightWorkStartTime:
            workTo = datetime.combine(workTo.date(), nightWorkStartTime)
        # print("fromTime.time(), workTo.time(): ", workFrom.time(), " ", workTo.time())
        # print("fromTime, toTime: ", workFrom, " ", workTo)
        # print("type(fromTime), type(toTime): ", type(workFrom), " ", type(workTo))
        workingSeconds = (workTo - workFrom).seconds
        # print("workingSeconds: ", workingSeconds)
        # print("type(workingSeconds): ", type(workingSeconds))

        # codeTwins = str(dfSets.at[i, 'codetwins']).strip()
        code = dfSets.at[i, 'code'].strip()  # ***** 여기서 반드시 strip() 처리를 해야만, 아래에서 제대로 검색함.
        # print("type(code): ", type(code))
        # print("code: ", code)

        codeTwins = dfSets.at[i, 'codetwins'].strip()  # ***** 여기서 반드시 strip() 처리를 해야만, 아래에서 제대로 검색함.
        standardSeconds = dfSets.at[i, 'standardtime']  # [MySQL]에서는 int64 타입이고, [MSSQL]에서는 Decimal 타입임. int 타입이 아님에 주의...
        #if type(standardSeconds) == Decimal:
        standardSeconds = float(standardSeconds)  # int(standardSecondsTwins): 여긴 에러 주의.

        # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!type(code): ", type(code))
        # if code == "8000013555" or code == "8000013554":
        #     print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!code: ", code, ", codeTwins: ", codeTwins)
        # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!type(codeTwins): ", type(codeTwins))
        # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!standardSeconds: ", standardSeconds)
        # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!type(standardSeconds): ", type(standardSeconds))
        # if codeTwins == 'nan' or codeTwins == "":  # 여기서 [Null] 체크하면, 이상하게 에러가 나네...
        if codeTwins == "":  # 일반 제품... 쌍둥이 제품이 아님... # or len(codeTwins) < 8:
            # print("???????????????????????????????????????????codeTwins type is str, codeTwins is Blank", codeTwins)
            # if standardSeconds == 'nan' | standardSeconds is None | standardSeconds <= 1:  # 여기서 [Null] 체크하면, 이상하게 에러가 나네...
            if standardSeconds <= 1:
                # 여기는 사실, BOM 정리가 제대로 안 되어 있는 제품이라는 의미...
                standardSeconds = 10  # 아무리 안 걸려도 [10초]는 걸리게 한다???
        else:  # 쌍둥이 제품...
            # print("???????????????????????????????????????????codeTwins type is codeTwins:", codeTwins)
            # if standardSeconds == 'nan' | standardSeconds is None | standardSeconds <= 1:
            # if code == "8000013557" or code == "8000013541":
            #     print("동생일 때 code: ", code, ", codeTwins: ", codeTwins, ", standardSeconds: ", standardSeconds)
            # if code == "8000013555" or code == "8000013554":
            #     print("동생이네! code: ", code, ", codeTwins: ", codeTwins, ", standardSeconds: ", standardSeconds)
            if standardSeconds <= 1:
                # 1. 동생 제품이면, 즉 [작업 소요 시간]이 [1]이고, [codetwins.쌍둥이 제품]이 있다면,
                #    형 제품의 작업 소요 시간은 가져온다.
                # standardSeconds = dfSets.loc[str(dfSets['code']).strip() == codeTwins]

                # 아래는 [index] 값만 배열로 얻어진다. 참고로...
                # codeTwinsIndexes = dfSets.index[dfSets['code'] == codeTwins].tolist()
                codeTwinsData = dfSets.loc[dfSets['code'] == codeTwins, ['code', 'codetwins', 'standardtime']]
                # if code == "8000013555" or code == "8000013554":
                #     print("1111111 code: ", code, ", codeTwins: ", codeTwins)
                #     print("1111111 codeTwinsData: \n", codeTwinsData)
                #     print("1111111 len(codeTwinsData): ", len(codeTwinsData))
                if len(codeTwinsData) > 0:
                    standardSecondsTwins = codeTwinsData.iloc[0, 2]  # 'standardtime']  # [MySQL]에서는 int64 타입이고, [MSSQL]에서는 Decimal 타입임. int 타입이 아님에 주의...
                    # if type(standardSecondsTwins) == Decimal:
                    standardSecondsTwins = float(standardSecondsTwins)  # int(standardSecondsTwins): 여긴 에러 주의.
                    # print("2 standardSecondsTwins: ", standardSecondsTwins)
                else:
                    standardSecondsTwins = 0
                # if code == "8000013555" or code == "8000013554":
                #     print("standardSecondsTwins: ", standardSecondsTwins)

                # if code == "8000013555" or code == "8000013554":
                #     print("형 꺼는? code: ", code, ", codeTwins: ", codeTwins, ", standardSecondsTwins: ", standardSecondsTwins)

                # if standardSecondsTwins == 'nan' | standardSecondsTwins is None | standardSecondsTwins <= 1.0:

                if standardSecondsTwins <= 1:
                    # 여기는 사실, BOM 정리가 제대로 안 되어 있는 제품이라는 의미...
                    standardSeconds = 10  # 아무리 안 걸려도 [10초]는 걸리게 한다???
                else:
                    # print("standardSeconds code: ", code, ", codeTwins: ", codeTwins)
                    # print("standardSecondsTwins: ", standardSecondsTwins)
                    # print("type(standardSecondsTwins): ", type(standardSecondsTwins))

                    # 2021.03.06 Conclusion. 제품 입장에서는 온전한 [CT]로 계산되어야 한다. 설비 기준에서는 [반 CT]가 맞다.
                    # standardSeconds = int(standardSecondsTwins * 0.5)  # 형꺼 작업 시간의 반...
                    # standardSeconds = int(standardSecondsTwins)  # * 0.5)  # 형꺼 작업 시간의 반...
                    standardSeconds = float(standardSecondsTwins)  # * 0.5)  # 형꺼 작업 시간의 반...

                    # [또한 작업 시간.workingSeconds]을 반만 할당하여 계산하여도 같은 것이지만, [CT]를 온전히 하는 것이 더 좋다.
                    # workingSeconds = int(workingSeconds * 0.5)  # 형꺼 작업 시간의 반...
                    # print("workingSeconds: ", workingSeconds)
                    # print("type(workingSeconds): ", type(workingSeconds)) # 작업 시간도 반만 할당한다.

                # if code == "8000013555" or code == "8000013554":
                #     print("동생일 때 standardSeconds code: ", code, ", standardSeconds: ", standardSeconds)
                #     print("동생일 때 standardSeconds code: ", code, ", codeTwins: ", codeTwins)

            else:  # 지금 [code.제품]에 [standardtime.작업시간] 값이 정상적으로 들어 있으면, [반]만 할당해야 한다. => 그대로.
                # 2. 자기 자신의 [CT]가 온전한 [CT]이면...
                # 2021.03.06 Conclusion. 제품 입장에서는 온전한 [CT]로 계산되어야 한다. 설비 기준에서는 [반 CT]가 맞다.
                # workingSeconds = int(workingSeconds * 0.5)  # 자기 자신의 작업 시간도 반만 할당한다.
                # print("else standardSeconds code: ", code, ", codeTwins: ", codeTwins)
                # print("else standardSecondsTwins: ", standardSecondsTwins)
                # print("else type(standardSecondsTwins): ", type(standardSecondsTwins))
                # standardSeconds = int(standardSeconds)  # * 0.5)  # 자기 자신의 작업 시간의 반...
                standardSeconds = float(standardSeconds)  # * 0.5)  # 자기 자신의 작업 시간의 반...

        # print("i: ", i, ", standardsSeconds: ", standardSeconds)

        # print("workingSeconds: ", workingSeconds)
        # print("type(workingSeconds): ", type(workingSeconds))
        if workingSeconds > 7200 & workingSeconds < 14400:
            workingSeconds = workingSeconds - 600  # 10분 휴식 시간 공제
        elif workingSeconds > 14400 & workingSeconds < 25200:
            workingSeconds = workingSeconds - 600 - 3600  # 10분 휴식, 점심 시간 공제
        elif workingSeconds > 25200 & workingSeconds < 32400:
            workingSeconds = workingSeconds - 600 - 3600 - 600  # 10분 휴식, 점심 시간, 10분 휴식 공제
        elif workingSeconds > 32400 & workingSeconds < 39600:
            workingSeconds = workingSeconds - 600 - 3600 - 600 - 600  # 10분 휴식, 점심 시간, 10분 휴식, 10분 저녁 공제
        elif workingSeconds > 39600 & workingSeconds < 46800:
            workingSeconds = workingSeconds - 600 - 3600 - 600 - 600  # 10분 휴식, 점심 시간, 10분 휴식, 10분 저녁, 10분 휴식 공제
        else:
            workingSeconds = workingSeconds - 600 - 3600 - 600 - 600  # 10분 휴식, 점심 시간, 10분 휴식, 10분 저녁, 10분 휴식 공제

        # if code == "8000013555" or code == "8000013554":
        # if code == "FA1A0NUPAA02" or code == "FA1A0NUPAA03":
        #     print("결국 standardSeconds code: ", code, ", standardSeconds: ", standardSeconds, ", workingSeconds: ", workingSeconds)
        #     print("결국 standardSeconds code: ", code, ", codeTwins: ", codeTwins)
        #     print("fromTime.time(), workTo.time(): ", workFrom.time(), " ", workTo.time())
        #     print("fromTime, toTime: ", workFrom, " ", workTo)

        # 2021.03.06 Added. [CT]가 [-] 나오는 제품 확인...
        if workingSeconds < 0:
            print("workingSecond 음수인 code: ", code, ", workingSeconds: ", workingSeconds)
            print("workingSecond 음수인 code: ", code, ", codeTwins: ", codeTwins)

        # print("index i 값: ", i)
        volume = int(workingSeconds / standardSeconds)
        # volume = float(workingSeconds / standardSeconds)
        volumes.append(volume)

        # if code == "FA1A0NUPAA02" or code == "FA1A0NUPAA03":
        #     print("결국 standardSeconds code: ", code, ", standardSeconds: ", standardSeconds, ", workingSeconds: ", workingSeconds, ", volume: ", volume)
        #     print("결국 standardSeconds code: ", code, ", codeTwins: ", codeTwins)
        #     print("fromTime.time(), workTo.time(): ", workFrom.time(), " ", workTo.time())
        #     print("fromTime, toTime: ", workFrom, " ", workTo)

        # dfSets.set_value(i, 'volume', volume, takeable=False)  # 여긴 에러...
        # dfSets.at(i, 'volume', volume)  #, takeable=True)  # 여기도 에러...
        # dfSets.iloc[i]['volume'] = volume  # 여긴 에러가 안 나는데, 값이 변경이 안 되네...

    # print("volumes: ", volumes)
    dfSets['volumes'] = volumes

    # print("dfSets: \n", dfSets[['step9', 'goodness', 'volume', 'codespec']])
    # print("dfSets: \n", dfSets[['step9', 'goodness', 'volumes', 'volume']])
    ##########################################################################################################

    df_data_prd_pro_wor = dfSets.sort_values(['process', 'workdate', 'step9'], ascending=True)
    # print("sort_values() 후 makingProduction::type(df_data_prd_pro_wor): ", type(df_data_prd_pro_wor))
    # print("sort_values() 후 makingProduction::df_data_prd_pro_wor.head(): \n", df_data_prd_pro_wor.head())

    ''' 여기는 제품과 상관없이 날짜별 총 합계를 구하는 것이다. 
    df_data_prd_pro_wor['workdate'] = pd.to_datetime(df_data_prd_pro_wor['workdate'])
    print("to_datetime() 후 makingProduction::type(df_data_prd_pro_wor): ", type(df_data_prd_pro_wor))
    print("to_datetime() 후 makingProduction::df_data_prd_pro_wor.head(): \n", df_data_prd_pro_wor.head())
    df_current_date = df_data_prd_pro_wor.resample('1D', on='workdate')['step9', 'goodness'].sum()  #  groupby(['step9']).sum()
    print("resample() 후 makingProduction::type(df_current_date): ", type(df_current_date))
    print("resample() 후 makingProduction::df_current_date.head(): \n", df_current_date.head())
    '''

    ##########################################################################################################
    # 2021.02.21 Added. 일자별 생산 수량 총괄표. 컬럼명이 [d1 ~ D31]

    ##########################################################################################################

    df_data_prd_pro_wor1 = df_data_prd_pro_wor.groupby(['workdate', 'step9'])['goodness'].sum().reset_index()
    # df_data_prd_pro_wor2 = df_data_prd_pro_wor.groupby(['workdate', 'step9'])['goodness', 'volumes'].sum().reset_index()
    df_data_prd_pro_wor2 = df_data_prd_pro_wor.groupby(['workdate', 'step9'])['volumes'].sum().reset_index()

    # print("groupby() 후 makingProduction::type(df_data_prd_pro_wor1): ", type(df_data_prd_pro_wor1))
    # print("groupby () 후 makingProduction::df_data_prd_pro_wor1.tail(20): \n", df_data_prd_pro_wor1.tail(20))
    # print("groupby() 후 makingProduction::df_data_prd_pro_wor1: \n", df_data_prd_pro_wor1)

    # ********************************************************************************************************
    # ********************************************************************************************************
    # ********************************************************************************************************
    # ********************************************************************************************************
    # ********************************************************************************************************
    # 2021.01.30 Conclusion. ***** 엄청 중요 *****
    # 1. 그룹화한 자료는 반드시 set_index()를 실행하여, 새로운 DataFrame.데이터프레임을 만들어야 한다.
    # 2. 날짜로 그룹화]한 후에, 리스트를 만든다.
    ppData = df_data_prd_pro_wor1.reset_index(drop=True, inplace=False)  # 반드시 따로 [reset_index()] 실행.
    # print("reset_index() 후 makingProduction::type(ppData): ", type(ppData))
    # print("reset_index() 후 makingProduction::ppData: \n", ppData)

    ppData = df_data_prd_pro_wor1.values.tolist()  # 데이터프레임을 ===> 리스트로 변환...
    # ppData2 = df_data_prd_pro_wor1.values.tolist()  # 데이터프레임을 ===> 리스트로 변환...

    # ppData = [{data for data in ppData}]  # 아...깜빡 착각... DataFrame.데이터프레임은 이렇게 리스트화가 안 됨...
    ppDataOrigin = [data for data in sqlQuerySets]  # 이것은 완전한 원시 데이터임...
    # print("리스트로 만든 후 makingProduction::type(ppData): ", type(ppData))
    # print("리스트로 만든 후 makingProduction::ppData: \n", ppData)
    # print("리스트로 만든 후 makingProduction::type(ppDataOrigin): ", type(ppDataOrigin))
    # print("리스트로 만든 후 makingProduction::ppDataOrigin: \n", ppDataOrigin)

    # 2021.01.24 Conclusion. 그동안 그래프 작업을 안 해서 생소한, 자료의 그룹핑 로직을 만들어야 하네...
    # 날짜 : A.step9,   B.step9,    C.step9...
    # 2020.12.01, A 제품 수량, B 제품 수량, C 제품 수량...
    # 2020.12.02, A 제품 수량, B 제품 수량, C 제품 수량...
    # 2020.12.03, A 제품 수량, B 제품 수량, C 제품 수량...
    # ...

    # 0. 먼저 [workdate]만 Series로 만든 다음, 그룹화해서 unique 날짜 값 1개만 남긴다.
    # ppDataPeriodProcessWorkdate = df_data_prd_pro_wor1[['workdate']].unique()  # 대괄호 2개는 에러 나네...
    # ppDataPeriodProcessWorkdate = df_data_prd_pro_wor1[['workdate', 'step9']]  # 컬럼이 2개 이상일 때만, 정상 작동...
    # ppDataPeriodProcessWorkdate = df_data_prd_pro_wor1['workdate'].unique()  # <class 'numpy.ndarray'>
    # ppDataPeriodProcessWorkdate = pd.DataFrame(df_data_prd_pro_wor1['workdate'].unique())  # <class 'pandas.core.frame.DataFrame'>
    # ppDataPeriodProcessWorkdate = df_data_prd_pro_wor1.drop_duplicates(['workdate'])  # <class 'pandas.core.frame.DataFrame'>
    ppDataPeriodProcessWorkdate = df_data_prd_pro_wor1.drop_duplicates(['workdate'])[
        ['workdate']]  # <class 'pandas.core.frame.DataFrame'>
    # ppDataPeriodProcessWorkdate2 = df_data_prd_pro_wor1.drop_duplicates(['workdate'])[
    #     ['workdate']]  # <class 'pandas.core.frame.DataFrame'>
    # print("process_selected::len(ppDataPeriodProcessWorkdate): ", len(ppDataPeriodProcessWorkdate))
    # print("workdate 컬럼만 makingProduction::type(ppDataPeriodProcessWorkdate): ", type(ppDataPeriodProcessWorkdate))
    # print("workdate 컬럼만 makingProduction::ppDataPeriodProcessWorkdate: \n", ppDataPeriodProcessWorkdate)

    # 1. [workdate] 날짜 자료만 따로 리스트로 만들어 보내서, 그래프의 [Labels]로 활용하게 한다.
    ppDataPeriod = ppDataPeriodProcessWorkdate.values.tolist()  # [['날짜'],['날짜'],...['날짜']] : 괄호가 2개임에 주의.
    # print("process_selected::len(ppDataPeriod): ", len(ppDataPeriod))
    # print("workdate 컬럼만 makingProduction::type(ppDataPeriod): ", type(ppDataPeriod))
    # print("workdate 컬럼만 makingProduction::ppDataPeriod: \n", ppDataPeriod)

    # 2. [step9]만 Series로 만든 다음, 그룹화해서 unique 제품명 값 1개만 남긴다.
    ppDataPeriodProcessStep9 = df_data_prd_pro_wor1['step9'].unique()  # <class 'numpy.ndarray'>
    # ppDataPeriodProcessStep9 = pd.DataFrame(df_data_prd_pro_wor1['step9'].unique())  # <class 'pandas.core.frame.DataFrame'>
    # ppDataPeriodProcessStep9 = pd.DataFrame(df_data_prd_pro_wor1['step9'].unique()).values.tolist()  # <class 'List'>
    # print("makingProduction::len(ppDataPeriodProcessStep9): ", len(ppDataPeriodProcessStep9))
    # print("step9 컬럼만 makingProduction::type(ppDataPeriodProcessStep9): ", type(ppDataPeriodProcessStep9))
    # print("step9 컬럼만 makingProduction::ppDataPeriodProcessStep9: \n", ppDataPeriodProcessStep9)

    # 3. 제품명을 [컬럼명]으로 전환하기 위해, [공백 문자, 특수 문자] 제거...
    # pattern = '[-=.#/?$:}{@% ]'  # 맨뒤에 [공백 문자]가 [중간 공백]까지 없애기 위해 있으며, [^A-Za-z0-9] 첫문자가 이것일 경우에는 [부정문]이 된다.
    # pattern = '[-=.#/?$:}{@%]'  # [중간 공백]은 그대로 둔다.
    pattern = '[=.#/?$:}{@%]'  # 2021.03.13 Conclusion. 공백 문자에 [-]는 빼지 않는다. [step9] 값 중간에 BHMC.PartNo 값에 [-]가 들어 있기 때문이다.
    pattern = pattern.strip()  # [양쪽 공백]만 없앤다.
    # products = [product for (re.sub(pattern, '', product)) in ppDataPeriodProcessStep9]
    products = []
    for product in ppDataPeriodProcessStep9:
        prd = re.sub(pattern, '', product).strip()
        products.append(prd)
    productsCount = len(products)
    # print("makingProduction products: ", products)
    # print("makingProduction productsCount: ", productsCount)

    # 4. [workdate.작업일자]만 있는 데이터프레임에, [step9.제품명] 필드를 더해준다.
    # temp = ['CN7CK97775BU300874组装品', 'ID97762F9100374组装品', 'NUPE97762S6500374组装品',
    #         'NUPE97775S6500874组装品', 'TLCFL97775F8100874组装品', 'TMCCOM97762S3700374组装品',
    #         'CN7CG97775BU000874组装品', 'TLCFL97762F8000374组装品', 'VBSTDU281660Q3000DRIVEUNIT组装品',
    #         'VBSTTLC81635F8100DRIVEUNIT组装品', 'DN8CNU97775L4100874组装品', 'TMCSI97759S3700874组装品',
    #         'NUPEKT97762S6600374组装品', 'DN8CG97775L4000874组装品', 'NUPEKT97775S6600874组装品',
    #         'YCPE97775F9500874组装品', 'DU2EV97775Z3000874组装品', 'YCPE97762F9000374组装品',
    #         'DU2EV97762Z3000374组装品']
    ppDataPeriodProcess = ppDataPeriodProcessWorkdate.reindex(
        columns=ppDataPeriodProcessWorkdate.columns.tolist() + products)
    ppDataPeriodProcess2 = ppDataPeriodProcessWorkdate.reindex(
        columns=ppDataPeriodProcessWorkdate.columns.tolist() + products)
    # print("makingProduction::len(ppDataPeriodProcess): ", len(ppDataPeriodProcess))
    # print("종합표 makingProduction::type(ppDataPeriodProcess): ", type(ppDataPeriodProcess))
    # print("종합표 makingProduction::ppDataPeriodProcess: \n", ppDataPeriodProcess)

    # 5-1. 날짜별 제품별 goodness.생산 실적 수량을 해당 셀에 치환한다.
    goodnessTotal = 0
    for rows in df_data_prd_pro_wor1.iterrows():
        # print("type(rows): ", type(rows))
        day = str(rows[1][0])[:10]
        product = rows[1][1].strip()
        product = re.sub(pattern, '', product)
        goodness = rows[1][2]
        goodnessTotal += goodness
        # print("makingProduction goodnessTotal: ", goodnessTotal)

        # 먼저 확인해야 하는 것이, [product.현재 제품명]으로 [products.컬렴명]이 있는지부터 확인해야 한다.
        if product not in products:
            print("makingProduction 현재 자료를 정리하지 못 했습니다. 관리자에게 문의하시오!", day, " ", product, " ", goodness)
            print("makingProduction 해당 자료가 전혀 없습니다!")
            return [], [], 0, [], []
            # context = {'process': process, 'ppData': [], 'total_pp_data_count': 0,
            #            'sqlQuerySets': sqlQuerySets, 'LANGUAGE_NO': LANGUAGE_NO}
            # return render(request, 'ppp/process.html', context)

        # boolean = ppDataPeriodProcess['workdate'] == day
        # row = ppDataPeriodProcess.query("workdate == 2020-12-01").index.tolist()

        # 2021.01.31 Conclusion. 아래 2 문장은 동일하다.
        # beOrNot = len(ppDataPeriodProcess[ppDataPeriodProcess['workdate'] == day])
        beOrNot = len(ppDataPeriodProcess[ppDataPeriodProcess.workdate == day])
        # print("beOrNot: ", beOrNot)

        if beOrNot > 0:
            # print("len(ppDataPeriodProcess[ppDataPeriodProcess.workdate == day]): ",
            #       len(ppDataPeriodProcess[ppDataPeriodProcess.workdate == day]))
            # print("True: ", ppDataPeriodProcess[ppDataPeriodProcess.workdate == day])
            ppDataPeriodProcess.loc[(ppDataPeriodProcess.workdate == day), product] = goodness
        else:
            print("makingProduction 현재 자료를 정리하지 못 했습니다. 관리자에게 문의하시오!", day, " ", product, " ", goodness)
            print("makingProduction 해당 자료가 전혀 없습니다!")
            return [], [], 0, [], []
            # context = {'process': process, 'ppData': [], 'total_pp_data_count': 0,
            #            'sqlQuerySets': sqlQuerySets, 'LANGUAGE_NO': LANGUAGE_NO}
            # return render(request, 'ppp/process.html', context)

    # print("makingProduction::len(ppDataPeriodProcess): ", len(ppDataPeriodProcess))
    # print("종합표 df 정리 후 makingProduction::type(ppDataPeriodProcess): ", type(ppDataPeriodProcess))
    # print("종합표 df 정리 후 makingProduction::ppDataPeriodProcess: \n", ppDataPeriodProcess)
    # print("makingProduction goodnessTotal: ", goodnessTotal)

    # 5-2. 날짜별 제품별 volumes.생산 능력 수량을 해당 셀에 치환한다.
    volumesTotal = 0
    for rows in df_data_prd_pro_wor2.iterrows():
        # print("type(rows): ", type(rows))
        day = str(rows[1][0])[:10]
        product = rows[1][1].strip()
        product = re.sub(pattern, '', product)
        volumes = rows[1][2]
        volumesTotal += volumes
        # print("makingProduction volumesTotal: ", volumesTotal)

        # 먼저 확인해야 하는 것이, [product.현재 제품명]으로 [products.컬렴명]이 있는지부터 확인해야 한다.
        if product not in products:
            print("makingProduction 현재 자료를 정리하지 못 했습니다. 관리자에게 문의하시오!", day, " ", product, " ", volumes)
            print("makingProduction 해당 자료가 전혀 없습니다!")
            return [], [], 0, [], []
            # context = {'process': process, 'ppData': [], 'total_pp_data_count': 0,
            #            'sqlQuerySets': sqlQuerySets, 'LANGUAGE_NO': LANGUAGE_NO}
            # return render(request, 'ppp/process.html', context)

        # boolean = ppDataPeriodProcess2['workdate'] == day
        # row = ppDataPeriodProcess2.query("workdate == 2020-12-01").index.tolist()

        # 2021.01.31 Conclusion. 아래 2 문장은 동일하다.
        # beOrNot = len(ppDataPeriodProcess2[ppDataPeriodProcess2['workdate'] == day])
        beOrNot = len(ppDataPeriodProcess2[ppDataPeriodProcess2.workdate == day])
        # print("beOrNot: ", beOrNot)

        if beOrNot > 0:
            # print("len(ppDataPeriodProcess2[ppDataPeriodProcess2.workdate == day]): ",
            #       len(ppDataPeriodProcess2[ppDataPeriodProcess2.workdate == day]))
            # print("True: ", ppDataPeriodProcess2[ppDataPeriodProcess2.workdate == day])
            ppDataPeriodProcess2.loc[(ppDataPeriodProcess2.workdate == day), product] = volumes
        else:
            print("makingProduction 현재 자료를 정리하지 못 했습니다. 관리자에게 문의하시오!", day, " ", product, " ", volumes)
            print("makingProduction 해당 자료가 전혀 없습니다!")
            return [], [], 0, [], []
            # context = {'process': process, 'ppData': [], 'total_pp_data_count': 0,
            #            'sqlQuerySets': sqlQuerySets, 'LANGUAGE_NO': LANGUAGE_NO}
            # return render(request, 'ppp/process.html', context)

    # print("makingProduction::len(ppDataPeriodProcess2): ", len(ppDataPeriodProcess2))
    # print("종합표 df 정리 후 makingProduction::type(ppDataPeriodProcess2): ", type(ppDataPeriodProcess2))
    # print("종합표 df 정리 후 makingProduction::ppDataPeriodProcess2: \n", ppDataPeriodProcess2)
    # print("makingProduction volumesTotal: ", volumesTotal)

    # 6. 최종적으로 html 쪽으로 넘겨줄 수 있도록, 리스트로 변경해 준다.
    ppDataPeriodProcessList0 = ppDataPeriodProcess.fillna(0)  # NaN 값을 [0]으로 치환. 반드시 [새로운 DataFrame 명] 사용...
    ppDataPeriodProcessList = ppDataPeriodProcessList0.values.tolist()
    ppDataPeriodProcessList22 = ppDataPeriodProcess2.fillna(0)  # NaN 값을 [0]으로 치환. 반드시 [새로운 DataFrame 명] 사용...
    ppDataPeriodProcessList2 = ppDataPeriodProcessList22.values.tolist()
    # print("process_selected::len(ppDataPeriodProcessList): ", len(ppDataPeriodProcessList))
    # print("종합표 리스트 정리 후 makingProduction::type(ppDataPeriodProcessList): ", type(ppDataPeriodProcessList))
    # print("종합표 리스트 정리 후 makingProduction::ppDataPeriodProcessList: \n", ppDataPeriodProcessList)
    # print("종합표 리스트 정리 후 makingProduction::type(ppDataPeriodProcessList2): ", type(ppDataPeriodProcessList2))
    # print("종합표 리스트 정리 후 makingProduction::ppDataPeriodProcessList2: \n", ppDataPeriodProcessList2)

    # 2021.02.21 Conclusion. 여기 아래로는, 사실은 [products, productsCount, ppDataPeriod] 이것만 필요함...
    # 이미 가장 중요한 자료인 [ppDataPeriodProcessList]는 나왔음.
    # return ppDataPeriodProcessList, products, productsCount, ppDataPeriod

    # 데이터프레임을 ===> 튜플로 변환... *****
    # 2020.03.03 Conclusion. 이건 정상 작동하는데, 속도 향상을 위해 실행을 시키지 않는다.
    # rsTupleSum = [tuple(r) for r in df_data_prd_pro_wor1.to_numpy()]

    # 2020.03.03 Conclusion. 이건 정상 작동하는데, 속도 향상을 위해 실행을 시키지 않는다.
    # ppDataCount = len(ppData)
    # print("리스트로 만든 후 makingProduction ppDataCount: ", ppDataCount)

    ppDataOriginCount = len(ppDataOrigin)
    # print("리스트로 만든 후 makingProduction ppDataOriginCount: ", ppDataOriginCount)
    # ********************************************************************************************************
    # ********************************************************************************************************
    # ********************************************************************************************************
    # ********************************************************************************************************
    # ********************************************************************************************************

    '''
    # 2021.01.30 Conclusion. 다시 dictionary.딕셔너리로 처리한다.
    # ********************************************************************************************************
    # ********************************************************************************************************

    # 2021.01.28 Conclusion. 아래 주석 처리된 부분은,
    # 전체 자료를 날짜별로 필터해서, 31번을 루프로 돌려서 처리하는 방식으로, 여기서 1번에 처리하게 하였다.
    # =========================================================================================================

    # # 여기서는 위와 아래의 자료가 동일하지만, 아래 내용은 다른 내용이다.
    # # 아래 내용은, cumsum 컬럼을 새로 만들어서, 그 컬럼에, 'step9'를 기준으로 다시 'goodness'를 합산하여, 찍어주는 것이다.
    # df_data_prd_pro_wor1['cumsum'] = df_data_prd_pro_wor1.groupby(['step9'])['goodness'].apply(lambda x: x.cumsum())
    # print("1 resample() 후 makingProduction::type(df_data_prd_pro_wor1): ", type(df_data_prd_pro_wor1))
    # print("1 resample() 후 makingProduction::df_data_prd_pro_wor1.head(): \n", df_data_prd_pro_wor1.head())
    # print("1 resample() 후 makingProduction::df_data_prd_pro_wor1: \n", df_data_prd_pro_wor1)

    # 데이터프레임을 ===> 리스트 + 튜플 [{}] 로 변환... ***** : 결론 : 리스트로 변환하면, javascript 에서 for 문장을 못 쓰네...
    # context = [{'process': data['process'], 'goodness': data['goodness']} for index, data in df_data_prd_pro_wor1.iterrows()]
    # rsList = [{'step9': data['step9'], 'goodness': data['goodness']} for index, data in df_data_prd_pro_wor1.iterrows()]  # if data[0] == process_code]
    # print("0 리스트 변환 후 makingProduction::type(rsList): ", type(rsList))  # <class 'list'>
    # print("0 리스트 변환 후 makingProduction::rsList: \n", rsList)

    # 데이터프레임을 ===> 리스트로 변환...
    rsListSum = df_data_prd_pro_wor1.values.tolist()
    print("0 리스트 변환 후 makingProduction::type(rsListSum): ", type(rsListSum))  # <class 'list'>
    print("0 리스트 변환 후 makingProduction::rsListSum: \n", rsListSum)

    rsDataFrameCount = len(df_data_prd_pro_wor1)
    print("0 데이터프레임 로우 수 makingProduction::rsDataFrameCount: ", rsDataFrameCount)

    # 데이터프레임을 ===> 튜플로 변환... *****
    rsTupleSum = [tuple(r) for r in df_data_prd_pro_wor1.to_numpy()]
    # print("0 튜플 변환 후 makingProduction::type(rsTupleSum): ", type(rsTupleSum))  #  <class 'list'>: 'tuple' 아님...
    # print("0 튜플 변환 후 makingProduction::rsTupleSum: \n", rsTupleSum)

    # =========================================================================================================
    # ********************************************************************************************************
    # ********************************************************************************************************
    '''

    '''
    # pp_data_period_process_selected = sqlQuerySets.filter(process=process_code)  # 에러...
    pp_data_period_process_selected = [data for data in sqlQuerySets if data[5] == process_code]  # 가장 파이썬스러운 필터링...
    # print("makingProduction type(pp_data_period_process_selected): ", type(pp_data_period_process_selected))
    for i, v in enumerate(pp_data_period_process_selected):
        if i < 5:
            # print("makingProduction pp_data_period_process_selected.i: ", i)
            print("makingProduction pp_data_period_process_selected.v: ", v)
    '''

    # 2021.01.30 Conclusion. 다시 dictionary.딕셔너리로 처리한다.
    # ********************************************************************************************************
    # ********************************************************************************************************

    # '''
    # 2021.01.28 Conclusion. 아래 주석 처리된 부분은,
    # 전체 자료를 날짜별로 필터해서, 31번을 루프로 돌려서 처리하는 방식으로, 위에서 1번에 처리하게 하였다.
    ################################################################################################################
    # 2021.01.23 Added. [특정 공정 보기]를 클릭했을 때, 아예 그래프까지 뿌려준다.
    # 여기 자료.df_data_prd_pro_wor1 [이미 선택한 공정에 대한 실적 자료만] 필터된 것이므로,
    # [workdate.작업 일자] 별로 각각의 제품을 그룹화하면 된다.

    # 임시로 12월 자료를 보게 한다. 현재 20212년 1월 자료가 없기 때문이다.
    current_date_previous_month = first_date_this_month - relativedelta.relativedelta(months=1)
    current_date = current_date_previous_month.date()  # '2020-12-01'  # first_day_this_month.date()  # 날짜를 직접 String 값으로 주면, 아래 current_date += timedelta(days=1)에서 에러난다.
    # print("makingProduction current_date: ", current_date)  # 2021-01-01

    temp_first_date_this_month = current_date.replace(day=1)  # 임시로 12월 자료를 보게 한다. 현재 20212년 1월 자료가 없기 때문이다.
    first_date_next_month = temp_first_date_this_month + relativedelta.relativedelta(months=1)
    max_date_this_month = first_date_next_month - timedelta(days=1)
    max_day_this_month = max_date_this_month.day
    # print("process_selected max_date_this_month: ", max_date_this_month, ", max_day_this_month: ", max_day_this_month)  # 2021-12-31

    days = 1
    while days < max_day_this_month:
        # pp_data_period_process_selected_df = pd.DataFrame(df_data_prd_pro_wor1, df_data_prd_pro_wor1['workdate'] == current_day_this_month)  # 가장 파이썬스러운 필터링...
        # pp_data_period_process_selected_df = df_data_prd_pro_wor1[['workdate', 'step9', 'goodness']]
        # is_current_date = df_data_prd_pro_wor1['workdate'] == current_date  # 먼저 특정 조건에 맞는 시리즈만 추출...
        # df_current_date = df_data_prd_pro_wor1[is_current_date]

        # df_current_date = df_data_prd_pro_wor1.query("workdate >= '" + current_date + "' and workdate <= '" + current_date + "'")
        df_current_date = df_data_prd_pro_wor1[
            df_data_prd_pro_wor1["workdate"].isin(pd.date_range(current_date, current_date))]
        # print("makingProduction while 문장 내부 type(df_current_date): ", type(df_current_date))
        # print("makingProduction while 문장 내부 df_current_date: \n", df_current_date.head())
        # print("makingProduction while 문장 내부 current_date: ", current_date)  # 2021-01-01
        # print("makingProduction while 문장 내부 days: ", days)

        current_date += timedelta(days=1)

        df_current_date = df_data_prd_pro_wor1.groupby(['step9']).sum()

        # 2021.01.21 Conclusion. ***** 아래 for 문장에서 값을 가져올 때, [index] 컬럼이 없으면, iterrows()에서 에러 발생. *****
        df_current_date = df_current_date.reset_index(drop=False, inplace=False)  # 반드시 따로 [reset_index()] 실행.
        # print("2-리셋 후 makingProduction::type(df_current_date): ", type(df_current_date))  # <class 'pandas.core.frame.DataFrame'>
        # print("2-1리셋 후 makingProduction::df_current_date: \n", df_current_date)

        # df_current_date = df_current_date.reset_index(drop=True, inplace=False)  # 반드시 따로 [reset_index()] 실행.
        # print("2-리셋 후 makingProduction::type(df_current_date): ", type(df_current_date))  # <class 'pandas.core.frame.DataFrame'>
        # print("2-2리셋 후 makingProduction::df_current_date: \n", df_current_date)
        # df_current_date = df_current_date.reset_index(drop=True, inplace=True)  # 반드시 따로 [reset_index()] 실행.
        # print("2-리셋 후 makingProduction::type(df_current_date): ", type(df_current_date))  # <class 'pandas.core.frame.DataFrame'>
        # print("2-4리셋 후 makingProduction::df_current_date: \n", df_current_date)

        if df_current_date is None:
            print("makingProduction 해당 자료가 전혀 없습니다!")
            return [], [], 0, [], []
            # context = {'process': process, 'rsListSum': [], 'total_pp_data_count': 0,
            #            'sqlQuerySets': sqlQuerySets, 'LANGUAGE_NO': LANGUAGE_NO}
            # return render(request, 'ppp/process.html', context)

        # 데이터프레임에서 3개 컬럼(workdate, step9, goodness)만 다시 데이터프레임으로 추출.
        # df_current_date_goodness = df_current_date[['workdate', 'step9', 'goodness']]  # 'workdate' 컬럼은 에러나네... 위에서 reset_index() 하면, workdate 컬럼이 없어지네...
        # df_current_date_goodness = df_current_date[['step9', 'goodness', 'process']]  # 'process' 컬럼은 에러 안 나는데
        df_current_date_goodness = df_current_date[['step9', 'goodness']]
        # print("2개 컬럼만 makingProduction type(df_current_date_goodness): ", type(df_current_date_goodness))  # <class 'pandas.core.frame.DataFrame'>
        # print("2개 컬럼만 makingProduction df_current_date_goodness: \n", df_current_date_goodness)

        # 2020.03.03 Conclusion. 이건 정상 작동하는데, 속도 향상을 위해 실행을 시키지 않는다.
        # current_date_key = "day" + str(days)

        # print("process_selected current_date_key rsDict: ", current_date_key)

        # 2020.03.03 Conclusion. 이건 정상 작동하는데, 속도 향상을 위해 실행을 시키지 않는다.
        # rsDict = {}  # 반드시 여기서 초기화 해야 한다. 여기 [process_selected] 함수에서는, 날짜별로 finalrep 값을 갖는다.

        # 데이터프레임을 ===> 딕셔너리로 변환... *****
        # 2020.03.03 Conclusion. 이건 정상 작동하는데, 속도 향상을 위해 실행을 시키지 않는다.
        '''
        def df2dict(df):
            # print("makingProduction df.shape[1]: ", df.shape[1])
            if df.shape[1] != 2:
                return print("컬럼이 정확히 2개만 있어야, Dictionary 형식으로 변경이 가능 합니다!")
            for k, v in zip(df.iloc[:, 0], df.iloc[:, 1]):
                # print("makingProduction df2dict k: ", k)
                # print("makingProduction df2dict v: ", v)
                rsDict[k] = v
            return rsDict      
        # rsDict = df2dict(df_current_date_goodness)
        '''

        # print("makingProduction type(rsDict): ", type(rsDict))  # <class 'dict'>
        # print("makingProduction rsDict: \n", rsDict)

        # 2021.01.25 Conclusion. 아래와 같이 딕셔너리를 날짜별로 만들어, 그것을 [rsDictSum]에 더할 수는 없고,
        # 아래와 같이 직접 날짜별 딕셔너리를 바로 추가하면 된다. rsDictSum[current_date_key] = rsDict  # 바로 추가...

        # currentDict = {}
        # currentDict = {current_date_key: rsDict}  # 그것을 [rsDictSum]에 더할 수는 없고,
        # print("makingProduction type(currentDict): \n", type(currentDict))
        # print("makingProduction currentDict: \n", currentDict)

        # print("더하기 전 makingProduction type(rsDict): ", type(rsDictSum))  # <class 'dict'>
        # print("더하기 전 makingProduction rsDictSum: \n", rsDictSum)

        # 2020.03.03 Conclusion. 이건 정상 작동하는데, 속도 향상을 위해 실행을 시키지 않는다.
        # rsDictSum[current_date_key] = rsDict  # 바로 추가...

        # print("더한 후 makingProduction type(rsDict): ", type(rsDictSum))  # <class 'dict'>
        # print("다한 후 makingProduction rsDictSum: \n", rsDictSum)

        # 2020.03.03 Conclusion. 이건 정상 작동하는데, 속도 향상을 위해 실행을 시키지 않는다.
        # rsList = []  # 반드시 여기서 초기화 해야 한다. 여기 [process_selected] 함수에서는, 날짜별로 rsListSum 값을 갖는다.

        # 데이터프레임에서 3개 컬럼(step9, goodness, workday)
        # df_current_date_goodness['workday'] = str(days)  # current_date_key: [day] 빼고 날짜만 넣자

        # 2020.03.03 Conclusion. 이건 정상 작동하는데, 속도 향상을 위해 실행을 시키지 않는다.
        # df_current_date_goodness.loc[:, 'workday'] = str(days)  # current_date_key: [day] 빼고 날짜만 넣자

        # if days == 2:
        #     print("3개 컬럼만 makingProduction df_current_date_goodness: \n", df_current_date_goodness)

        # 데이터프레임을 ===> 리스트로 변환... *****
        # rsList = [data for data in df_current_date_goodness]  # if data[0] == process_code]

        # 2020.03.03 Conclusion. 이건 정상 작동하는데, 속도 향상을 위해 실행을 시키지 않는다.
        # rsList = df_current_date_goodness.values.tolist()

        # print("makingProduction type(rsList): ", type(rsList))  # <class 'list'>
        # print("makingProduction rsList: \n", rsList)

        # rsList = df2list(df_current_date_goodness)
        # print("makingProduction type(rsList): ", type(rsList))  # <class 'list'>
        # print("makingProduction rsList: \n", rsList)

        # print("리스트로 변환 후 makingProduction type(rsListSum): ", type(rsListSum))  # <class 'list'>
        # print("리스트로 변환 후 makingProduction rsListSum: \n", rsListSum)

        # 2020.03.03 Conclusion. 이건 정상 작동하는데, 속도 향상을 위해 실행을 시키지 않는다.
        # rsListSum.append(rsList)  # 바로 추가...

        # if days <= 1:
        #     print("리스트로 변환 후 makingProduction len(rsListSum): ", len(rsListSum))  # <class 'list'>
        #     print("리스트로 변환 후 makingProduction type(rsListSum): ", type(rsListSum))  # <class 'list'>
        #     print("리스트로 변환 후 makingProduction rsListSum: \n", rsListSum)

        # days = current_date.day  # 이거는 무한 루프 도네... 특히 주의...
        days += 1

    ################################################################################################################
    # '''

    # ********************************************************************************************************
    # ********************************************************************************************************

    # 또한, 같은 화면 customer.html에서, Total Orders 수량을 찍어줘야 하므로,
    # 2020.03.03 Conclusion. 이건 정상 작동하는데, 속도 향상을 위해 실행을 시키지 않는다.
    # total_pp_data_count = len(rsListSum)  # len(df_data_prd_pro_wor1)  # df_data_prd_pro_wor1.count()
    # print("makingProduction total_pp_data_count: ", total_pp_data_count)

    # windll = ctypes.windll.kernel32
    # LANGUAGE_NO = windll.GetUserDefaultUILanguage()  # 1033, 1042
    # LANGUAGE_CODE = locale.windows_locale[windll.GetUserDefaultUILanguage()]  # en_US, ko_KR
    # print("makingProduction LANGUAGE_NO: ", LANGUAGE_NO, ", LANGUAGE_CODE: ", LANGUAGE_CODE)

    # print("makingProduction 리턴 바로 전 LANGUAGE_NO: ", LANGUAGE_NO, ", LANGUAGE_CODE: ", LANGUAGE_CODE)
    # print("makingProduction 리턴 바로 전 products: ", products)
    # print("makingProduction 리턴 바로 전 productsCount: ", productsCount)
    # print("makingProduction 리턴 바로 전 ppDataPeriod: \n", ppDataPeriod)
    # print("makingProduction 리턴 바로 전 ppDataPeriod: \n", ppDataPeriod)

    return ppDataPeriodProcessList, products, productsCount, ppDataPeriod, ppDataPeriodProcessList2, goodnessTotal, volumesTotal


@csrf_exempt
# 2021.02.10 Added. 조건에 맞는 자료만을 만들어서 도로 보낸다.
def makingCapacity(sqlQuerySets, dfSets, revision):

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    # pd.set_option('display.max_colwidth', -1)  # 무슨 Future 경고가 나오네...
    # print("makingCapacity 가져 온 dfSets: \n", dfSets)

    # 제일 먼저 [현재 공정의 근무 일수]를 가져 온다. 사용 예) k = dfSets.loc[[1,5,7], ['revision', 'needshour', 'dpt']]
    # workingdays = dfSets.loc[[0], ['workingdays']]  # 리턴 값이 [DataFrame] Object 임에 주의...
    # print("makingCapacity 가져 온 type(workingdays): ", type(workingdays))  # 리턴 값이 [DataFrame] Object 임에 주의...
    workingdays = dfSets.at[0, 'workingdays']
    if workingdays is None:
        workingdays = 22  # 만약 근무일 값이 없으면, 기본 값으로 [22]일을 준다.
    # print("makingCapacity 가져 온 type(workingdays): ", type(workingdays))
    # print("makingCapacity 가져 온 workingdays: ", workingdays)

    capacityHour8 = workingdays * 8
    capacityHour10 = workingdays * 10
    capacityHour12 = workingdays * 12
    # print("makingCapacity capacityHour8: ", capacityHour8)
    # print("makingCapacity capacityHour10: ", capacityHour10)
    # print("makingCapacity capacityHour12: ", capacityHour12)

    ##########################################################################################################
    # 2021.03.04 Conclusion. groupbyAll = df.groupby(['성별', '교육년수']): 이러면 모든 컬럼이 다 나오네?: doc.mindscale.kr/km/python/12.html
    # 참고: groupbyAll[['근무시간']].mean(): [[]]: 데이터프레임 형식, []: Series 형식.
    # 1. 설비별로 수량을 합산한다. 현재 넘어 온 자료가 제품별로 되어 있다.
    # dictNeedsHour = dfSets.groupby(['revision', 'machine'])['needshour'].sum().reset_index()  # dict type
    # dfNeedsHourIndexFalse = dfSets.groupby(by=['revision', 'machine'], as_index=False)['needshour'].sum().reset_index()  # df type
    # dfNeedsHour = dfSets.groupby(by=['revision', 'machine'], as_index=False)['needshour'].sum()  # df type
    # 2021.03.05 Conclusion. 2개 컬럼도 동시에 합산이 되네...
    # 1. [생산 계획 수량.dpt]와 [실제 생산 소요 시간.needshour]를 [작업반명.machine_kor+코드.machine]를 기준으로 합산한다.
    #   : 혹시나 1일에 2개 설비에서 [같은 제품]을 생산한 경우에, 1개 로우로 정리한다.
    dfSetsGroupBy = dfSets.groupby(by=['machine_kor', 'machine'], as_index=False)['needshour', 'dpt'].sum().reset_index()  # df type
    # print("makingCapacity 안 지정하고 합계 type(dfNeedsHourIndexFalse): ", type(dfSetsGroupBy))
    # print("makingCapacity 안 지정하고 합계 dfNeedsHourIndexFalse: \n", dfSetsGroupBy)
    # dfNeedsHourIndexTrue = dfSets.groupby(by=['revision', 'machine'], as_index=True)['needshour'].sum().reset_index()  # df type
    # dfNeedsHourIndexTrue = dfSets.groupby(by=['revision', 'machine'], as_index=True)['needshour'].sum()  # df type
    # print("makingCapacity 안 지정하고 합계 dfNeedsHourIndexTrue: \n", dfNeedsHourIndexTrue)

    # dfDptIndexFalse = dfSets.groupby(by=['revision', 'machine'], as_index=False)['dpt'].sum().reset_index()  # df type
    # dfPlanQty = dfSets.groupby(by=['revision', 'machine'], as_index=False)['dpt'].sum()  # df type
    # dfPlanQty = dfSets.groupby(by=['machine'], as_index=False)['dpt'].sum()  # df type
    # dfDptIndexTrue = dfSets.groupby(by=['revision', 'machine'], as_index=True)['dpt'].sum().reset_index()  # df type
    # print("makingCapacitydpt 컬럼만 지정 합계 dfPlanQty: \n", dfPlanQty)

    # dfDpt = dfSets.groupby(by=['revision', 'machine'], as_index=True)['dpt'].sum()  # 결론: 여기는 [index] 컬럼이 생기지 않는다. 그럼 아래에서 sum() 함수에서 에러가 발생한다.
    # print("makingCapacitydpt 컬럼만 지정 합계 dfDpt: \n", dfDpt)

    # Dataframe.데이터프레임 컬럼 합산
    # 1. 원본 [dfSets]에서 합산: 아래에서 원본 df 총합과 그룹화한 df 총합이 맞는지 확인하기 위함. 특별한 의미는 없음.
    needshourSum = dfSets['needshour'].sum()
    planQtySum = dfSets['dpt'].sum()
    # print("makingCapacity 원본 dfSets_needshourSum: ", needshourSum)
    # print("makingCapacity 원본 dfSets_planQtySum: ", planQtySum)
    # 2. [as_index=False]로 groupby() 후 합산
    # dfNeedsHourIndexFalseSum = dfNeedsHourIndexFalse['needshour'].sum()
    # print("makingCapacity dfNeedsHourIndexFalseSum: ", dfNeedsHourIndexFalseSum)
    # 2021.03.04 Conclusion. 이상 실험 결과는 모두 동일하게 값이 나온다. [needshourSum == dfNeedsHourIndexFalseSum == dfNeedsIndexTrueSum]
    # 그러나 맨 뒤의 옵션 [reset_index()]를 사용하지 않는 경우에서는, [as_index=True]로 했을 때, 아래 sum() 함수에서 에러가 발생한다.
    # 그러므로 앞으로는 아래 2.항을 사용한다.
    # 3. [as_index=True]로 groupby() 후 합산
    needsHourSum = dfSetsGroupBy['needshour'].sum()
    planQtySum = dfSetsGroupBy['dpt'].sum()
    # print("makingCapacity groupby 후 dfNeedsHour_needsHourSum: ", needsHourSum)
    # print("makingCapacity groupby 후 dfPlanQty_planQtySum: ", planQtySum)
    # planQtySum = dfPlanQty['dpt'].sum()
    # print("makingCapacity dpt로 groupby 후 dfPlanQty_planQtySum: ", planQtySum)

    # dfSetsGroupBy['capacityHour8'] = dfSets['workingdays'] * 8  # 반드시 [str] 타입으로 추가해야만, 전체 로우가 잘 추가된다.
    dfSetsGroupBy['capacityhour8'] = str(capacityHour8)  # 반드시 [str] 타입으로 추가해야만, 전체 로우가 잘 추가된다.
    dfSetsGroupBy['capacityhour10'] = str(capacityHour10)
    dfSetsGroupBy['capacityhour12'] = str(capacityHour12)
    # print("makingCapacity dfSetsGroupBy: \n", dfSetsGroupBy)

    # 가동률은 [capacityHour8] 기준으로 처리한다???
    # needshourSeries = dfSetsGroupBy['needshour']  # Series type
    # capacityHour8Series = dfSetsGroupBy['capacityhour8']
    # print("makingCapacity type(needshourSeries): ", type(needshourSeries))
    # print("makingCapacity needshourSeries: \n", needshourSeries)
    # print("makingCapacity capacityHour8Series: \n", capacityHour8Series)

    dfSetsGroupBy['availability8'] = (pd.to_numeric(dfSetsGroupBy['needshour']) / pd.to_numeric(dfSetsGroupBy['capacityhour8']) * 100).__round__(1).astype(str)
    dfSetsGroupBy['availability10'] = (pd.to_numeric(dfSetsGroupBy['needshour']) / pd.to_numeric(dfSetsGroupBy['capacityhour10']) * 100).__round__(1).astype(str)
    dfSetsGroupBy['availability12'] = (pd.to_numeric(dfSetsGroupBy['needshour']) / pd.to_numeric(dfSetsGroupBy['capacityhour12']) * 100).__round__(1).astype(str)
    # dfSetsGroupBy['availability8'] = (pd.to_numeric(dfSetsGroupBy['needshour']) / pd.to_numeric(dfSetsGroupBy['capacityhour8']) * 100).astype(str).str.extract(r'([A-Z]*)')  # 이건 값을 모두 지우네...

    # 여기 아래 내용은 모두 에러 나네요...
    # dfSetsGroupBy[:, 'availability8'] = dfSetsGroupBy.where(dfSetsGroupBy.round(0).astype(str).add('%'))
    # dfSetsGroupBy['availability8'] = dfSetsGroupBy[['needshour']] / dfSetsGroupBy[['capacityHour8']]
    # dfSetsGroupBy['availability8'] = np.float(dfSetsGroupBy['needshour']) + np.float(dfSetsGroupBy['capacityHour8'])
    # dfSetsGroupBy['availability8'] = float(dfSetsGroupBy['needshour']) / float(dfSetsGroupBy['capacityHour8']) * 100
    # dfSetsGroupBy['availability8'] = dfSetsGroupBy.apply(lambda x: float(dfSetsGroupBy['needshour']) / float(dfSetsGroupBy['capacityHour8']), axis=1)
    # dfSetsGroupBy['availability8'] = dfSetsGroupBy.apply((dfSetsGroupBy['needshour'] / dfSetsGroupBy['capacityHour8'] * 100), axis=1)

    # 2021.03.06 Added. 윤여사 요청.
    dfSetsGroupBy['needsdays8'] = (pd.to_numeric(dfSetsGroupBy['needshour']) / 8).__round__(1).astype(str)
    dfSetsGroupBy['needsdays10'] = (pd.to_numeric(dfSetsGroupBy['needshour']) / 10).__round__(1).astype(str)
    dfSetsGroupBy['needsdays12'] = (pd.to_numeric(dfSetsGroupBy['needshour']) / 12).__round__(1).astype(str)

    # 판다스에서 소숫점처리하기
    # 기본값은 6자리
    # pd.options.display.float_format = '{:.소숫점자리수f}'.format
    # 예) 소숫점 2번째자리까지 표시
    # pd.options.display.float_format = '{:.2f}'.format
    # print("makingCapacity dfSetsGroupBy: \n", dfSetsGroupBy)

    # 6. 최종적으로 html 쪽으로 넘겨줄 수 있도록, 리스트로 변경해 준다.
    capacityList0 = dfSetsGroupBy.fillna(0)  # NaN 값을 [0]으로 치환. 반드시 [새로운 DataFrame 명] 사용...
    capacityList = capacityList0.values.tolist()
    # capacityList22 = dfSetsGroupBy.fillna(0)  # NaN 값을 [0]으로 치환. 반드시 [새로운 DataFrame 명] 사용...
    # capacityList2 = capacityList22.values.tolist()
    # print("makingCapacity::len(capacityList): ", len(capacityList))
    # print("종합표 리스트 정리 후 makingCapacity::type(capacityList): ", type(capacityList))
    # print("종합표 리스트 정리 후 makingCapacity::capacityList: \n", capacityList)

    # machine = [item('machine_kor') for item('machine_kor') in capacityList]
    machineList = dfSetsGroupBy['machine_kor'].tolist()
    machineListCount = len(machineList)
    needsHourList = dfSetsGroupBy['needshour'].tolist()
    planQtyList = dfSetsGroupBy['dpt'].tolist()
    capacityHour8List = dfSetsGroupBy['capacityhour8'].tolist()
    capacityHour10List = dfSetsGroupBy['capacityhour10'].tolist()
    capacityHour12List = dfSetsGroupBy['capacityhour12'].tolist()
    # print("makingCapacity type(machineList): ", type(machineList))
    # print("makingCapacity machineList: \n", machineList)
    # print("makingCapacity machineListCount: ", machineListCount)

    return capacityList, machineList, machineListCount, needsHourList, planQtyList, \
           capacityHour8List, capacityHour10List, capacityHour12List, needsHourSum, planQtySum, dfSetsGroupBy


# 2021.02.10 Added. 조건에 맞는 자료만을 만들어서 도로 보낸다.
@csrf_exempt
def makingCurrent(sqlQuerySets, dfSets, dfSetsPlanQty, revision):
    # A. 먼저 [생산 능력 분석.사업 계획 자료.생산 계획 수량.ForecastHistory.dsp]을 자료를 가져온다.
    #     1. ForecastHistoryDay.NFxx: 먼저 선택한 달의 1개월간 생산 실적 누계 수량를 불러온다.
    #     2. 이건 필요 없음 => 아니다, 일단 가져온다: ForecastHistoryDay.DMxx: 먼저 선택한 달의 1개월간 생산 실적 수량를 불러온다.
    #     3. ForecastHistoryDay.Dpt: 해달 월의 생산 계획 총량을 가져온다.
    # B. [생산 실적 자료.ProductionActual] 자료를 가져와서, [dfSetsPlanQtyGroupBy.dpt.생산 계획 수량] 컬럼을 추가한다.
    #     1. 2021.03.13 Added. [dfSetsPlanQtyGroupBy.dpt.생산 계획 수량] 컬럼을 추가한다.

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    # pd.set_option('display.max_colwidth', -1)  # 무슨 Future 경고가 나오네...

    # print("000 makingCapacity 가져 온 생산 계획 자료 dfSetsPlanQty: \n", dfSetsPlanQty)

    yearCurrent = revision[:4]
    monthCurrent = revision[-2:]
    # print("makingCurrent 11 yearCurrent: ", yearCurrent, "monthCurrent: ", monthCurrent, ", revision: ", revision)

    # 해당 월도의 마지막 날짜를 찾는다.
    maxDate = getMaxDate(yearCurrent, monthCurrent)
    print("makingCurrent 55 maxDate: ", maxDate)

    # print("makingCurrent 55 dfSetsPlanQty: \n", dfSetsPlanQty)
    # print("makingCurrent 55 len(dfSetsPlanQty): ", len(dfSetsPlanQty))

    # A. 먼저 [생산 능력 분석.사업 계획 자료.생산 계획 수량.ForecastHistory.dsp]을 자료를 가져온다.
    if len(dfSetsPlanQty) == 0:
        print("makingCurrent 56 생산 계획 자료가 전혀 없습니다. 다시 확인하시오!")
        planQtyByCodeList = []
        planqtySum = 0
        ppDataPeriod = []
        products = []
        goodnessList = []
        goodnessCumsumList = []
        planqtyFinalList = []
        dfSetsCumsum = 0
        planQtyByCodeList = []
        goodnessSum = 0
        goodnessCumsumSum = 0
        planqtySum = 0

        return ppDataPeriod, products, goodnessList, goodnessCumsumList, planqtyFinalList, \
               dfSetsCumsum, planQtyByCodeList, goodnessSum, goodnessCumsumSum, planqtySum
    else:
        # dfSetsPlanQtyGroupBy = dfSetsPlanQty.groupby(by=['code', 'step9'], as_index=False)['dpt'].apply(pd.to_numeric).sum().reset_index()
        dfSetsPlanQtyGroupBy = dfSetsPlanQty.groupby(by=['code', 'step9', 'processinfo'], as_index=False)['dpt'].sum().reset_index()
        # dfSetsPlanQtyGroupBy = dfSetsPlanQty.groupby(by=['code', 'step9'], as_index=False)['dpt'].sum().reset_index()
        # dfSetsPlanQtyGroupBy = dfSetsPlanQty.groupby(by=['code'], as_index=False)['dpt'].sum().reset_index()  # ['code', 'dpt'] 딱 2개 컬럼만으로 만든다.
        # dfSetsPlanQtyGroupBy = dfSetsPlanQty.groupby(by=['codespec'], as_index=False)['dpt'].sum().reset_index()  # [codespec]은 [그래프.legend]에서 너무 길다.
        # print("0 makingCurrent groupby 후 dfSetsPlanQtyGroupBy: \n", dfSetsPlanQtyGroupBy)
        # print("0 makingCurrent groupby 후 type(dfSetsPlanQtyGroupBy): ", type(dfSetsPlanQtyGroupBy))

        # [yeraCurrent-monthCurrent-00] 강제 날짜로 넣는다.
        # ===> zeroDateStr = yearCurrent + "-" + monthCurrent + "-00"
        # ===> dfSetsPlanQtyGroupBy['workdate'] = zeroDateStr
        # print("0 makingCurrent zero 날짜 컬럼 추가 후 dfSetsPlanQtyGroupBy: \n", dfSetsPlanQtyGroupBy)
        # print("0 makingCurrent zero 날짜 컬럼 추가 후 type(dfSetsPlanQtyGroupBy): ", type(dfSetsPlanQtyGroupBy))
        # [processinfo] 강제 날짜로 넣는다.
        # ===> processinfo = ""
        # ===> dfSetsPlanQtyGroupBy['processinfo'] = processinfo
        # print("0 makingCurrent zero 날짜 컬럼 추가 후 dfSetsPlanQtyGroupBy: \n", dfSetsPlanQtyGroupBy)
        # print("0 makingCurrent zero 날짜 컬럼 추가 후 type(dfSetsPlanQtyGroupBy): ", type(dfSetsPlanQtyGroupBy))
        # [yeraCurrent-monthCurrent-00] 강제 날짜로 넣는다.
        # ===> zeroDateStr = yearCurrent + "-" + monthCurrent + "-00"
        # ===> dfSetsPlanQtyGroupBy['workdate'] = zeroDateStr
        # print("0 makingCurrent zero 날짜 컬럼 추가 후 dfSetsPlanQtyGroupBy: \n", dfSetsPlanQtyGroupBy)
        # print("0 makingCurrent zero 날짜 컬럼 추가 후 type(dfSetsPlanQtyGroupBy): ", type(dfSetsPlanQtyGroupBy))

        planQtyByCodeList = dfSetsPlanQtyGroupBy.values.tolist()
        # print("1 makingCurrent 소트 후 planQtyByCodeList: \n", planQtyByCodeList)
        # print("1 makingCurrent type(planQtyByCodeList): ", type(planQtyByCodeList))
        planqtySum = dfSetsPlanQtyGroupBy['dpt'].sum()
        # print("1 makingCurrent 소트 후 planqtySum: \n", planqtySum)

    # B. [생산 실적 자료.ProductionActual] 자료를 가져와서, [dfSetsPlanQtyGroupBy.dpt.생산 계획 수량] 컬럼을 추가한다.
    # ############################################################################################################
    # 1. 2021.03.13 Added. [dfSetsPlanQtyGroupBy.dpt.생산 계획 수량] 컬럼을 추가한다.
    # Full Outer Join : Left Outer Join + Right Outer Join, 양쪽 df 모두 합친다. 기준 칼럼 = 'id'
    # df_outer = pd.merge(df1, df2, on='id', how='outer')
    # Out Join 이면서, 컬럼명에 x, y가 붙는다.
    # df_outer = pd.merge(df1, df2, left_on='id', right_on='on', how='outer', suffixes=('_left', '_right'))
    # Inner Join : 양쪽 df에 기준 컬럼인 'id' 값이 모두 존재하는 레코드만 합친다.
    # df_inner = pd.merge(df1, df2, on='id', how='inner')
    # Right Join : 우측 df2.id를 기준으로 합친다. 우측 'id' 값이 없는 좌측 df1 레코드들은 합쳐지지 않음에 주의...
    # df_right = pd.merge(df1, df2, on='id', how='right')
    # Left Join : 좌측 df1.id를 기준으로 합친다. 좌측 'id' 값이 없는 우측 df2 레크드들은 합쳐지지 않음에 주의...
    # df_left = pd.merge(df1, df2, on='id', how='left')
    # DataFrame.merge(합칠 DataFrame, how="inner", on=None, left_on=None, right_on=None, left_index=False, right_index=False)
    # dfSetsMergedPlan = pd.merge(dfSets, dfSetsPlanQtyGroupBy, on="code", how="outer")

    # 2. 2021.03.13 Conclusion. pd.merge()는 'code' 컬럼을 기준으로 데이터를 합치는 것이고,
    #    여기서는 순수하게 [yyyy-mm-00] 날짜로 생산 계획 자료를 로우 추가해야 하므로,
    #    concat()을 사용해야 한다.
    # print("22 makingCurrent 계획 수량 추가 전 dfSets: \n", dfSets)
    # print("22 makingCurrent 계획 수량 추가 전 type(dfSets): ", type(dfSets))
    # ===> dfSetsConcatedPlan = pd.concat([dfSets, dfSetsPlanQtyGroupBy])
    # print("22 makingCurrent 계획 수량 추가 후 dfSetsConcatedPlan: \n", dfSetsConcatedPlan)
    # print("22 makingCurrent 계획 수량 추가 후 type(dfSetsConcatedPlan): ", type(dfSetsConcatedPlan))
    # ############################################################################################################

    # 2021.03.13 Added. 위에서는 [yyyy-mm-00] 날짜로 [로우.레코드] 자료를 추가했다면,
    # 아래 쪽은, 모든 로우의 자료를 [workdate.날짜 + code.품번]을 기준으로 [planqty.생산 계획 수량]을 모든 로우에 다 찍어준다.
    # 즉, 위의 방법은, 그래프 x축 맨 왼쪽에 [yyyy-mm-00] 에 [막대 그래프]로 해당 월도의 생산 계획 수량을 그리는 것이고,
    # 아래 방법은, 모든 날짜에 품목별 동일한 계획 수량을 [선 그래프]로 그려 주는 것이다.

    # 1가지만 선택해야 하는 것이므로, 위의 방법은 [주석.# ===> ] 처리한다.

    # ############################################################################################################
    # 아래에서 처리...
    # ############################################################################################################


    # 아래 피벗 테이블 [컬럼] 값으로 [날짜] 텍스트를 뽑는다.
    # xDateList = []
    # for i in range(1, maxDate):
    #     d = yearCurrent + "-" + monthCurrent + "-" + str(i).zfill(2)
    #     xDateList.append(d)
    #     print("makingCurrent 55 maxDate: ", maxDate)

    # 가져온 2개의 데이터프레임 컬럼 현황.
    # dfSets.columns = ['revision', 'code', 'step9', 'workingdays', 'ct', 'needsday', 'needshour', 'uph',
    #                   'division', 'upd', 'stockfirst', 'dpt', 'dft', 'dmt', 'dst', 'npt', 'nft', 'nst',
    #                   'machine', 'machine_kor', 'machine_loc', 'process', 'process_kor', 'process_loc']
    # dfSets.columns = ['workdate', 'productionactualno', 'code', 'step9', 'goodness', 'badness', 'volume', 'schedule',
    #                   'codetwins',
    #                   'process', 'process_kor', 'process_loc', 'machine', 'groups', 'workfrom', 'workto',
    #                   'standardtime']
    # print("makingCurrent 소트 전 dfSets: \n", dfSets)

    # dfSetsSort = dfSets.sort_values(by=['productionactualno'], ascending=False)
    # dfSetsSort = dfSets.sort_values(by=['productionactualno'], ascending=True)
    # dfSetsSort = dfSets.sort_values(by=['productionactualno'])  # Default: [ascending=True]  # 아래와 같은 결과...
    # ===> dfSetsSorted = dfSetsConcatedPlan.sort_values(['workdate', 'code'])  # Default: [ascending=True]  # 위와 같은 결과...
    # dfSetsSorted = dfSets.sort_values(by=['workdate', 'code']).reset_index()  # Default: [ascending=True]  # 위와 같은 결과...
    dfSets.sort_values(by=['workdate', 'code'], inplace=True)  # Default: [ascending=True]  # 위와 같은 결과...
    # print("00 makingCurrent 소트 후 dfSets: \n", dfSets)
    # print("00 makingCurrent type(dfSets): ", type(dfSets))

    # dfSetsGroupBy = dfSetsSorted.groupby(by=['workdate', 'step9'],as_index=False)['goodness', 'badness'].sum().reset_index()
    # print("00 makingCurrent type(dfSetsGroupBy): ", type(dfSetsGroupBy))
    # print("00 makingCurrent dfSetsGroupBy: \n", dfSetsGroupBy)
    # 여기 위와 아래는 같은 결과 값이 나온다. 아래 대괄호가 2개 [[]] 인 것에 특히 주의... 1개 일 경우: Future Warning 발생...

    # 2021.03.10 Conclusion. ***** 중요한 발견 *****
    # reset_index()를 주면서 생긴, 왼쪽 [index] 컬럼이 2개 이상 생기면, to_json() 파싱할 때, 에러가 나네.. 그래서 여기서는 생략.
    # dfSetsGroupBy = dfSetsSorted.groupby(by=['workdate', 'code', 'step9'], as_index=False)[['goodness', 'badness', 'productionactualno', 'process']].sum().reset_index()
    # ===> dfSetsGroupBy = dfSetsSorted.groupby(by=['workdate', 'code', 'step9'], as_index=False)[['goodness', 'badness', 'dpt', 'productionactualno', 'processinfo']].sum()
    dfSetsGroupBy = dfSets.groupby(by=['workdate', 'code', 'step9'], as_index=False)[['goodness', 'badness', 'productionactualno', 'processinfo']].sum()
    # dfSetsGroupBy = dfSetsSorted.groupby(['workdate', 'code', 'step9'])[['goodness', 'badness', 'productionactualno', 'process']].sum().reset_index()
    # print("11 makingCurrent dfSetsGroupBy: \n", dfSetsGroupBy)
    # print("11 makingCurrent type(dfSetsGroupBy): ", type(dfSetsGroupBy))

    # 2021.03.09 Conclusion. 아래 모두 [전체 자료를 누계] 낸다. ['workdate', 'code']별로는 누계를 못 내네..
    # dfSetsGroupByCumSum = dfSetsGroupBy.sort_values(['workdate', 'code']).reset_index(drop=True)
    # dfSetsGroupByCumSum = dfSetsGroupBy.sort_values(['code', 'workdate']).reset_index(drop=True)

    # 여기는 아직은 사용하지 않는다...
    # dfSetsGroupByCumSum = dfSetsGroupBy.sort_values(['code']).reset_index(drop=True)

    # print("77 makingCurrent 피벗 후 type(dfSetsGroupByCumSum): ", type(dfSetsGroupByCumSum))
    # print("77 makingCurrent 피벗 후 dfSetsGroupByCumSum: \n", dfSetsGroupByCumSum)
    # dfSetsGroupByCumSum["goodnesscumsum"] = dfSetsGroupBy.groupby(['code'])[['goodness']].cumsum(axis=0)
    # dfSetsGroupByCumSum["goodnesscumsum"] = dfSetsGroupBy.groupby(['code'])['goodness'].astype(float).cumsum(axis=0)
    # dfSetsGroupByCumSum["goodnesscumsum"] = dfSetsGroupBy.groupby(['code', 'workdate'])['goodness'].apply(pd.to_numeric).cumsum(axis=0)
    # dfSetsGroupByCumSum["goodnesscumsum"] = dfSetsGroupBy.groupby(by=['workdate', 'code'])['goodness'].apply(pd.to_numeric).cumsum(axis=0)
    # dfSetsGroupByCumSum["goodnesscumsum"] = dfSetsGroupBy.groupby(by=['workdate', 'code'])['goodness'].apply(pd.to_numeric).cumsum()
    # dfSetsGroupBy["goodnesscumsum"] = dfSetsGroupBy.groupby(by=['code', 'workdate'])['goodness'].apply(pd.to_numeric).cumsum()
    # dfSetsGroupBy["goodnesscumsum"] = dfSetsGroupBy.groupby(by=['code'])['goodness'].apply(pd.to_numeric).cumsum()
    # dfSetsGroupBy["goodnesscumsum"] = dfSetsGroupBy.groupby(by=['workdate'])['goodness'].apply(pd.to_numeric).cumsum()
    # print("88 makingCurrent 피벗 후 type(dfSetsGroupBy): ", type(dfSetsGroupBy))
    # print("88 makingCurrent 피벗 후 dfSetsGroupBy: \n", dfSetsGroupBy)

    # 2021.03.08 Conclusion. Pivot.피벗 테이블 생성...
    # WorkDate      Code        Goodness            ===> Pivot ===>     WorkDate    2021-03-01  2021-03-02  2021-03-03
    # 2021.03.01  8000011111        504                                 8000011111      504         654         ...
    # 2021.03.01  8000022222        325                                 8000022222      325         456
    # 2021.03.02  8000011111        654
    # 2021.03.02  8000022222        456
    # 2021.03.03  ...
    # 여기서는 Pivot.피벗이 필요 없음...
    # dfSetsGroupByPivoted = dfSetsGroupBy.pivot(columns="workdate", index=["code", "step9"], values="goodness").fillna(0).reset_index()
    # print("22 makingCurrent 피벗 후 type(dfSetsGroupByPivoted): ", type(dfSetsGroupByPivoted))
    # print("22 makingCurrent 피벗 후 dfSetsGroupByPivoted: \n", dfSetsGroupByPivoted)

    # dfSetsGroupByPivotedCumSum = dfSetsGroupByPivoted.cumsum(axis=1)
    # dfSetsGroupByPivoted.iloc[:, 3:6].cumsum(axis=1).reset_index()
    # # dfSetsGroupByPivoted.loc[3:, '3':'4'].cumsum(axis=1)
    # print("33 makingCurrent 피벗 누계 후 type(dfSetsGroupByPivoted): ", type(dfSetsGroupByPivoted))
    # print("33 makingCurrent 피벗 누계 후 dfSetsGroupByPivoted: \n", dfSetsGroupByPivoted)

    # dfSetsGroupByCumSum = pd.pivot_table(dfSetsGroupBy, values=["goodness"], index=["workdate"], columns=["step9"], aggfunc=np.sum)  # 이건 안 되네...
    # dfSetsGroupByCumSum.cumsum().reset_index()
    # print("77 makingCurrent type(dfSetsGroupByCumSum): ", type(dfSetsGroupByCumSum))
    # print("77 makingCurrent dfSetsGroupByCumSum: \n", dfSetsGroupByCumSum)

    # ############################################################################################################
    # 모든 로우의 자료를 [workdate.날짜 + code.품번]을 기준으로 [dpt=planqty.생산 계획 수량]을 모든 로우에 다 찍어준다.
    # dfSetsGroupBy['planqty'] = 0  # 누계 컬럼 이름. ===> 여기서 컬럼을 더하지 말고, 보낸다. 함수에서 더해야 하기 때문이다.
    # ############################################################################################################
    cumusumColumnName = "goodnesscumsum"  # 누계 컬럼 이름.
    dfSetsCumsum = makeCumulativeColumn(dfSetsGroupBy, planQtyByCodeList, revision, cumusumColumnName)
    # print("makingCurrent 누계 후 dfSetsCumsum: \n", dfSetsCumsum)
    # print("makingCurrent 누계 후 type(dfSetsCumsum): ", type(dfSetsCumsum))

    goodnessSum = dfSetsCumsum['goodness'].sum()
    goodnessCumsumSum = dfSetsCumsum['goodnesscumsum'].sum()
    print("66 makingCurrent goodnessSum: ", goodnessSum)
    print("66 makingCurrent goodnessCumsumSum: ", goodnessCumsumSum)

    # 6. 최종적으로 html 쪽으로 넘겨줄 수 있도록, 리스트로 변경해 준다.
    #    1) 날짜별 제품 생산 수량(goodness)을 막대 그래프 용으로, goodnessList[].
    #    2) 날짜별 제품 생산 누계 수량(goodnesscumsum)을 선 그래프 용으로, goodnesscumsumList[].
    #    3) table_pp_current <table> 태그에 찍을,
    #       [jsonCurrent]를 만들기 위해, [workdate, step9, goodness, goodnesscumsum] 형식의 dfSetsCumsum.

    # currentList = dfSetsCumsum.values.tolist()  # 이것은 2021.03.10 기준, 아직까지는 쓸 일이 없을 것 같은데... df 자체를 그대로 jsonCurrent로 파싱...
    # print("makingCurrent currentList: \n", currentList)

    # 날짜별 [생산 실적 수량] 리스트.
    # dfSetsPivoted = pd.pivot_table(dfSetsCumsum, index=["workdate"], columns=["code", "step9"], values=["goodness"], aggfunc=int).fillna(0).reset_index()
    dfSetsPivotedTemp = pd.pivot_table(dfSetsCumsum, index=["workdate"], columns=["step9"], values=["goodness"], aggfunc=int).fillna(0).reset_index()
    print("77 makingCurrent 피벗 후 dfSetsPivotedTemp: \n", dfSetsPivotedTemp)
    print("77 makingCurrent 피벗 후 type(dfSetsPivotedTemp): ", type(dfSetsPivotedTemp))

    # 1) 날짜별 제품 생산 수량(goodness)을 막대 그래프 용으로, goodnessList[].
    #    그래프 막대기를 그리기 위해, 날짜별 제품별 goodness.생산 수량을 리스트를 만든다. 막대 그래프.
    goodnessList = dfSetsPivotedTemp.values.tolist()
    # print("makingCurrent 피벗 후 리스트 type(goodnessList): ", type(goodnessList))
    # print("makingCurrent 피벗 후 리스트 goodnessList: \n", goodnessList)

    # 우선, x축 용의 날짜 값과 legend 용의 [제품명]을 뽑아 낸다.
    # 1. [workdate] 날짜 자료만 따로 리스트로 만들어 보내서, 그래프의 [Labels]로 활용하게 한다.
    #    최초 [ppp_process.생산 실적 분석] 로직에서, 날짜 값을 괄호 2개로 처리해서, process.html로 넘겼기 때문에,
    #    여기 [ppp_current.생산 진도 관리] 로직에서도, 괄호 2개로 처리해서 current.html로 넘겨주게 한다.
    # ppDataPeriod = ppDataPeriodProcessWorkdate.values.tolist()  # [['날짜'],['날짜'],...['날짜']] : 괄호가 2개임에 주의.
    # ppDataPeriod = dfSetsPivotedTemp["workdate"].tolist()  # ['날짜','날짜',...'날짜'] : 괄호가 1개임에 주의.
    # print("1 makingCurrent ppDataPeriod: ", ppDataPeriod)
    ppDataPeriod = [dfSetsPivotedTemp["workdate"].values.tolist()]  # [['날짜'],['날짜'],...['날짜']] : 괄호가 2개임에 주의.
    # print("2 makingCurrent ppDataPeriod: ", ppDataPeriod)

    # [index]와 [columns]를 바꿔서 pivot_table. : 이것은 2021.03.10 기준, 아직까지는 쓸 일이 없을 것 같은데...
    # 아니다, 바로 아래에서 [productsList.제품 정보]를 만들기 위해서 필요하다. 그래프의 legend 용...
    dfSetsPivoted = pd.pivot_table(dfSetsCumsum, index=["step9"], columns=["workdate"], values=["goodness"],
                                   aggfunc=int).fillna(0).reset_index()
    # print("makingCurrent 피벗 후 type(dfSetsPivoted): ", type(dfSetsPivoted))
    # print("makingCurrent 피벗 후 dfSetsPivoted: \n", dfSetsPivoted)

    # legend 용으로 제품 리스트를 만든다.
    # 1. # 이렇게 처리하면, 그 값이 Serial 형식으로, [index / step9] 이렇게 넘어간다. 이렇게 하면 current.js에서, 처리가 이상하게 된다는 것에 특히 주의...
    # productsList = dfSetsPivoted["step9"]
    # print("makingCurrent productsList: ", productsList)
    # 2. # 이렇게 처리하면, ['','',''...]. 반드시 이런 형식으로 처리해야 한다.
    products = dfSetsPivoted["step9"].values.tolist()
    # print("makingCurrent productsList: ", productsList)

    # 생산 실적 누계 수량 데이터프레임을 리스트로 전환. : 이게 의미가 있나? 데이터프레임을 json 파싱해서 보내는 것이 좋을 듯...
    # goodnessByCodeList = dfSetsPivoted.values.tolist()
    # print("makingCurrent goodnessByCodeList: ", goodnessByCodeList)

    # 날짜별 [생산 실적 누계] 리스트: 그냥은 안 되고, [goodnesscumsum] 필드만 뽑아서 처리한다.
    # dfSetsCumsumOnly = dfSetsCumsum["workdate", "step9", "goodnesscumsum"].reset_index()
    # dfSetsCumsumPivoted = pd.pivot_table(dfSetsCumsum, index=["workdate"], columns=["code", "step9"], values=["goodnesscumsum"], aggfunc=int).fillna(0).reset_index()
    # dfSetsCumsumPivoted = pd.pivot_table(dfSetsCumsumOnly, index=["workdate"], columns=["step9"], values=["goodnesscumsum"], aggfunc=int).fillna(0).reset_index()

    dfSetsCumsumPivoted = pd.pivot_table(dfSetsCumsum, index=["workdate"], columns=["step9"], values=["goodnesscumsum"],
                                         aggfunc=int).fillna(0).reset_index()
    # print("makingCurrent 피벗 후 type(dfSetsPivotedTemp): ", type(dfSetsPivotedTemp))
    # print("makingCurrent 피벗 후 dfSetsPivotedTemp: \n", dfSetsPivotedTemp)

    # [index]와 [columns]를 바꿔서 pivot_table.: 이것은 2021.03.10 기준, 아직까지는 쓸 일이 없을 것 같은데. 이것은 진짜 불필요.
    # dfSetsCumsumPivoted = pd.pivot_table(dfSetsCumsum, index=["step9"], columns=["workdate"], values=["goodnesscumsum"],
    #                                      aggfunc=int).fillna(0).reset_index()
    # print("88 makingCurrent 피벗 후 type(dfSetsCumsumPivoted): ", type(dfSetsCumsumPivoted))
    # print("88 makingCurrent 피벗 후 dfSetsCumsumPivoted: \n", dfSetsCumsumPivoted)

    # 2) 생산 실적 누계 수량 데이터프레임을 리스트로 전환.
    #    그래프 막대기를 그리기 위해, 날짜별 제품별 goodnesscumsum.생산 누계 수량을 리스트를 만든다. 선 그래프.
    goodnessCumsumList = dfSetsCumsumPivoted.values.tolist()
    # print("makingCurrent 피벗 후 리스트 type(goodnessCumsumList): ", type(goodnessCumsumList))
    # print("makingCurrent 피벗 후 리스트 goodnessCumsumList: \n", goodnessCumsumList)

    dfSetsPlanQtyPivoted = pd.pivot_table(dfSetsCumsum, index=["workdate"], columns=["step9"], values=["planqty"],
                                         aggfunc=int).fillna(0).reset_index()
    # print("makingCurrent 피벗 후 type(dfSetsPlanQtyPivoted): ", type(dfSetsPlanQtyPivoted))
    # print("makingCurrent 피벗 후 dfSetsPlanQtyPivoted: \n", dfSetsPlanQtyPivoted)

    planqtyFinalList = dfSetsPlanQtyPivoted.values.tolist()
    # print("makingCurrent 피벗 후 리스트 type(planqtyFinalList): ", type(planqtyFinalList))
    # print("makingCurrent 피벗 후 리스트 planqtyFinalList: \n", planqtyFinalList)

    return ppDataPeriod, products, goodnessList, goodnessCumsumList, planqtyFinalList, \
           dfSetsCumsum, planQtyByCodeList, goodnessSum, goodnessCumsumSum, planqtySum


class Index(View):
    def get(self, request):
        print("views.py::Index::request: ", request)
        # return render(request, 'ppp/dashboard.html')
        return render(request, 'ppp/index.html')

@csrf_exempt
def sudoku(request):
    context = {}
    return render(request, 'ppp/index_sudoku.html', context)


# 출처: https://cholol.tistory.com/454 [IT, I Think ]
# ▷ 일별, 월별 데이터 뽑기
# 이제 로그데이터를 바탕으로 통계 페이지를 만들 예정입니다. 가장 간단하게 일별 통계를 먼저 만들껀데...
# dJango에서 쿼리 셋으로 날짜별 count를 출력할 수 있을지 모르겠네요. 일단 구글링 꼬~
# 구글링 결과 annotate를 사용해서 group by 효과를 볼 수 있는 쿼리 셋을 만들 수 있다고 합니다. 대략적으로 아래와 같이 만들면...

# adminpage/views.py
from django.db.models.functions import TruncMonth, TruncDate
# def statisticslogs(request):
#     stat_type = request.GET.get('stat_type')
#     if stat_type == 'M':
#         stats = Log.objects \
#             .annotate(stat_date=TruncMonth('log_date')) \
#             .values('stat_date') \
#             .annotate(stat_count=Count('log_userid')).values('stat_date', 'stat_count')
#         else:
#             stats = Log.objects \
#                 .annotate(stat_date=TruncDate('log_date')) \
#                 .values('stat_date') \
#                 .annotate(stat_count=Count('log_userid')).values('stat_date', 'stat_count')
#
#     context = {'stats': stats}
#     return render(request, 'adminpage/statistics_logs.html', context)

# 위에서는 [datetimepicker]이고, 아래는 [datepicker] 임에 유의...


def statisticslogs(request):
    stat_type = request.GET.get('stat_type')
    stat_gbn = request.GET.get('optionRadios')
    to_date = request.GET.get('to_date')
    from_date = request.GET.get('from_date')
    if stat_type == 'M':
        if stat_gbn == 'period':
            stats = Log.objects \
                .filter(log_date__range=[from_date, to_date]) \
                .annotate(stat_date=TruncMonth('log_date')) \
                .values('stat_date') \
                .annotate(stat_count=Count('log_userid')).values('stat_date', 'stat_count')
        else:
            stats = Log.objects \
                .annotate(stat_date=TruncMonth('log_date')) \
                .values('stat_date') \
                .annotate(stat_count=Count('log_userid')).values('stat_date', 'stat_count')
    else:
        if stat_gbn == 'period':
            stats = Log.objects \
                .filter(log_date__range=[from_date, to_date])\
                .annotate(stat_date=TruncDate('log_date')) \
                .values('stat_date') \
                .annotate(stat_count=Count('log_userid')).values('stat_date', 'stat_count')
        else:
            stats = Log.objects \
                .annotate(stat_date=TruncDate('log_date')) \
                .values('stat_date') \
                .annotate(stat_count=Count('log_userid')).values('stat_date', 'stat_count')
        context = {'stats': stats, 'stat_type': stat_type, 'optionRadios': stat_gbn, 'to_date': to_date, 'from_date': from_date}
        return render(request, 'adminpage/statistics_logs.html', context)


class ListSubjects(ListView):
    template_name = 'home_teacher.html'
    model = Student

    def get(self, request, *args, **kwargs):
        name = request.GET['name']
        student_subjects = Student.objects.get(name=name)
        subjects = student_subjects.subject_student.all()
        data = serializers.serialize('json', subjects, fields=('name', 'number_credits'))
        return HttpResponse(data, content_type='application/json')


@csrf_exempt
def ppp_capacity(request):
    global fromDate, toDate, processCode

    # 1. 설비 자료를 가져온다.
    # 2. ForecastHistoryDay.생산 계획.WorkBaseDay: 생산 CAPACITY 수량: 8h 수량, 10h 수량, 12h 수량 구분
    # 3. ForecastHistoryDay.생산 계획.DPT: 생산 계획 수량을 [설비]별로 합산한다.

    print("\n\n\n\n\nppp_capacity*******************************************************************************************")

    data = dict()
    data['is_valid_post'] = False
    data['is_valid_get'] = False

    if request.method == "POST":
        if len(request.POST) > 0:
            data['is_valid_post'] = True
            fromDate = request.POST['fromDate']
            toDate = request.POST['toDate']
            processCode = request.POST['processCode']
            # print("views.py ppp_capacity() POST fromDate: ", fromDate)
            # print("views.py ppp_capacity() POST toDate: ", toDate)
            # print("views.py ppp_capacity() POST processCode: ", processCode)
        else:
            fromDate = fromDateDefault  # "2020.12.01"
            toDate = toDateDefault  # "2020.12.31"
            processCode = "all"  # "all"  # "2100"
            # print("views.py ppp_capacity() POST 0 fromDate: ", fromDate)
            # print("views.py ppp_capacity() POST 0 toDate: ", toDate)
            # print("views.py ppp_capacity() POST 0 processCode: ", processCode)
    elif request.method == "GET":
        if len(request.GET) > 0:
            data['is_valid_get'] = True
            fromDate = request.GET['fromDate']
            toDate = request.GET['toDate']
            processCode = request.GET['processCode']
            # print("views.py ppp_capacity() GET fromDate: ", fromDate)
            # print("views.py ppp_capacity() GET toDate: ", toDate)
            # print("views.py ppp_capacity() GET processCode: ", processCode)
        else:
            fromDate = fromDateDefault  # "2020.12.01"
            toDate = toDateDefault  # "2020.12.31"
            processCode = "all"  # "all"  # "2100"
            # print("views.py ppp_capacity() GET 0 fromDate: ", fromDate)
            # print("views.py ppp_capacity() GET 0 toDate: ", toDate)
            # print("views.py ppp_capacity() GET 0 processCode: ", processCode)

        # print("views.py ppp_capacity() fromDate: ", fromDate)
        # print("views.py ppp_capacity() toDate: ", toDate)
        # print("views.py ppp_capacity() processCode: ", processCode)

    # qr_process, df_process = __process(beInUse)  # Process.objects.get(code=process_code_selected)
    qrProcess, processList,  total_process_count = __getProcess(beInUse)  # Process.objects.get(code=process_code_selected)
    # print("ppp_capacity qrProcess: ", qrProcess)
    # print("ppp_capacity processList: ", processList)
    # print("ppp_capacity total_process_count: ", total_process_count)

    # sqlQuerySets, dfSets = __pp_data_period_process(from_date, to_date, process_code)
    # sqlQuerySets, dfSets = __pp_data_period_process(fromDate, toDate, processCode)

    sqlQuerySets, dfSets, revision, toDate = __getProductionCapacity(fromDate, toDate, processCode)
    # sqlQuerySets, dfSets = __getProductionPerformance(fromDate, toDate, processCode)
    # print("ppp_capacity dfSets: \n", dfSets)
    # print("ppp_capacity type(dfSets): ", type(dfSets))
    # print("ppp_capacity len(dfSets): ", len(dfSets))

    # 2021.02.06 Added. 빈 df 확인.
    if len(sqlQuerySets) == 0:  # len(df.index) == 0: 또는 df.shape[0] == 0: 같은 구문이다.
        # print("views.py ppp_capacity 조건에 맞는 자료가 없습니다. 다시 확인하시오!")
        # print("views.py ppp_capacity 현재 자료를 정리하지 못 했습니다. 관리자에게 문의하시오!", fromDate, " ", toDate, " ", processCode)
        # print("views.py ppp_capacity 해당 자료가 전혀 없습니다!")
        context = {"qrProcess": qrProcess, "products": [], "productsCount": 0,
                   "ppDataPeriodProcessList": [], "ppDataPeriodProcessList2": [],
                   "sqlQuerySets": sqlQuerySets,
                   'fromDate': fromDate, 'toDate': toDate, 'processCode': processCode,
                   "LANGUAGE_NO": LANGUAGE_NO, "goodnessTotal": 0, "volumesTotal": 0}
        return render(request, 'ppp/index.html', context)
        # return redirect("home")

    capacityList, machineList, machineListCount, needsHourList, planQtyList, capacityHour8List, capacityHour10List, \
    capacityHour12List, needsHourSum, planQtySum, dfSetsGroupBy = makingCapacity(sqlQuerySets, dfSets, revision)

    # print("ppp_capacity::type(capacityList): ", type(capacityList))
    # print("ppp_capacity::capacityList: \n", capacityList)
    # print("ppp_capacity::type(process): ", type(process))
    # print("ppp_capacity::process: \n", process)
    # print("ppp_capacity::type(machineList): ", type(machineList))
    # print("ppp_capacity::machineList: \n", machineList)
    # print("ppp_capacity::type(needsHourList): ", type(needsHourList))
    # print("ppp_capacity::needsHourList: \n", needsHourList)
    # print("ppp_capacity::sqlQuerySets: \n", sqlQuerySets)

    print("ppp_capacity dfSetsGroupBy: ", dfSetsGroupBy)
    print("ppp_capacity type(dfSetsGroupBy): ", type(dfSetsGroupBy))

    # 2021.03.05 Added. ***** [df.데이터프레임]은 context로 가기 전에 반드시 [json.load()]로 parsing 처리해야 함 *****
    jsonRecords = dfSetsGroupBy.reset_index().to_json(orient='records')
    jsonCapacity = []
    jsonCapacity = json.loads(jsonRecords)

    context = {"qrProcess": qrProcess, "sqlQuerySets": sqlQuerySets, "jsonCapacity": jsonCapacity,
               "capacityList": capacityList, "machineList": machineList, "machineListCount": machineListCount,
               "needsHourList": needsHourList, "planQtyList": planQtyList, "capacityHour8List": capacityHour8List,
               "capacityHour10List": capacityHour10List, 'capacityHour12List': capacityHour12List,
               'fromDate': fromDate, 'toDate': toDate, 'processCode': processCode, "LANGUAGE_NO": LANGUAGE_NO,
               "needsHourSum": needsHourSum, "planQtySum": planQtySum, "revision": revision}
    # "capacityHour8Sum": capacityHour8Sum, "capacityHour10Sum": capacityHour10Sum, "capacityHour12Sum": capacityHour12Sum}
    # print("views.py ppp_capacity() request: ", request)
    # print("views.py ppp_capacity() request.POST: ", request.POST)
    # print("views.py ppp_capacity() len(request.POST): ", len(request.POST))
    # print("views.py ppp_capacity() request.method: ", request.method)
    # print("views.py ppp_capacity() fromDate: ", fromDate)
    # print("views.py ppp_capacity() toDate: ", toDate)
    # print("views.py ppp_capacity() processCode: ", processCode)

    # return HttpResponse('Customer page')  # [127.0.0.1:8000/about]으로 연결 시, 바로 뿌려준다. ===> 아래 : path('about/', contact),
    return render(request, 'ppp/ppp_capacity.html', context)
    # return JsonResponse(render(request, 'ppp/process.html', context), safe=False)  # 여긴 에러 나네...

    # data['context'] = render_to_string("ppp/process.html", context, request=request)
    # return JsonResponse(data, safe=False)


@csrf_exempt
def ppp_monitoring(request):
    global fromDate, toDate, processCode

    # 1. 설비 자료를 가져온다.
    # 2. ForecastHistoryDay.생산 계획.WorkBaseDay: 생산 CAPACITY 수량: 8h 수량, 10h 수량, 12h 수량 구분
    # 3. ForecastHistoryDay.생산 계획.DPT: 생산 계획 수량을 [설비]별로 합산한다.

    print("\n\n\n\n\nppp_capacity*******************************************************************************************")

    data = dict()
    data['is_valid_post'] = False
    data['is_valid_get'] = False

    if request.method == "POST":
        if len(request.POST) > 0:
            data['is_valid_post'] = True
            fromDate = request.POST['fromDate']
            toDate = request.POST['toDate']
            processCode = request.POST['processCode']
            print("views.py ppp_capacity() POST fromDate: ", fromDate)
            print("views.py ppp_capacity() POST toDate: ", toDate)
            print("views.py ppp_capacity() POST processCode: ", processCode)
        else:
            fromDate = fromDateDefault  # "2020.12.01"
            toDate = toDateDefault  # "2020.12.31"
            processCode = "all"  # "all"  # "2100"
            print("views.py ppp_capacity() POST 0 fromDate: ", fromDate)
            print("views.py ppp_capacity() POST 0 toDate: ", toDate)
            print("views.py ppp_capacity() POST 0 processCode: ", processCode)
    elif request.method == "GET":
        if len(request.GET) > 0:
            data['is_valid_get'] = True
            fromDate = request.GET['fromDate']
            toDate = request.GET['toDate']
            processCode = request.GET['processCode']
            print("views.py ppp_capacity() GET fromDate: ", fromDate)
            print("views.py ppp_capacity() GET toDate: ", toDate)
            print("views.py ppp_capacity() GET processCode: ", processCode)
        else:
            fromDate = fromDateDefault  # "2020.12.01"
            toDate = toDateDefault  # "2020.12.31"
            processCode = "all"  # "all"  # "2100"
            print("views.py ppp_capacity() GET 0 fromDate: ", fromDate)
            print("views.py ppp_capacity() GET 0 toDate: ", toDate)
            print("views.py ppp_capacity() GET 0 processCode: ", processCode)

        # print("views.py ppp_capacity() fromDate: ", fromDate)
        # print("views.py ppp_capacity() toDate: ", toDate)
        # print("views.py ppp_capacity() processCode: ", processCode)

    # qr_process, df_process = __process(beInUse)  # Process.objects.get(code=process_code_selected)
    qrProcess, processList,  total_process_count = __getProcess(beInUse)  # Process.objects.get(code=process_code_selected)

    # print("ppp_capacity qrProcess: ", qrProcess)
    # print("ppp_capacity processList: ", processList)
    # print("ppp_capacity total_process_count: ", total_process_count)

    # sqlQuerySets, dfSets = __pp_data_period_process(from_date, to_date, process_code)
    # sqlQuerySets, dfSets = __pp_data_period_process(fromDate, toDate, processCode)

    sqlQuerySets, dfSets, revision, toDate = __getProductionCapacity(fromDate, toDate, processCode)
    # sqlQuerySets, dfSets = __getProductionPerformance(fromDate, toDate, processCode)

    # 2021.02.06 Added. 빈 df 확인.
    if len(sqlQuerySets) == 0:  # len(df.index) == 0: 또는 df.shape[0] == 0: 같은 구문이다.
        print("views.py ppp_capacity 조건에 맞는 자료가 없습니다. 다시 확인하시오!")
        print("views.py ppp_capacity 현재 자료를 정리하지 못 했습니다. 관리자에게 문의하시오!", fromDate, " ", toDate, " ", processCode)
        print("views.py ppp_capacity 해당 자료가 전혀 없습니다!")
        # context = {'process': process, 'ppData': [], 'total_pp_data_count': 0,
        #            'sqlQuerySets': sqlQuerySets, 'LANGUAGE_NO': LANGUAGE_NO}
        context = {"qrProcess": qrProcess, "products": [], "productsCount": 0,
                   "ppDataPeriodProcessList": [], "ppDataPeriodProcessList2": [],
                   "sqlQuerySets": sqlQuerySets,
                   'fromDate': fromDate, 'toDate': toDate, 'processCode': processCode,
                   "LANGUAGE_NO": LANGUAGE_NO, "goodnessTotal": 0, "volumesTotal": 0}
        return render(request, 'ppp/index.html', context)
        # return redirect("home")

    # ppDataPeriodProcessList, products, productsCount, ppDataPeriod, ppDataPeriodProcessList2, \
    # goodnessTotal, volumesTotal = makingCapacity(sqlQuerySets, dfSets)
    capacityList, machineList, machineListCount, needsHourList, planQtyList, capacityHour8List, capacityHour10List, \
    capacityHour12List, needsHourSum, planQtySum, dfSetsGroupBy = makingCapacity(sqlQuerySets, dfSets, revision)

    # print("ppp_capacity::type(capacityList): ", type(capacityList))
    # print("ppp_capacity::capacityList: \n", capacityList)
    # print("ppp_capacity::type(process): ", type(process))
    # print("ppp_capacity::process: \n", process)
    # print("ppp_capacity::type(machineList): ", type(machineList))
    # print("ppp_capacity::machineList: \n", machineList)
    # print("ppp_capacity::type(needsHourList): ", type(needsHourList))
    # print("ppp_capacity::needsHourList: \n", needsHourList)
    # print("ppp_capacity::sqlQuerySets: \n", sqlQuerySets)

    # print("ppp_capacity dfSetsGroupBy: ", dfSetsGroupBy)
    # print("ppp_capacity type(dfSetsGroupBy): ", type(dfSetsGroupBy))

    # 2021.03.05 Added. ***** [df.데이터프레임]은 context로 가기 전에 반드시 [json.load()]로 parsing 처리해야 함 *****
    jsonRecords = dfSetsGroupBy.reset_index().to_json(orient='records')
    jsonCapacity = []
    jsonCapacity = json.loads(jsonRecords)

    context = {"qrProcess": qrProcess, "sqlQuerySets": sqlQuerySets, "jsonCapacity": jsonCapacity,
               "capacityList": capacityList, "machineList": machineList, "machineListCount": machineListCount,
               "needsHourList": needsHourList, "planQtyList": planQtyList, "capacityHour8List": capacityHour8List,
               "capacityHour10List": capacityHour10List, 'capacityHour12List': capacityHour12List,
               'fromDate': fromDate, 'toDate': toDate, 'processCode': processCode, "LANGUAGE_NO": LANGUAGE_NO,
               "needsHourSum": needsHourSum, "planQtySum": planQtySum, "revision": revision}
    print("views.py ppp_capacity() request: ", request)
    print("views.py ppp_capacity() request.POST: ", request.POST)
    print("views.py ppp_capacity() len(request.POST): ", len(request.POST))
    print("views.py ppp_capacity() request.method: ", request.method)
    print("views.py ppp_capacity() fromDate: ", fromDate)
    print("views.py ppp_capacity() toDate: ", toDate)
    print("views.py ppp_capacity() processCode: ", processCode)

    # return HttpResponse('Customer page')  # [127.0.0.1:8000/about]으로 연결 시, 바로 뿌려준다. ===> 아래 : path('about/', contact),
    return render(request, 'ppp/ppp_current.html', context)
    # return JsonResponse(render(request, 'ppp/process.html', context), safe=False)  # 여긴 에러 나네...

    # data['context'] = render_to_string("ppp/process.html", context, request=request)
    # return JsonResponse(data, safe=False)


@csrf_exempt
def ppp_current(request):
    global fromDate, toDate, processCode

    # 우선적으로, 조회 기간 제한: [formDate] 월도를 기준으로, 자료를 가져온다. : [__getProductionCapacity()]에서 처리한다.
    # 사용자가 선택한 [fromDate]를 기준으로 해당월의 [1일]부터 [말일]까지 [1개월간]만의 자료로 제한.

    # *. 제품 / 기초 재고 / 당월 계획 수량 / 날짜별 생산 실적 누계 / 날짜별 앞으로 생산해야 할 잔량 / 공정정
    # *.

    # 0. 반드시 선택한 달의 [1일]부터 [말일]까지 [1개월간 자료]만 뿌린다.
    # 1. ForecastHistoryDay.NFxx: 먼저 선택한 달의 1개월간 생산 실적 누계 수량를 불러온다.
    # 2. 이건 필요 없음 => 아니다, 일단 가져온다: ForecastHistoryDay.DMxx: 먼저 선택한 달의 1개월간 생산 실적 수량를 불러온다.
    # 3. ForecastHistoryDay.Dpt: 해달 월의 생산 계획 총량을 가져온다.


    # 1. 설비 자료를 가져온다.
    # 2. ForecastHistoryDay.생산 계획.WorkBaseDay: 생산 CAPACITY 수량: 8h 수량, 10h 수량, 12h 수량 구분
    # 3. ForecastHistoryDay.생산 계획.DPT: 생산 계획 수량을 [설비]별로 합산한다.

    print("\n\n\n\n\nppp_current*******************************************************************************************")

    data = dict()
    data['is_valid_post'] = False
    data['is_valid_get'] = False

    if request.method == "POST":
        if len(request.POST) > 0:
            data['is_valid_post'] = True
            fromDate = request.POST['fromDate']
            toDate = request.POST['toDate']
            processCode = request.POST['processCode']
            print("views.py ppp_current() POST fromDate: ", fromDate)
            print("views.py ppp_current() POST toDate: ", toDate)
            print("views.py ppp_current() POST processCode: ", processCode)
        else:
            fromDate = fromDateDefault  # "2020.12.01"
            toDate = toDateDefault  # "2020.12.31"
            processCode = "all"  # "all"  # "2100"
            print("views.py ppp_current() POST 0 fromDate: ", fromDate)
            print("views.py ppp_current() POST 0 toDate: ", toDate)
            print("views.py ppp_current() POST 0 processCode: ", processCode)
    elif request.method == "GET":
        if len(request.GET) > 0:
            data['is_valid_get'] = True
            fromDate = request.GET['fromDate']
            toDate = request.GET['toDate']
            processCode = request.GET['processCode']
            print("views.py ppp_current() GET fromDate: ", fromDate)
            print("views.py ppp_current() GET toDate: ", toDate)
            print("views.py ppp_current() GET processCode: ", processCode)
        else:
            fromDate = fromDateDefault  # "2020.12.01"
            toDate = toDateDefault  # "2020.12.31"
            processCode = "all"  # "all"  # "2100"
            print("views.py ppp_current() GET 0 fromDate: ", fromDate)
            print("views.py ppp_current() GET 0 toDate: ", toDate)
            print("views.py ppp_current() GET 0 processCode: ", processCode)

        # print("views.py ppp_current() fromDate: ", fromDate)
        # print("views.py ppp_current() toDate: ", toDate)
        # print("views.py ppp_current() processCode: ", processCode)

    # qr_process, df_process = __process(beInUse)  # Process.objects.get(code=process_code_selected)
    qrProcess, processList,  total_process_count = __getProcess(beInUse)  # Process.objects.get(code=process_code_selected)
    # print("ppp_current qrProcess: ", qrProcess)
    # print("ppp_current processList: ", processList)
    # print("ppp_current total_process_count: ", total_process_count)

    # sqlQuerySets, dfSets = __pp_data_period_process(from_date, to_date, process_code)
    # sqlQuerySets, dfSets = __pp_data_period_process(fromDate, toDate, processCode)

    # [ppp_current.생산 진도 관리]는 [ppp_capacity.생산 능력 관리] 자료를 공유하므로, [__getProductionCapacity()]을 사용한다.
    # 2021.3.08 Conclusion. 아니다. 제품별 생산 계획 수량은 [__getProductionCapacity()]에서 가져오고,
    # 생산 실적 자료는 [__getProductionCurrent()]에서 가져오고, 2번 가져와서 처리...
    # 반드시 따로 가야 한다.
    sqlQuerySetsPlanQty, dfSetsPlanQty, revision, toDate = __getProductionCapacity(fromDate, toDate, processCode)
    # print("00 ppp_current sqlQuerySetsPlanQty: \n", sqlQuerySetsPlanQty)
    # print("00 ppp_current type(sqlQuerySetsPlanQty): ", type(sqlQuerySetsPlanQty))
    # print("00 ppp_current len(sqlQuerySetsPlanQty): ", len(sqlQuerySetsPlanQty))

    # 2021.02.06 Added. 빈 df 확인.
    if len(sqlQuerySetsPlanQty) == 0:  # len(df.index) == 0: 또는 df.shape[0] == 0: 같은 구문이다.
        print("views.py ppp_current sqlQuerySetsPlanQty 조건에 맞는 자료가 없습니다. 다시 확인하시오!")
        print("views.py ppp_current sqlQuerySetsPlanQty 현재 자료를 정리하지 못 했습니다. 관리자에게 문의하시오!", fromDate, " ", toDate, " ", processCode)
        print("views.py ppp_current sqlQuerySetsPlanQty 해당 자료가 전혀 없습니다!")
        jsonCurrent = {}
        ppDataPeriod = []
        products = []
        planqtySum = 0
        goodnessSum = 0
        goodnessCumsumSum = 0
        planqtyFinalList = []
        goodnessList = []
        goodnessCumsumList = []
        sqlQuerySets = sqlQuerySetsPlanQty  # 아무 의미 없지만, 에러 방지를 위해 임시로 담어 준다.

    else:

        sqlQuerySets, dfSets, toDate = __getProductionCurrent(fromDate, toDate, processCode)
        # print("ppp_current dfSets: \n", dfSets)
        # print("ppp_current type(dfSets): ", type(dfSets))
        # print("ppp_current len(dfSets): ", len(dfSets))

        # 2021.02.06 Added. 빈 df 확인.
        if len(sqlQuerySets) == 0:  # len(df.index) == 0: 또는 df.shape[0] == 0: 같은 구문이다.
            print("views.py ppp_current sqlQuerySets 조건에 맞는 자료가 없습니다. 다시 확인하시오!")
            print("views.py ppp_current sqlQuerySets 현재 자료를 정리하지 못 했습니다. 관리자에게 문의하시오!", fromDate, " ", toDate, " ", processCode)
            print("views.py ppp_current sqlQuerySets 해당 자료가 전혀 없습니다!")
            jsonCurrent = {}
            ppDataPeriod = []
            products = []
            planqtySum = 0
            goodnessSum = 0
            goodnessCumsumSum = 0
            planqtyFinalList = []
            goodnessList = []
            goodnessCumsumList = []

        else:

            # capacityList, machineList, machineListCount, needsHourList, planQtyList, capacityHour8List, capacityHour10List, \
            # capacityHour12List, needsHourSum, planQtySum, dfSetsGroupBy = makingCapacity(sqlQuerySets, dfSets, dfSetsPlanQty, revision)

            # dfSetsPlanQtyGroupBy  # 제품별 월간 생산 계획 자료 데이터프레임
            # return dateList, productsList, goodnessList, goodnessCumsumList, dfSetsCumsum, planQtyByCodeList

            ppDataPeriod, products, goodnessList, goodnessCumsumList, planqtyFinalList, dfSetsCumsum, planQtyByCodeList, \
            goodnessSum, goodnessCumsumSum, planqtySum = makingCurrent(sqlQuerySets, dfSets, dfSetsPlanQty, revision)
            # print("ppp_current ppDataPeriod: \n", ppDataPeriod)
            # print("ppp_current type(ppDataPeriod): ", type(ppDataPeriod))
            # print("ppp_current len(ppDataPeriod): ", len(ppDataPeriod))
            # print("ppp_current products: \n", products)
            # print("ppp_current type(products): ", type(products))
            # print("ppp_current len(products): ", len(products))

            # print("ppp_current goodnessList: \n", goodnessList)
            # print("ppp_current type(goodnessList): ", type(goodnessList))
            # print("ppp_current len(goodnessList): ", len(goodnessList))
            # print("ppp_current goodnessCumsumList: \n", goodnessCumsumList)
            # print("ppp_current type(goodnessCumsumList): ", type(goodnessCumsumList))
            # print("ppp_current len(goodnessCumsumList): ", len(goodnessCumsumList))
            # print("ppp_current planqtyFinalList: \n", planqtyFinalList)
            # print("ppp_current type(planqtyFinalList): ", type(planqtyFinalList))
            # print("ppp_current len(planqtyFinalList): ", len(planqtyFinalList))

            # print("ppp_current dfSetsCumsum: \n", dfSetsCumsum)
            # print("ppp_current type(dfSetsCumsum): ", type(dfSetsCumsum))
            # print("ppp_current len(dfSetsCumsum): ", len(dfSetsCumsum))
            # print("ppp_current planQtyByCodeList: \n", planQtyByCodeList)
            # print("ppp_current type(planQtyByCodeList): ", type(planQtyByCodeList))
            # print("ppp_current len(planQtyByCodeList): ", len(planQtyByCodeList))
            # print("ppp_current goodnessSum: \n", goodnessSum)
            # print("ppp_current type(goodnessSum): ", type(goodnessSum))
            # print("ppp_current len(goodnessSum): ", len(goodnessSum))
            # print("ppp_current goodnessCumsumSum: \n", goodnessCumsumSum)
            # print("ppp_current type(goodnessCumsumSum): ", type(goodnessCumsumSum))
            # print("ppp_current len(goodnessCumsumSum): ", len(goodnessCumsumSum))


            # 2021.03.05 Added. ***** [df.데이터프레임]은 context로 가기 전에 반드시 [json.load()]로 parsing 처리해야 함 *****
            jsonRecords = dfSetsCumsum.reset_index().to_json(orient='records')
            jsonCurrent = []
            jsonCurrent = json.loads(jsonRecords)

    context = {"qrProcess": qrProcess, "sqlQuerySets": sqlQuerySets, "jsonCurrent": jsonCurrent,
               "ppDataPeriod": ppDataPeriod, "products": products, "goodnessSum": goodnessSum,
               "goodnessCumsumSum": goodnessCumsumSum, "planqtyFinalList": planqtyFinalList,
               "goodnessList": goodnessList, "goodnessCumsumList": goodnessCumsumList, "planqtySum": planqtySum,
               'fromDate': fromDate, 'toDate': toDate, 'processCode': processCode, "LANGUAGE_NO": LANGUAGE_NO,
               "revision": revision}

    print("views.py ppp_current() request: ", request)
    print("views.py ppp_current() request.POST: ", request.POST)
    print("views.py ppp_current() len(request.POST): ", len(request.POST))
    print("views.py ppp_current() request.method: ", request.method)
    print("views.py ppp_current() fromDate: ", fromDate)
    print("views.py ppp_current() toDate: ", toDate)
    print("views.py ppp_current() processCode: ", processCode)
    print("LANGUAGE_NO: ", LANGUAGE_NO, ", LANGUAGE_NO: ", LANGUAGE_NO)

    # print("views.py ppp_current() productsList: \n", productsList)
    # print("views.py ppp_current() goodnessCumsumList: \n", goodnessCumsumList)  # [['날짜', 123.0, 456.0, ...], ...[]]
    # print("views.py ppp_current() jsonCurrent: \n", jsonCurrent)  # [['날짜', 123.0, 456.0, ...], ...[]]
    # print("views.py ppp_current() type(jsonCurrent): ", type(jsonCurrent))  # [['날짜', 123.0, 456.0, ...], ...[]]
    # print("views.py ppp_current() len(jsonCurrent): ", len(jsonCurrent))  # [['날짜', 123.0, 456.0, ...], ...[]]

    # return HttpResponse('Customer page')  # [127.0.0.1:8000/about]으로 연결 시, 바로 뿌려준다. ===> 아래 : path('about/', contact),
    return render(request, 'ppp/ppp_current.html', context)
    # return JsonResponse(render(request, 'ppp/process.html', context), safe=False)  # 여긴 에러 나네...

    # data['context'] = render_to_string("ppp/process.html", context, request=request)
    # return JsonResponse(data, safe=False)


# 2021.03.08 Created. [누계]를 자동으로 계산해 주는 함수와 dpt.생산 계획 수량에 df 찍어서 리턴하는 함수.
def makeCumulativeColumn(df, planQtyByCodeList, revision, cumsumColumnName):
    yearCurrent = revision[:4]
    monthCurrent = revision[-2:]

    # print("makingCurrent 11 yearCurrent: ", yearCurrent, "monthCurrent: ", monthCurrent, ", revision: ", revision)

    # print("makingCurrent 11 df: \n", df)
    # print("makingCurrent 11 planQtyByCodeList: \n", planQtyByCodeList)

    # dfSetsPlanQtyGroupBySorted = dfSetsPlanQtyGroupBy.sort_values(['code'])

    # print("00 views.py makeCumulativeColumn() cumsumColumnName: ", cumsumColumnName)

    # df['cumulativeColumnName'] = 0  # df['goodness']
    # print("11 views.py makeCumulativeColumn() df: \n", df)

    # dfSorted = df.sort_values(by=[0][1], ascending=True)  # 안 됨.
    # print("22 views.py makeCumulativeColumn() dfSorted: \n", dfSorted)
    # dfSorted = df.sort_values(by=[[0][1]], ascending=True)  # 안 됨.
    # print("33 views.py makeCumulativeColumn() dfSorted: \n", dfSorted)
    # dfSorted = df.sort_values(by=['workdate', 'code'], ascending=True)

    # print("33 views.py makeCumulativeColumn() 소트 전 df: \n", df)
    df.sort_values(by=['workdate', 'code'], axis=0, inplace=True)
    # dfSorted = df.sort_values(by=['workdate', 'code'], ascending=True, inplace=True)  #.reset_index()
    # print("33 views.py makeCumulativeColumn() 소트 후 df: \n", df)
    # print("33 views.py makeCumulativeColumn() type(df): ", type(df))

    dfSorted = df.fillna(0)  # NaN 값을 [0]으로 치환. 반드시 [새로운 DataFrame 명] 사용...
    # print("33 views.py makeCumulativeColumn()dfSorted: \n", dfSorted)  #.[['workdate', 'dpt', 'goodness', 'goodnesscumsum', 'step9', 'processinfo']])

    breakValue = 0
    thisMonthStartDay = 0
    minDate = 1
    tempList = []
    cumulativeValue = []
    cumulativePrevious = 0
    planqtyList = []
    replacedList = []

    # 2021.03.14 Conclusion. DataFrame 방식으로 처리했더니, 리스트 방식보다 시간이 더 걸리는 관계로, 리스트 방식으로 처리한다.
    # dfCumsumOnly = pd.DataFrame(index=(0, 0), columns=['workdate', 'code', 'goodness', 'cumsum'])
    # ===> dfCumsumOnly = pd.DataFrame(columns=['index', 'workdate', 'code', 'goodness', 'cumsum'])
    # print("0 dfCumsumOnly: \n", dfCumsumOnly)

    messageShow = 1
    # for row in dfSorted.items():
    for i in dfSorted.index:
        # print("i: ", i)
        workdateCurrent = dfSorted.at[i, 'workdate']
        yearCurrent = workdateCurrent[:4]
        monthCurrent = workdateCurrent[5:7]

        # 첫 날짜가 2일이나 3일에 시작할 수도 있으므로, 현재 월도의 [실제 시작 날짜]를 담아 둔다.
        if i == 0:
            thisMonthStartDay = int(workdateCurrent[-2:])
            # print("33 views.py makeCumulativeColumn() thisMonthStartDay: ", thisMonthStartDay)
            # print("33 views.py makeCumulativeColumn() type(thisMonthStartDay): ", type(thisMonthStartDay))

        # dateCurrent = workdateCurrent[-2:]
        # print("333 views.py makeCumulativeColumn() workdateCurrent: ", workdateCurrent)
        # print("333 views.py makeCumulativeColumn() yearCurrent: ", yearCurrent)
        # print("333 views.py makeCumulativeColumn() monthCurrent: ", monthCurrent)
        # print("333 views.py makeCumulativeColumn() dateCurrent: ", dateCurrent)
        # print("333 views.py makeCumulativeColumn() type(workdateCurrent): ", type(workdateCurrent))
        workdateCurrent = dfSorted.at[i, 'workdate'].strip()
        # print("333 views.py makeCumulativeColumn() workdateCurrent: ", workdateCurrent)
        codeCurrent = dfSorted.at[i, 'code'].strip()
        # print("333 views.py makeCumulativeColumn() codeCurrent: ", codeCurrent)
        # print("333 views.py makeCumulativeColumn() type(codeCurrent): ", type(codeCurrent))

        # 2021.03.13 Added. 생산 계획 수량을 가져와서 [dpt.planqty] 컬럼에 찍어준다.
        result = [data for data in planQtyByCodeList[:] if codeCurrent in data[:]]
        if len(result) > 0:
            # print("3 찾은 result: ", result)
            # print("3 찾은 type(result): ", type(result))
            # print("3 찾은 len(result): ", len(result))
            # print("3 찾은 result[0]: ", result[0])
            # print("3 찾은 result[0][4]: ", result[0][4])
            # print("3 찾은 type(result[0][4]): ", type(result[0][4]))
            planqtyCurrent = float(result[0][4])

            # if codeCurrent == "8000013554":
            #     print("33 찾은 planqtyCurrent: ", planqtyCurrent)
            #     print("33 찾은 type(planqtyCurrent): ", type(planqtyCurrent))
            #     if messageShow == 1:
            #         rtnString = pyautogui.confirm(text="현재 여기까지 실행되었음을 확인함!!!!!!!!!!!", title="000", buttons=["OK", "Cancel"])
            #         print("000 rtnString: ", rtnString)
            #         if rtnString != "OK":
            #             messageShow = 0

            # 2021.03.14 Added. 혹시라도 [dpt.생산 계획 수량]은 있는데, 실적이 아직 없는 품목이 있을 수 있으므로, 표시를 해 둔다
            # replaced = 1
        else:
            # planqtyCurrent = 0
            replaced = 0

        # if messageShow == 1:
        #     rtnString = pyautogui.confirm(text="현재 여기까지 실행되었음을 확인함!!!!!!!!!!!", title="111", buttons=["OK", "Cancel"])
        #     print("111 rtnString: ", rtnString)
        #     if rtnString != "OK":
        #         messageShow = 0

        # replacedList.append(replaced)
        planqtyList.append(planqtyCurrent)
        planqtyCurrent = 0  # 반드시 초기화를 해 주어야 한다.
        # print("3 찾은 planqtyList: ", planqtyList)
        # print("3 찾은 type(planqtyList): ", type(planqtyList))

        goodnessCurrent = int(dfSorted.at[i, 'goodness'])
        # print("33 views.py makeCumulativeColumn() codeCurrent: ", codeCurrent)
        # print("33 views.py makeCumulativeColumn() type(codeCurrent): ", type(codeCurrent))

        # 3개 항목을 [str] 타입으로 리스트에 저장한다.
        tempText = workdateCurrent + " " + codeCurrent + " " + str(goodnessCurrent)
        # print("55 views.py makeCumulativeColumn() tempText: ", tempText)
        # print("55 views.py makeCumulativeColumn() type(tempText): ", type(tempText))

        # ===> listCurrent = [i, workdateCurrent, codeCurrent, float(goodnessCurrent), float(goodnessCurrent)]

        dateCurrent = int(workdateCurrent[-2:])
        # print("61 views.py makeCumulativeColumn() dateCurrent: ", dateCurrent, ", thisMonthStartDay: ", thisMonthStartDay)

        if dateCurrent < thisMonthStartDay:
            dateCurrent = thisMonthStartDay

        # print("62 views.py makeCumulativeColumn() dateCurrent: ", dateCurrent, ", thisMonthStartDay: ", thisMonthStartDay)

        # if dateCurrent == 1:  # 첫 날짜가 2일이나 3일에 시작할 수도 있으므로, 현재 월도의 [실제 시작 날짜]를 담아 둔다.
        if dateCurrent == thisMonthStartDay:  # 첫 날짜가 2일이나 3일에 시작할 수도 있으므로, 현재 월도의 [실제 시작 날짜]를 담아 둔다.
            tempList.append(tempText)
            cumulativeValue.append(goodnessCurrent)

            # 2021.03.14 Conclusion. DataFrame 방식으로 처리했더니, 리스트 방식보다 시간이 더 걸리는 관계로, 리스트 방식으로 처리한다.
            # 2021.03.14 Added. DataFrame도 만들어 둔다.
            # ===> dfNew = pd.Series(listCurrent, index=dfCumsumOnly.columns)
            # print("111 dfNew: \n", dfNew)
            # ===> dfCumsumOnly = dfCumsumOnly.append(dfNew, ignore_index=True)
            # print("222 dfCumsumOnly: \n", dfCumsumOnly)
            # dfCumsumOnly = dfCumsumOnly.sort_values(['workdate', 'code'], ascending=True)
            # print("333 dfCumsumOnly: \n", dfCumsumOnly)
            # 2021.03.14 Conclusion. 아래 것은 의미없고, 위의 2개는 동일한 결과가 나온다.
            # dfCumsumOnly = dfCumsumOnly.sort_values(['workdate', 'code'], ascending=True).reset_index()
            # print("444 dfCumsumOnly: \n", dfCumsumOnly)

        else:

            datePrevious = dateCurrent - 1
            # print("77 views.py codeCurrent: ", codeCurrent, ", datePrevious: ", datePrevious, ", thisMonthStartDay: ", thisMonthStartDay)

            # [datePrevious=0]은 [dateCurrent=1]: 매월 [1일]은 찾을 필요도 없다.
            # ===> 매월 [1일]이 아니고, 매월 [시작 날짜]와 그 이전 날짜는 찾을 필요가 없다.

            cumulativePrevious = 0  # 반드시 초기화...
            cumsumPrevious = 0
            # while datePrevious > thisMonthStartDay:  # 0:
            while datePrevious > 0:
                findText = yearCurrent + "-" + monthCurrent + "-" + str(datePrevious).zfill(2) + " " + codeCurrent
                findTextLen = len(findText)
                # print("0 i: ", i, ", codeCurrent: ", codeCurrent, ",       goodnessCurrent: ", goodnessCurrent)
                # print("0 i: ", i, ", dateCurrent: ", dateCurrent)
                # print("0 i: ", i, ", findText: ", findText, ", findTextLen: ", findTextLen, ", workdateCurrent: ", workdateCurrent)
                # print("0 i: ", i, ", tempList: \n", tempList)

                # DataFrame으로 처리.
                # resultData = dfCumsumOnly['code'][dfCumsumOnly['code'] == codeCurrent]  # []: Series type 임에 주의.
                # ===> resultData = dfCumsumOnly[['index', 'workdate', 'code', 'goodness', 'cumsum']][dfCumsumOnly['code'] == codeCurrent]  # [[]]: DataFrame type 임에 주의.
                # print("9 i: ", i, ", 찾은 type(resultData): ", type(resultData))
                # print("9 i: ", i, ", 찾은 len(resultData): ", len(resultData))
                # print("9 i: ", i, ", 찾은 resultData: ", resultData)
                # print("9 i: ", i, ", 찾은 resultData.index: ", resultData.index)
                # print("9 i: ", i, ", 찾은 resultData.values: ", resultData.values)
                # dfCumsumOnly = pd.DataFrame(columns=['index', 'workdate', 'code', 'goodness', 'cumsum'])
                # ===> if len(resultData) > 0:
                    # cumsumPrevious = float(resultData[0][4])  # ***** 요기는 절대적으로 에러나네... resultData.values[0][4]
                    # ===> cumsumPrevious = float(resultData.values[0][4])
                    # if codeCurrent == "8000031274":
                    # print("99999999 i: ", i, ", 찾은 cumsumPrevious: ", cumsumPrevious)
                # ===> else:
                    # ===> cumsumPrevious = 0

                # 2021.03.14 Conclusion. 리스트로 처리.
                # result 값으로 찾으면, 리스트['2021-03-01 FA1A0HCJAD04 241']를 돌려 주고, 못 찾으면, 빈 리스트[]를 돌려 준다.
                result = [data for data in tempList[::-1] if findText in data[:findTextLen]]  # 꺼꾸로 뒤집어서 찾는다.
                if result:
                    cumulativePrevious = int(result[0][findTextLen:])  # 그냥 [+1] 안 해도 될 껄...
                    break
                else:
                    datePrevious = datePrevious - 1
                    # if == thisMonthStartDay: 이렇게 하면, 절대 안 됨...
                    # 시작 일자에도 생산을 할 수 있으므로, 시작 일자에서 찾게 할려면, [0]일 때까지 찾아야 함에 특히 주의...
                    if datePrevious == 0:
                        # 여기가 헷갈릴 수 있는데, [0]을 세팅하는 것이 정확하다.
                        # 이전 자료가 전혀 없으면, 여기 while 문을 빠져 나간 후에, 오늘 생산 수량이 누계로 넘어가야 된다.
                        # 여기서 [이전 누계 수량 변수.cumulativePrevious]에 [현재 생산 실적 수량.goodnessCurrent]을 넣으면,
                        # while 문장을 빠진 후에, 누계 변수에 또 더해 줌으로 2중으로 누계 수량이 잡히게 된다. 주의할 것...
                        cumulativePrevious = 0  # goodnessCurrent
                        break
                    else:
                        cumulativePrevious = 0  # 여기서 이전 자료가 있을 수 있으니, 확실하고 [0]을 넣어 준다.

                # if codeCurrent == "FA1A0HCJAD04":  # "8000031274":
                #     rtnString = pyautogui.confirm(text="현재 여기까지 실행되었음을 확인함!!!!!!!!!!!", title="111", buttons=["OK", "Cancel"])
                #     print("1 rtnString: ", rtnString)
                #     if rtnString != "OK":
                #         break


            # ===> if breakValue == 1:
            # ===>     break

            # 먼저 오늘 날짜의 누계를 먼저 추가한다.
            # print("88 goodnessCurrent : ", goodnessCurrent)
            # print("88 cumulativePrevious: ", cumulativePrevious)
            goodnessCumulative = goodnessCurrent + cumulativePrevious
            cumulativeValue.append(goodnessCumulative)
            # print("88 cumulativeValue: \n", cumulativeValue)

            # 다음 검색을 위해, 임시 리스트에도 추가해 준다.
            tempText = workdateCurrent + " " + codeCurrent + " " + str(goodnessCumulative)
            tempList.append(tempText)
            # print("99 workdateCurrent: ", workdateCurrent)
            # print("99 codeCurrent: ", codeCurrent)
            # print("99 goodnessCumulative: ", goodnessCumulative)
            # print("99 tempText: ", tempText)
            # print("99 tempList: \n", tempList)

            # if codeCurrent == "FA1A0HCJAD04":
            #     rtnString = pyautogui.confirm(text="현재 여기까지 실행되었음을 확인함!!!!!!!!!!!", title="333", buttons=["OK", "Cancel"])
            #     print("1 rtnString: ", rtnString)
            #     if rtnString != "OK":
            #         break

            # 2021.03.14 Conclusion. DataFrame 방식으로 처리했더니, 리스트 방식보다 시간이 더 걸리는 관계로, 리스트 방식으로 처리한다.
            # 2021.03.14 Added. DataFrame도 만들어 둔다.
            # print("888 cumsumPrevious : ", cumsumPrevious)
            # print("888 workdateCurrent: ", workdateCurrent)
            # ===> cumsumCurrent = goodnessCurrent + cumsumPrevious
            # ===> listCurrent = [0, workdateCurrent, codeCurrent, float(goodnessCurrent), float(cumsumCurrent)]
            # ===> dfNew = pd.Series(listCurrent, index=dfCumsumOnly.columns)
            # print("1 dfNew: \n", dfNew)
            # ===> dfCumsumOnly = dfCumsumOnly.append(dfNew, ignore_index=True)
            # print("2 dfCumsumOnly: \n", dfCumsumOnly)
            # dfCumsumOnly = dfCumsumOnly.sort_values(['workdate', 'code'], ascending=True)
            # print("3 dfCumsumOnly: \n", dfCumsumOnly)
            # 2021.03.14 Conclusion. 아래 것은 의미없고, 위의 2개는 동일한 결과가 나온다.
            # dfCumsumOnly = dfCumsumOnly.sort_values(['workdate', 'code'], ascending=True).reset_index()
            # print("4 dfCumsumOnly: \n", dfCumsumOnly)

    # print("88 최종 누계 리스트 cumulativeValue: \n", cumulativeValue)
    dfSorted['goodnesscumsum'] = cumulativeValue
    # print("99 views.py makeCumulativeColumn() dfSorted: \n", dfSorted)
    # print("99 views.py makeCumulativeColumn() type(dfSorted): ", type(dfSorted))

    # print("999 views.py makeCumulativeColumn() planqtyList: \n", planqtyList)
    # print("999 views.py makeCumulativeColumn() type(planqtyList): ", type(planqtyList))
    dfSorted['planqty'] = planqtyList
    dfSorted.sort_values(by=['workdate', 'code'], axis=0, inplace=True)
    # print("999 views.py makeCumulativeColumn() dfSorted: \n", dfSorted)
    # print("999 views.py makeCumulativeColumn() type(dfSorted): ", type(dfSorted))

    # 2021.03.14 Added. 혹시라도 [dpt.생산 계획 수량]은 있는데, 실적이 아직 없는 품목이 있을 수 있으므로,
    # 여기서 그것을 확인하여, 계획 품목을 추가해 준다.
    # for i, data in enumerate(planQtyByCodeList):  # 이렇게 해도 되고, 아래처럼 해도 된다.
    for data in planQtyByCodeList:  # 이렇게 해도 되고, 아래처럼 해도 된다.
        # print("planQtyByCodeList.row i: ", i)
        # print("planQtyByCodeList.row data: ", data)
        # print("planQtyByCodeList.row type(data): ", type(data))  # List
        indexCurrent = data[0]
        workdateCurrent = yearCurrent + "-" + monthCurrent + "-01"
        codeCurrent = data[1]
        step9Current = data[2]
        goodnessCurrent = 0
        badnessCurrent = 0
        productionactualnoCurrent = yearCurrent[-2:] + monthCurrent + "01PSC001999"+codeCurrent
        processinfo = data[3]
        goodnessCumulativeCurrent = 0
        planqtyCurrent = float(data[4])

        # print("planQtyByCodeList.row codeCurrent: ", codeCurrent)

        # ***** 중요 ***** 일반적으로 result = dfSorted['code'] == codeCurrent 이와 같이 검색할 것 같지만,
        # 이렇게 하면 전체 값에 대한 [True, False]를 리턴한다.
        # 그러므로 반드시 2번째 방법인 result = dfSorted['code'][dfSorted['code'] == codeCurrent] 이렇게 처리해야 한다.
        # result = dfSorted['code'] == codeCurrent
        # print("planQtyByCodeList.row result: ", result)
        # print("planQtyByCodeList.row type(result): ", type(result))
        # print("planQtyByCodeList.row len(result): ", len(result))

        # resultData = dfCumsumOnly['code'][dfCumsumOnly['code'] == codeCurrent]  # []: Series type 임에 주의.
        # resultData = dfCumsumOnly[['workdate', 'code', 'goodness', 'cumsum']][dfCumsumOnly['code'] == codeCurrent]  # [[]]: DataFrame type 임에 주의.
        # value = float(resultData[0][4])  # ***** 요기는 절대적으로 에러나네... resultData.values[0][4]
        # value = float(resultData.values[0][4])  # ***** 반드시 이런식으로... resultData.values[0][4]

        result = dfSorted['code'][dfSorted['code'] == codeCurrent]  # Series type 임에 주의.
        # print("planQtyByCodeList.row result: ", result)
        # print("planQtyByCodeList.row type(result): ", type(result))  # Series type 임에 주의.
        # print("planQtyByCodeList.row len(result): ", len(result))

        if len(result) == 0:
            # data = [indexCurrent, workdateCurrent, codeCurrent, step9Current, 0, 0, productionactualnoCurrent, processinfo, 0, planqtyCurrent]
            data = [workdateCurrent, codeCurrent, step9Current, 0, 0, productionactualnoCurrent, processinfo, 0, planqtyCurrent]
            # dfNew = pd.DataFrame(data, columns=['index', 'code', 'step9', 'processinfo', 'planqty'])
            # dfNew = pd.DataFrame(data, columns=['code', 'step9', 'processinfo', 'planqty'])
            # dfNew = pd.Series(data, columns=['index', 'code', 'step9', 'processinfo', 'planqty'])
            dfNew = pd.Series(data, index=dfSorted.columns)
            # dfNew = pd.DataFrame(data, index=dfSorted.columns)
            # print("dfNew: ", dfNew)

            # [ignore_index=True] : 현재 [dfSorted.마지막 index] 바로 이어서 [index]를 매겨라는 뜻.
            dfSorted = dfSorted.append(dfNew, ignore_index=True)
            # dfSorted = dfSorted.append(dfNew)

    # DataFrame 자체 내에서 정렬된 상태로 다시 저장하기 : inplace=True
    # 결측값을 처음에(na_position='first'), 혹은 마지막(na_position='last') 위치에 정렬하기
    dfSorted.sort_values(by=['workdate', 'code'], axis=0, inplace=True)
    # print("9 views.py makeCumulativeColumn() 리턴 바로 전 dfSorted: \n", dfSorted)
    # print("9 views.py makeCumulativeColumn() 리턴 바로 전 type(dfSorted): ", type(dfSorted))

    return dfSorted


# 2021.03.01 월별 첫날과 마지막 날 값을 리턴한다.
def getMaxDate(year, month):
    yearCurrent = year
    monthCurrent = month
    print("makingCurrent 11 yearCurrent: ", yearCurrent, "monthCurrent: ", monthCurrent)

    # 해당 월도의 마지막 날짜를 찾는다.
    if int(monthCurrent) == 12:
        yearCurrent = str(int(yearCurrent) - 1)
        monthNext = "01"
    else:
        monthNext = str(int(monthCurrent) + 1).zfill(2)
    print("makingCurrent 22 yearCurrent: ", yearCurrent, "monthCurrent: ", monthCurrent, ", monthNext: ", monthNext)

    minDateTimeNextMonth = datetime.strptime(yearCurrent + "-" + monthNext + "-" + "01", "%Y-%m-%d")
    print("makingCurrent 33 minDateTimeNextMonth: ", minDateTimeNextMonth)

    maxDateTimeThisMonth = minDateTimeNextMonth - timedelta(days=1)
    print("makingCurrent 44 maxDateTimeThisMonth: ", maxDateTimeThisMonth)

    minDateTimeThisMonth = datetime.strptime(yearCurrent + "-" + monthCurrent + "-" + "01", "%Y-%m-%d")
    print("makingCurrent 55 minDateTimeThisMonth: ", minDateTimeThisMonth)

    maxDate = str(maxDateTimeThisMonth.day).zfill(2)
    print("makingCurrent 55 maxDate: ", maxDate)

    return maxDate