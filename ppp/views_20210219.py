# 2021.02.05 To Do List
# 1. 생산 실적 검색 기간 설정
# 2. 서버 데이터베이스 변경 : Ms Sql ===> MySql
# 3. 서버로 데이터 상시 전송 프로그램
# 4. process.html : 함수를 활용한 javascript 단에서 data 정리...


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


from django.core import serializers
from django.views.generic.list import ListView
# from rest_app.models import Repository
from django.http.response import HttpResponse

from ppp.f_common import connectDB, connectRemoteDB, connectWebDB

import pyautogui
# import pyodbc
# import pymssql
import pandas as pd
# import pandas.io.sql as pdsql  # 이것도 안 되네...
import numpy as np

import pytz

from datetime import date, datetime, timedelta
from django.utils import timezone
from dateutil import relativedelta
from collections import defaultdict

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # csrf_exempt 사용을 위해...
import re

from django.db import connection  # 테이블 존재 여부 확인용.

from django.db.models.functions import TruncMonth, TruncDate  # 일별, 월별 데이터 뽑기

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

# from_date = "2020.12.01"
# to_date = "2020.12.30"

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
    global cursArray, cursDict, CONNECTEDSERVER, CONNECTEDWEB

    print("view.py __getProductionPerformance type(fromDate): ", type(fromDate))
    print("view.py __getProductionPerformance fromDate: ", fromDate)
    print("view.py __getProductionPerformance toDate: ", toDate)
    print("view.py __getProductionPerformance ProcessCode: ", ProcessCode)
    print("view.py __getProductionPerformance timezone.now(): ", timezone.now())

    # # locale.setlocale(locale.LC_ALL, 'ko_KR.UTF-8')
    # fromDate = fromDate  #+ " 08:00:00.000000"
    # toDate = toDate  #+ " 08:00:00.000000"
    # fromDateDate = datetime.datetime.strptime(fromDate, '%Y.%m.%d')  # .date()  # combine(current_date, day_closing_time)
    # toDateDate = datetime.datetime.strptime(toDate, '%Y.%m.%d')  # .date()  # combine
    # print("view.py __getProductionPerformance type(fromDateDate): ", type(fromDateDate))
    # print("view.py __getProductionPerformance fromDateDate: ", fromDateDate)
    # print("view.py __getProductionPerformance toDateDate: ", toDateDate)

    # fromDate = fromDate + " 08:00:00.000000"
    # toDate = toDate + " 08:00:00.000000"
    # fromDateDate = datetime.datetime.strptime(fromDate, "%Y.%m.%d %H:%M:%S.%f")  #.date()  # combine(current_date, day_closing_time)
    # toDateDate = datetime.datetime.strptime(toDate, "%Y.%m.%d %H:%M:%S.%f")  #.date()  # combine
    # print("view.py __getProductionPerformance type(fromDateDate): ", type(fromDateDate))
    # print("view.py __getProductionPerformance fromDateDate: ", fromDateDate)
    # print("view.py __getProductionPerformance toDateDate: ", toDateDate)

    # 2021.02.18 Conclusion. 아래는 다음과 같은 에러가 발생한다.
    # RuntimeWarning: DateTimeField ProductionActual.workdate received a naive datetime (2020-12-31 08:00:00) while time zone support is acti
    # ve.
    #   RuntimeWarning)
    # qrProductionPerformance = ProductionActual.objects\
    #     .values('workdate', 'productionactualno', 'code', 'goodness', 'badness', 'daywork')\
    #     .filter(workdate_lte=fromDateDate, workdate__gte=toDateDate)

    if CONNECTEDWEB == False:
        mySqlLocalDb, cursArray, cursDict, \
        COMPANY_CODE, HOST3, USER3, PASS3, DBNAME3, BOUNCE_TIME, SLEEP_TIME, \
        TIME_GAP, NIGHT_CLOSING_HHMMSS, DAY_CLOSING_HHMMSS, \
        FORPRODUCINGORDERDATA, PROCESS, GROUPS, DESCRIPTION_TEXT, LINE_CODE, \
        WORK_DATE, DAY_NIGHT, GOODS, CODE, CAVITY, GOODSRIGHT, CODERIGHT, CAVITYRIGHT, TO_WAREHOUSE, \
        FACODE, PRODUCTSELECTION, PLCBIT, FRONTJISNO, TRADE, UI, BAUDRATE = connectWebDB()
        if mySqlLocalDb:
            CONNECTEDWEB = True
            print("3 __getProductionPerformance Database 연결 성공!")
        else:
            CONNECTEDWEB = False
            print("3 __getProductionPerformance Database 연결을 확인하시오!")
        # print("__getProductionPerformance mySqlLocalDb: ", mySqlLocalDb, "type(mySqlLocalDb):", type(mySqlLocalDb))
        # print("__getProductionPerformance cursArray: ", cursArray, "type(cursArray):", type(cursArray))
        # print("__getProductionPerformance cursDict: ", cursDict, "type(cursDict):", type(cursDict))
        # print("__getProductionPerformance HOST3: ", HOST3, "type(HOST3):", type(HOST3))
        # print("__getProductionPerformance USER3: ", USER3, "type(USER3):", type(USER3))
        # print("__getProductionPerformance DBNAME3: ", DBNAME3, "type(DBNAME3):", type(DBNAME3))

    if str(processCode).lower() == 'all' or str(processCode) == '0000':
        print("1 __getProductionPerformance() Database 선택한 공정 코드가 없습니다. 전체 공정 자료를 뿌려줍니다.")
        values = (fromDate, toDate)
        sql = "Select pa.WorkDate, pa.ProductionActualNo, pa.Code, ma.Step9, pa.Goodness, " \
              "ma.Process, pr.Language2, pr.Language3, pa.Machine, pa.Groups " \
              "From ProductionActual AS pa INNER JOIN GoodsMaster AS ma ON pa.Code = ma.Code " \
              "INNER JOIN Process AS pr ON ma.Process = pr.Code " \
              "WHERE pa.WorkDate BETWEEN %s AND %s ORDER BY pa.WorkDate DESC "
    else:
        print("__getProductionPerformance processCode: ", processCode, "에 대한 자료만 필터합니다.")
        values = (fromDate, toDate, processCode)
        sql = "Select pa.WorkDate, pa.ProductionActualNo, pa.Code, ma.Step9, pa.Goodness, " \
              "ma.Process, pr.Language2, pr.Language3, pa.Machine, pa.Groups " \
              "From ProductionActual AS pa INNER JOIN GoodsMaster AS ma ON pa.Code = ma.Code " \
              "INNER JOIN Process AS pr ON ma.Process = pr.Code " \
              "WHERE pa.WorkDate BETWEEN %s AND %s AND ma.Process = %s ORDER BY pa.WorkDate DESC "

    try:
        print("view.py __getProductionPerformance 디버깅... 1")
        print("===========================================================================================")
        print("sql: \n", sql)
        # print("values: ", values)
        print("__getProductionPerformance views.cursArrayServer() 접속을 시도합니다. 시간이 오래 걸릴수도 있습니다 잠시만 기다려 주세요...", values)
        print("===========================================================================================")
        cursArray.execute(sql, values)  # 우측은 에러 발생함에 주의. cursArrayServer.execute(sql, from_date, to_date)
        print("view.py __getProductionPerformance 디버깅... 2")
    except:
        if CONNECTEDSERVER == False:
            mySqlLocalDb, cursArray, cursDict, \
            COMPANY_CODE, HOST3, USER3, PASS3, DBNAME3, BOUNCE_TIME, SLEEP_TIME, \
            TIME_GAP, NIGHT_CLOSING_HHMMSS, DAY_CLOSING_HHMMSS, \
            FORPRODUCINGORDERDATA, PROCESS, GROUPS, DESCRIPTION_TEXT, LINE_CODE, \
            WORK_DATE, DAY_NIGHT, GOODS, CODE, CAVITY, GOODSRIGHT, CODERIGHT, CAVITYRIGHT, TO_WAREHOUSE, \
            FACODE, PRODUCTSELECTION, PLCBIT, FRONTJISNO, TRADE, UI, BAUDRATE = connectWebDB()
            if mySqlLocalDb:
                CONNECTEDWEB = True
                print("3 __getProductionPerformance Database 연결 성공!")
            else:
                CONNECTEDWEB = False
                print("3 __getProductionPerformance Database 연결을 확인하시오!")
            # print("__getProductionPerformance mySqlLocalDb: ", mySqlLocalDb, "type(mySqlLocalDb):", type(mySqlLocalDb))
            # print("__getProductionPerformance cursArray: ", cursArray, "type(cursArray):", type(cursArray))
            # print("__getProductionPerformance cursDict: ", cursDict, "type(cursDict):", type(cursDict))
            # print("__getProductionPerformance HOST3: ", HOST3, "type(HOST3):", type(HOST3))
            # print("__getProductionPerformance USER3: ", USER3, "type(USER3):", type(USER3))
            # print("__getProductionPerformance DBNAME3: ", DBNAME3, "type(DBNAME3):", type(DBNAME3))

        print("view.py __getProductionPerformance 디버깅... 1-1")
        # print("sql: \n", sql)
        # print("values: ", values)
        cursArray.execute(sql, values)  # 우측은 에러 발생함에 주의. cursArrayServer.execute(sql, from_date, to_date)
        print("view.py __getProductionPerformance 디버깅... 2-1")

    try:

        print("view.py __getProductionPerformance 디버깅... 3")
        array_sets_server = cursArray.fetchall()  # Dictionary based cursor, 선택한 "로우"가 1개 이상일 때.
        # print("view.py __getProductionPerformance 디버깅... 4")
        # print("array_sets_server: ", array_sets_server)
        # print("type(array_sets_server): ", type(array_sets_server))
        # for i, data in enumerate(array_sets_server):
        #     if i == 11314:
        #         print("i: ", i, ", data: ", data)

        print("view.py __getProductionPerformance array_sets_server: \n", array_sets_server)
        print("view.py __getProductionPerformance type(array_sets_server): ", type(array_sets_server))
        print("view.py __getProductionPerformance len(array_sets_server): ", len(array_sets_server))

        print("view.py __getProductionPerformance 디버깅... 5")
        df = pd.DataFrame(array_sets_server)  # <class 'pandas.core.frame.DataFrame'>
        # print("view.py __pp_data_period_process 디버깅... 6")

        # 2021.02.06 Added. 빈 df 확인.
        if len(df) == 0:  # len(df.index) == 0: 또는 df.shape[0] == 0: 같은 구문이다.
            print("__getProductionPerformance 조건에 맞는 자료가 없습니다. 다시 확인하시오!")
        else:
            # df.columns = ['workdate', 'code', 'machine', 'groups', 'daywork', 'goodness', 'process', 'specification']
            df.columns = ['workdate', 'productionactualno', 'code', 'step9', 'goodness',
                          'process', 'process_kor', 'process_loc', 'machine', 'groups']
            # print("컬럼명 변경 후 df: \n", df)

            # 2021.01.31 Added. workdate.작업일자 컬럼은 TimeStamp.시간 정보는 전혀 필요가 없기에, [문자형 타입]으로 변환...
            df['workdate'] = df['workdate'].astype(str)
            # print("__pp_data_period_process::type(df): ", type(df))
            # print("__pp_data_period_process::len(df): ", len(df))
            # print("__pp_data_period_process::df: \n", df)

            print("view.py __getProductionPerformance 디버깅... 7")
            df['codespec'] = df['code'] + df['step9']
            # print("__getProductionPerformance codespec 추가 후 df: \n", df)
            # print("view.py __getProductionPerformance 디버깅... 8")

    except:

        CONNECTEDSERVER = False
        # [df = pd.DataFrame()] 이 문장을 실행하지 않더라도,
        # 아래 [if df is None and isinstance(df, pd.DataFrame) and not df.empty] 여기서 걸러진다.
        # 그렇지만, 프로그램 오류 없이 걸러지기 위해, retrun 값 [df] 변수는 정의해 준다.
        df = ""
        df = pd.DataFrame(np.nan, index=[0, 1, 2, 3], columns=['A'])
        print("경고, [callMainData]에서 치명적 에러가 발생하였습니다. 관리자에게 문의하시오!")
        print("경고 df: \n", df)

    return array_sets_server, df


# def __pp_data_period_process(from_date, to_date, process_code):
def __pp_data_period_process(fromDate, toDate, processCode):
    global array_sets_server
    global CONNECTEDSERVER

    # print("__pp_data_period_process::type(fromDate): ", type(fromDate))
    # print("__pp_data_period_process::fromDate: ", fromDate)
    # print("__pp_data_period_process::type(toDate): ", type(toDate))
    # print("__pp_data_period_process::toDate: ", toDate)
    # print("__pp_data_period_process::processCode: ", processCode)

    """ UTC 로컬 시간 조정
    # date_format = '%d-%m-%Y'
    date_format = '%Y-%m-%d'

    if type(fromDate) is not str:
        unaware_start_date = datetime.datetime.strptime(fromDate, date_format)
        print("unaware_start_date: ", unaware_start_date)
        aware_start_date = pytz.utc.localize(unaware_start_date)
        print("pytz aware_start_date: ", aware_start_date)
        aware_start_date = timezone.utc.localize(unaware_start_date)
        print("timezone aware_start_date: ", aware_start_date)
    if type(toDate) is not str:
        unaware_end_date = datetime.datetime.strptime(toDate, date_format)
        print("unaware_end_date: ", unaware_end_date)
        aware_end_date = pytz.utc.localize(unaware_end_date)
        print("pytz aware_end_date: ", aware_end_date)

    # my_list = MyModel.objects.filter(created_at__range=(aware_start_date, aware_end_date))

    if type(fromDate) is not str:
        fromDate = datetime.datetime.strptime(fromDate, date_format)
    if type(toDate) is not str:
        toDate = datetime.datetime.strptime(toDate, date_format)
    """

    # print("__pp_data_period_process::자료 확인 바로 전 type(fromDate): ", type(fromDate))
    # print("__pp_data_period_process::자료 확인 바로 전 fromDate: ", fromDate)
    # print("__pp_data_period_process::자료 확인 바로 전 type(toDate): ", type(toDate))
    # print("__pp_data_period_process::자료 확인 바로 전 toDate: ", toDate)
    # print("__pp_data_period_process::자료 확인 바로 전 processCode: ", processCode)

    if CONNECTEDSERVER == False:
        try:
            msSqlServerDb, cursArrayServer, HOST0, USER0, PASS0, DBNAME0 = connectRemoteDB()
            if msSqlServerDb:
                print("1 __pp_data_period_process() Database 연결 성공!")
            else:
                CONNECTEDSERVER = False
                print("1 __pp_data_period_process() Database 연결을 확인하시오!")
            # print("msSqlServerDb: ", msSqlServerDb, "type(msSqlServerDb):", type(msSqlServerDb))  # <class 'pymssql.Connection'>
            # print("cursArrayServer: ", cursArrayServer, "type(cursArrayServer):", type(cursArrayServer))  # <class 'pymssql.Cursor'>
            # print("HOST0: ", HOST0, "type(HOST0):", type(HOST0))
            # print("USER0: ", USER0, "type(USER0):", type(USER0))
            # print("DBNAME0: ", DBNAME0, "type(DBNAME0):", type(DBNAME0))
        except:
            print("__pp_data_period_process() Database 연결 실패!!!")

    # from_date = "2020.12.28"
    # to_date = "2020.12.29"
    # process = process_code  # "2100"
    # print("__pp_data_period_process::process: ", process)

    if str(processCode).lower() == 'all' or str(processCode) == '0000':
        print("1 __pp_data_period_process() Database 선택한 공정 코드가 없습니다. 전체 공정 자료를 뿌려줍니다.")
        values = (fromDate, toDate)
        # sql = "Select pa.WorkDate, pa.ProductionActualNo, pa.Code, ma.Step9, pa.Goodness, ma.Process " \
        #       "From ProductionActual AS pa INNER JOIN GoodsMaster AS ma ON pa.Code = ma.Code " \
        #       "WHERE pa.WorkDate BETWEEN %s AND %s ORDER BY pa.WorkDate DESC "
        sql = "Select pa.WorkDate, pa.ProductionActualNo, pa.Code, ma.Step9, pa.Goodness, " \
              "ma.Process, pr.Language2, pr.Language3, pa.Machine, pa.Groups " \
              "From ProductionActual AS pa INNER JOIN GoodsMaster AS ma ON pa.Code = ma.Code " \
              "INNER JOIN Process AS pr ON ma.Process = pr.Code " \
              "WHERE pa.WorkDate BETWEEN %s AND %s ORDER BY pa.WorkDate DESC "
    else:
        print("__pp_data_period_process processCode: ", processCode, "에 대한 자료만 필터합니다.")
        values = (fromDate, toDate, processCode)
        # sql = "Select pa.WorkDate, pa.ProductionActualNo, pa.Code, ma.Step9, pa.Goodness, ma.Process " \
        #       "From ProductionActual AS pa INNER JOIN GoodsMaster AS ma ON pa.Code = ma.Code " \
        #       "WHERE pa.WorkDate BETWEEN %s AND %s AND ma.Process = %s ORDER BY pa.WorkDate DESC "
        sql = "Select pa.WorkDate, pa.ProductionActualNo, pa.Code, ma.Step9, pa.Goodness, " \
              "ma.Process, pr.Language2, pr.Language3, pa.Machine, pa.Groups " \
              "From ProductionActual AS pa INNER JOIN GoodsMaster AS ma ON pa.Code = ma.Code " \
              "INNER JOIN Process AS pr ON ma.Process = pr.Code " \
              "WHERE pa.WorkDate BETWEEN %s AND %s AND ma.Process = %s ORDER BY pa.WorkDate DESC "

    try:
        print("view.py __pp_data_period_process 디버깅... 1")
        print("===========================================================================================")
        print("sql: \n", sql)
        # print("values: ", values)
        print("views.cursArrayServer() 접속을 시도합니다. 시간이 오래 걸릴수도 있습니다 잠시만 기다려 주세요...", values)
        print("===========================================================================================")
        cursArrayServer.execute(sql, values)  # 우측은 에러 발생함에 주의. cursArrayServer.execute(sql, from_date, to_date)
        print("view.py __pp_data_period_process 디버깅... 2")
    except:
        if CONNECTEDSERVER == False:
            msSqlServerDb, cursArrayServer, HOST0, USER0, PASS0, DBNAME0 = connectRemoteDB()
            if msSqlServerDb == -1:
                CONNECTEDSERVER = False
                # print("view.py __pp_data_period_process HOST0: ", HOST0)
                # print("view.py __pp_data_period_process USER0: ", USER0)
                # print("view.py __pp_data_period_process DBNAME0: ", DBNAME0)
                # print("cursArrayServer: ", cursArrayServer)
                # print("2 __pp_data_period_process() Database 연결을 확인하시오!")
                df = ""
                df = pd.DataFrame(np.nan, index=[0, 1, 2, 3], columns=['A'])
                print("경고, [callMainData]에서 치명적 에러가 발생하였습니다. 관리자에게 문의하시오!")
                print("경고 df: \n", df)
            else:
                print("view.py __pp_data_period_process 연결 성공! msSqlServerDb: ", msSqlServerDb)

        print("view.py __pp_data_period_process 디버깅... 1-1")
        # print("sql: \n", sql)
        # print("values: ", values)
        cursArrayServer.execute(sql, values)  # 우측은 에러 발생함에 주의. cursArrayServer.execute(sql, from_date, to_date)
        print("view.py __pp_data_period_process 디버깅... 2-1")

    try:
        print("view.py __pp_data_period_process 디버깅... 3")
        array_sets_server = cursArrayServer.fetchall()  # Dictionary based cursor, 선택한 "로우"가 1개 이상일 때.
        # print("view.py __pp_data_period_process 디버깅... 4")
        # print("array_sets_server: ", array_sets_server)
        # print("type(array_sets_server): ", type(array_sets_server))
        # for i, data in enumerate(array_sets_server):
        #     if i == 11314:
        #         print("i: ", i, ", data: ", data)

        # 2020.12.17 Conclusion. 여기 까지 정상적으로 처리되었을 때, 아래와 같이 [pandas]로 처리해 준다.
        # 2021.01.09 Conclusion. read_sql()도 안 읽어 지고, frame_query()도 안 읽어 지네...
        # 또한 f_common.py/def connectRemoteDB() 내부에서,
        # cursArrayServer = msSqlServerDb.cursor(as_dict=True) : 와 같이, [as_dict=True] 옵션을 주면, 절대 안 된다...

        # df = pd.read_sql(sql, msSqlServerDb)
        # df = pd.read_sql(sql=sql, con=msSqlServerDb)
        # df = pdsql.frame_query(sql, msSqlServerDb)
        # for index, row in df.iterrows():
        #     print("index: ", index, ", row[0]: ", row[0])
        #     print("index: ", index, ", row[0]: ", row[1])

        print("view.py __pp_data_period_process 디버깅... 5")
        df = pd.DataFrame(array_sets_server)  # <class 'pandas.core.frame.DataFrame'>
        # print("view.py __pp_data_period_process 디버깅... 6")
        # 2021.02.06 Added. 빈 df 확인.
        if len(df) == 0:  # len(df.index) == 0: 또는 df.shape[0] == 0: 같은 구문이다.
            print("조건에 맞는 자료가 없습니다. 다시 확인하시오!")
        else:
            # print("df: \n", df, "\n")
            # print("type(df): ", type(df))  # <class 'pandas.core.frame.DataFrame'>

            # queryset = []
            # for i, d in enumerate(df):
            #     queryset =
            #     print("__pp_data_period_process index: ", i, ", d: ", d)

            # # if df is not None and isinstance(df, pd.DataFrame) and not df.empty:
            # if df is None or df.empty:
            #     print("DataFrame [df]에 자료가 없습니다. 전월 자료를 검색합니다.")
            # else:

            # if LANGUAGE_NO == 1042:

            # df.columns = ['workdate', 'code', 'machine', 'groups', 'daywork', 'goodness', 'process', 'specification']
            df.columns = ['workdate', 'productionactualno', 'code', 'step9', 'goodness',
                          'process', 'process_kor', 'process_loc', 'machine', 'groups']
            # print("컬럼명 변경 후 df: \n", df)

            # 2021.01.31 Added. workdate.작업일자 컬럼은 TimeStamp.시간 정보는 전혀 필요가 없기에, [문자형 타입]으로 변환...
            df['workdate'] = df['workdate'].astype(str)
            # print("__pp_data_period_process::type(df): ", type(df))
            # print("__pp_data_period_process::len(df): ", len(df))
            # print("__pp_data_period_process::df: \n", df)

            print("view.py __pp_data_period_process 디버깅... 7")
            df['codespec'] = df['code'] + df['step9']
            # print("codespec 추가 후 df: \n", df)
            # print("view.py __pp_data_period_process 디버깅... 8")

            # # 먼저 지정된 기간만의 자료 필터...
            # df = df.loc[df['workdate'].between(from_date, to_date)]
                # df['codespec'] = df['code'] + df['specification']
                # print("codespec 추가 후 df: \n", df)

    except:

        CONNECTEDSERVER = False
        # [df = pd.DataFrame()] 이 문장을 실행하지 않더라도,
        # 아래 [if df is None and isinstance(df, pd.DataFrame) and not df.empty] 여기서 걸러진다.
        # 그렇지만, 프로그램 오류 없이 걸러지기 위해, retrun 값 [df] 변수는 정의해 준다.
        df = ""
        df = pd.DataFrame(np.nan, index=[0, 1, 2, 3], columns=['A'])
        print("경고, [callMainData]에서 치명적 에러가 발생하였습니다. 관리자에게 문의하시오!")
        print("경고 df: \n", df)

    cursArrayServer.close()
    msSqlServerDb.close()

    # serializer = dict(results1)
    # print("serializer: \n", serializer)

    print("view.py __pp_data_period_process len(array_sets_server): ", len(array_sets_server))
    # print("len(df): ", len(df))
    # print("df.count(): ", df.count())

    # return render(request, 'index.html', {'ProductionActual': results1})
    return array_sets_server, df  # df


def __getProcess(beInUse):
    # qrProcess = Process.objects.filter(beInUse=beInUse)
    qrProcess = Process.objects.all()
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

    # 컬럼 [codespec] 추가...
    # if LANGUAGE_NO == 1042:
    #     dfProcess['codespec'] = dfProcess['code'] + " " + dfProcess['language2']
    # else:
    #     dfProcess['codespec'] = dfProcess['code'] + " " + dfProcess['language3']
    # print("__getProcess codespec 추가 후 dfProcess: \n", dfProcess)

    # options = [{'label': x, 'value': x} for x in sorted(dfProcess.codespec.unique())],


def __process(beInUse):
    global CONNECTEDSERVER
    if CONNECTEDSERVER == False:
        try:
            msSqlServerDb, cursArrayServer, HOST0, USER0, PASS0, DBNAME0 = connectRemoteDB()
            if msSqlServerDb:
                print("1 __process() 연결 성공!")

                # for Debugging...
                # ls = ""
                # rtnString = pyautogui.alert("현재 여기까지 실행되었음을 확인함!!!!!!!!!!!", "Info", "OK")
                # rtnString = pyautogui.confirm(text="현재 views.py __process() 여기!", title="Info", buttons=["OK", "Cancel"])

            else:
                CONNECTEDSERVER = False
                print("1 __process() Database 연결을 확인하시오!")
            # print("msSqlServerDb: ", msSqlServerDb, "type(msSqlServerDb):", type(msSqlServerDb))  # <class 'pymssql.Connection'>
            # print("cursArrayServer: ", cursArrayServer, "type(cursArrayServer):", type(cursArrayServer))  # <class 'pymssql.Cursor'>
            # print("HOST0: ", HOST0, "type(HOST0):", type(HOST0))
            # print("USER0: ", USER0, "type(USER0):", type(USER0))
            # print("DBNAME0: ", DBNAME0, "type(DBNAME0):", type(DBNAME0))
        except:
            CONNECTEDSERVER = False
            dfProcess = ""
            dfProcess = pd.DataFrame(np.nan, index=[0, 1, 2, 3], columns=['A'])
            print("경고, [callProcess]에서 치명적 에러가 발생하였습니다. 관리자에게 문의하시오!")
            print("경고 dfProcess: \n", dfProcess)
            print("__process() Database 연결 실패!!!")

    # 1. 공정별
    sql = "Select Code, Language1, Language2, Language3, Language4 From Process " \
          "Where BeInUse = %s ORDER BY Code DESC"

    try:
        cursArrayServer.execute(sql, beInUse)
    except:
        if CONNECTEDSERVER == False:
            msSqlServerDb, cursArrayServer, HOST0, USER0, PASS0, DBNAME0 = connectRemoteDB()
            if msSqlServerDb:
                print("2 __process() 연결 성공!")
            else:
                CONNECTEDSERVER = False
                print("2 __process() Database 연결을 확인하시오!")

        cursArrayServer.execute(sql, beInUse)

    try:
        array_sets_server = cursArrayServer.fetchall()  # Dictionary based cursor, 선택한 "로우"가 1개 이상일 때.
        # print("\nProcess type(array_sets_server): ", type(array_sets_server))  # <class 'list'>
        # print("array_sets_server: \n", array_sets_server, "\n")
        # for i, data in enumerate(array_sets_server):
        #     print("i: ", i, ", data: ", data)

        # # 2020.12.17 Conclusion. 여기 까지 정상적으로 처리되었을 때, 아래와 같이 [pandas]로 처리해 준다.
        # # df = pd.read_sql(sql, msSqlServerDb)
        # dfProcess = pd.DataFrame(array_sets_server)  # <class 'pandas.core.frame.DataFrame'>
        # # print("dfProcess: \n", dfProcess)
        # # print("type(dfProcess): ", type(dfProcess))  # <class 'pandas.core.frame.DataFrame'>
        #
        # dfProcess.columns = ['code', 'language1', 'language2', 'language3', 'language4']
        # # print("컬럼명 변경 후 dfProcess: \n", dfProcess)
        #
        # # 컬럼 [codespec] 추가...
        # dfProcess['codespec'] = dfProcess['code'] + " " + dfProcess['language3']
        # # print("codespec 추가 후 dfProcess: \n", dfProcess)
        #
        # # options = [{'label': x, 'value': x} for x in sorted(dfProcess.codespec.unique())],

    except:
        CONNECTEDSERVER = False
        # # [dfProcess = pd.DataFrame()] 이 문장을 실행하지 않더라도,
        # # 아래 [if df_process is None and isinstance(dfProcess, pd.DataFrame) and not dfProcess.empty] 여기서 걸러진다.
        # # 그렇지만, 프로그램 오류 없이 걸러지기 위해, retrun 값 [dfProcess] 변수는 정의해 준다.
        # dfProcess = ""
        # dfProcess = pd.DataFrame(np.nan, index=[0, 1, 2, 3], columns=['A'])
        print("경고, [callProcess]에서 치명적 에러가 발생하였습니다. 관리자에게 문의하시오!")
        # print("경고 dfProcess: \n", dfProcess)

    cursArrayServer.close()
    msSqlServerDb.close()

    # serializer = dict(dfProcess)
    # print("serializer: \n", serializer)

    if processCode == 'all':
        processList = [data for data in array_sets_server]
    else:
        processList = [data for data in array_sets_server if data[0] == processCode]

    # processList = [data for data in processList]
    # print("process_selected::type(processList): ", type(processList))
    # print("process_selected::processList: \n", processList)
    total_process_count = len(processList)
    # print("process_selected total_process_count: ", total_process_count)

    return array_sets_server, processList, total_process_count


def production_performance(request, process):
    pp_data = ProductionActual.objects.filter(process=process)

    context = {'pp_data': pp_data}

    return render(request, 'ppp/dashboard.html', context)

# {% url 'process' process.code %}

class Index(View):
    def get(self, request):
        print("views.py::Index::request: ", request)
        # return render(request, 'ppp/dashboard.html')
        return render(request, 'ppp/index.html')


# @csrf_exempt
# class PeriodView(View):
#     def get(self, request):
#         context = {}
#



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

    # pyautogui.alert(fromDate+", "+toDate+", "+processCode, "views.py home()")

    # if request.POST['process_code'] == "":
    #     # 2021.01.20 Conclusion. urls.py 내부에,
    #     # path('process/<str:process_code>/', views.process_code, name='process-code'), 요래 [process_code] 함수가 있는
    #     # 상태에서, 아래와 같이 같은 이름으로 변수를 지정하면, 절대 안 된다. 변수 값을 얻지 못하네요... 함수명을 변경한다.
    #     process_code = "all"  # "all"  # "2100"
    # else:
    #     print("views.py home request.POST['process_code']: ", request.POST['process_code'])

    # for Debugging...
    # 여기 views.py에서 어떤 messages를 .html 파일로 보낼 때...
    # return render("example.html", messages=anyValue)
    # 저쪽 example.html에서,
    # <script>
    #    alert({{messages}})
    # </script>

    # .html 파일에서 여기 views.py로 보내온 어떤 messages를 확인할 때...
    # def postNew(request):
        # if form.is_valid():
        # post = form.save()
        # messages.add_message(request, messages.INFO, "새 글이 등록되었습니다!") # 첫번째, 초기 지원
        # messages.info(request, "새 글이 등록되었습니다!!!") # 두번째, shortcut 형태
        # return redirect(post)

    # .html 파일에서 렌더링을 통해 메시지 노출...
    # messages context processors를 통해 message list 접근
    # {% if messages %}
    # <div class="container">
    #    {% for message in messages %}
    #        <div class="alert alert-{{ message.tags }}">
    #        [{{ message.tags }}]
    #        [{{ message.message }}]
    #        </div>
    #    {% endfor %}
    # </div>
    # {% endif %}

    # qr_process, df_process = __process(beInUse)  # Process.objects.get(code=process_code_selected)
    qrProcess, processList,  total_process_count = __getProcess(beInUse)  # Process.objects.get(code=process_code_selected)

    print("home qrProcess: ", qrProcess)
    print("home processList: ", processList)
    print("home total_process_count: ", total_process_count)

    # pp_data_period_process, df_data_period_process = __pp_data_period_process(from_date, to_date, process_code)
    # pp_data_period_process, df_data_period_process = __pp_data_period_process(fromDate, toDate, processCode)

    pp_data_period_process, df_data_period_process = __getProductionPerformance(fromDate, toDate, processCode)

    # 2021.02.06 Added. 빈 df 확인.
    if len(df_data_period_process) == 0:  # len(df.index) == 0: 또는 df.shape[0] == 0: 같은 구문이다.
        print("views.py home 조건에 맞는 자료가 없습니다. 다시 확인하시오!")
        print("views.py home 현재 자료를 정리하지 못 했습니다. 관리자에게 문의하시오!", fromDate, " ", toDate, " ", processCode)
        print("views.py home 해당 자료가 전혀 없습니다!")
        # context = {'process': process, 'ppData': [], 'total_pp_data_count': 0,
        #            'pp_data_period_process': pp_data_period_process, 'LANGUAGE_NO': LANGUAGE_NO}
        context = {"qrProcess": qrProcess, "ppDataPeriodProcessList": [], "products": [],
                   "productsCount": 0, "pp_data_period_process": pp_data_period_process,
                   'fromDate': fromDate, 'toDate': toDate, 'processCode': processCode, 'LANGUAGE_NO': LANGUAGE_NO}
        return render(request, 'ppp/index.html', context)
        # return redirect("home")


    ppDataPeriodProcessList, products, productsCount, ppDataPeriod = makingProduction(
        pp_data_period_process, df_data_period_process)
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
    # print("home::type(pp_data_period_process): ", type(pp_data_period_process))
    # print("home::pp_data_period_process: \n", pp_data_period_process)

    # windll = ctypes.windll.kernel32
    # LANGUAGE_NO = windll.GetUserDefaultUILanguage()  # 1033, 1042
    # LANGUAGE_CODE = locale.windows_locale[windll.GetUserDefaultUILanguage()]  # en_US, ko_KR
    # print("process_selected LANGUAGE_NO: ", LANGUAGE_NO, ", LANGUAGE_CODE: ", LANGUAGE_CODE)

    context = {"qrProcess": qrProcess, "ppDataPeriodProcessList": ppDataPeriodProcessList, "products": products,
               "productsCount": productsCount, "pp_data_period_process": pp_data_period_process,
               "ppDataPeriod": ppDataPeriod, 'fromDate': fromDate, 'toDate': toDate, 'processCode': processCode}
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


@csrf_exempt
# def period(request, from_date, to_date, process_code):
def period(request):  #, *args, **kwargs):
# def post(self, request):  #, *args, **kwargs):
    global fromDate, toDate, processCode

    print("\n\n\n\n\nperiod------------------------------------------------------------------------------------------")

    data = dict()
    data['is_valid_post'] = False
    data['is_valid_get'] = False

    if request.method == "POST":
        if len(request.POST) > 0:
            data['is_valid_post'] = True
            fromDate = request.POST['fromDate']
            toDate = request.POST['toDate']
            processCode = request.POST['processCode']
            print("views.py period() POST fromDate: ", fromDate)
            print("views.py period() POST toDate: ", toDate)
            print("views.py period() POST processCode: ", processCode)
        else:
            # 2021.02.05 for Debugging... 잠깐만...
            fromDate = fromDateDefault  # "2020.12.01"
            toDate = toDateDefault  # "2020.12.31"
            processCode = "all"  # "all"  # "2100"
            print("views.py period() POST 0 fromDate: ", fromDate)
            print("views.py period() POST 0 toDate: ", toDate)
            print("views.py period() POST 0 processCode: ", processCode)
    elif request.method == "GET":
        if len(request.GET) > 0:
            data['is_valid_get'] = True
            fromDate = request.GET['fromDate']
            toDate = request.GET['toDate']
            processCode = request.GET['processCode']
            print("views.py period() GET fromDate: ", fromDate)
            print("views.py period() GET toDate: ", toDate)
            print("views.py period() GET processCode: ", processCode)
        else:
            # 2021.02.05 for Debugging... 잠깐만...
            fromDate = fromDateDefault  # "2020.12.01"
            toDate = toDateDefault  # "2020.12.31"
            processCode = "all"  # "all"  # "2100"
            print("views.py period() GET 0 fromDate: ", fromDate)
            print("views.py period() GET 0 Date: ", toDate)
            print("views.py period() GET 0 processCode: ", processCode)

        # print("views.py period() fromDate: ", fromDate)
        # print("views.py period() toDate: ", toDate)
        # print("views.py period() processCode: ", processCode)

    # pyautogui.alert(fromDate+", "+toDate+", "+processCode, "views.py period()")

    # 2021.01.27 Conclusion. ***** Dictionary.딕셔너리 자료형으로 만들어서 보내면, 절대 안 된다. 반드시 리스트 형식으로 보낸다.
    rsDictSum = {}
    rsListSum = []

    # print("\views.py period 확인 process_code: ", processCode)
    # print("views.py period 확인 fromDate: ", fromDate)
    # print("views.py period 확인 toDate: ", toDate)

    # 2021.01.20 Conclusion. urls.py 내부에,
    # path('process/<str:process_code>/', views.process_code, name='process-code'), 요래 [process_code] 함수가 있는
    # 상태에서, 아래와 같이 같은 이름으로 변수를 지정하면, 절대 안 된다. 변수 값을 얻지 못하네요... 함수명을 변경한다.

    # from .views import __process, __pp_data_period_process
    # qr_process, df_process = __process(beInUse)  # Process.objects.get(code=process_code_selected)
    qrProcess, processList, total_process_count = __getProcess(beInUse)  # Process.objects.get(code=process_code_selected)

    print("views.py period qrProcess: \n", qrProcess)
    print("views.py period processList: \n", processList)
    print("views.py period total_process_count: ", total_process_count)

    # ***** 여기서 또한 엄청 중요한 것은, ***** : customer.html 화면의 아래 부분에, Order 정보를 뿌려 주는 화면이 있으므로,
    # customer를 클릭하면, 해당 customer가 주문한 order 정보를 같이 가져다가, Order 정보 부분에 뿌려줘야 한다.
    # pp_data_period_process, df_data_period_process = __pp_data_period_process(fromDate, toDate, processCode)

    pp_data_period_process, df_data_period_process = __getProductionPerformance(fromDate, toDate, processCode)
    # print("period 리턴 값 len(pp_data_period_process): ", len(pp_data_period_process))
    # print("period 리턴 값 type(pp_data_period_process): ", type(pp_data_period_process))
    # print("period 리턴 값 pp_data_period_process: \n", pp_data_period_process)
    # print("period 리턴 값 len(df_data_period_process): ", len(df_data_period_process))
    # print("period 리턴 값 type(df_data_period_process): ", type(df_data_period_process))
    # print("period 리턴 값 df_data_period_process: \n", df_data_period_process)

    # 2021.02.06 Added. 빈 df 확인.
    if len(df_data_period_process) == 0:  # len(df.index) == 0: 또는 df.shape[0] == 0: 같은 구문이다.
        print("views.py period 조건에 맞는 자료가 없습니다. 다시 확인하시오!")
        print("views.py period 현재 자료를 정리하지 못 했습니다. 관리자에게 문의하시오!", fromDate, " ", toDate, " ", processCode)
        print("views.py period 해당 자료가 전혀 없습니다!")
        # context = {'process': process, 'ppData': [], 'total_pp_data_count': 0,
        #            'pp_data_period_process': pp_data_period_process, 'LANGUAGE_NO': LANGUAGE_NO}
        context = {"qrProcess": qrProcess, "ppDataPeriodProcessList": [], "products": [],
                   "productsCount": 0, "pp_data_period_process": pp_data_period_process,
                   'fromDate': fromDate, 'toDate': toDate, 'processCode': processCode, 'LANGUAGE_NO': LANGUAGE_NO}
        # return render(request, 'ppp/process.html', context)
        return render(request, 'ppp/index.html', context)
        # 2021.02.19 Conclusion. [자료가 없습니다.] 메시지를 뿌리고, [home]으로 가도 가야된다. 메시지 없이 바로 가면 헷갈린다.
        # return redirect("home")

        # return JsonResponse(context, safe=False)
        # data['pp_data'] = render_to_string("ppp/process.html", {"pp_data_period_process": pp_data_period_process})

        # context = {"pp_data_period_process": pp_data_period_process}
        # data['pp_data'] = render_to_string("ppp/process.html", context, request=request)
        # return JsonResponse(data, safe=False)

    ppDataPeriodProcessList, products, productsCount, ppDataPeriod = makingProduction(
        pp_data_period_process, df_data_period_process)
    # return ppDataPeriodProcessList, products, productsCount, pp_data_period_process, ppDataPeriod

    # print("period::type(ppDataPeriodProcessList): ", type(ppDataPeriodProcessList))
    # print("period::ppDataPeriodProcessList: \n", ppDataPeriodProcessList)
    # print("period::type(products): ", type(products))
    # print("period::products: \n", products)
    # print("period::type(productsCount): ", type(productsCount))
    # print("period::productsCount: \n", productsCount)
    # print("period::type(pp_data_period_process): ", type(pp_data_period_process))
    # print("period::pp_data_period_process: \n", pp_data_period_process)
    # print("period::type(ppDataPeriod): ", type(ppDataPeriod))
    # print("period::ppDataPeriod: \n", ppDataPeriod)

    # windll = ctypes.windll.kernel32
    # LANGUAGE_NO = windll.GetUserDefaultUILanguage()  # 1033, 1042
    # LANGUAGE_CODE = locale.windows_locale[windll.GetUserDefaultUILanguage()]  # en_US, ko_KR
    # print("period LANGUAGE_NO: ", LANGUAGE_NO, ", LANGUAGE_CODE: ", LANGUAGE_CODE)

    # context = {"process": process, "ppDataPeriodProcessList": ppDataPeriodProcessList, "products": products,
    #            "productsCount": productsCount, "pp_data_period_process": pp_data_period_process,
    #            "ppDataPeriod": ppDataPeriod, 'fromDate': fromDate, 'toDate': toDate, 'processCode': processCode}
    context = {"qrProcess": qrProcess, "ppDataPeriodProcessList": ppDataPeriodProcessList, "products": products,
               "productsCount": productsCount, "pp_data_period_process": pp_data_period_process,
               "ppDataPeriod": ppDataPeriod, 'fromDate': fromDate, 'toDate': toDate, 'processCode': processCode}

    print("views.py period() fromDate: ", fromDate)
    print("views.py period() toDate: ", toDate)
    print("views.py period() processCode: ", processCode)

    return render(request, 'ppp/index.html', context)

    # return render(request, 'ppp/process.html', context)
    # return JsonResponse(context, safe=False)
    # return jsonify({'htmlresponse': render_template('table_pp_data.html', context=context)})

    # 2021.02.18 Conclusion. Ajax 회신 값으로는 반드시 아래와 같이 보내야 한다.
    # data['pp_data'] = render_to_string("ppp/process.html", {"pp_data_period_process": pp_data_period_process})

    # context = {"pp_data_period_process": pp_data_period_process}
    # data['pp_data'] = render_to_string("ppp/process.html", context, request=request)
    # return JsonResponse(data, safe=False)


# ***** 엄청 중요 ***** # 원래 위와 같은 [class]에서, 사용자가 customer.html 뿌려진 화면에서, 특정 customer를 클릭했을 때, 특정한 customer만 화면에 뿌려주는 방법...
@csrf_exempt
# def process_selected(request, process_code):
def process_selected(request):  #, processCode):
    global fromDate, toDate, processCode

    print("\n\n\n\n\nprocess_selected================================================================================")

    data = dict()
    data['is_valid_post'] = False
    data['is_valid_get'] = False

    if request.method == "POST":
        if len(request.POST) > 0:
            data['is_valid_post'] = True
            fromDate = request.POST['fromDate']
            toDate = request.POST['toDate']
            processCode = request.POST['processCode']
            print("views.py process_selected() POST fromDate: ", fromDate)
            print("views.py process_selected() POST oDate: ", toDate)
            print("views.py process_selected() POST processCode: ", processCode)
        else:
            # 2021.02.05 for Debugging... 잠깐만...
            fromDate = fromDateDefault  # "2020.12.01"
            toDate = toDateDefault  # "2020.12.31"
            processCode = "all"  # "all"  # "2100"
    elif request.method == "GET":
        if len(request.GET) > 0:
            data['is_valid_get'] = True
            fromDate = request.GET['fromDate']
            toDate = request.GET['toDate']
            processCode = request.GET['processCode']
            print("views.py process_selected() GET fromDate: ", fromDate)
            print("views.py process_selected() GET toDate: ", toDate)
            print("views.py process_selected() GET processCode: ", processCode)
        else:
            # 2021.02.05 for Debugging... 잠깐만...
            fromDate = fromDateDefault  # "2020.12.01"
            toDate = toDateDefault  # "2020.12.31"
            processCode = "all"  # "all"  # "2100"

        # print("views.py process_selected() fromDate: ", fromDate)
        # print("views.py process_selected() toDate: ", toDate)
        # print("views.py process_selected() processCode: ", processCode)

    # process_code_selected = process_code
    # print("\nprocess_selected process_code_selected: ", process_code_selected)

    # 2021.01.27 Conclusion. ***** Dictionary.딕셔너리 자료형으로 만들어서 보내면, 절대 안 된다. 반드시 리스트 형식으로 보낸다.
    rsDictSum = {}
    rsListSum = []

    # print("\nprocess_selected process_code: ", process_code)
    # print("process_selected from_date: ", from_date)
    # print("process_selected to_date: ", to_date)

    # 2021.01.20 Conclusion. urls.py 내부에,
    # path('process/<str:process_code>/', views.process_code, name='process-code'), 요래 [process_code] 함수가 있는
    # 상태에서, 아래와 같이 같은 이름으로 변수를 지정하면, 절대 안 된다. 변수 값을 얻지 못하네요... 함수명을 변경한다.

    # qr_process, df_process = __process(beInUse)  # Process.objects.get(code=process_code_selected)
    qrProcess, processList, total_process_count = __getProcess(beInUse)  # Process.objects.get(code=process_code_selected)

    print("process_selected qrProcess: \n", qrProcess)
    print("process_selected processList: \n", processList)
    print("process_selected total_process_count: ", total_process_count)

    # process = process.filter(code=process_code)  # 에러...
    # print("process_selected total_process_count: ", total_process_count)

    # ***** 여기서 또한 엄청 중요한 것은, ***** : customer.html 화면의 아래 부분에, Order 정보를 뿌려 주는 화면이 있으므로,
    # customer를 클릭하면, 해당 customer가 주문한 order 정보를 같이 가져다가, Order 정보 부분에 뿌려줘야 한다.
    # pp_data_period_process, df_data_period_process = __pp_data_period_process(fromDate, toDate, processCode)
    pp_data_period_process, df_data_period_process = __getProductionPerformance(fromDate, toDate, processCode)

    # 2021.02.06 Added. 빈 df 확인.
    if len(df_data_period_process) == 0:  # len(df.index) == 0: 또는 df.shape[0] == 0: 같은 구문이다.
        print("views.py home 조건에 맞는 자료가 없습니다. 다시 확인하시오!")
        print("views.py home 현재 자료를 정리하지 못 했습니다. 관리자에게 문의하시오!", fromDate, " ", toDate, " ", processCode)
        print("views.py home 해당 자료가 전혀 없습니다!")
        # context = {'process': process, 'ppData': [], 'total_pp_data_count': 0,
        #            'pp_data_period_process': pp_data_period_process, 'LANGUAGE_NO': LANGUAGE_NO}
        context = {"qrProcess": qrProcess, "ppDataPeriodProcessList": [], "products": [],
                   "productsCount": 0, "pp_data_period_process": pp_data_period_process,
                   'fromDate': fromDate, 'toDate': toDate, 'processCode': processCode, 'LANGUAGE_NO': LANGUAGE_NO}
        return render(request, 'ppp/index.html', context)
        # return redirect("home")
        # data['pp_data'] = render_to_string("ppp/process.html", {"pp_data_period_process": pp_data_period_process})
        # context = {"pp_data_period_process": pp_data_period_process}
        # data['pp_data'] = render_to_string("ppp/process.html", context, request=request)
        # return JsonResponse(data, safe=False)

    # 2021.01.27 Conclusion. [pp_data_period_process] 이넘은 [table_pp_data.html]에서 항상 사용해야 하므로, 절대 이름 유지.
    # print("process_selected::type(pp_data_period_process): ", type(pp_data_period_process))
    # print("process_selected::len(pp_data_period_process): ", len(pp_data_period_process))
    # print("process_selected::pp_data_period_process: \n", pp_data_period_process)
    # print("process_selected::type(df_data_period_process): ", type(df_data_period_process))
    # print("process_selected::len(df_data_period_process): ", len(df_data_period_process))
    # print("process_selected::df_data_period_process: \n", df_data_period_process)


    ppDataPeriodProcessList, products, productsCount, ppDataPeriod = makingProduction(pp_data_period_process, df_data_period_process)
    # print("process_selected::type(ppDataPeriod): ", type(ppDataPeriod))
    # print("process_selected::ppDataPeriod: \n", ppDataPeriod)
    # print("process_selected::type(process): ", type(process))
    # print("process_selected::process: \n", process)
    # print("process_selected::type(rsDictSum): ", type(ppData))
    # print("process_selected::rsDictSum: \n", ppData)
    # print("process_selected::type(rsDictSum): ", type(rsDictSum))
    # print("process_selected::rsDictSum: \n", rsDictSum)
    # print("process_selected::type(rsListSum): ", type(rsListSum))
    # print("process_selected::rsListSum: \n", rsListSum)
    # print("process_selected::type(rsTupleSum): ", type(rsTupleSum))
    # print("process_selected::rsTupleSum: \n", rsTupleSum)
    # print("process_selected::type(pp_data_period_process): ", type(pp_data_period_process))
    # print("process_selected::pp_data_period_process: \n", pp_data_period_process)

    # windll = ctypes.windll.kernel32
    # LANGUAGE_NO = windll.GetUserDefaultUILanguage()  # 1033, 1042
    # LANGUAGE_CODE = locale.windows_locale[windll.GetUserDefaultUILanguage()]  # en_US, ko_KR
    # print("process_selected LANGUAGE_NO: ", LANGUAGE_NO, ", LANGUAGE_CODE: ", LANGUAGE_CODE)

    context = {"qrProcess": qrProcess, "ppDataPeriodProcessList": ppDataPeriodProcessList, "products": products,
               "productsCount": productsCount, "pp_data_period_process": pp_data_period_process,
               "ppDataPeriod": ppDataPeriod, 'fromDate': fromDate, 'toDate': toDate, 'processCode': processCode}
    print("views.py process_selected() fromDate: ", fromDate)
    print("views.py process_selected() toDate: ", toDate)
    print("views.py process_selected() processCode: ", processCode)
    print("views.py process_selected() productsCount: ", productsCount)
    # print("views.py process_selected() pp_data_period_process: \n", pp_data_period_process)
    print("views.py process_selected() len(pp_data_period_process): ", len(pp_data_period_process))

    print("views.py process_selected() request: ", request)
    print("views.py process_selected() request.POST: ", request.POST)
    print("views.py process_selected() len(request.POST): ", len(request.POST))
    print("views.py process_selected() request.method: ", request.method)

    # return render(request, 'ppp/index.html', context)
    # return render(request, 'ppp/process.html', context)

    # 2021.02.18 Conclusion. Ajax 회신 값으로는 반드시 아래와 같이 보내야 한다.

    # 아래와 같이 직접 값{}을 보내면 이런 치명적 에러가 발생한다.
    # data['pp_data'] = render_to_string("ppp/process.html", {"pp_data_period_process": pp_data_period_process})

    # E:\ps\venv\lib\site-packages\django\template\defaulttags.py:65: UserWarning: A {% csrf_token %} was used
    # in a template, but the context did not provide the value.  This is usually caused by not using Request Context.

    return render(request, 'ppp/index.html', context)

    # context = {"pp_data_period_process": pp_data_period_process}
    data['pp_data'] = render_to_string("ppp/process.html", context, request=request)
    # data['pp_data'] = render_to_string("ppp/process.html", context)
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


def pp_process_summary(request):
    # global from_date, to_date, process_code
    #
    # from_date = from_date
    # to_date = to_date
    # process_code = process_code

    finalrep = {}

    '''
    all_tables = connection.introspection.table_names()
    print("all_tables: ", all_tables)
    if 'productionactual' in all_tables:  # 반드시 소문자로 기입해야 된다. 'ProductionActual' 이렇게 기록하면, 에러...
        # pp_data = ProductionActual.objects.filter(owner=request.user, workdate__gte=six_months_ago, workdate__lte=todays_date)  # Cannot resolve keyword 'owner' into field.
        pp_data = ProductionActual.objects.filter(workdate__gte=six_months_ago, workdate__lte=todays_date)
        # 여기서는 요기를 사용하지 않는다. 다만, 디버깅을 해본 것이다.
        print("ProductionActual 테이블이 있습니다!")
    else:
        print("ProductionActual 테이블이 없습니다!")

    # print("pp_process_summary::type(pp_data): ", type(pp_data))  # 테이블 자체가 없어도, 요기만은 에러가 나지 않는다.

    # if not pp_data:  # 테이블 자체가 없으면, 이것도 에러...
    #     print("조건에 만족하는 생산 실적 자료가 없습니다!")
    # print("pp_process_summary::type(pp_data): ", type(pp_data))  # 테이블 자체가 없으면, 이것도 에러...
    # if not pp_data:  # 테이블 자체가 없으면, 이것도 에러...
    #     print("pp_data 자료가 없습니다!!!!!!!!!!!!!!!!!!!!!!!!")
    # if len(pp_data) == 0:  # 테이블 자체가 없으면, 이것도 에러...
        # if ProductionActual.objects.none():  # 테이블 자체가 없으면, 이것도 에러...
        # if pp_data is None:  # 테이블 자체가 없으면, 이것도 에러...

    # 2021.01.21 Conclusion. 도대체 django.QuerySet 객체의, pp_data 값은 무었일까?
    # [productionactual] 테이블에는 [process] 필드가 없기 때문에, [productionactualno] 필드로 한다.
    def get_productionactualno(pp_data):
        # print("pp_process_summary::get_productionactualno::type(pp_data): ", type(pp_data))
        # print("pp_process_summary::get_productionactualno::pp_data: \n", pp_data)
        # print("pp_process_summary::get_productionactualno::pp_data.productionactualno: ", pp_data.productionactualno)
        return pp_data.productionactualno

    get_productionactualno_list = list(set(map(get_productionactualno, pp_data)))
    # print("pp_process_summary::get_pp_data_process::get_productionactualno: ", get_productionactualno_list)
    
    # def get_pp_data_productionactualno_amount(process_list):
    #     pp_qty = 0
    #     filtered_by_productionactualno = get_productionactualno_list.filter(productionactualno=productionactualno)
    #
    #     for item in filtered_by_productionactualno:
    #         pp_qty += item.daywork
    #
    #     return pp_qty
    #
    # for x in pp_data:
    #     for y in get_productionactualno_list:
    #         finalrep[y] = get_pp_data_productionactualno_amount(y)
    '''

    pp_data_period_process, df_data_period_process = __pp_data_period_process(fromDate, toDate, processCode)
    # print("pp_process_summary::type(pp_data_period_process): ", type(pp_data_period_process))
    # print("pp_process_summary::pp_data_period_process: \n", pp_data_period_process)
    # print("pp_process_summary::type(df_data_period_process): ", type(df_data_period_process))
    # print("pp_process_summary::df_data_period_process: \n", df_data_period_process)

    ###################################################################################################################
    # 2021.01.21 Conclusion. [df_data_period_process]는 이미 판다스 데이터 프레임이므로,
    # 아래 [process] 값만을 리스트로 받기 위한 함수는 필요가 없고,
    # 1차로 [df명.필드명]과 같이 [Series]로 받아 와서, 리스트로 변환하면 된다. map 함수도 필요가 없다.
    # def get_process(df_data_period_process):
    #     print("pp_process_summary::get_process::type(df_data_period_process): ", type(df_data_period_process))
    #     print("pp_process_summary::get_process::df_data_period_process: \n", df_data_period_process)
    #     print("pp_process_summary::get_process::df_data_period_process.process: ", df_data_period_process.process)
    #     return get_process.process

    # tolist() 함수를 사용하여 바로 List 형식. ===> ***** 가장 간단 *****
    process_list = df_data_period_process.process.unique().tolist()  # 이것은 [process] 모든 로우 전체 값. [process] 컬럼만.
    # print("0-tolist pp_process_summary::type(process_list): ", type(process_list))  # <class 'pandas.core.series.Series'>
    # print("0-tolist pp_process_summary::process_list: \n", process_list)

    ################################################################################################################
    ''' DataFrame.데이터프레임 변환 사용법..

    # DataFrame.Series 형식.
    get_process_series = df_data_period_process.process  # 이것은 [process] 모든 로우 전체 값. [process] 컬럼만.
    # print("0-series pp_process_summary::type(get_process_series): ", type(get_process_series))  # <class 'pandas.core.series.Series'>
    # print("0-series pp_process_summary::get_process_series: \n", get_process_series)

    # Index 필드가 포함된 List 형식. [0 2093, 1 2090 ...]
    get_process_list = [df_data_period_process.process]  # 이것은 [process] 모든 로우 전체 값. [process] 컬럼만.
    # print("0-list pp_process_summary::type(get_process_list): ", type(get_process_list))  # <class 'List'>
    # print("0-list pp_process_summary::get_process_list: \n", get_process_list)

    # DataFrame을 다시 DataFrame 형식으로 가져오기.
    get_process_df = df_data_period_process[['process']]  # 이것은 [process] 모든 로우 전체 값. [process] 컬럼만.
    # print("0-df pp_process_summary::type(get_process_df): ", type(get_process_df))  # <class 'pandas.core.frame.DataFrame'>
    # print("0-df pp_process_summary::get_process_df: \n", get_process_df)

    # # DataFrame을 다시 DataFrame 형식으로 가져오는데, 특정 필드 [process]를 그룹화 한 후 가져온다. : 이건 에러 난다.
    # get_process = df_data_period_process[['process']].groupby['process']  # 이것은 [process] 모든 로우 전체 값. [process] 컬럼만.
    # print("0-그룹 pp_process_summary::type(get_process): ", type(get_process))
    # print("0-그룹 pp_process_summary::get_process: \n", get_process)

    # DataFrame을 다시 DataFrame 형식으로 가져오는데, 특정 필드 [process]를 그룹화 한 후 가져온다.
    get_process = df_data_period_process[['process']].groupby(df_data_period_process['process'])  # 이것은 [process] 모든 로우 전체 값. [process] 컬럼만.
    # print("1-그룹 pp_process_summary::type(get_process): ", type(get_process))  # <class 'pandas.core.frame.DataFrame'>
    # print("1-그룹 pp_process_summary::get_process: \n", get_process)
    # for data in get_process:  # 이런 식의 for 문장은, 전체 자료가 다 뿌려지게 된다.
    #     print("data: \n", data)

    '''
    ################################################################################################################

    # # average.평균과 sum.합계를 동시에 구할 수도 있다.
    # get_process_sum_goodness = (
    #     df_data_period_process.set_index('process').groupby(level=0)['process'].agg({'avg': np.average, 'sum': np.sum}))
    # sum.합계만 구한다.
    # get_process_sum_goodness = (df_data_period_process.set_index('process').groupby(df_data_period_process['goodness']).agg({sum('goodness')}))
    # print("1-그룹 합계 pp_process_summary::type(get_process_sum_goodness): ", type(get_process_sum_goodness))  # <class 'pandas.core.series.Series'>
    # print("1-그룹 합계 pp_process_summary::get_process_sum_goodness: \n", get_process_sum_goodness)

    # get_process_sum_df = df_data_period_process.reset_index().groupby('process').sum()  # 절대 안 됨... 에러...
    # get_process_sum_df = df_data_period_process.set_index("process").groupby('process').sum()  # 절대 안 됨... 에러...
    get_process_sum_df = df_data_period_process.groupby('process').sum()
    # print("1-그룹 합계 pp_process_summary::type(get_process_sum_df): ", type(get_process_sum_df))  # <class 'pandas.core.frame.DataFrame'>
    # print("1-그룹 합계 pp_process_summary::get_process_sum_df: \n", get_process_sum_df)

    # 2021.01.21 Conclusion. ***** 아래 for 문장에서 값을 가져올 때, [index] 컬럼이 없으면, iterrows()에서 에러 발생. *****
    get_process_sum_df = get_process_sum_df.reset_index(drop=False, inplace=False)  # 반드시 따로 [reset_index()] 실행.
    # print("2-리셋 후 pp_process_summary::type(get_process_sum_df): ", type(get_process_sum_df))  # <class 'pandas.core.frame.DataFrame'>
    # print("2-리셋 후 pp_process_summary::get_process_sum_df.head(): \n", get_process_sum_df.head())

    # for data in get_process_sum_df.iterrows():  # iteritems():  ***** 엄청 중요 ***** : [index] 변수가 빠지면, 에러 발생.
    # for index, data in get_process_sum_df.iterrows():  # iteritems():  ***** 데이터프레임 값 얻기 ******
        # print("data: \n", data)
        # print("data.process: ", data['process'])
        # print("data.goodness: ", data['goodness'])

    # 아래 2개 라인은 모두 잘 되는 것이다. 다만 모두 리스트 형식으로 받는다. :: 데이터프레임 ===> 리스트
    # context = [{'process': data['process'], 'goodness': data['goodness']} for index, data in get_process_sum_df.iterrows()]
    # pp_data_period_process_list = [{data['process']: data['goodness']} for index, data in get_process_sum_df.iterrows()]
    # print("pp_data_period_process_list: \n", pp_data_period_process_list)

    # 데이터프레임에서 2개 컬럼(process, goodness)만 다시 데이터프레임으로 추출.
    df_process_goodness = get_process_sum_df[['process', 'goodness']]
    # print("2개 컬럼만 df_process_goodness::type(df_process_goodness): ", type(df_process_goodness))  # <class 'pandas.core.frame.DataFrame'>
    # print("2개 컬럼만 df_process_goodness.head(): \n", df_process_goodness.head())

    # 데이터프레임을 ===> 딕셔너리로 변환... *****
    def df2dict(df):
        print("pp_process_summary df.shape[1]: ", df.shape[1])
        if df.shape[1] != 2:
            return print("pp_process_summary 컬럼이 정확히 2개만 있어야, Dictionary 형식으로 변경이 가능 합니다!")

        for k, v in zip(df.iloc[:, 0], df.iloc[:, 1]):
            # print("pp_process_summary df2dict k: ", k)
            # print("pp_process_summary df2dict v: ", v)
            finalrep[k] = v

        return finalrep

    finalrep = df2dict(df_process_goodness)


    # def get_period_process_goodness(process_list):
    #     pp_period_process_goodness = 0
    #     # filtered_by_process_selected = pp_data_period_process_list.filter(process=process_code)
    #
    #     for item in pp_data_period_process_list:  # filtered_by_process_selected:
    #         print("item: ", item)
    #         print("item.goodness: ", item.values())
    #         pp_period_process_goodness += item.values()
    #
    #     print("pp_period_process_goodness: ", pp_period_process_goodness)
    #
    #     return pp_period_process_goodness
    #
    # for x in get_process_sum_df:
    #     for y in pp_data_period_process_list:
    #         finalrep[y] = get_period_process_goodness(y)

    ###################################################################################################################

    print("pp_process_summary type(finalrep): ", type(finalrep))  # <class 'dict'>
    print("pp_process_summary::finalrep: \n", finalrep)
    print("\n\n")
    return JsonResponse({'pp_period_process_sum': finalrep}, safe=False)


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


# 2021.02.10 Added. 조건에 맞는 자료만을 만들어서 도로 보낸다.
def makingProduction(pp_data_period_process, df_data_period_process):
    rsDictSum = {}
    rsListSum = []

    df_data_prd_pro_wor = df_data_period_process.sort_values(['process', 'workdate', 'step9'], ascending=True)
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

    df_data_prd_pro_wor = df_data_prd_pro_wor.groupby(['workdate', 'step9'])['goodness'].sum().reset_index()
    # print("groupby() 후 makingProduction::type(df_data_prd_pro_wor): ", type(df_data_prd_pro_wor))
    # print("groupby () 후 makingProduction::df_data_prd_pro_wor.tail(20): \n", df_data_prd_pro_wor.tail(20))
    # print("groupby() 후 makingProduction::df_data_prd_pro_wor: \n", df_data_prd_pro_wor)

    # ********************************************************************************************************
    # ********************************************************************************************************
    # ********************************************************************************************************
    # ********************************************************************************************************
    # ********************************************************************************************************
    # 2021.01.30 Conclusion. ***** 엄청 중요 *****
    # 1. 그룹화한 자료는 반드시 set_index()를 실행하여, 새로운 DataFrame.데이터프레임을 만들어야 한다.
    # 2. 날짜로 그룹화]한 후에, 리스트를 만든다.
    ppData = df_data_prd_pro_wor.reset_index(drop=True, inplace=False)  # 반드시 따로 [reset_index()] 실행.
    # print("reset_index() 후 makingProduction::type(ppData): ", type(ppData))
    # print("reset_index() 후 makingProduction::ppData: \n", ppData)

    ppData = df_data_prd_pro_wor.values.tolist()  # 데이터프레임을 ===> 리스트로 변환...
    # ppData = [{data for data in ppData}]  # 아...깜빡 착각... DataFrame.데이터프레임은 이렇게 리스트화가 안 됨...
    ppDataOrigin = [data for data in pp_data_period_process]  # 이것은 완전한 원시 데이터임...
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
    # ppDataPeriodProcessWorkdate = df_data_prd_pro_wor[['workdate']].unique()  # 대괄호 2개는 에러 나네...
    # ppDataPeriodProcessWorkdate = df_data_prd_pro_wor[['workdate', 'step9']]  # 컬럼이 2개 이상일 때만, 정상 작동...
    # ppDataPeriodProcessWorkdate = df_data_prd_pro_wor['workdate'].unique()  # <class 'numpy.ndarray'>
    # ppDataPeriodProcessWorkdate = pd.DataFrame(df_data_prd_pro_wor['workdate'].unique())  # <class 'pandas.core.frame.DataFrame'>
    # ppDataPeriodProcessWorkdate = df_data_prd_pro_wor.drop_duplicates(['workdate'])  # <class 'pandas.core.frame.DataFrame'>
    ppDataPeriodProcessWorkdate = df_data_prd_pro_wor.drop_duplicates(['workdate'])[
        ['workdate']]  # <class 'pandas.core.frame.DataFrame'>
    # print("process_selected::len(ppDataPeriodProcessWorkdate): ", len(ppDataPeriodProcessWorkdate))
    # print("workdate 컬럼만 makingProduction::type(ppDataPeriodProcessWorkdate): ", type(ppDataPeriodProcessWorkdate))
    # print("workdate 컬럼만 makingProduction::ppDataPeriodProcessWorkdate: \n", ppDataPeriodProcessWorkdate)

    # 1. [workdate] 날짜 자료만 따로 리스트로 만들어 보내서, 그래프의 [Labels]로 활용하게 한다.
    ppDataPeriod = ppDataPeriodProcessWorkdate.values.tolist()
    # print("process_selected::len(ppDataPeriod): ", len(ppDataPeriod))
    # print("workdate 컬럼만 makingProduction::type(ppDataPeriod): ", type(ppDataPeriod))
    # print("workdate 컬럼만 makingProduction::ppDataPeriod: \n", ppDataPeriod)

    # 2. [step9]만 Series로 만든 다음, 그룹화해서 unique 제품명 값 1개만 남긴다.
    ppDataPeriodProcessStep9 = df_data_prd_pro_wor['step9'].unique()  # <class 'numpy.ndarray'>
    # ppDataPeriodProcessStep9 = pd.DataFrame(df_data_prd_pro_wor['step9'].unique())  # <class 'pandas.core.frame.DataFrame'>
    # ppDataPeriodProcessStep9 = pd.DataFrame(df_data_prd_pro_wor['step9'].unique()).values.tolist()  # <class 'List'>
    # print("makingProduction::len(ppDataPeriodProcessStep9): ", len(ppDataPeriodProcessStep9))
    # print("step9 컬럼만 makingProduction::type(ppDataPeriodProcessStep9): ", type(ppDataPeriodProcessStep9))
    # print("step9 컬럼만 makingProduction::ppDataPeriodProcessStep9: \n", ppDataPeriodProcessStep9)

    # 3. 제품명을 [컬럼명]으로 전환하기 위해, [공백 문자, 특수 문자] 제거...
    pattern = '[-=.#/?$:}{@% ]'  # 맨뒤에 [공백 문자]가 있으며, [^A-Za-z0-9] 첫문자가 이것일 경우에는 [부정문]이 된다.
    # products = [product for (re.sub(pattern, '', product)) in ppDataPeriodProcessStep9]
    products = []
    for product in ppDataPeriodProcessStep9:
        prd = re.sub(pattern, '', product)
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
    # print("makingProduction::len(ppDataPeriodProcess): ", len(ppDataPeriodProcess))
    # print("종합표 makingProduction::type(ppDataPeriodProcess): ", type(ppDataPeriodProcess))
    # print("종합표 makingProduction::ppDataPeriodProcess: \n", ppDataPeriodProcess)

    # 5. 날짜별 제품별 생산 수량을 해당 셀에 치환한다.
    for rows in df_data_prd_pro_wor.iterrows():
        # print("type(rows): ", type(rows))
        day = str(rows[1][0])[:10]
        product = rows[1][1]
        product = re.sub(pattern, '', product)
        goodness = rows[1][2]

        # 먼저 확인해야 하는 것이, [product.현재 제품명]으로 [products.컬렴명]이 있는지부터 확인해야 한다.
        if product not in products:
            print("makingProduction 현재 자료를 정리하지 못 했습니다. 관리자에게 문의하시오!", day, " ", product, " ", goodness)
            print("makingProduction 해당 자료가 전혀 없습니다!")
            return [], [], 0, [], []
            # context = {'process': process, 'ppData': [], 'total_pp_data_count': 0,
            #            'pp_data_period_process': pp_data_period_process, 'LANGUAGE_NO': LANGUAGE_NO}
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
            #            'pp_data_period_process': pp_data_period_process, 'LANGUAGE_NO': LANGUAGE_NO}
            # return render(request, 'ppp/process.html', context)

    # print("makingProduction::len(ppDataPeriodProcess): ", len(ppDataPeriodProcess))
    # print("종합표 df 정리 후 makingProduction::type(ppDataPeriodProcess): ", type(ppDataPeriodProcess))
    # print("종합표 df 정리 후 makingProduction::ppDataPeriodProcess: \n", ppDataPeriodProcess)

    # 6. 최종적으로 html 쪽으로 넘겨줄 수 있도록, 리스트로 변경해 준다.
    ppDataPeriodProcessList0 = ppDataPeriodProcess.fillna(0)  # NaN 값을 [0]으로 치환. 반드시 [새로운 DataFrame 명] 사용...
    ppDataPeriodProcessList = ppDataPeriodProcessList0.values.tolist()
    # print("process_selected::len(ppDataPeriodProcessList): ", len(ppDataPeriodProcessList))
    # print("종합표 리스트 정리 후 makingProduction::type(ppDataPeriodProcessList): ", type(ppDataPeriodProcessList))
    # print("종합표 리스트 정리 후 makingProduction::ppDataPeriodProcessList: \n", ppDataPeriodProcessList)

    # 데이터프레임을 ===> 튜플로 변환... *****
    rsTupleSum = [tuple(r) for r in df_data_prd_pro_wor.to_numpy()]

    ppDataCount = len(ppData)
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
    # df_data_prd_pro_wor['cumsum'] = df_data_prd_pro_wor.groupby(['step9'])['goodness'].apply(lambda x: x.cumsum())
    # print("1 resample() 후 makingProduction::type(df_data_prd_pro_wor): ", type(df_data_prd_pro_wor))
    # print("1 resample() 후 makingProduction::df_data_prd_pro_wor.head(): \n", df_data_prd_pro_wor.head())
    # print("1 resample() 후 makingProduction::df_data_prd_pro_wor: \n", df_data_prd_pro_wor)

    # 데이터프레임을 ===> 리스트 + 튜플 [{}] 로 변환... ***** : 결론 : 리스트로 변환하면, javascript 에서 for 문장을 못 쓰네...
    # context = [{'process': data['process'], 'goodness': data['goodness']} for index, data in df_data_prd_pro_wor.iterrows()]
    # rsList = [{'step9': data['step9'], 'goodness': data['goodness']} for index, data in df_data_prd_pro_wor.iterrows()]  # if data[0] == process_code]
    # print("0 리스트 변환 후 makingProduction::type(rsList): ", type(rsList))  # <class 'list'>
    # print("0 리스트 변환 후 makingProduction::rsList: \n", rsList)

    # 데이터프레임을 ===> 리스트로 변환...
    rsListSum = df_data_prd_pro_wor.values.tolist()
    print("0 리스트 변환 후 makingProduction::type(rsListSum): ", type(rsListSum))  # <class 'list'>
    print("0 리스트 변환 후 makingProduction::rsListSum: \n", rsListSum)

    rsDataFrameCount = len(df_data_prd_pro_wor)
    print("0 데이터프레임 로우 수 makingProduction::rsDataFrameCount: ", rsDataFrameCount)

    # 데이터프레임을 ===> 튜플로 변환... *****
    rsTupleSum = [tuple(r) for r in df_data_prd_pro_wor.to_numpy()]
    # print("0 튜플 변환 후 makingProduction::type(rsTupleSum): ", type(rsTupleSum))  #  <class 'list'>: 'tuple' 아님...
    # print("0 튜플 변환 후 makingProduction::rsTupleSum: \n", rsTupleSum)

    # =========================================================================================================
    # ********************************************************************************************************
    # ********************************************************************************************************
    '''

    '''
    # pp_data_period_process_selected = array_sets_server.filter(process=process_code)  # 에러...
    pp_data_period_process_selected = [data for data in array_sets_server if data[5] == process_code]  # 가장 파이썬스러운 필터링...
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
    # 여기 자료.df_data_prd_pro_wor [이미 선택한 공정에 대한 실적 자료만] 필터된 것이므로,
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
        # pp_data_period_process_selected_df = pd.DataFrame(df_data_prd_pro_wor, df_data_prd_pro_wor['workdate'] == current_day_this_month)  # 가장 파이썬스러운 필터링...
        # pp_data_period_process_selected_df = df_data_prd_pro_wor[['workdate', 'step9', 'goodness']]
        # is_current_date = df_data_prd_pro_wor['workdate'] == current_date  # 먼저 특정 조건에 맞는 시리즈만 추출...
        # df_current_date = df_data_prd_pro_wor[is_current_date]

        # df_current_date = df_data_prd_pro_wor.query("workdate >= '" + current_date + "' and workdate <= '" + current_date + "'")
        df_current_date = df_data_prd_pro_wor[
            df_data_prd_pro_wor["workdate"].isin(pd.date_range(current_date, current_date))]
        # print("makingProduction while 문장 내부 type(df_current_date): ", type(df_current_date))
        # print("makingProduction while 문장 내부 df_current_date: \n", df_current_date.head())
        # print("makingProduction while 문장 내부 current_date: ", current_date)  # 2021-01-01
        # print("makingProduction while 문장 내부 days: ", days)

        current_date += timedelta(days=1)

        df_current_date = df_data_prd_pro_wor.groupby(['step9']).sum()
        # 2021.01.21 Conclusion. ***** 아래 for 문장에서 값을 가져올 때, [index] 컬럼이 없으면, iterrows()에서 에러 발생. *****
        df_current_date = df_current_date.reset_index(drop=False, inplace=False)  # 반드시 따로 [reset_index()] 실행.
        # print("2-리셋 후 makingProduction::type(df_current_date): ", type(df_current_date))  # <class 'pandas.core.frame.DataFrame'>
        # print("2-1리셋 후 makingProduction::df_current_date: \n", df_current_date)
        df_current_date = df_current_date.reset_index(drop=True, inplace=False)  # 반드시 따로 [reset_index()] 실행.
        # print("2-리셋 후 makingProduction::type(df_current_date): ", type(df_current_date))  # <class 'pandas.core.frame.DataFrame'>
        # print("2-2리셋 후 makingProduction::df_current_date: \n", df_current_date)
        # df_current_date = df_current_date.reset_index(drop=True, inplace=True)  # 반드시 따로 [reset_index()] 실행.
        # print("2-리셋 후 makingProduction::type(df_current_date): ", type(df_current_date))  # <class 'pandas.core.frame.DataFrame'>
        # print("2-4리셋 후 makingProduction::df_current_date: \n", df_current_date)

        if df_current_date is None:
            print("makingProduction 해당 자료가 전혀 없습니다!")
            return [], [], 0, [], []

            # context = {'process': process, 'rsListSum': [], 'total_pp_data_count': 0,
            #            'pp_data_period_process': pp_data_period_process, 'LANGUAGE_NO': LANGUAGE_NO}
            # return render(request, 'ppp/process.html', context)

        # 데이터프레임에서 3개 컬럼(workdate, step9, goodness)만 다시 데이터프레임으로 추출.
        # df_current_date_goodness = df_current_date[['workdate', 'step9', 'goodness']]  # 'workdate' 컬럼은 에러나네... 위에서 reset_index() 하면, workdate 컬럼이 없어지네...
        # df_current_date_goodness = df_current_date[['step9', 'goodness', 'process']]  # 'process' 컬럼은 에러 안 나는데
        df_current_date_goodness = df_current_date[['step9', 'goodness']]
        # print("2개 컬럼만 makingProduction type(df_current_date_goodness): ", type(df_current_date_goodness))  # <class 'pandas.core.frame.DataFrame'>
        # print("2개 컬럼만 makingProduction df_current_date_goodness: \n", df_current_date_goodness)

        current_date_key = "day" + str(days)
        # print("process_selected current_date_key rsDict: ", current_date_key)

        rsDict = {}  # 반드시 여기서 초기화 해야 한다. 여기 [process_selected] 함수에서는, 날짜별로 finalrep 값을 갖는다.

        # 데이터프레임을 ===> 딕셔너리로 변환... *****
        def df2dict(df):
            # print("makingProduction df.shape[1]: ", df.shape[1])
            if df.shape[1] != 2:
                return print("컬럼이 정확히 2개만 있어야, Dictionary 형식으로 변경이 가능 합니다!")

            for k, v in zip(df.iloc[:, 0], df.iloc[:, 1]):
                # print("makingProduction df2dict k: ", k)
                # print("makingProduction df2dict v: ", v)
                rsDict[k] = v

            return rsDict

        rsDict = df2dict(df_current_date_goodness)
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
        rsDictSum[current_date_key] = rsDict  # 바로 추가...
        # print("더한 후 makingProduction type(rsDict): ", type(rsDictSum))  # <class 'dict'>
        # print("다한 후 makingProduction rsDictSum: \n", rsDictSum)

        rsList = []  # 반드시 여기서 초기화 해야 한다. 여기 [process_selected] 함수에서는, 날짜별로 rsListSum 값을 갖는다.

        # 데이터프레임에서 3개 컬럼(step9, goodness, workday)
        # df_current_date_goodness['workday'] = str(days)  # current_date_key: [day] 빼고 날짜만 넣자
        df_current_date_goodness.loc[:, 'workday'] = str(days)  # current_date_key: [day] 빼고 날짜만 넣자
        # if days == 2:
        #     print("3개 컬럼만 makingProduction df_current_date_goodness: \n", df_current_date_goodness)

        # 데이터프레임을 ===> 리스트로 변환... *****
        # rsList = [data for data in df_current_date_goodness]  # if data[0] == process_code]
        rsList = df_current_date_goodness.values.tolist()
        # print("makingProduction type(rsList): ", type(rsList))  # <class 'list'>
        # print("makingProduction rsList: \n", rsList)

        # rsList = df2list(df_current_date_goodness)
        # print("makingProduction type(rsList): ", type(rsList))  # <class 'list'>
        # print("makingProduction rsList: \n", rsList)

        # print("리스트로 변환 후 makingProduction type(rsListSum): ", type(rsListSum))  # <class 'list'>
        # print("리스트로 변환 후 makingProduction rsListSum: \n", rsListSum)
        rsListSum.append(rsList)  # 바로 추가...
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
    total_pp_data_count = len(rsListSum)  # len(df_data_prd_pro_wor)  # df_data_prd_pro_wor.count()
    # print("makingProduction total_pp_data_count: ", total_pp_data_count)

    # windll = ctypes.windll.kernel32
    # LANGUAGE_NO = windll.GetUserDefaultUILanguage()  # 1033, 1042
    # LANGUAGE_CODE = locale.windows_locale[windll.GetUserDefaultUILanguage()]  # en_US, ko_KR
    # print("makingProduction LANGUAGE_NO: ", LANGUAGE_NO, ", LANGUAGE_CODE: ", LANGUAGE_CODE)

    # print("makingProduction 리턴 바로 전 LANGUAGE_NO: ", LANGUAGE_NO, ", LANGUAGE_CODE: ", LANGUAGE_CODE)
    # print("makingProduction 리턴 바로 전 products: ", products)
    # print("makingProduction 리턴 바로 전 productsCount: ", productsCount)

    return ppDataPeriodProcessList, products, productsCount, ppDataPeriod



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

def production(request):
    global fromDate, toDate, processCode

    print("\nviews.py production:: 시작!!!!!!!!!!!!!!!!!!!!!!!! ")

    print("production request: ", request)
    print("production request.POST: ", request.POST)
    print("production len(request.POST): ", len(request.POST))
    print("production request.method: ", request.method)
    # print("request: ", request.REQUEST)  # 이건 에러...
    if len(request.POST) > 0:
        fromDate = request.POST['from_date']
        toDate = request.POST['to_date']
        processCode = request.POST['process_code']
        print("views.py production  fromDate: ", fromDate)
        print("views.py production  toDate: ", toDate)
        print("views.py production  processCode: ", processCode)
    else:
        # 2021.02.05 for Debugging... 잠깐만...
        fromDate = "2020.12.01"
        toDate = "2020.12.31"
        processCode = "all"  # "all"  # "2100"

        print("production  fromDate: ", fromDate)
        print("production  toDate: ", toDate)
        print("production  processCode: ", processCode)

    pyautogui.alert("현재 views.py production()...", "Info")

    pp_data_period_process, df_data_period_process = __pp_data_period_process(fromDate, toDate, processCode)

    process, df_process = __process(beInUse)  # Process.objects.all()
    total_process_count = len(process)
    # print("home total_process_count: \n", total_process_count)
    delivered = 2  # orders.filter(process='2110').count()
    pending = 3  # orders.filter(process='2080').count()

    # context = {'pp_data_period_process': pp_data_period_process, 'process': process,
    #            'total_process_count': total_process_count, 'total_pp_data_count': total_pp_data_count,
    #            'delivered': delivered, 'pending': pending}
    #
    # return render(request, 'ppp/index.html', context)


    stat_type = request.GET.get('stat_type')
    stat_gbn = request.GET.get('optionRadios')
    to_date = request.GET.get('to_date')
    from_date = request.GET.get('from_date')
    # print("production stat_type: ", stat_type)
    # print("production stat_gbn: ", stat_gbn)
    # print("production to_date: ", to_date)
    # print("production from_date: ", from_date)
    # print("production type(stat_type): ", type(stat_type))
    # print("production type(stat_gbn): ", type(stat_gbn))
    # print("production type(to_date): ", type(to_date))
    # print("production type(from_date): ", type(from_date))

    print("production fromDate: ", fromDate)
    print("production toDate: ", toDate)
    print("production processCode: ", processCode)
    # print("production pp_data_period_process: ", pp_data_period_process)
    print("production type(fromDate): ", type(fromDate))
    print("production type(toDate): ", type(toDate))
    print("production type(processCode): ", type(processCode))
    print("production type(pp_data_period_process): ", type(pp_data_period_process))

    ppData = pp_data_period_process
    # context = {'ppData': ppData, 'stat_type': stat_type, 'optionRadios': stat_gbn, 'to_date': to_date,
    #            'from_date': from_date}
    context = {'pp_data_period_process': pp_data_period_process, 'process': process,
               'total_process_count': total_process_count,
               'delivered': delivered, 'pending': pending,
               'fromDate': fromDate, 'toDate': toDate, 'processCode': processCode}
    # return render(request, 'ppp/statistics_logs.html', context)
    return render(request, 'ppp/index.html', context)



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
