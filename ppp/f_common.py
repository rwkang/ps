import qrcode
import sys
import os
import platform
from tkinter import *  # import re 를 대신한다.
from configparser import ConfigParser
# from PyQt5.QtCore import (pyqtSlot, pyqtSignal, QObject, QEventLoop, Qt, QDate, QTime, QPoint)
import pymysql
import pymssql
# import pyodbc
import datetime
import time

remoteDbConnection = 0
localDbConnection = 0

# print("\nf_common 1 started.")

# 2020.12.09 Added. 품목 마스터 정보 등 기본 정보를 파이컴으로 업데이트 할지 여부 판단 루틴...
# msSqlServerDb, cursArrayServer = self.connectRemoteDB()
# cursArrayServer.execute(sql, values)  # 2019.08.25 Conclusion. 여기 리턴 값 [results]는 전혀 의미 없음.

# 2020.04.19 Added. 천신만고 끝에 찾아낸, [QThread] 클래스를 상속받는 GatheringReadPlc() 클래스에,
#   [인자.Parameter]를 전달하는 방식을 찾았다. 여기서 새로운 클래스 SendMsg()를 만들고,
#   SendMsg() 클래스 내부에 전달하고자 하는 [변수 값]들을 세팅하고,
#   GatheringReadPlc() 클래스를 생성할 때, 다중 클래스 상속으로 처리하면 된다.
#   GatheringReadPlc(QThread) ===> GatheringReadPlc(QThread, SendMsg) : 요래 처리하면 된다.
# updateGoodsMaster = 1
# updateEquipmentOfProduct = 2
# updateGroups = 3


class SendMsg():
    param1 = "1"
    param2 = 1
    # updateGoodsMaster = updateGoodsMaster
    # updateEquipmentOfProduct = updateEquipmentOfProduct
    # updateGroups = updateGroups


# @pyqtSlot()
def test():
    aaa = 2
    # print("f_common test() aaa : ", aaa)
    return 1

# print("\n2 f_common started.")


# @pyqtSlot()
def connectRemoteWmsDB():
    # print("\nf_common.connectRemoteAmsDB...")
    try:
        # 2019.01.16 Added. config.ini 값을 함수로 얻어오기.
        HOST0, USER0, PASS0, DBNAME0 = getRemoteDbParameter()
        # print("\nf_common.connectRemoteAmsDB HOST0 : ", HOST0)
        # print("f_common.connectRemoteAmsDB USER0 : ", USER0)
        # print("f_common.connectRemoteAmsDB PASS0 : ", PASS0)
        # print("f_common.connectRemoteAmsDB DBNAME0 : ", DBNAME0, "\n")

        DBNAME0 = 'PWMS'

        # MSSQL 접속
        msSqlServerWmsDb = pymssql.connect(server=HOST0, user=USER0, password=PASS0, database=DBNAME0)
        # msSqlServerWmsDb = pymssql.connect(server="192.168.1.107", user="sa", password="*963210z", database="PowErpKftcbj")
        # print('1 f_common.connectRemoteAmsDB.msSqlServerDb : ', msSqlServerWmsDb)
        cursArrayServerWms = msSqlServerWmsDb.cursor()
        # cursArrayServerWms = msSqlServerDb.cursor(pymssql.cursors.DictCursor)
        # print('2 f_common.connectRemoteAmsDB.cursArrayServerAms : ', cursArrayServerWms)
        # print('f_common.connectRemoteDB.cursDict : ' + str(cursDict))

        # remote_db_connection = 1  # 사실 이 변수는 [시스템 전체 글로벌 변수]로 가야 되는데...

        if msSqlServerWmsDb is None:
            # print("\nf_common.connectRemoteAmsDB mySqlLocalDb is None")
            # time.sleep(0.1)
            # __init__()
            return -1
        else:
            # msSqlServerDb.ping(True)
            # print("msSqlServerDb.ping(True)")
            print("\nf_common.connectRemoteAmsDB 원격 컴퓨터 PWMS 접속 성공 !!!")

            # QMessageBox.about(self, 'Connection', 'Successfully Connected to DB')
            # cursArrayServerWms.close()
            # msSqlServerWmsDb.close()

            return msSqlServerWmsDb, cursArrayServerWms, HOST0, USER0, PASS0, DBNAME0

    except:
        print("f_common connectRemoteAmsDB 원격 컴퓨터 PWMS 접속 실패")
        # time.sleep(0.1)
        # QMessageBox.about(self, '데이터베이스 연결', '데이터베이스 연결 실패!!! 시스템을 종료합니다!!!!!')

        return -1, -1, "N", "N", "N", "N"


# @pyqtSlot()
def connectRemoteAmsDB():
    # print("\nf_common.connectRemoteAmsDB...")
    try:
        # 2019.01.16 Added. config.ini 값을 함수로 얻어오기.
        HOST0, USER0, PASS0, DBNAME0 = getRemoteDbParameter()
        # print("\nf_common.connectRemoteAmsDB HOST0 : ", HOST0)
        # print("f_common.connectRemoteAmsDB USER0 : ", USER0)
        # print("f_common.connectRemoteAmsDB PASS0 : ", PASS0)
        # print("f_common.connectRemoteAmsDB DBNAME0 : ", DBNAME0, "\n")

        DBNAME0 = 'PERP1'

        # MSSQL 접속
        msSqlServerAmsDb = pymssql.connect(server=HOST0, user=USER0, password=PASS0, database=DBNAME0)
        # msSqlServerAmsDb = pymssql.connect(server="192.168.1.107", user="sa", password="*963210z", database="PowErpKftcbj")
        # print('1 f_common.connectRemoteAmsDB.msSqlServerDb : ', msSqlServerAmsDb)
        cursArrayServerAms = msSqlServerAmsDb.cursor()
        # cursArrayServerAms = msSqlServerDb.cursor(pymssql.cursors.DictCursor)
        # print('2 f_common.connectRemoteAmsDB.cursArrayServerAms : ', cursArrayServerAms)
        # print('f_common.connectRemoteDB.cursDict : ' + str(cursDict))

        # remote_db_connection = 1  # 사실 이 변수는 [시스템 전체 글로벌 변수]로 가야 되는데...

        if msSqlServerAmsDb is None:
            # print("\nf_common.connectRemoteAmsDB mySqlLocalDb is None")
            # time.sleep(0.1)
            # __init__()
            return -1
        else:
            # msSqlServerDb.ping(True)
            # print("msSqlServerDb.ping(True)")
            print("\nf_common.connectRemoteAmsDB 원격 컴퓨터 PERP1 접속 성공 !!!")

            # QMessageBox.about(self, 'Connection', 'Successfully Connected to DB')
            # cursArrayServerAms.close()
            # msSqlServerAmsDb.close()

            return msSqlServerAmsDb, cursArrayServerAms, HOST0, USER0, PASS0, DBNAME0

    except:
        print("f_common connectRemoteAmsDB 원격 컴퓨터 PERP1 접속 실패")
        # time.sleep(0.1)
        # QMessageBox.about(self, '데이터베이스 연결', '데이터베이스 연결 실패!!! 시스템을 종료합니다!!!!!')

        return -1, -1, "N", "N", "N", "N"


# @pyqtSlot()
def connectRemoteDB():
    # global remoteDbConnection
    print("\nf_common.connectRemoteDB() 내부로 들어 왔네요...")
    try:
        # 2019.01.16 Added. config.ini 값을 함수로 얻어오기.
        HOST0, USER0, PASS0, DBNAME0 = getRemoteDbParameter()
        print("\nf_common.connectRemoteDB HOST0 : ", HOST0)
        # print("f_common.connectRemoteDB USER0 : ", USER0)
        # print("f_common.connectRemoteDB PASS0 : ", PASS0)
        # print("f_common.connectRemoteDB DBNAME0 : ", DBNAME0, "\n")

        # MSSQL 접속
        print("==========================================================================================")
        print("f_common.connectRemoteDB 접속을 시도합니다. 시간이 오래 걸릴수도 있습니다 잠시만 기다려 주세요...")
        print("==========================================================================================")
        msSqlServerDb = pymssql.connect(server=HOST0, user=USER0, password=PASS0, database=DBNAME0)
        # msSqlServerDb = pymssql.connect(server="192.168.1.107", user="sa", password="*963210z", database="PowErpKftcbj")
        print('1 f_common.connectRemoteDB.msSqlServerDb : ', msSqlServerDb)
        # cursArrayServer = msSqlServerDb.cursor(as_dict=True)
        cursArrayServer = msSqlServerDb.cursor()
        # cursDictServer = msSqlServerDb.cursor(pymssql.cursors.DictCursor)
        print('2 f_common.connectRemoteDB.cursArrayServer : ', cursArrayServer)

        # remoteDbConnection = 1  # 사실 이 변수는 [시스템 전체 글로벌 변수]로 가야 되는데...

        if msSqlServerDb is None:
            print("\nf_common.connectRemoteDB mySqlLocalDb is None")
            # time.sleep(0.1)
            # __init__()
            return -1
        else:
            # msSqlServerDb.ping(True)
            # print("msSqlServerDb.ping(True)")
            print("\nf_common.connectRemoteDB 원격 컴퓨터 ERP 접속 성공 !!!")

            # QMessageBox.about(self, 'Connection', 'Successfully Connected to DB')
            # cursArrayServer.close()
            # msSqlServerDb.close()

            return msSqlServerDb, cursArrayServer, HOST0, USER0, PASS0, DBNAME0

    except:
        print("f_common connectRemoteDB 원격 컴퓨터 ERP 접속 실패")
        # time.sleep(0.1)
        # QMessageBox.about(self, '데이터베이스 연결', '데이터베이스 연결 실패!!! 시스템을 종료합니다!!!!!')

        return -1, -1, "N", "N", "N", "N"


# @pyqtSlot()
def connectDB():
    # # 2017.01.17 Conclusion. global 변수는 반드시 "최초 지정"하는 함수에 정의되야 한다.
    # global COMPANY_CODE, HOST1, USER1, PASS1, DBNAME1
    # global BOUNCE_TIME, SLEEP_TIME, TIME_GAP, NIGHT_CLOSING_HHMMSS, DAY_CLOSING_HHMMSS
    # global FORPRODUCINGORDERDATA, PROCESS, GROUPS, DESCRIPTION_TEXT, LINE_CODE
    # global WORK_DATE, DAY_NIGHT, GOODS, CODE, CAVITY, TO_WAREHOUSE
    # global FACODE, PRODUCTSELECTION, PLCBIT, FRONTJISNO, TRADE
    # global mySqlLocalDb, cursArray, cursDict

    # print("\nf_common.connectDB...")
    try:
        # 2019.01.16 Added. config.ini 값을 함수로 얻어오기.
        COMPANY_CODE, HOST1, USER1, PASS1, DBNAME1, BOUNCE_TIME, SLEEP_TIME, \
        TIME_GAP, NIGHT_CLOSING_HHMMSS, DAY_CLOSING_HHMMSS = getLocalDbParameter()
        # print("\nf_common.connectDB COMPANY_CODE : " + COMPANY_CODE + "\n")

        FORPRODUCINGORDERDATA, PROCESS, GROUPS, DESCRIPTION_TEXT, LINE_CODE, \
        WORK_DATE, DAY_NIGHT, GOODS, CODE, CAVITY, GOODSRIGHT, CODERIGHT, CAVITYRIGHT, TO_WAREHOUSE, FACODE, \
        PRODUCTSELECTION, PLCBIT, FRONTJISNO, TRADE, UI, BAUDRATE = getFacParameter()
        # # print("\n__connectDB LINE_CODE : " + str(LINE_CODE) + "\n")
        # # print("\n__connectDB GROUPS : " + str(GROUPS) + "\n")
        # # print("\n__connectDB PROCESS : " + str(PROCESS) + "\n")
        # # print("\n__connectDB FACODE : " + str(FACODE) + "\n")
        # print("\n__connectDB TRADE : " + str(TRADE) + "\n")
        # print("\n__connectDB BAUDRATE : " + str(BAUDRATE) + "\n")

        # 2019.07.12 Conclusion. 그러니까 여기서 설혹 모든 변수 값이 "None"로 받어질 수가 없다.
        # 왜냐하면, Pi 컴 세팅 프로그램인 "setpi.py" 프로그램으로 이미 변수 값을 정확하게 저장하였기 때문이다.

        # MySQL 접속

        # mySqlLocalDb = pymysql.connect(host=HOST1, port=3306, user=USER1,
        #                                password=PASS1, db=DBNAME1, charset='utf8')

        # cursor = pymysql.cursors.DictCursor
        # mySqlLocalDb = pymysql.connect(host=HOST1, port=3306, user=USER1,
        #                                password=PASS1, db=DBNAME1, cursorclass=cursor, charset='utf8')

        # print('__connectDB... HOST1 : ' + str(HOST1))
        # print('__connectDB... USER1 : ' + str(USER1))
        # print('__connectDB... PASS1 : ' + str(PASS1))
        # print('__connectDB... DBNAME1 : ' + str(DBNAME1))
        mySqlLocalDb = pymysql.connect(host=HOST1, port=3306, user=USER1,
                                       password=PASS1, db=DBNAME1, charset='utf8')

        cursArray = mySqlLocalDb.cursor()
        cursDict = mySqlLocalDb.cursor(pymysql.cursors.DictCursor)
        # print('f_common.cursArray : ' + str(cursArray))
        # print('f_common.cursDict : ' + str(cursDict))

        # if self.cursor() is None:
        #     print("self.cursor() is None\n")
        #     time.sleep(0.1)
        #     return -1, -1

        # if self.conn is None:
        #     self.__init__()
        # else:
        #     self.conn.ping(True)

        if mySqlLocalDb is None:
            # print("\nf_common.connectDB mySqlLocalDb is None")
            # time.sleep(0.1)
            # __init__()
            return -1
        else:
            mySqlLocalDb.ping(True)
            # print("mySqlLocalDb.ping(True)")
            # print("\nf_common.connectDB 내 컴퓨터 접속 성공 !!!")

            # QMessageBox.about(self, 'Connection', 'Successfully Connected to DB')

            # print("f_common UI : " + str(UI))
            # print("f_common LINE_CODE : ", LINE_CODE)
            # print("f_common BAUDRATE : ", BAUDRATE)
            # cursArray.close()
            # cursDict.close()
            # mySqlLocalDb.close()

            return mySqlLocalDb, cursArray, cursDict, \
                   COMPANY_CODE, HOST1, USER1, PASS1, DBNAME1, \
                   BOUNCE_TIME, SLEEP_TIME, TIME_GAP, NIGHT_CLOSING_HHMMSS, DAY_CLOSING_HHMMSS, \
                   FORPRODUCINGORDERDATA, PROCESS, GROUPS, DESCRIPTION_TEXT, LINE_CODE, \
                   WORK_DATE, DAY_NIGHT, GOODS, CODE, CAVITY, GOODSRIGHT, CODERIGHT, CAVITYRIGHT, TO_WAREHOUSE, \
                   FACODE, PRODUCTSELECTION, PLCBIT, FRONTJISNO, TRADE, UI, BAUDRATE

    except:
        print("내 컴퓨터 접속 실패")
        # time.sleep(0.1)
        # QMessageBox.about(self, '데이터베이스 연결', '데이터베이스 연결 실패!!! 시스템을 종료합니다!!!!!')

        return -1, -1, -1, \
               "N", "N", "N", "N", "N", \
               "N", "N", "N", "N", "N", \
               "N", "N", "N", "N", "N", \
               "N", "N", "N", "N", "N", "N", "N", "N", "N", \
               "N", "N", "N", "N", "N", "N", "N"

        # sys.exit()
        # sys.exit(app.exec())

        # if not open():
        #     return False
        # return True


# @pyqtSlot()
def connectWebDB():
    # print("\nf_common.connectWebDB...")
    try:
        # 2019.01.16 Added. config.ini 값을 함수로 얻어오기.
        # HOST3, USER3, PASS3, DBNAME3 = getWebDbParameter()  # connectRemoteDB() 하고는 Return 값이 다른다.
        COMPANY_CODE, HOST3, USER3, PASS3, DBNAME3, \
        BOUNCE_TIME, SLEEP_TIME, TIME_GAP, NIGHT_CLOSING_HHMMSS, DAY_CLOSING_HHMMSS = getWebDbParameter()
        print("\nf_common.connectWebDB HOST3 : ", HOST3)
        # print("f_common.connectWebDB USER3 : ", USER3)
        # print("f_common.connectWebDB PASS3 : ", PASS3)
        # print("f_common.connectWebDB DBNAME3 : ", DBNAME3, "\n")

        # MSSQL 접속
        print("==========================================================================================")
        print("f_common.connectWebDB 웹 접속을 시도합니다. 시간이 오래 걸릴수도 있습니다 잠시만 기다려 주세요...")
        print("==========================================================================================")
        msSqlServerDb = pymssql.connect(server=HOST3, user=USER3, password=PASS3, database=DBNAME3)
        # msSqlServerDb = pymssql.connect(server="192.168.1.107", user="sa", password="*963210z", database="PowErpKftcbj")
        print('1 f_common.msSqlServerDb.msSqlServerDb : ', msSqlServerDb)
        # cursArrayServer = msSqlServerDb.cursor(as_dict=True)
        cursArrayServer = msSqlServerDb.cursor()
        # cursDictServer = msSqlServerDb.cursor(pymssql.cursors.DictCursor)
        print('2 f_common.connectWebDB.cursArrayServer : ', cursArrayServer)

        # remoteDbConnection = 1  # 사실 이 변수는 [시스템 전체 글로벌 변수]로 가야 되는데...

        if msSqlServerDb is None:
            print("\nf_common.connectWebDB mySqlLocalDb is None")
            # time.sleep(0.1)
            # __init__()
            return -1
        else:
            # msSqlServerDb.ping(True)
            # print("msSqlServerDb.ping(True)")
            print("\nf_common.connectWebDB 웹 컴퓨터 ERP 접속 성공 !!!")

            # QMessageBox.about(self, 'Connection', 'Successfully Connected to DB')
            # cursArrayServer.close()
            # msSqlServerDb.close()

            return msSqlServerDb, cursArrayServer, HOST3, USER3, PASS3, DBNAME3

    except:
        print("f_common connectWebDB 웹 컴퓨터 ERP 접속 실패")
        # time.sleep(0.1)
        # QMessageBox.about(self, '데이터베이스 연결', '데이터베이스 연결 실패!!! 시스템을 종료합니다!!!!!')

        return -1, -1, "N", "N", "N", "N"

    ''' 2021.03.01 Conclusion. WEB DB 웹 Database 또한 [MS SQL]로 최종 결정되었다. 
    try:
        # 2019.01.16 Added. config.ini 값을 함수로 얻어오기.
        COMPANY_CODE, HOST3, USER3, PASS3, DBNAME3, BOUNCE_TIME, SLEEP_TIME, \
        TIME_GAP, NIGHT_CLOSING_HHMMSS, DAY_CLOSING_HHMMSS = getWebDbParameter()
        # print("\nf_common.connectWebDB COMPANY_CODE : " + COMPANY_CODE + "\n")

        FORPRODUCINGORDERDATA, PROCESS, GROUPS, DESCRIPTION_TEXT, LINE_CODE, \
        WORK_DATE, DAY_NIGHT, GOODS, CODE, CAVITY, GOODSRIGHT, CODERIGHT, CAVITYRIGHT, TO_WAREHOUSE, FACODE, \
        PRODUCTSELECTION, PLCBIT, FRONTJISNO, TRADE, UI, BAUDRATE = getFacParameter()
        # # print("\connectWebDB LINE_CODE : " + str(LINE_CODE) + "\n")
        # # print("\connectWebDB GROUPS : " + str(GROUPS) + "\n")
        # # print("\connectWebDB PROCESS : " + str(PROCESS) + "\n")
        # # print("\connectWebDB FACODE : " + str(FACODE) + "\n")
        # print("\connectWebDB TRADE : " + str(TRADE) + "\n")
        # print("\connectWebDB BAUDRATE : " + str(BAUDRATE) + "\n")

        # 2019.07.12 Conclusion. 그러니까 여기서 설혹 모든 변수 값이 "None"로 받어질 수가 없다.
        # 왜냐하면, Pi 컴 세팅 프로그램인 "setpi.py" 프로그램으로 이미 변수 값을 정확하게 저장하였기 때문이다.

        # MySQL 접속

        # print('connectWebDB... HOST3 : ' + str(HOST3))
        # print('connectWebDB... USER3 : ' + str(USER3))
        # print('connectWebDB... DBNAME3 : ' + str(DBNAME3))

        # mySqlLocalDb = pymysql.connect(host=HOST3, port=3306, user=USER3, password=PASS3, db=DBNAME3, charset='utf8')

        # cursor = pymysql.cursors.DictCursor
        # mySqlLocalDb = pymysql.connect(host=HOST3, port=3306, user=USER3, password=PASS3, db=DBNAME3,
        #                                cursorclass=cursor, charset='utf8')

        mySqlLocalDb = pymysql.connect(host=HOST3, port=3306, user=USER3, password=PASS3, db=DBNAME3, charset='utf8')
        # print('f_common_connectWebDB.type(mySqlLocalDb) : ', type(mySqlLocalDb))

        cursArray = mySqlLocalDb.cursor()
        cursDict = mySqlLocalDb.cursor(pymysql.cursors.DictCursor)
        # print('f_common_connectWebDB.cursArray : ' + str(cursArray))
        # print('f_common_connectWebDB.cursDict : ' + str(cursDict))

        # if self.cursor() is None:
        #     print("self.cursor() is None\n")
        #     time.sleep(0.1)
        #     return -1, -1

        # if self.conn is None:
        #     self.__init__()
        # else:
        #     self.conn.ping(True)

        if mySqlLocalDb is None:
            print("\nf_common_connectWebDB mySqlLocalDb is None")
            # time.sleep(0.1)
            # __init__()
            return -1
        else:
            mySqlLocalDb.ping(True)
            # print("f_common_connectWebDB mySqlLocalDb.ping(True)")
            print("\nf_common_connectWebDB 웹 컴퓨터 접속 성공 !!!")

            # QMessageBox.about(self, 'Connection', 'Successfully Connected to DB')

            # print("f_common UI : " + str(UI))
            # print("f_common LINE_CODE : ", LINE_CODE)
            # print("f_common BAUDRATE : ", BAUDRATE)

            return mySqlLocalDb, cursArray, cursDict, \
                   COMPANY_CODE, HOST3, USER3, PASS3, DBNAME3, \
                   BOUNCE_TIME, SLEEP_TIME, TIME_GAP, NIGHT_CLOSING_HHMMSS, DAY_CLOSING_HHMMSS, \
                   FORPRODUCINGORDERDATA, PROCESS, GROUPS, DESCRIPTION_TEXT, LINE_CODE, \
                   WORK_DATE, DAY_NIGHT, GOODS, CODE, CAVITY, GOODSRIGHT, CODERIGHT, CAVITYRIGHT, TO_WAREHOUSE, \
                   FACODE, PRODUCTSELECTION, PLCBIT, FRONTJISNO, TRADE, UI, BAUDRATE

    except:
        print("f_common_connectWebDB 웹 컴퓨터 접속 실패")
        # time.sleep(0.1)
        # QMessageBox.about(self, '데이터베이스 연결', '데이터베이스 연결 실패!!! 시스템을 종료합니다!!!!!')

        return -1, -1, -1, \
               "N", "N", "N", "N", "N", \
               "N", "N", "N", "N", "N", \
               "N", "N", "N", "N", "N", \
               "N", "N", "N", "N", "N", "N", "N", "N", "N", \
               "N", "N", "N", "N", "N", "N", "N"

        # sys.exit()
        # sys.exit(app.exec())

        # if not open():
        #     return False
        #     return True
    
    '''


# @pyqtSlot()
def getRemoteDbParameter():
    # 2018.08.09 config.ini 파일로 설정해서, 프로그램이 루프 돌고 있을 때,
    # config.ini 파일 값을 변경한 것이, 프로그램에 바로 적용될 수 있도록 한다.

    # print('getLocalDbParameter 함수에서 config 값을 읽습니다.')
    config = __open_config_file()
    # print('getLocalDbParameter config : ' + str(config))

    config.options('SERVER')  # 옵션 이름 리스트 얻기 # ['host0','user0','pass0','dbname0']
    if 'SERVER' in config:
        HOST0 = config.get('SERVER', 'host0')
        USER0 = config.get('SERVER', 'user0')
        PASS0 = config.get('SERVER', 'pass0')
        DBNAME0 = config.get('SERVER', 'dbname0')

    # print('f_common.getRemoteDbParameter HOST0 : ' + str(HOST0))
    # print('f_common.getRemoteDbParameter USER0 : ' + str(USER0))
    # print('f_common.getRemoteDbParameter PASS0 : ' + str(PASS0))
    # print('f_common.getRemoteDbParameter DBNAME0 : ' + str(DBNAME0))

    remote_db_connection = 1

    # IN_OK_PIN_DEFAULT = config.get('LOCAL', 'in_ok_pin_default')
    # IN_NG_PIN_DEFAULT = config.get('LOCAL', 'in_ng_pin_default')

    return HOST0, USER0, PASS0, DBNAME0


# @pyqtSlot()
def getLocalDbParameter():
    # # 2017.01.17 Conclusion. global 변수는 반드시 "최초 지정"하는 함수에 정의되야 한다.
    # global COMPANY_CODE, HOST1, USER1, PASS1, DBNAME1
    # global BOUNCE_TIME, SLEEP_TIME, TIME_GAP, NIGHT_CLOSING_HHMMSS, DAY_CLOSING_HHMMSS

    # print('__getLocalDbParameter 함수 내부')

    # QMessageBox.about(self, '__getLocalDbParameter', '__getLocalDbParameter')

    # print('getLocalDbParameter config : 함수 __open_config_file()로 들어 갑니다.')
    config = __open_config_file()
    # print('getLocalDbParameter config : ' + str(config))

    # config = ConfigParser()
    # # print('1 __getLocalDbParameter 함수 내부')
    #
    # # pyinstaller를 사용하지 않는다면, elif 부분만 필요함
    # if getattr(sys, 'frozen', False):
    #     # pyinstaller로 패키징한 실행파일의 경우
    #     cur_path = os.path.dirname(sys.executable)
    #     # print('if cur_path : ' + str(cur_path))
    # elif __file__:
    #     # *.py 형태의 파일로 실행할 경우 로직
    #     cur_path = os.path.dirname(os.path.abspath(__file__))
    #     # print('elif cur_path : ' + str(cur_path))
    #
    # currentDir = os.path.dirname(os.path.realpath(__file__))
    # # print("__getLocalDbParameter currentDir : " + currentDir)
    # # config.read(filenames='/home/pi/dev/gathering/config.ini', encoding='utf-8')  # INI 파일 읽기
    # config.read(filenames=currentDir + '/config.ini', encoding='utf-8')
    #
    # # ['config.ini']
    # config.sections()  # 섹션 리스트 읽기
    # # ['LOCAL']
    config.options('LOCAL')  # 옵션 이름 리스트 얻기 # ['host0','user0','pass0','dbname0']
    # print('getLocalDbParameter config : ' + str(config))
    if 'LOCAL' in config:
        COMPANY_CODE = config.get('LOCAL', 'COMPANY_CODE')  # COMPANY_CODE = "PSB001" # "KFTCBJ"
        HOST1 = config.get('LOCAL', 'host1')
        USER1 = config.get('LOCAL', 'user1')
        PASS1 = config.get('LOCAL', 'pass1')
        DBNAME1 = config.get('LOCAL', 'dbname1')
        BOUNCE_TIME = int(config.get('LOCAL', 'bounce_time'))
        SLEEP_TIME = int(config.get('LOCAL', 'sleep_time'))
        SLEEP_TIME = float(SLEEP_TIME / 1000)
        TIME_GAP = int(config.get('LOCAL', 'time_gap'))
        TIME_GAP = float(TIME_GAP / 1000)
        NIGHT_CLOSING_HHMMSS = config.get('LOCAL', 'night_closing_hhmmss')
        DAY_CLOSING_HHMMSS = config.get('LOCAL', 'day_closing_hhmmss')

        # print("호출 후 COMPANY_CODE : " + COMPANY_CODE)
        # print("호출 후 HOST1 : " + HOST1)
        # print("호출 후 USER1 : " + USER1)
        # print("호출 후 PASS1 : " + PASS1)
        # print("호출 후 DBNAME1 : " + DBNAME1)
        # print("호출 후 BOUNCE_TIME : " + str(BOUNCE_TIME))
        # print("호출 후 SLEEP_TIME : " + str(SLEEP_TIME))
        # print("호출 후 TIME_GAP : " + str(TIME_GAP))
        # print("호출 후 NIGHT_CLOSING_HHMMSS : " + str(NIGHT_CLOSING_HHMMSS))
        # print("호출 후 DAY_CLOSING_HHMMSS : " + str(DAY_CLOSING_HHMMSS))

        # IN_OK_PIN_DEFAULT = config.get('LOCAL', 'in_ok_pin_default')
        # IN_NG_PIN_DEFAULT = config.get('LOCAL', 'in_ng_pin_default')

        return COMPANY_CODE, HOST1, USER1, PASS1, DBNAME1, BOUNCE_TIME, SLEEP_TIME, \
               TIME_GAP, NIGHT_CLOSING_HHMMSS, DAY_CLOSING_HHMMSS


# @pyqtSlot()
def getWebDbParameter():
    # # 2017.01.17 Conclusion. global 변수는 반드시 "최초 지정"하는 함수에 정의되야 한다.
    # global COMPANY_CODE, HOST1, USER1, PASS1, DBNAME1
    # global BOUNCE_TIME, SLEEP_TIME, TIME_GAP, NIGHT_CLOSING_HHMMSS, DAY_CLOSING_HHMMSS

    # print('getLocalDbParameter config : 함수 __open_config_file()로 들어 갑니다.')
    config = __open_config_file()
    # print('getLocalDbParameter config : ' + str(config))
    # # ['config.ini']
    # config.sections()  # 섹션 리스트 읽기
    # # ['LOCAL']
    config.options('WEB')  # 옵션 이름 리스트 얻기 # ['host0','user0','pass0','dbname0']
    # print('getLocalDbParameter config : ' + str(config))
    if 'WEB' in config:
        COMPANY_CODE = config.get('WEB', 'COMPANY_CODE')  # COMPANY_CODE = "PSB001" # "KFTCBJ"
        HOST3 = config.get('WEB', 'host3')
        USER3 = config.get('WEB', 'user3')
        PASS3 = config.get('WEB', 'pass3')
        DBNAME3 = config.get('WEB', 'dbname3')
        BOUNCE_TIME = int(config.get('WEB', 'bounce_time'))
        SLEEP_TIME = int(config.get('WEB', 'sleep_time'))
        SLEEP_TIME = float(SLEEP_TIME / 1000)
        TIME_GAP = int(config.get('WEB', 'time_gap'))
        TIME_GAP = float(TIME_GAP / 1000)
        NIGHT_CLOSING_HHMMSS = config.get('WEB', 'night_closing_hhmmss')
        DAY_CLOSING_HHMMSS = config.get('WEB', 'day_closing_hhmmss')

        # print("f_common_getWebDbParameter 호출 후 COMPANY_CODE : " + COMPANY_CODE)
        print("f_common_getWebDbParameter 호출 후 HOST3 : " + HOST3)
        print("f_common_getWebDbParameter 호출 후 USER3 : " + USER3)
        print("f_common_getWebDbParameter 호출 후 DBNAME3 : " + DBNAME3)
        # print("f_common_getWebDbParameter 호출 후 BOUNCE_TIME : " + str(BOUNCE_TIME))
        # print("f_common_getWebDbParameter 호출 후 SLEEP_TIME : " + str(SLEEP_TIME))
        # print("f_common_getWebDbParameter 호출 후 TIME_GAP : " + str(TIME_GAP))
        # print("f_common_getWebDbParameter 호출 후 NIGHT_CLOSING_HHMMSS : " + str(NIGHT_CLOSING_HHMMSS))
        # print("f_common_getWebDbParameter 호출 후 DAY_CLOSING_HHMMSS : " + str(DAY_CLOSING_HHMMSS))

        # IN_OK_PIN_DEFAULT = config.get('LOCAL', 'in_ok_pin_default')
        # IN_NG_PIN_DEFAULT = config.get('LOCAL', 'in_ng_pin_default')

        return COMPANY_CODE, HOST3, USER3, PASS3, DBNAME3, BOUNCE_TIME, SLEEP_TIME, \
               TIME_GAP, NIGHT_CLOSING_HHMMSS, DAY_CLOSING_HHMMSS


# @pyqtSlot()  # 가져오기
def getFacParameter():
    # # 2017.01.17 Conclusion. global 변수는 반드시 "최초 지정"하는 함수에 정의되야 한다.
    # global FORPRODUCINGORDERDATA, PROCESS, GROUPS, DESCRIPTION_TEXT, LINE_CODE, \
    #     WORK_DATE, DAY_NIGHT, GOODS, CODE, CAVITY, TO_WAREHOUSE, FACODE, \
    #     PRODUCTSELECTION, PLCBIT, FRONTJISNO, TRADE

    # print("__getFacParameter 내부 : ")
    # print("__getFacParameter LINE_CODE : ", LINE_CODE)
    # print("__getFacParameter GROUPS : ", GROUPS)
    # print("__getFacParameter PROCESS : ", PROCESS)
    # print("__getFacParameter FACODE : ", FACODE)
    # print("__getFacParameter CAVITY : ", CAVITY)
    # print("__getFacParameter PRODUCTSELECTION : ", PRODUCTSELECTION)
    # print("__getFacParameter PLCBIT : ", PLCBIT)
    # print("__getFacParameter FRONTJISNO : ", FRONTJISNO)
    # print("f_common TRADE : " + str(TRADE))
    # print("f_common UI : " + str(UI))

    # QMessageBox.about(self, '__getFacParameter', '__getFacParameter')
    # 2017.01.17 Conclusion. global 변수는 반드시 "최초 지정"하는 함수에 정의되야 한다.
    # global FORPRODUCINGORDERDATA, process, groups, DESCRIPTION_TEXT, line_code
    # global WORK_DATE, DAY_NIGHT, GOODS, CODE, CAVITY
    # 2017.01.17 Conclusion. global 변수는 반드시 "최초 지정"하는 함수(__startWork())에 정의되야 한다.
    # global description, work_date_ymd_string

    # print("__getFacParameter 1 : ")

    config = __open_config_file()

    # config = ConfigParser()
    # # pyinstaller를 사용하지 않는다면, elif 부분만 필요함
    # if getattr(sys, 'frozen', False):
    #     # print("1")
    #     # pyinstaller로 패키징한 실행파일의 경우
    #     cur_path = os.path.dirname(sys.executable)
    #     # print('if cur_path : ' + str(cur_path))
    # elif __file__:
    #     # print("2")
    #     # *.py 형태의 파일로 실행할 경우 로직
    #     cur_path = os.path.dirname(os.path.abspath(__file__))
    #     # print('elif cur_path : ' + str(cur_path))
    #
    # currentDir = os.path.dirname(os.path.realpath(__file__))
    # # print("__getLocalDbParameter currentDir : " + currentDir)
    # # config.read(filenames='/home/pi/dev/gathering/config.ini', encoding='utf-8')  # INI 파일 읽기
    # config.read(filenames=currentDir + '../config.ini', encoding='utf-8')
    # # ['config.ini']
    # config.sections()  # 섹션 리스트 읽기
    # # ['LOCAL']
    # # config.read('/home/pi/dev/gathering/config.ini')  # INI 파일 읽기
    # # # ['config.ini']
    # # config.sections()  # 섹션 리스트 읽기
    # # # ['LOCAL']
    config.options('PRODUCT_ENV')  # 옵션 이름 리스트 얻기 # ['host0','user0','pass0','dbname0']
    # print('getFacParameter config : ' + str(config))
    if 'PRODUCT_ENV' in config:
        FORPRODUCINGORDERDATA = config.get('PRODUCT_ENV', 'forproducingorderdata')
        PROCESS = config.get('PRODUCT_ENV', 'process')
        GROUPS = config.get('PRODUCT_ENV', 'groups')
        DESCRIPTION_TEXT = config.get('PRODUCT_ENV', 'description')
        LINE_CODE = config.get('PRODUCT_ENV', 'line_code')
        WORK_DATE = config.get('PRODUCT_ENV', 'work_date')
        DAY_NIGHT = config.get('PRODUCT_ENV', 'day_night')
        GOODS = config.get('PRODUCT_ENV', 'goods')
        CODE = config.get('PRODUCT_ENV', 'code')
        CAVITY = config.get('PRODUCT_ENV', 'cavity')
        TO_WAREHOUSE = config.get('PRODUCT_ENV', 'to_warehouse')
        FACODE = config.get('PRODUCT_ENV', 'facode')
        PRODUCTSELECTION = config.get('PRODUCT_ENV', 'productselection')
        PLCBIT = config.get('PRODUCT_ENV', 'plcbit')
        FRONTJISNO = config.get('PRODUCT_ENV', 'frontjisno')
        TRADE = config.get('PRODUCT_ENV', 'trade')
        UI = config.get('PRODUCT_ENV', 'ui')
        BAUDRATE = config.get('PRODUCT_ENV', 'baudrate')
        GOODSRIGHT = config.get('PRODUCT_ENV', 'goodsright')
        CODERIGHT = config.get('PRODUCT_ENV', 'coderight')
        CAVITYRIGHT = config.get('PRODUCT_ENV', 'cavityright')
        # print('__getFacParameter PROCESS : ' + str(PROCESS))
        # print("__getFacParameter GROUPS : " + str(GROUPS))
        # print("__getFacParameter DESCRIPTION_TEXT : " + str(DESCRIPTION_TEXT))
        # print("__getFacParameter LINE_CODE : " + str(LINE_CODE))
        # print("__getFacParameter WORK_DATE : " + str(WORK_DATE))
        # print("__getFacParameter DAY_NIGHT : " + str(DAY_NIGHT))
        # print("__getFacParameter GOODS : " + str(GOODS))
        # print("__getFacParameter CODE : " + str(CODE))
        # print("__getFacParameter CAVITY : " + str(CAVITY))
        # print("__getFacParameter TO_WAREHOUSE : " + str(TO_WAREHOUSE))
        # print("__getFacParameter FACODE : " + str(FACODE))
        # print("__getFacParameter PRODUCTSELECTION : " + str(PRODUCTSELECTION))
        # print("__getFacParameter PLCBIT : " + str(PLCBIT))
        # print("__getFacParameter FRONTJISNO : " + str(FRONTJISNO))
        # print("__getFacParameter TRADE : " + str(TRADE))
        # print("__getFacParameter UI : " + str(UI))
        # print("__getFacParameter BAUDRATE : " + str(BAUDRATE))
        # print("__getFacParameter GOODSRIGHT : " + str(GOODSRIGHT))
        # print("__getFacParameter CODERIGHT : " + str(CODERIGHT))
        # print("__getFacParameter CAVITYRIGHT : " + str(CAVITYRIGHT))
        return FORPRODUCINGORDERDATA, PROCESS, GROUPS, DESCRIPTION_TEXT, LINE_CODE, \
               WORK_DATE, DAY_NIGHT, GOODS, CODE, CAVITY, GOODSRIGHT, CODERIGHT, CAVITYRIGHT, TO_WAREHOUSE, FACODE, \
               PRODUCTSELECTION, PLCBIT, FRONTJISNO, TRADE, UI, BAUDRATE
    else:
        print("getFacParameter ???")


# @pyqtSlot()  # 세팅하기
def setFacParameter(PROCESS, GROUPS, DESCRIPTION, LINE_CODE, work_date_ymd_string,
                      DAY_NIGHT, GOODS, CODE, CAVITY, GOODSRIGHT, CODERIGHT, CAVITYRIGHT, TO_WAREHOUSE, FACODE,
                      PRODUCTSELECTION, PLCBIT, FRONTJISNO, TRADE, UI, BAUDRATE):
    # print('\setFacParameter CAVITY : ', CAVITY)
    # print('setFacParameter CAVITYRIGHT : ', CAVITYRIGHT)

    # config.set('PRODUCT_ENV', 'FORPRODUCINGORDERDATA', yn_producing_order_data)

    config = __open_config_file()

    # config = ConfigParser()
    # # pyinstaller를 사용하지 않는다면, elif 부분만 필요함
    # if getattr(sys, 'frozen', False):
    #     # pyinstaller로 패키징한 실행파일의 경우
    #     cur_path = os.path.dirname(sys.executable)
    #     # print('if cur_path : ' + str(cur_path))
    # elif __file__:
    #     # *.py 형태의 파일로 실행할 경우 로직
    #     cur_path = os.path.dirname(os.path.abspath(__file__))
    #     # print('elif cur_path : ' + str(cur_path))
    #
    # currentDir = os.path.dirname(os.path.realpath(__file__))
    # # print("__getLocalDbParameter currentDir : " + currentDir)
    # # config.read(filenames='/home/pi/dev/gathering/config.ini', encoding='utf-8')  # INI 파일 읽기
    # config.read(filenames=currentDir + '../config.ini', encoding='utf-8')
    # # ['config.ini']
    # config.sections()  # 섹션 리스트 읽기
    # # ['LOCAL']
    # # config.read('/home/pi/dev/gathering/config.ini')  # INI 파일 읽기
    # # # ['config.ini']
    # # config.sections()  # 섹션 리스트 읽기
    # # # ['LOCAL']
    config.options('PRODUCT_ENV')  # 옵션 이름 리스트 얻기 # ['host0','user0','pass0','dbname0']
    # print('setFacParameter config : ' + str(config))
    if 'PRODUCT_ENV' in config:
        # QMessageBox.about(self, '__setDbParameter', 'PROCESS : ' + str(PROCESS))
        # print("\n\n\n\n")
        PROCESS, GROUPS, DESCRIPTION, LINE_CODE, work_date_ymd_string,
        DAY_NIGHT, GOODS, CODE, CAVITY, GOODSRIGHT, CODERIGHT, CAVITYRIGHT, TO_WAREHOUSE, FACODE,
        PRODUCTSELECTION, PLCBIT, FRONTJISNO, TRADE, UI, BAUDRATE
        # print("__setFacParameter PROCESS : " + str(PROCESS))
        # print("__setFacParameter groups : " + str(GROUPS))
        # print("__setFacParameter description : " + str(DESCRIPTION))
        # print("__setFacParameter line_code : " + str(LINE_CODE))
        # print("__setFacParameter work_date_ymd_string : " + str(work_date_ymd_string))
        # print("__setFacParameter DAY_NIGHT : " + str(DAY_NIGHT))
        # print("__setFacParameter GOODS : " + str(GOODS))
        # print("__setFacParameter CODE : " + str(CODE))
        # print("__setFacParameter CAVITY : " + str(CAVITY))
        # print("__setFacParameter GOODSRIGHT : " + str(GOODSRIGHT))
        # print("__setFacParameter CODERIGHT : " + str(CODERIGHT))
        # print("__setFacParameter CAVITYRIGHT : " + str(CAVITYRIGHT))
        # print("__setFacParameter CAVITYRIGHT : " + str(CAVITYRIGHT))
        # print("__setFacParameter TO_WAREHOUSE : " + str(TO_WAREHOUSE))
        # print("__setFacParameter FACODE : " + str(FACODE))
        # print("__setFacParameter PRODUCTSELECTION : " + str(PRODUCTSELECTION))
        # print("__setFacParameter PLCBIT : " + str(PLCBIT))
        # print("__setFacParameter FRONTJISNO : " + str(FRONTJISNO))
        # print("__setFacParameter TRADE : " + str(TRADE))
        # print("__setFacParameter UI : " + str(UI))
        # print("__setFacParameter BAUDRATE : " + str(BAUDRATE))
        #
        # print("\n\n\n\n")
        config.set('PRODUCT_ENV', 'process', PROCESS)
        config.set('PRODUCT_ENV', 'groups', GROUPS)
        config.set('PRODUCT_ENV', 'description', DESCRIPTION)
        config.set('PRODUCT_ENV', 'line_code', LINE_CODE)
        config.set('PRODUCT_ENV', 'work_date', work_date_ymd_string)
        if DAY_NIGHT == '2' or DAY_NIGHT == '야' or DAY_NIGHT == '夜':
            DAY_NIGHT = '2'
        else:
            DAY_NIGHT = '1'
        config.set('PRODUCT_ENV', 'day_night', DAY_NIGHT)
        config.set('PRODUCT_ENV', 'goods', GOODS)
        config.set('PRODUCT_ENV', 'code', CODE)
        config.set('PRODUCT_ENV', 'cavity', CAVITY)
        config.set('PRODUCT_ENV', 'to_warehouse', TO_WAREHOUSE)
        config.set('PRODUCT_ENV', 'facode', FACODE)
        config.set('PRODUCT_ENV', 'productselection', PRODUCTSELECTION)
        config.set('PRODUCT_ENV', 'plcbit', PLCBIT)
        config.set('PRODUCT_ENV', 'frontjisno', FRONTJISNO)
        config.set('PRODUCT_ENV', 'trade', TRADE)
        config.set('PRODUCT_ENV', 'ui', UI)
        config.set('PRODUCT_ENV', 'baudrate', BAUDRATE)
        config.set('PRODUCT_ENV', 'goodsright', GOODSRIGHT)
        config.set('PRODUCT_ENV', 'coderight', CODERIGHT)
        config.set('PRODUCT_ENV', 'cavityright', CAVITYRIGHT)

        # config.read(filenames=currentDir + '/config.ini', encoding='utf-8')
        # config_file = open('/home/pi/dev/gathering/config.ini', 'w')
        # config_file = open('config.ini', 'w')

        is_write = __save_config_file(config)
        # print("setFacParameter is_write : ", is_write)
        return is_write

        # currentDir = os.path.dirname(os.path.realpath(__file__))
        # config_file = open(file=currentDir + '/config.ini', mode='wt', encoding='utf-8')
        # config.write(config_file)
        # config_file.close()
        # print("setFacParameter config_file : ", config_file)
        # return 1


# @pyqtSlot()  # 가져오기 1
def getQrcode():
    # global VERSION, ERROR_CORRECTION, BOX_SIZER, BORDER, QRCODEDATA, FILL, BACK_COLOR

    # QMessageBox.about(self, '__getFacParameter', '__getFacParameter')
    # 2017.01.17 Conclusion. global 변수는 반드시 "최초 지정"하는 함수에 정의되야 한다.
    # global FORPRODUCINGORDERDATA, process, groups, DESCRIPTION_TEXT, line_code
    # global WORK_DATE, DAY_NIGHT, GOODS, CODE, CAVITY
    # 2017.01.17 Conclusion. global 변수는 반드시 "최초 지정"하는 함수(__startWork())에 정의되야 한다.
    # global description, work_date_ymd_string

    config = __open_config_file()

    # config = ConfigParser()
    # # pyinstaller를 사용하지 않는다면, elif 부분만 필요함
    # if getattr(sys, 'frozen', False):
    #     # print("1")
    #     # pyinstaller로 패키징한 실행파일의 경우
    #     cur_path = os.path.dirname(sys.executable)
    #     # print('if cur_path : ' + str(cur_path))
    # elif __file__:
    #     # print("2")
    #     # *.py 형태의 파일로 실행할 경우 로직
    #     cur_path = os.path.dirname(os.path.abspath(__file__))
    #     # print('elif cur_path : ' + str(cur_path))
    #
    # currentDir = os.path.dirname(os.path.realpath(__file__))
    # # print("__getLocalDbParameter currentDir : " + currentDir)
    # # config.read(filenames='/home/pi/dev/gathering/config.ini', encoding='utf-8')  # INI 파일 읽기
    # # config.read(filenames=currentDir + '../config.ini', encoding='utf-8')
    # config_file = open(file=currentDir + '/config.ini', mode='wt', encoding='utf-8')
    # # ['config.ini']
    # config.sections()  # 섹션 리스트 읽기
    # # ['LOCAL']
    # # config.read('/home/pi/dev/gathering/config.ini')  # INI 파일 읽기
    # # # ['config.ini']
    # # config.sections()  # 섹션 리스트 읽기
    # # # ['LOCAL']
    config.options('QRCODE')  # 옵션 이름 리스트 얻기 # ['host0','user0','pass0','dbname0']
    # print('getQrcode config : ' + str(config))
    if 'QRCODE' in config:
        VERSION = config.get('QRCODE', 'version')
        ERROR_CORRECTION = config.get('QRCODE', 'error_correction')
        BOX_SIZER = config.get('QRCODE', 'box_sizer')
        BORDER = config.get('QRCODE', 'border')
        QRCODEDATA = config.get('QRCODE', 'qrcodedata')
        FILL = config.get('QRCODE', 'fill')
        BACK_COLOR = config.get('QRCODE', 'back_color')
        # print("__getQrcode VERSION : " + str(VERSION))
        # print("__getQrcode ERROR_CORRECTION : " + str(ERROR_CORRECTION))
        # print("__getQrcode BOX_SIZER : " + str(BOX_SIZER))
        # print("__getQrcode BORDER : " + str(BORDER))
        # print("__getQrcode DATA : " + str(DATA))
        return VERSION, ERROR_CORRECTION, BOX_SIZER, BORDER, QRCODEDATA, FILL, BACK_COLOR


# @pyqtSlot()  # 세팅하기
def setQrcode(VERSION, ERROR_CORRECTION, BOX_SIZER, BORDER, QRCODEDATA, FILL, BACK_COLOR):
    # config.set('PRODUCT_ENV', 'FORPRODUCINGORDERDATA', yn_producing_order_data)
    config = __open_config_file()
    # config = ConfigParser()
    # # pyinstaller를 사용하지 않는다면, elif 부분만 필요함
    # if getattr(sys, 'frozen', False):
    #     print("1")
    #     # pyinstaller로 패키징한 실행파일의 경우
    #     cur_path = os.path.dirname(sys.executable)
    #     print('if cur_path : ' + str(cur_path))
    # elif __file__:
    #     print("2")
    #     # *.py 형태의 파일로 실행할 경우 로직
    #     cur_path = os.path.dirname(os.path.abspath(__file__))
    #     print('elif cur_path : ' + str(cur_path))
    #
    # currentDir = os.path.dirname(os.path.realpath(__file__))
    # # print("__getLocalDbParameter currentDir : " + currentDir)
    # # config.read(filenames='/home/pi/dev/gathering/config.ini', encoding='utf-8')  # INI 파일 읽기
    # config.read(filenames=currentDir + '/config.ini', encoding='utf-8')
    # # ['config.ini']
    # config.sections()  # 섹션 리스트 읽기
    # # ['LOCAL']
    # # config.read('/home/pi/dev/gathering/config.ini')  # INI 파일 읽기
    # # # ['config.ini']
    # # config.sections()  # 섹션 리스트 읽기
    # # # ['LOCAL']
    config.options('QRCODE')  # 옵션 이름 리스트 얻기 # ['host0','user0','pass0','dbname0']
    # print('setQrcode config : ' + str(config))
    if 'QRCODE' in config:
        # return VERSION, ERROR_CORRECTION, BOX_SIZER, BORDER, DATA, FILL, BACK_COLOR
        config.set('QRCODE', 'version', VERSION)
        config.set('QRCODE', 'error_correction', ERROR_CORRECTION)
        config.set('QRCODE', 'box_sizer', BOX_SIZER)
        config.set('QRCODE', 'border', BORDER)
        config.set('QRCODE', 'qrcodedata', QRCODEDATA)
        config.set('QRCODE', 'fill', FILL)
        config.set('QRCODE', 'back_color', BACK_COLOR)
        # config.read(filenames=currentDir + '/config.ini', encoding='utf-8')
        # config_file = open('/home/pi/dev/gathering/config.ini', 'w')
        # config_file = open('config.ini', 'w')

        # config = __open_config_file()

        is_write = __save_config_file()
        # print("setQrcode is_write : ", is_write)

        return is_write

# def __generateQrcode():
#     # q = pyqrcode.create("My first Qrcode")
#     # q.png('MyFirstQrcode.png', scale=6)
#     qr = qrcode.make('My first Qrcode')
#     qr.save('MyFirstQrcode.png')
#     print("Qrcode generated ...")


# @pyqtSlot()
def generateQrcode(qrcodeGenerateData):
    VERSION, ERROR_CORRECTION, BOX_SIZER, BORDER, QRCODEDATA, FILL, BACK_COLOR = getQrcode()
    # print("generateQrcode VERSION : " + str(VERSION) + "\n")
    # print("generateQrcode ERROR_CORRECTION : " + str(ERROR_CORRECTION) + "\n")
    # print("generateQrcode BOX_SIZER : " + str(BOX_SIZER) + "\n")
    # print("generateQrcode BORDER : " + str(BORDER) + "\n")
    # print("generateQrcode generateQrcode QRCODEDATA : " + str(QRCODEDATA) + "\n")
    # print("generateQrcode generateQrcode FILL : " + str(FILL) + "\n")
    # print("generateQrcode generateQrcode BACK_COLOR : " + str(BACK_COLOR) + "\n")

    # print("generateQrcode generateQrcode qrcodeGenerateData : " + str(qrcodeGenerateData) + "\n")

    # 2019.10.19 Created. QRCode 생성 기준
    # 1. 191019 : 날짜 : 8자리
    # 2. PSB001 : 회사명 : 6자리
    # 3. 01 : 생산 라인 번호
    # 4. 1 : 주/야간
    # 5. F374EXFDE03 또는 PSKEI4321 : 품번
    # 6. 0001 : 해당 일자 기준 일련 번호
    # 7. 9999 : 박스(파렛트) 포장 기준 수량 : 20개면 : 0020

    # qr = qrcode.QRCode(
    #     version=VERSION,
    #     error_correction=ERROR_CORRECTION,
    #     box_size=BOX_SIZER,
    #     border=BORDER
    # )
    qr = qrcode.QRCode(
        version=VERSION,
        box_size=BOX_SIZER,
        border=BORDER
    )
    qrcodeSerialNo = "0001"
    data = qrcodeGenerateData  # '191022PSB0010518000013052'
    qr.add_data(qrcodeGenerateData)
    qr.make(fit=True)
    img = qr.make_image(fill=FILL, back_color=BACK_COLOR)

    config = ConfigParser()
    # print('1 __getLocalDbParameter 함수 내부')

    # pyinstaller를 사용하지 않는다면, elif 부분만 필요함
    if getattr(sys, 'frozen', False):
        # pyinstaller로 패키징한 실행파일의 경우
        cur_path = os.path.dirname(sys.executable)
        # print('if cur_path : ' + str(cur_path))
    elif __file__:
        # *.py 형태의 파일로 실행할 경우 로직
        cur_path = os.path.dirname(os.path.abspath(__file__))
        # print('elif cur_path : ' + str(cur_path))

    currentDir = os.path.dirname(os.path.realpath(__file__))
    # print("__getLocalDbParameter currentDir : " + currentDir)
    # config.read(filenames='/home/pi/dev/gathering/config.ini', encoding='utf-8')  # INI 파일 읽기
    # config.read(filenames=currentDir + '/config.ini', encoding='utf-8')

    current_date = datetime.date.today()
    # print("\ngenerateQrcode current_date : " + str(current_date))
    date_format = "%y%m%d"  # 소문자 "y"임에 주의, "%Y%m%d" = "20191022" : 대문자 "Y"임에 주의.
    # current_date_ymd_string = current_date.toString("yyMMdd")  # 2019.10.22 Conclusion. 요기 today() 값은 에러 난다.
    current_date_ymd_string = current_date.strftime(date_format)
    # print("\ngenerateQrcode current_date_ymd_string : " + str(current_date_ymd_string))

    qrcodeDir = currentDir + '/qrcode/'
    if os.path.isdir(qrcodeDir):
        os.path.join(currentDir, 'qrcode')  # 기존 경로와 새로운 폴더 이름을 합쳐서 하위 경로 만들기.
    else:
        os.mkdir(qrcodeDir)
    os.chdir(qrcodeDir)  # 작업 경로 바꾸기: os.chdir(path)

    qrcodeDirYear = qrcodeDir + '/' + current_date_ymd_string + '/'
    if os.path.isdir(qrcodeDirYear):
        os.path.join(qrcodeDirYear, 'current_date_ymd_string')  # 기존 경로와 새로운 폴더 이름을 합쳐서 하위 경로 만들기.
    else:
        os.mkdir(qrcodeDirYear)
    os.chdir(qrcodeDirYear)  # 작업 경로 바꾸기: os.chdir(path)

    # 2019.10.22 Added. 여기서 Qrcode 마지막 시리얼 번호를 찾는다. 파일명의 끝에서 4자리.
    path = "./"
    file_list = os.listdir(path)
    file_list_png = [file for file in file_list if file.endswith(".png")]
    # print("1 generateQrcode file_list_png: {}".format(file_list_png))
    file_list_png.reverse()
    # print("1 generateQrcode reverse file_list_png: {}".format(file_list_png))

    # path = "./"
    file_list = os.listdir(qrcodeDirYear)
    file_list_png = [file for file in file_list if file.endswith(".png")]
    # print("2 generateQrcode file_list_png: {}".format(file_list_png))
    file_list_png.reverse()
    # print("2 generateQrcode reverse file_list_png: {}".format(file_list_png))

    file_count = len(file_list_png)
    # print("generateQrcode file_count : ", file_count)

    if file_count == 0:
        qrcodeSerialNo = "QR0001"
    else:
        for i, fileNameFull in enumerate(file_list_png):  # 또는 for i in file_count:
            # print("generateQrcode i : " + str(i) + ", fileNameFull : " + fileNameFull)
            # fileNames = fileNameFull[0].split('.')  # 값은 리스트로 ['file name', 'extension name']
            # print("fileNames : ", fileNames)
            # fileName = fileNames[0]  # 값은 문자열로 'file name'
            # print("Only fileName : ", fileName)
            # qrcodeSerialNo = fileName[-4:]
            # print("\nqrcodeSerialNo : ", qrcodeSerialNo)

            fileNames = file_list_png[i].split('.')  # 값은 리스트로 ['file name', 'extension name']
            # print("generateQrcode fileNames : ", fileNames)
            fileName = fileNames[0]  # 값은 문자열로 'file name'
            # print("generateQrcode Only fileName : ", fileName)
            qrcodeSerialNo = fileName[-4:]
            # print("\ngenerateQrcode qrcodeSerialNo : ", qrcodeSerialNo)

            checkSpecialCharacters = '[A-Za-z@_!#$%^&*()<>?/\|}{~:]'  # '[A-Za-z!@#$%^&*]'
            # print("generateQrcode checkSpecialCharacters origin : ", checkSpecialCharacters)
            checkSpecialCharacters = re.compile(checkSpecialCharacters)
            # print("generateQrcode checkSpecialCharacters compiled : ", checkSpecialCharacters)
            # print("(checkSpecialCharacters.search(qrcodeSerialNo) : ", (checkSpecialCharacters.search(qrcodeSerialNo)))
            if (checkSpecialCharacters.search(qrcodeSerialNo) == None):  # 값이 모두 숫자임. 한 글자도 문자나 특수 문자가 없다.
                break
            else:  # 값 중에 한 글자라도 문자나 특수 문자가 있다면,
                qrcodeSerialNo = "0000"  # 초기화의 의미임.
                continue

        # print("\ngenerateQrcode 현재 파일 중 마지막 qrcodeSerialNo : ", qrcodeSerialNo)

    qrcodeSerialNo = str(int(qrcodeSerialNo) + 1).zfill(4)
    qrcodeSerialNo = "QR" + qrcodeSerialNo
    # print("\ngenerateQrcode 새로 발행할 최종 qrcodeSerialNo : ", qrcodeSerialNo)


    # qrcodeFileName = qrcodeGenerateData + "BOX0020" + qrcodeSerialNo  # 'YoutubeChannel.png'
    qrcodeFileName = qrcodeGenerateData + qrcodeSerialNo + '.png'  # 'YoutubeChannel.png'
    img.save(qrcodeFileName)
    # print("generateQrcode Qrcode generated qrcodeFileName : ", qrcodeFileName)

    os.chdir(currentDir)  # 작업경로 바꾸기: os.chdir(path)

    return qrcodeFileName


def __open_config_file():
    # print('__open_config_file config : ')
    config = ConfigParser()
    # print('1 __getLocalDbParameter 함수 내부')
    # print('1 __getLocalDbParameter 함수 내부 type(config): ', type(config))
    # print('1 __getLocalDbParameter 함수 내부 config:', config)


    # pyinstaller를 사용하지 않는다면, elif 부분만 필요함
    if getattr(sys, 'frozen', False):
        # pyinstaller로 패키징한 실행 파일의 경우
        cur_path = os.path.dirname(sys.executable)
        # print('if cur_path : ' + str(cur_path))
    elif __file__:
        # *.py 형태의 파일로 실행할 경우 로직
        cur_path = os.path.dirname(os.path.abspath(__file__))
        # print('elif cur_path : ' + str(cur_path))


    # 2021.01.25 Conclusion. os가 윈도우일 경우에는, 즉 일반 PC 사용자일 경우에는,
    # [config.ini] 파일을 [C:\Windows\SysWOW64\config] 루트 드라이브 및 윈도우 폴더를 활용한다.
    # print('1 __getLocalDbParameter 함수 내부 type(platform.system()):', type(platform.system()))
    # print('1 __getLocalDbParameter 함수 내부 platform.system():', platform.system())
    if platform.system() == 'Windows':
        projectDir = os.path.dirname(os.path.realpath(__file__))[2:]  # \ps\ppp : [C:\] 드라이브는 뺀다.
        # print("__getLocalDbParameter projectDir : " + projectDir)
        currentDir = "C:\Windows\SysWOW64\config\\rwkang" + projectDir
        print("합 변환 전 __getLocalDbParameter currentDir : " + currentDir)
        currentDirBackSlash = currentDir.replace("\\", '/')
        print("합 변환 후 __getLocalDbParameter currentDirBackSlash : " + currentDirBackSlash)
        # path = "./python/test"
        if not os.path.isdir(currentDirBackSlash):
            print("이쪽으로 들어 왔나?")
            try:
                # 2021.01.25 Conclusion. 아래 명령으로 폴더는 못 만드네... 그냥 수동으로 반드시 만들고 진행한다.
                # os.mkdirs(currentDirBackSlash, exist_ok=True)
                # kkk = os.mkdirs(currentDirBackSlash)
                print("설정 폴더가 없습니다. 관리자에게 문의하시오!")
                return
            except Exception as e:
            # except EnvironmentError.errno:
                print("만들었나? __getLocalDbParameter Exception.e : " + e)
                print("만들었나? __getLocalDbParameter EnvironmentError.errno : " + EnvironmentError.errno)
                print("만들었나? __getLocalDbParameter EnvironmentError.strerror : " + EnvironmentError.strerror)
        else:
            print("이미 파일이 있습니다. __getLocalDbParameter currentDirBackSlash : " + currentDirBackSlash)
    else:
        currentDir = os.path.dirname(os.path.realpath(__file__))
        # print("여기 os는 ? ", platform.system()) : Raspberry PI.라즈베리파이컴은, 현재 디렉토리로 바로 온다...
        # print("여기 os는 ? __getLocalDbParameter currentDir : " + currentDir)

    # config.read(filenames='/home/pi/dev/gathering/config.ini', encoding='utf-8')  # INI 파일 읽기
    config.read(filenames=currentDir + '/config.ini', encoding='utf-8')

    # ['config.ini']
    config.sections()  # 섹션 리스트 읽기
    # ['LOCAL']
    config.options('LOCAL')  # 옵션 이름 리스트 얻기 # ['host0','user0','pass0','dbname0']
    print('__open_config_file config : ', config)
    # if 'LOCAL' in config:
    #     # print("__open_config_file config.options() : ")
    #     # print("__open_config_file config.options() : ", config.options())
    #     FORPRODUCINGORDERDATA = config.get('PRODUCT_ENV', 'forproducingorderdata')
    #     PROCESS = config.get('PRODUCT_ENV', 'process')
    #     GROUPS = config.get('PRODUCT_ENV', 'groups')
    #     DESCRIPTION_TEXT = config.get('PRODUCT_ENV', 'description')
    #     LINE_CODE = config.get('PRODUCT_ENV', 'line_code')
    #     WORK_DATE = config.get('PRODUCT_ENV', 'work_date')
    #     DAY_NIGHT = config.get('PRODUCT_ENV', 'day_night')
    #     GOODS = config.get('PRODUCT_ENV', 'goods')
    #     CODE = config.get('PRODUCT_ENV', 'code')
    #     CAVITY = config.get('PRODUCT_ENV', 'cavity')
    #     TO_WAREHOUSE = config.get('PRODUCT_ENV', 'to_warehouse')
    #     FACODE = config.get('PRODUCT_ENV', 'facode')
    #     PRODUCTSELECTION = config.get('PRODUCT_ENV', 'productselection')
    #     PLCBIT = config.get('PRODUCT_ENV', 'plcbit')
    #     FRONTJISNO = config.get('PRODUCT_ENV', 'frontjisno')
    #     TRADE = config.get('PRODUCT_ENV', 'trade')
    #     UI = config.get('PRODUCT_ENV', 'ui')
    #     GOODSRIGHT = config.get('PRODUCT_ENV', 'goodsright')
    #     CODERIGHT = config.get('PRODUCT_ENV', 'coderight')
    #     CAVITYRIGHT = config.get('PRODUCT_ENV', 'cavityright')
    #     print('__open_config_file PROCESS : ' + str(PROCESS))
    # else:
    #     print("__open_config_file config.options() : ???")

    return config


def __save_config_file(config):
    # print("__save_config_file : config", config)

    # 2021.01.25 Conclusion. os가 윈도우일 경우에는, 즉 일반 PC 사용자일 경우에는,
    # [config.ini] 파일을 [C:\Windows\SysWOW64\config] 루트 드라이브 및 윈도우 폴더를 활용한다.
    # print('1 __save_config_file 함수 내부 type(platform.system()):', type(platform.system()))
    # print('1 __save_config_file 함수 내부 platform.system():', platform.system())
    if platform.system() == 'Windows':
        projectDir = os.path.dirname(os.path.realpath(__file__))[2:]  # \ps\ppp : [C:\] 드라이브는 뺀다.
        print("__save_config_file projectDir : " + projectDir)
        currentDir = "C:\Windows\SysWOW64\config\\rwkang" + projectDir
        print("합 __save_config_file currentDir : " + currentDir)
        currentDir = currentDir.replace("\\", '/')
        print("합 변환 __save_config_file currentDir : " + currentDir)
    else:
        currentDir = os.path.dirname(os.path.realpath(__file__))
        # print("여기 os는 ? ", platform.system()) : Raspberry PI.라즈베리파이컴은, 현재 디렉토리로 바로 온다...
        # print("여기 os는 ? __getLocalDbParameter currentDir : " + currentDir)

    config_file = open(file=currentDir + '/config.ini', mode='wt', encoding='utf-8')
    # print("__save_config_file config_file : ", config_file)
    config.write(config_file)
    # print("__save_config_file config_file : ", config_file)
    config_file.close()
    return 1


    # config = __open_config_file()
    # currentDir = os.path.dirname(os.path.realpath(__file__))
    # config_file = open(file=currentDir + '/config.ini', mode='wt', encoding='utf-8')
    # config.write(config_file)
    # config_file.close()
    # return 1


def setPlcDataLog(gathering_no_max_this, COMPANY_CODE, PROCESS, GROUPS, LINE_CODE, CODE, GOODS, PLC_ADDRESS, PLC_VALUE):
    # print('setPlcDataLog gathering_no_max_this : ', gathering_no_max_this)
    # print('setPlcDataLog COMPANY_CODE : ', COMPANY_CODE)
    # print('setPlcDataLog PROCESS : ', PROCESS)
    # print('setPlcDataLog GROUPS : ', GROUPS)
    # print('setPlcDataLog LINE_CODE : ', LINE_CODE)
    # print('setPlcDataLog CODE : ', CODE)
    # print('setPlcDataLog GOODS : ', GOODS)
    # print('setPlcDataLog PLC_ADDRESS : ', PLC_ADDRESS)
    # print('setPlcDataLog PLC_VALUE : ', PLC_VALUE)
    # print('setPlcDataLog COMPANY_CODE type : ', type(COMPANY_CODE))
    # print('setPlcDataLog PROCESS type : ', type(PROCESS))
    # print('setPlcDataLog GROUPS type : ', type(GROUPS))
    # print('setPlcDataLog LINE_CODE type : ', type(LINE_CODE))
    # print('setPlcDataLog CODE type : ', type(CODE))
    # print('setPlcDataLog GOODS type : ', type(GOODS))
    # print('setPlcDataLog PLC_ADDRESS type : ', type(PLC_ADDRESS))
    # print('setPlcDataLog PLC_VALUE type : ', type(PLC_VALUE))

    currentDir = os.path.dirname(os.path.realpath(__file__))

    date_time_current = datetime.datetime.now()
    time_format = "%Y-%m-%d %H:%M:%S"
    currentDateTime = datetime.date.today().strftime("%Y-%m-%d")  # 오늘 날짜만.  # .date.에 주의
    # print('\nsetPlcDataLog currentDateTime : ', currentDateTime, "\n")
    currentDateTimeStr = date_time_current.strftime(time_format)  # 오늘 날짜만.  # .date.에 주의
    # print('\nsetPlcDataLog currentDateTime : ', currentDateTime, "\n")
    currentMonth = date_time_current.month
    currentMonthStr = str("{0:0>2}".format(currentMonth))
    currentDay = date_time_current.day
    currentDayStr = str("{0:0>2}".format(currentDay))

    se = ","
    plcData = gathering_no_max_this + se + currentDateTimeStr + se + COMPANY_CODE + se + PROCESS + se + \
              GROUPS + se + LINE_CODE + se + CODE + se + GOODS + se + PLC_ADDRESS + se + PLC_VALUE + "\n"
    # print('\nsetPlcDataLog plcData : ', plcData, "\n")

    file = './PlcDataLog' + currentMonthStr + currentDayStr + '.txt'
    fileName = '/PlcDataLog' + currentMonthStr + currentDayStr + '.txt'
    fileNameFull = currentDir + fileName
    # plcDataLog = open(file, 'w')  #
    if os.path.isfile(fileNameFull):  # os.path.isfile(file) => 이건 파일 못 찾음.
        print("파일이 있습니다. fileNameFull : ", fileNameFull)
        # time.sleep(3)
        plcDataLog = open(file=fileNameFull, mode='a', encoding='utf-8')
    else:
        print("파일이 없네... fileNameFull : ", fileNameFull)
        # time.sleep(3)
        plcDataLog = open(file=fileNameFull, mode='wt', encoding='utf-8')
    is_write = plcDataLog.write(plcData)
    plcDataLog.close()
    # print("setPlcDataLog is_write : ", is_write)
    return is_write


def __delete_PlcDataLog():
    # 최근 자료 10개 파일 삭제
    date_time_current = datetime.datetime.now()
    currentMonth = date_time_current.month
    currentMonthStr = str("{0:0>2}".format(currentMonth))
    currentDay = date_time_current.day
    currentDayStr = str("{0:0>2}".format(currentDay))

    time_format = "%Y-%m-%d %H:%M:%S"
    # now_utc = time.time()  # UTC 현재 시각(초)
    # print("now_utc : " + str(now_utc))
    # now_date = datetime.date.today().strftime("%Y-%m-%d")  # 오늘 날짜만.  # .date.에 주의
    now_date = datetime.date.today().strftime("%Y%m%d")  # 오늘 날짜만.  # .date.에 주의

    i = 1  # 2020.04.23 Modified. 어제 파일은 살려 둔다. 그제 파일까지 삭제하도록...
    while i < 9:
        i += 1

        deleteDay = currentDay - i
        if deleteDay == 0:
            currentMonth = currentMonth - 1
            if currentMonth == 0:
                currentMonth = 12
            if currentMonth == 4 or currentMonth == 6 or currentMonth == 9 or currentMonth == 11:
                currentDay = 30
            elif int(currentMonth) == 2:
                currentDay = 28
            else:
                currentDay = 31
        deleteDayStr = str("{0:0>2}".format(deleteDay))

        # file = './upload/test.txt'  # 하위 디렉토리 이용.
        # file = './PlcDataLog' + currentMonthStr + deleteDayStr + '.txt'
        # if os.path.isfile(file):

        currentDir = os.path.dirname(os.path.realpath(__file__))
        file = './PlcDataLog' + currentMonthStr + deleteDayStr + '.txt'
        fileName = '/PlcDataLog' + currentMonthStr + deleteDayStr + '.txt'
        fileNameFull = currentDir + fileName
        if os.path.isfile(fileNameFull):  # os.path.isfile(file) => 이건 파일 못 찾음.
            print("__delete_PlcDataLog 파일이 있습니다. fileNameFull : ", fileNameFull)
            os.remove(fileNameFull)
            time.sleep(1)
            return 'okay'
        else:
            print("__delete_PlcDataLog 파일이 없네... fileNameFull : ", fileNameFull)
            time.sleep(1)
            return 'NG'


def creating_gathering_goods(mySqlLocalDb, cursArray):
    # 2018.11.05 Added. 테이블 존재 여부 확인, 없으면 자동 생성.
    sql = "CREATE TABLE IF NOT EXISTS gathering_goods (" \
          "Id bigint(20) unsigned Not Null Auto_Increment PRIMARY KEY ," \
          "code varchar(100) unique," \
          "code_no varchar(100)," \
          "part_no varchar(100)," \
          "marking_no varchar(100)," \
          "goods varchar(255)," \
          "process varchar(255)," \
          "step1 varchar(255)," \
          "step2 varchar(255)," \
          "step3 varchar(255)," \
          "step4 varchar(255)," \
          "step9 varchar(255)," \
          "goods0 int," \
          "goods1 int," \
          "goods2 int," \
          "goods3 int," \
          "description int Not Null," \
          "goods_assets int Not Null," \
          "unit bigint(20)," \
          "box_qty bigint(20)," \
          "trade bigint(20)," \
          "trade_name varchar(255)," \
          "user_id varchar(100)," \
          "modified_date datetime Not Null Default Current_TimeStamp " \
          ")"
    cursArray.execute(sql)
    try:
        mySqlLocalDb.commit()
        print("1 : Local 제품 테이블(gathering_goods) 생성 완료! ")
        # sleep(1)  # 10분 = 600
        tf = True
    except:
        mySqlLocalDb.rollback()
        print("2 : Local 제품 테이블(gathering_goods) 생성 실패! ")
        # sleep(1)  # 10분 = 600
        sys.exit()
        tf = False
    return sql, tf


def creating_gathering_description(mySqlLocalDb, cursArray):
    # 2018.11.05 Added. 테이블 존재 여부 확인, 없으면 자동 생성.
    sql = "CREATE TABLE IF NOT EXISTS Gathering_Description (" \
          "Id bigint(20) unsigned Not Null Auto_Increment PRIMARY KEY ," \
          "Language1 varchar(255)," \
          "Language2 varchar(255)," \
          "Language3 varchar(255)," \
          "language4 varchar(255)," \
          "Process varchar(100) Not Null," \
          "GoodsAssets int Not Null," \
          "UserId varchar(100)," \
          "ModifiedDate datetime Not Null Default Current_TimeStamp " \
          ")"
    cursArray.execute(sql)

    # UNIQUE Column 만들기 위해서는, 테이블 생성 후 따로 명령한다.
    # ALTER TABLE Gathering_ProductionActual UNIQUE(ProductionActualNo(100));

    try:
        mySqlLocalDb.commit()
        tf = True
        print(" : Local 품명 테이블(Descrition) 생성 완료! ")
        time.sleep(1)  # 10분 = 600
    except:
        mySqlLocalDb.rollback()
        tf = False
        print(" : Local 품명 테이블(Description) 생성 실패! ")
        time.sleep(1)  # 10분 = 600
        sys.exit()

    return sql, tf


def creating_gathering_groups(mySqlLocalDb, cursArray):
    # 2018.11.05 Added. 테이블 존재 여부 확인, 없으면 자동 생성.
    sql = "CREATE TABLE IF NOT EXISTS Gathering_Groups (" \
          "Id bigint(20) unsigned Not Null Auto_Increment PRIMARY KEY ," \
          "Code varchar(100) Not Null," \
          "PaCode varchar(100) Not Null, " \
          "Language1 varchar(255)," \
          "Language2 varchar(255)," \
          "Language3 varchar(255)," \
          "language4 varchar(255)," \
          "Process varchar(100) Not Null," \
          "Team int Not Null," \
          "LineCode int Not Null," \
          "FaCode varchar(100)," \
          "UserId varchar(100)," \
          "ModifiedDate datetime Not Null Default Current_TimeStamp " \
          ")"

    cursArray.execute(sql)
    # UNIQUE Column 만들기 위해서는, 테이블 생성 후 따로 명령한다.
    # ALTER TABLE Gathering_ProductionActual UNIQUE(ProductionActualNo(100));

    try:
        mySqlLocalDb.commit()
        tf = True
        print(" : Local 품명 테이블(Descrition) 생성 완료! ")
        time.sleep(1)  # 10분 = 600
    except:
        mySqlLocalDb.rollback()
        tf = False
        print(" : Local 품명 테이블(Description) 생성 실패! ")
        time.sleep(1)  # 10분 = 600
        sys.exit()

    return sql, tf


def creating_gathering_equipmentofproduct(mySqlLocalDb, cursArray):
    # 2018.11.05 Added. 테이블 존재 여부 확인, 없으면 자동 생성.
    sql = "CREATE TABLE IF NOT EXISTS Gathering_EquipmentOfProduct (" \
          "Id bigint(20) unsigned Not Null AUTO_INCREMENT PRIMARY KEY ," \
          "Process varchar(100) Not Null," \
          "LineCode varchar(100) Not Null," \
          "Code varchar(100) Not Null," \
          "FaCode varchar(100), " \
          "BarcodeInfo varchar(200)," \
          "BeInUse varchar(10) Not Null," \
          "DescriptionEquipment varchar(200)," \
          "CreatedUser varchar(200)," \
          "CreatedDate datetime Not Null Default Current_TimeStamp," \
          "ModifiedUser varchar(200)," \
          "ModifiedDate datetime Not Null Default Current_TimeStamp " \
          ")"

    cursArray.execute(sql)
    # UNIQUE Column 만들기 위해서는, 테이블 생성 후 따로 명령한다.
    # ALTER TABLE Gathering_ProductionActual UNIQUE(ProductionActualNo(100));

    try:
        mySqlLocalDb.commit()
        tf = True
        print(" : Local 설비별 생산품 등록 테이블(Gathering_EquipmentOfProduct) 생성 완료! ")
        time.sleep(1)  # 10분 = 600
    except:
        mySqlLocalDb.rollback()
        tf = False
        print(" : Local 설비별 생산품 등록 테이블(Gathering_EquipmentOfProduct) 생성 실패! ")
        time.sleep(1)  # 10분 = 600
        sys.exit()

    return sql, tf


def getting_goodsmaster(msSqlServerDb, cursArrayServer, HOST0, USER0, PASS0, DBNAME0,
                          mySqlLocalDb, cursArray, cursDict, HOST1, USER1, PASS1, DBNAME1):
    if len(DBNAME0) > 1:

        loop_count = 0
        # if remoteDbConnection == 1 and localDbConnection == 1:

        loop_count += 1
        # print("loop_count : "+str(loop_count))

        # 2018.11.05 Added. MySQL에서 테이블 존재 여부 확인 루틴
        # sql = "SELECT EXISTS (" \
        #       "FROM Information_schema.tables" \
        #       "WHERE table_name = 'gathering_goods' AND table_schema = 'PowerMes')" \
        #       "AS flag"

        # sql = "SELECT COUNT(*) FROM information_schema.tables " \
        #       "WHERE table_schema = 'PowerMes' AND table_name = 'gathering_goods'"

        # 2018.11.05 Added. 파이썬에서 테이블 존재 여부 확인 루틴
        check = "SHOW TABLES LIKE 'gathering_goods'"
        # cursArray.execute(check)
        try:
            result = cursArray.execute(check)
        except:
            mySqlLocalDb, cursArray, cursDict, \
            COMPANY_CODE, HOST1, USER1, PASS1, DBNAME1, BOUNCE_TIME, SLEEP_TIME, \
            TIME_GAP, NIGHT_CLOSING_HHMMSS, DAY_CLOSING_HHMMSS, \
            FORPRODUCINGORDERDATA, PROCESS, GROUPS, DESCRIPTION_TEXT, LINE_CODE, \
            WORK_DATE, DAY_NIGHT, GOODS, CODE, CAVITY, GOODSRIGHT, CODERIGHT, CAVITYRIGHT, TO_WAREHOUSE, \
            FACODE, PRODUCTSELECTION, PLCBIT, FRONTJISNO, TRADE, UI, BAUDRATE = connectDB()
            result = cursDict.execute(check)

        result = cursArray.fetchall()
        # print("first result : ", str(result), "len(result) : ", len(result))
        if len(result) == 0:
            # 2018.11.05 Added. 테이블 존재 여부 확인, 없으면 자동 생성.
            sql, tf = creating_gathering_goods(mySqlLocalDb, cursArray)
            if tf:
                pass
            else:
                print("[Gathering_Goods] 테이블 생성에 실패하였습니다. 다시 확인하시오!")
                sys.exit()
        else:
            # 2018.11.05 Added. 테이블 존재 여부 확인, 있으면 자동 삭제 : 일반적인 경우에는 사용하지 않고,
            # 테이블 삭제하고 새로 테이블을 생성하고자 할 때만, 아래 루틴을 사용한다.
            sql = "DROP TABLE gathering_goods"
            # print("2 else sql : ", sql)
            cursArray.execute(sql)
            # print("3 else cursArray : ", cursArray)
            array_sets_local = cursArray.fetchall()  # Dictionary based cursor, 선택한 "로우"가 1개 이상일 때.
            # print("4 array_sets_server : " + str(len(array_sets_local)))

            check = "SHOW TABLES LIKE 'gathering_goods'"
            cursArray.execute(check)
            result = cursArray.fetchall()
            # print("5 else result : ", str(result), "len(result) : ", len(result))
            if len(result) == 0:
                pass
                # print("6 : Local 제품 테이블(gathering_goods) 존재 확인 완료! ")
                # sleep(1)  # 10분 = 600
                # sys.exit()
            else:
                pass
                # print("7 : Local 제품 테이블(gathering_goods) 존재 확인 실패! ")
                # sleep(1)  # 10분 = 600
                # sys.exit()

            # 2018.11.05 Added. 테이블 존재 여부 확인, 없으면 자동 생성.
            sql, tf = creating_gathering_goods(mySqlLocalDb, cursArray)
            # print("8 gathering_goods 테이블 생성 : sql : ", sql)
            # print("9 gathering_goods 테이블 생성 : tf : ", tf)
            # if len(result) == 0:
            if tf:
                pass
            else:
                # 2018.11.05 Added. 테이블 존재 여부 확인, 없으면 자동 생성.
                sql, tf = creating_gathering_goods(mySqlLocalDb, cursArray)
                # print("11 gathering_goods 테이블 생성 : sql : ", sql)
                # print("12 gathering_goods 테이블 생성 : tf : ", tf)
                if tf:
                    pass
                else:
                    # print("13 [Gathering_Goods] 테이블 생성에 실패하였습니다. 다시 확인하시오!")
                    sys.exit()

        user_id = USER1
        today_ymd = datetime.date.today()
        # print("today_ymd Type : " + str(type(today_ymd)) + ", 값 : " + str(today_ymd))
        # today_ymd_string = datetime.date.today().strftime("%y%m%d")
        # print("today_ymd_string Type : " + str(type(today_ymd_string)) + ", 값 : " + str(today_ymd_string))

        # 2018.08.09 먼저 "Local.PowerMes.gathering_goods" 테이블의 기존 자료를 모두 삭제한다.
        # 아마도 "Foreign Key" 세팅으로 삭제가 안 되는 것 같은디, 그래서 그냥
        # "code"를 기준으로 먼저 찾게 하고, 없는 "품목"만 "Insert" 하게 한다.
        sql = "Delete From gathering_goods"
        # print(" : 삭제 sql : ", sql)
        # Where code=%s"
        # value = '8000010001'
        # cursDict.execute(sql, value)
        cursDict.execute(sql)
        try:
            mySqlLocalDb.commit()
            print(" : Local 제품 테이블에서 삭제 성공 XXXXXXXXXXXXX! ")
            # sleep(1)  # 10분 = 600
        except:
            mySqlLocalDb.rollback()
            print(" : Local 제품 테이블에서 삭제 실패 XXXXXXXXXXXXX! ")
            # sleep(1)  # 10분 = 600

        # 2018.08.09 서버 "GoodsMaster.자산=제품 And 폐기 안된 제품"만 가져온다.
        # sql = "Select code,goods From goodsmaster Where goodsassets=%s And abolitiondate is NULL Order By code "
        sql = "Select Code,Goods,Process,Description,GoodsAssets,CodeNo,PartNo,MarkingNo,Unit,Box_Qty," \
              "Goods0,Goods1,Goods2,Goods3,Step1,Step2,Step3,Step4,Step9, CompanyId " \
              "From GoodsMaster " \
              "Where (GoodsAssets=%s or GoodsAssets=%s) And abolitiondate is NULL Order By Code "
        product = 2
        semiproduct = 3
        values = (product, semiproduct)  # 재고 자산.goodsAssets.제품 코드.

        cursArrayServer.execute(sql, values)  # array_sets_server.execute() 아님에 주의.
        # cursDictServer.execute(sql, values)  # array_sets_server.execute() 아님에 주의.

        array_sets_server = cursArrayServer.fetchall()  # Dictionary based cursor, 선택한 "로우"가 1개 이상일 때.
        # print("array_sets_server : " + str(array_sets_server))

        row_count_server = len(array_sets_server)
        # print("서버 제품 마스터 총 수 : "+str(row_count_server))
        # sleep(5)  # 10분 = 600

        if row_count_server > 0:  # if array_sets_server is not None:

            r = 0
            for row in array_sets_server:
                r = r + 1
                # print("row_count_server : "+str(r)+", row : "+str(row))
                # print("row[0] :" + str(row[0]))
                # print("row[1] :" + str(row[1]))

                # code = row['code']
                code = row[0]
                code = code.strip()
                # goods = row['goods']
                goods = row[1]
                if goods is None: goods = ""
                goods = goods.strip()

                # print("code : "+str(code))
                # print("goods : " + str(goods))
                # sleep(1)  # 10분 = 600

                process = row[2]
                if process is None: process = ""
                process = process.strip()

                description = row[3]
                if description is None: description = 0

                goods_assets = row[4]
                if goods_assets is None: goods_assets = 0

                # 2019.07.26 Added. CodeNo, PartNo, MarkingNo, Unit, Box_qty,
                # Step1, Step2, Step3, Step4, Goods0, Goods1, Goods2, Goods3 필드 추가
                code_no = row[5]
                if code_no is None: code_no = ""
                code_no = code_no.strip()
                part_no = row[6]
                if part_no is None: part_no = ""
                part_no = part_no.strip()
                marking_no = row[7]
                if marking_no is None: marking_no = ""
                marking_no = marking_no.strip()
                unit = row[8]
                box_qty = row[9]
                if box_qty is None: box_qty = 0
                goods0 = row[10]
                if goods0 is None: goods0 = 0
                goods1 = row[11]
                if goods1 is None: goods1 = 0
                goods2 = row[12]
                if goods2 is None: goods2 = 0
                goods3 = row[13]
                if goods3 is None: goods3 = 0
                step1 = row[14]
                if step1 is None: step1 = ""
                step1 = step1.strip()
                step2 = row[15]
                if step2 is None: step2 = ""
                step2 = step2.strip()
                step3 = row[16]
                if step3 is None: step3 = ""
                step3 = step3.strip()
                step4 = row[17]
                if step4 is None: step4 = ""
                step4 = step4.strip()
                step9 = row[18]
                if step9 is None: step9 = ""
                step9 = step9.strip()
                trade = row[19]
                if trade is None: trade = 0
                # trade = trade.strip()

                # 거래처 이름 가져오기
                sql = "Select language2 From gathering_trade Where id = %s Order By id "
                cursDict.execute(sql, trade)
                array_sets = cursDict.fetchone()  # 맨 위의 첫번째 로우 값만 필요.
                trade_name = ""
                if array_sets is None:
                    # print("array_sets is None !")
                    trade_name = ""
                else:
                    trade_name = array_sets['language2']
                # trade_text = str(trade) + " " + trade_name
                # print("trade_text : ", trade_text)

                # 로컬 자료 가져와서 검색.
                sql = "Select code From gathering_goods Where code=%s Order By code "

                cursArray.execute(sql, code)  # "작업 일자"+"회사 코드"+"생산 라인"+"주야"+"제품 코드"+"일련 번호" 검색.
                # cursArray.execute(sql)
                # array_sets = cursArray.fetchone()  # 요넘 "fetchon()" 함수는 아래 "row_count = len(array_sets)"에서 에러가 발생한다.
                # 오직 1개 이므로 의미가 "len()" 의미가 없다는 것 같다.
                array_sets = cursArray.fetchall()
                row_count = len(array_sets)
                # print("array_sets_server.count() : "+str(row_count))

                if row_count < 1:
                    # 2020.03.05 Modified. PSC.평산 창주는 [goods] 값을 [GoodsMaster.Step9] 컬럼 값을 사용한다.
                    # print("dbname0 : ", dbname0)
                    if 'PSC' in DBNAME0.upper():
                        goods = step9

                    goods = goods[:37]  # 글자 수가 너무 많으면, [좌/우] 생산 설비를 화면에 뿌릴 때, 화면이 제대로 나오질 않는다.
                    sql = "Insert Into gathering_goods " \
                          "(code,goods,process,description,goods_assets,code_no,part_no,marking_no,unit,box_qty," \
                          "goods0,goods1,goods2,goods3,step1,step2,step3,step4,step9," \
                          "trade,trade_name,user_id,modified_date)" \
                          "Values (%s,%s,%s,%s,%s, %s,%s,%s,%s,%s, %s,%s,%s,%s,%s, %s,%s,%s,%s,%s, %s,%s,%s)"
                    values = (
                    code, goods, process, description, goods_assets, code_no, part_no, marking_no, unit, box_qty,
                    goods0, goods1, goods2, goods3, step1, step2, step3, step4, step9,
                    trade, trade_name, user_id, today_ymd)

                    cursArray.execute(sql, values)  # array_sets.execute() 아님에 주의.

                    try:
                        mySqlLocalDb.commit()
                        # print(code+"."+goods + " : 로컬 컴퓨터에 제품 추가 성공!!! ")
                        # QMessageBox.about(self, 'Successfully Saved','Saved to Remote Server DB Successfully')
                        # sleep(1)  # 10분 = 600

                    except:
                        msSqlServerDb.rollback()
                        print(code + "." + goods + " : 로컬 컴퓨터에 제품 추가 실패!!! ")
                        # sleep(1)  # 10분 = 600
                        # QMessageBox.about(self, 'Failure Saved', 'Saved to Remote Server DB Failure')

        print(str(row_count_server) + " 품목의 제품을 모두 로컬 컴퓨터에 성공적으로 추가하였습니다!!! ")
        return row_count_server


def getting_groups(msSqlServerDb, cursArrayServer, HOST0, USER0, PASS0, DBNAME0,
                          mySqlLocalDb, cursArray, cursDict, HOST1, USER1, PASS1, DBNAME1):
    if len(DBNAME0) > 1:

        loop_count = 0
        # if remoteDbConnection == 1 and localDbConnection == 1:

        loop_count += 1
        # print("loop_count : "+str(loop_count))

        # 2018.11.05 Added. MySQL에서 테이블 존재 여부 확인 루틴
        # sql = "SELECT EXISTS (" \
        #       "FROM Information_schema.tables" \
        #       "WHERE table_name = 'Gathering_Groups' AND table_schema = 'PowerMes')" \
        #       "AS flag"

        # sql = "SELECT COUNT(*) FROM information_schema.tables " \
        #       "WHERE table_schema = 'PowerMes' AND table_name = 'Gathering_Groups'"

        # 2018.11.05 Added. 파이썬에서 테이블 존재 여부 확인 루틴
        check = "SHOW TABLES LIKE 'Gathering_Groups'"
        try:
            result = cursArray.execute(check)
        except:
            mySqlLocalDb, cursArray, cursDict, \
            COMPANY_CODE, HOST1, USER1, PASS1, DBNAME1, BOUNCE_TIME, SLEEP_TIME, \
            TIME_GAP, NIGHT_CLOSING_HHMMSS, DAY_CLOSING_HHMMSS, \
            FORPRODUCINGORDERDATA, PROCESS, GROUPS, DESCRIPTION_TEXT, LINE_CODE, \
            WORK_DATE, DAY_NIGHT, GOODS, CODE, CAVITY, GOODSRIGHT, CODERIGHT, CAVITYRIGHT, TO_WAREHOUSE, \
            FACODE, PRODUCTSELECTION, PLCBIT, FRONTJISNO, TRADE, UI, BAUDRATE = connectDB()
            result = cursDict.execute(check)

        result = cursArray.fetchall()

        # print("first result : ", str(result), "len(result) : ", len(result))
        if len(result) == 0:
            # 2018.11.05 Added. 테이블 존재 여부 확인, 없으면 자동 생성.
            sql, tf = creating_gathering_groups(mySqlLocalDb, cursArray)
            if tf:
                pass
            else:
                print("[Gathering_Groups] 테이블 생성에 실패하였습니다. 다시 확인하시오!")
                sys.exit()
        else:
            # 2018.11.05 Added. 테이블 존재 여부 확인, 있으면 자동 삭제 : 일반적인 경우에는 사용하지 않고,
            # 테이블 삭제하고 새로 테이블을 생성하고자 할 때만, 아래 루틴을 사용한다.
            sql = "DROP TABLE Gathering_Groups"
            # print("2 else sql : ", sql)
            cursArray.execute(sql)
            # print("3 else cursArray : ", cursArray)
            array_sets_local = cursArray.fetchall()  # Dictionary based cursor, 선택한 "로우"가 1개 이상일 때.
            # print("4 array_sets_server : " + str(len(array_sets_local)))

            check = "SHOW TABLES LIKE 'Gathering_Groups'"
            cursArray.execute(check)
            result = cursArray.fetchall()
            # print("5 else result : ", str(result), "len(result) : ", len(result))
            if len(result) == 0:
                pass
                # print("6 : Local 작업조 테이블(Gathering_Groups) 존재 확인 완료! ")
                # sleep(1)  # 10분 = 600
                # sys.exit()
            else:
                pass
                # print("7 : Local 작업조 테이블(Gathering_Groups) 존재 확인 실패! ")
                # sleep(1)  # 10분 = 600
                # sys.exit()

            # 2018.11.05 Added. 테이블 존재 여부 확인, 없으면 자동 생성.
            sql, tf = creating_gathering_groups(mySqlLocalDb, cursArray)
            # print("8 Gathering_Groups 테이블 생성 : sql : ", sql)
            # print("9 Gathering_Groups 테이블 생성 : tf : ", tf)
            # if len(result) == 0:
            if tf:
                pass
            else:
                # 2018.11.05 Added. 테이블 존재 여부 확인, 없으면 자동 생성.
                sql, tf = creating_gathering_groups(mySqlLocalDb, cursArray)
                # print("11 Gathering_Groups 테이블 생성 : sql : ", sql)
                # print("12 Gathering_Groups 테이블 생성 : tf : ", tf)
                if tf:
                    pass
                else:
                    # print("13 [Gathering_Goods] 테이블 생성에 실패하였습니다. 다시 확인하시오!")
                    sys.exit()

        user_id = USER1
        today_ymd = datetime.date.today()
        # print("today_ymd Type : " + str(type(today_ymd)) + ", 값 : " + str(today_ymd))
        # today_ymd_string = datetime.date.today().strftime("%y%m%d")
        # print("today_ymd_string Type : " + str(type(today_ymd_string)) + ", 값 : " + str(today_ymd_string))

        # 2018.08.09 먼저 "Local.PowerMes.Gathering_Groups" 테이블의 기존 자료를 모두 삭제한다.
        # 아마도 "Foreign Key" 세팅으로 삭제가 안 되는 것 같은디, 그래서 그냥
        # "code"를 기준으로 먼저 찾게 하고, 없는 "품목"만 "Insert" 하게 한다.
        sql = "Delete From Gathering_Groups "
        # value = '8000010001'
        # cursDict.execute(sql, value)
        cursDict.execute(sql)
        try:
            mySqlLocalDb.commit()
            print(" : Local 작업 그룹 테이블(Gathering_Groups)에서 모든 자료 삭제 성공 XXXXXXXXXXXXX! ")
            time.sleep(1)  # 10분 = 600
        except:
            mySqlLocalDb.rollback()
            print(" : Local 작업 그룹 테이블(Gathering_Groups)에서 모든 자료 삭제 실패 XXXXXXXXXXXXX! ")
            time.sleep(1)  # 10분 = 600
            sys.exit()

        # 2018.08.09 서버 "GoodsMaster.자산=제품 And 폐기 안된 제품"만 가져온다.
        # "From GoodsMaster INNER JOIN Description ON GoodsMaster.Description = Description.Id " \
        # "WHERE GoodsMaster.GoodsAssets = %s" \
        # "ORDER BY GoodsMaster.Description "
        # sql = "Select code,goods From goodsmaster Where goodsassets=%s And abolitiondate is NULL Order By code "
        # sql = "Select Code, PaCode, Process, Language3, Team From Groups Order By Code "
        sql = "Select Groups.Code, Groups.PaCode, Groups.Process, Groups.Language3, Groups.Team, " \
              "Machine.LineCode, Machine.FaCode " \
              "From Groups INNER JOIN Machine On Groups.PaCode = Machine.Code WHERE Groups.Used = '1' " \
              "Order By Groups.Code "

        cursArrayServer.execute(sql)  # array_sets.execute() 아님에 주의.
        # cursDictServer.execute(sql, values)  # array_sets.execute() 아님에 주의.

        array_sets_server = cursArrayServer.fetchall()  # Dictionary based cursor, 선택한 "로우"가 1개 이상일 때.
        # print("array_sets_server : " + str(array_sets_server))

        row_count_server = len(array_sets_server)
        # print("서버 제품 마스터 총 수 : "+str(row_count_server))
        # sleep(1)  # 10분 = 600

        if row_count_server > 0:  # if array_sets_server is not None:

            r = 0
            for row in array_sets_server:
                r = r + 1
                # print("row_count_server : "+str(r)+", row : "+str(row))
                # print("row[0] :" + str(row[0]))
                # print("row[1] :" + str(row[1]))

                # code = row['code']
                # code = row[0]
                code = row[0].strip()
                pacode = row[1].strip()
                process = row[2].strip()
                groups = row[3].strip()
                team = row[4]  # Integer.
                linecode = row[5]  # Integer.
                facode = row[6]
                # print("code : "+str(code))
                # print("groups : " + str(groups))
                # sleep(1)  # 10분 = 600

                # 로컬 자료 가져와서 검색.
                sql = "Select Code From Gathering_Groups Where Code=%s Order By Code "

                cursArray.execute(sql, code)  # "작업 일자"+"회사 코드"+"생산 라인"+"주야"+"제품 코드"+"일련 번호" 검색.
                # cursArray.execute(sql)
                # array_sets = cursArray.fetchone()  # 요넘 "fetchon()" 함수는 아래 "row_count = len(array_sets)"에서 에러가 발생한다. 오직 1개 이므로 의미가 "len()" 의미가 없다는 것 같다.
                array_sets = cursArray.fetchall()
                row_count = len(array_sets)
                # print("array_sets_server.count() : "+str(row_count))

                if row_count < 1:
                    # print("Insert Into groups 시작합니다.")
                    sql = "Insert Into Gathering_Groups " \
                          "(Code, PaCode, Language1, Language2, Language3, Language4, Process, Team, " \
                          "LineCode, FaCode, UserId, ModifiedDate) " \
                          "Values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    values = (code, pacode, groups, groups, groups, groups, process, team,
                              linecode, facode, user_id, today_ymd)

                    cursArray.execute(sql, values)  # array_sets.execute() 아님에 주의.

                    try:
                        mySqlLocalDb.commit()
                        # print(code+"."+groups + " : 로컬 컴퓨터에 공정 추가 성공!!! ")
                        # QMessageBox.about(self, 'Successfully Saved','Saved to Remote Server DB Successfully')
                        # sleep(1)  # 10분 = 600

                    except:
                        msSqlServerDb.rollback()
                        print(code + "." + groups + " : 로컬 컴퓨터에 공정 추가 실패!!! ")
                        time.sleep(1)  # 10분 = 600
                        # QMessageBox.about(self, 'Failure Saved', 'Saved to Remote Server DB Failure')

            print(str(row_count_server) + " 전체 공정을 모두 로컬 컴퓨터에 성공적으로 추가하였습니다!!! ")
            return row_count_server


def getting_description(msSqlServerDb, cursArrayServer, HOST0, USER0, PASS0, DBNAME0,
                          mySqlLocalDb, cursArray, cursDict, HOST1, USER1, PASS1, DBNAME1):
    if len(DBNAME0) > 1:

        loop_count = 0
        # if remoteDbConnection == 1 and localDbConnection == 1:

        loop_count += 1
        # print("loop_count : "+str(loop_count))

        # 2018.11.05 Added. MySQL에서 테이블 존재 여부 확인 루틴
        # sql = "SELECT EXISTS (" \
        #       "FROM Information_schema.tables" \
        #       "WHERE table_name = 'Gathering_Description' AND table_schema = 'PowerMes')" \
        #       "AS flag"

        # sql = "SELECT COUNT(*) FROM information_schema.tables " \
        #       "WHERE table_schema = 'PowerMes' AND table_name = 'Gathering_Description'"

        # 2018.11.05 Added. 파이썬에서 테이블 존재 여부 확인 루틴
        check = "SHOW TABLES LIKE 'Gathering_Description'"
        # cursArray.execute(check)
        try:
            result = cursArray.execute(check)
        except:
            mySqlLocalDb, cursArray, cursDict, \
            COMPANY_CODE, HOST1, USER1, PASS1, DBNAME1, BOUNCE_TIME, SLEEP_TIME, \
            TIME_GAP, NIGHT_CLOSING_HHMMSS, DAY_CLOSING_HHMMSS, \
            FORPRODUCINGORDERDATA, PROCESS, GROUPS, DESCRIPTION_TEXT, LINE_CODE, \
            WORK_DATE, DAY_NIGHT, GOODS, CODE, CAVITY, GOODSRIGHT, CODERIGHT, CAVITYRIGHT, TO_WAREHOUSE, \
            FACODE, PRODUCTSELECTION, PLCBIT, FRONTJISNO, TRADE, UI, BAUDRATE = connectDB()
            result = cursDict.execute(check)
        result = cursArray.fetchall()
        print("first result : ", str(result), "len(result) : ", len(result))
        if len(result) == 0:
            # 2018.11.05 Added. 테이블 존재 여부 확인, 없으면 자동 생성.
            sql, tf = creating_gathering_description(mySqlLocalDb, cursArray)
            if tf:
                pass
            else:
                print("[품명 테이블(Description)] 테이블 생성에 실패하였습니다. 다시 확인하시오!")
                # sys.exit()
        else:
            # 2018.11.05 Added. 테이블 존재 여부 확인, 있으면 자동 삭제 : 일반적인 경우에는 사용하지 않고,
            # 테이블 삭제하고 새로 테이블을 생성하고자 할 때만, 아래 루틴을 사용한다.
            sql = "DROP TABLE Gathering_Description"
            # print("2 else sql : ", sql)
            cursArray.execute(sql)
            # print("3 else cursArray : ", cursArray)
            array_sets_local = cursArray.fetchall()  # Dictionary based cursor, 선택한 "로우"가 1개 이상일 때.
            # print("4 array_sets_server : " + str(len(array_sets_local)))

            check = "SHOW TABLES LIKE 'Gathering_Description'"
            cursArray.execute(check)
            result = cursArray.fetchall()
            # print("5 else result : ", str(result), "len(result) : ", len(result))
            if len(result) == 0:
                pass
                # print("6 : Local 품명 테이블(Gathering_Description) 존재 확인 완료! ")
                # sleep(1)  # 10분 = 600
            else:
                pass
                # print("7 : Local 품명 테이블(Gathering_Description) 존재 확인 실패! ")
                # sleep(1)  # 10분 = 600

            # 2018.11.05 Added. 테이블 존재 여부 확인, 없으면 자동 생성.
            sql, tf = creating_gathering_description(mySqlLocalDb, cursArray)
            # print("8 Gathering_Description 테이블 생성 : sql : ", sql)
            # print("9 Gathering_Description 테이블 생성 : tf : ", tf)
            # if len(result) == 0:
            if tf:
                pass
            else:
                # 2018.11.05 Added. 테이블 존재 여부 확인, 없으면 자동 생성.
                sql, tf = creating_gathering_description(mySqlLocalDb, cursArray)
                # print("11 Gathering_Description 테이블 생성 : sql : ", sql)
                # print("12 Gathering_Description 테이블 생성 : tf : ", tf)
                if tf:
                    pass
                else:
                    pass
                    # print("13 [Gathering_Description] 테이블 생성에 실패하였습니다. 다시 확인하시오!")
                    # sys.exit()

        user_id = USER1
        today_ymd = datetime.date.today()
        # print("today_ymd Type : " + str(type(today_ymd)) + ", 값 : " + str(today_ymd))
        # today_ymd_string = datetime.date.today().strftime("%y%m%d")
        # print("today_ymd_string Type : " + str(type(today_ymd_string)) + ", 값 : " + str(today_ymd_string))

        # 2018.08.09 먼저 "Local.PowerMes.Gathering_Description" 테이블의 기존 자료를 모두 삭제한다.
        # 아마도 "Foreign Key" 세팅으로 삭제가 안 되는 것 같은디, 그래서 그냥
        # "code"를 기준으로 먼저 찾게 하고, 없는 "품목"만 "Insert" 하게 한다.
        sql = "Delete From Gathering_Description"
        # Where code=%s"
        # value = '8000010001'
        # cursDict.execute(sql, value)
        cursDict.execute(sql)
        try:
            mySqlLocalDb.commit()
            print(" : Local 품명 테이블(Descrition)에서 모든 자료 삭제 성공 XXXXXXXXXXXXX! ")
            time.sleep(1)  # 10분 = 600
        except:
            mySqlLocalDb.rollback()
            print(" : Local 품명 테이블(Description)에서 모든 자료 삭제 실패 XXXXXXXXXXXXX! ")
            time.sleep(1)  # 10분 = 600
            sys.exit()

        # 2018.08.09 서버 "GoodsMaster.품명 1개 and 자산=제품"만 가져온다.
        # sql = "Select ProductByDayPlanData.ProducingOrderNo, ProductByDayPlanData.Code, GoodsMaster.Goods " \
        #       "From ProductByDayPlanData " \
        #       "Inner Join GoodsMaster On ProductByDayPlanData.Code = GoodsMaster.Code " \
        #       "Where SUBSTR(ProductByDayPlanData.producingorderno,1,15)=%s " \
        #       "Order By ProductByDayPlanData.producingorderno"

        # 아래 1.번 또는 2.번 모두 동일한 값으로 검색된다.
        # 1.
        sql = "Select DISTINCT GoodsMaster.Description, Description.Language2, Description.Language3, " \
              "GoodsMaster.Process, GoodsMaster.GoodsAssets " \
              "From GoodsMaster INNER JOIN Description ON GoodsMaster.Description = Description.Id " \
              "WHERE GoodsMaster.GoodsAssets = %s or GoodsMaster.GoodsAssets = %s" \
              "ORDER BY GoodsMaster.Description "
        # 2.
        # sql = "Select DISTINCT GoodsMaster.Description, GoodsMaster.GoodsAssets, Description.Language3 " \
        #       "From GoodsMaster,Description " \
        #       "WHERE GoodsMaster.Description = Description.Id AND GoodsMaster.GoodsAssets = %s " \
        #       "ORDER BY GoodsMaster.Description "

        product = 2
        semiproduct = 3
        values = (product, semiproduct)  # 재고 자산.goodsAssets.제품/반제품 코드.

        cursArrayServer.execute(sql, values)  # array_sets_server.execute() 아님에 주의.
        # cursDictServer.execute(sql, values)  # array_sets_server.execute() 아님에 주의.

        array_sets_server = cursArrayServer.fetchall()  # Dictionary based cursor, 선택한 "로우"가 1개 이상일 때.
        # print("array_sets_server : " + str(array_sets_server))

        # 2020.12.17 Conclusion. AutoIncreased = 1 : 자동 증가 값이 [ID] 값을 [1]부터 출발, 즉 초기화.
        # cursArrayServer.execute("Alter Table pp_DayTimeLine Auto_Increment=1")

        row_count_server = len(array_sets_server)
        print("\n서버 품명 총 수 : " + str(row_count_server) + "\n")
        # sleep(1)  # 10분 = 600

        if row_count_server > 0:  # if array_sets_server is not None:

            r = 0
            for row in array_sets_server:
                # r = r + 1
                # print("row_count_server : "+str(r)+", row : "+str(row))
                # print("row[0] :" + str(row[0]))
                # print("row[1] :" + str(row[1]))

                # code = row['code']
                description_id = row[0]
                # description_id = description_id.strip()
                # goods = row['goods']
                description_name = row[1]
                description_name = description_name.strip()
                description_name_chn = row[2]
                description_name_chn = description_name.strip()

                process = row[3]
                # print("\nprocess : " + str(process))
                if process is None:
                    process = ""
                else:
                    process = process.strip()
                # print("\nprocess : " + str(process) + "\n")

                goods_assets_id = row[4]
                # print("\ngoods_assets_id : %s\n" % goods_assets_id)

                # print("code : "+str(code))
                # print("goods : " + str(goods))
                # sleep(1)  # 10분 = 600

                # 로컬 자료 가져와서 검색.
                sql = "Select Id From Gathering_Description Where Id=%s Order By Id "

                cursArray.execute(sql, description_id)  #
                # cursArray.execute(sql)
                # array_sets = cursArray.fetchone()  # 요넘 "fetchon()" 함수는 아래 "row_count = len(array_sets)"에서 에러가 발생한다.
                # 오직 1개 이므로 의미가 "len()" 의미가 없다는 것 같다.
                array_sets = cursArray.fetchall()
                row_count = len(array_sets)
                # print("array_sets_server.count() : "+str(row_count))

                if row_count < 1:
                    # print("Insert Into gathering_data 시작합니다.")

                    sql = "Insert Into Gathering_Description (Id, Language1, Language2, Language3, Language4," \
                          "Process, GoodsAssets, UserId, ModifiedDate) " \
                          "Values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    values = (description_id, description_name, description_name, description_name, description_name,
                              process, goods_assets_id, user_id, today_ymd)

                    cursArray.execute(sql, values)  # array_sets.execute() 아님에 주의.
                    # print(str(description_id) + "." + description_name + " : 로컬 컴퓨터에 품명 추가 성공!!! ")

                try:
                    mySqlLocalDb.commit()
                    print(str(description_id) + "." + description_name + " : 로컬 컴퓨터에 Commit 성공!!! ")
                    # QMessageBox.about(self, 'Successfully Saved','Saved to Remote Server DB Successfully')
                    # sleep(1)  # 10분 = 600

                except:
                    msSqlServerDb.rollback()
                    print(str(description_id) + "." + description_name + " : 로컬 컴퓨터에 품명 추가 실패!!! ")
                    time.sleep(1)  # 10분 = 600
                    # QMessageBox.about(self, 'Failure Saved', 'Saved to Remote Server DB Failure')

            print(str(row_count_server) + "개 품명 모두 로컬 컴퓨터에 성공적으로 추가하였습니다!\n")
            return row_count_server


def getting_equipmentofproduct(msSqlServerDb, cursArrayServer, HOST0, USER0, PASS0, DBNAME0,
                          mySqlLocalDb, cursArray, cursDict, HOST1, USER1, PASS1, DBNAME1):
    if len(DBNAME0) > 1:

        loop_count = 0
        # if remoteDbConnection == 1 and localDbConnection == 1:

        loop_count += 1
        # print("loop_count : "+str(loop_count))

        # 2018.11.05 Added. MySQL에서 테이블 존재 여부 확인 루틴
        # sql = "SELECT EXISTS (" \
        #       "FROM Information_schema.tables" \
        #       "WHERE table_name = 'Gathering_EquipmentOfProduct' AND table_schema = 'PowerMes')" \
        #       "AS flag"

        # sql = "SELECT COUNT(*) FROM information_schema.tables " \
        #       "WHERE table_schema = 'PowerMes' AND table_name = 'Gathering_EquipmentOfProduct'"

        # 2018.11.05 Added. 파이썬에서 테이블 존재 여부 확인 루틴
        check = "SHOW TABLES LIKE 'Gathering_EquipmentOfProduct'"
        cursArray.execute(check)
        result = cursArray.fetchall()
        print("first result : ", str(result), "len(result) : ", len(result))
        if len(result) == 0:
            # 2018.11.05 Added. 테이블 존재 여부 확인, 없으면 자동 생성.
            sql, tf = creating_gathering_description(mySqlLocalDb, cursArray)
            if tf:
                pass
            else:
                print("[Local 설비별 생산품 등록 테이블(Gathering_EquipmentOfProduct) 테이블 생성에 실패하였습니다. 다시 확인하시오!")
                # sys.exit()
        else:
            # 2018.11.05 Added. 테이블 존재 여부 확인, 있으면 자동 삭제 : 일반적인 경우에는 사용하지 않고,
            # 테이블 삭제하고 새로 테이블을 생성하고자 할 때만, 아래 루틴을 사용한다.
            sql = "DROP TABLE Gathering_EquipmentOfProduct"
            # print("2 else sql : ", sql)
            cursArray.execute(sql)
            # print("3 else cursArray : ", cursArray)
            array_sets_local = cursArray.fetchall()  # Dictionary based cursor, 선택한 "로우"가 1개 이상일 때.
            # print("4 array_sets_server : " + str(len(array_sets_local)))

            check = "SHOW TABLES LIKE 'Gathering_EquipmentOfProduct'"
            cursArray.execute(check)
            result = cursArray.fetchall()
            # print("5 else result : ", str(result), "len(result) : ", len(result))
            if len(result) == 0:
                pass
                # print("6 : Local 설비별 생산품 등록 테이블(Gathering_EquipmentOfProduct) 존재 확인 완료! ")
                # sleep(1)  # 10분 = 600
            else:
                pass
                # print("7 : Local 설비별 생산품 등록 테이블(Gathering_EquipmentOfProduct) 존재 확인 실패! ")
                # sleep(1)  # 10분 = 600

            # 2018.11.05 Added. 테이블 존재 여부 확인, 없으면 자동 생성.
            sql, tf = creating_gathering_equipmentofproduct(mySqlLocalDb, cursArray)
            # print("8 Gathering_EquipmentOfProduct 테이블 생성 : sql : ", sql)
            # print("9 Gathering_EquipmentOfProduct 테이블 생성 : tf : ", tf)
            # if len(result) == 0:
            if tf:
                pass
            else:
                # 2018.11.05 Added. 테이블 존재 여부 확인, 없으면 자동 생성.
                sql, tf = creating_gathering_equipmentofproduct(mySqlLocalDb, cursArray)
                # print("11 Gathering_Description 테이블 생성 : sql : ", sql)
                # print("12 Gathering_Description 테이블 생성 : tf : ", tf)
                if tf:
                    pass
                else:
                    pass
                    # print("13 [Gathering_EquipmentOfProduct] 테이블 생성에 실패하였습니다. 다시 확인하시오!")
                    # sys.exit()

        user_id = USER1
        today_ymd = datetime.date.today()
        # print("today_ymd Type : " + str(type(today_ymd)) + ", 값 : " + str(today_ymd))
        # today_ymd_string = datetime.date.today().strftime("%y%m%d")
        # print("today_ymd_string Type : " + str(type(today_ymd_string)) + ", 값 : " + str(today_ymd_string))

        # 2018.08.09 먼저 "Local.PowerMes.Gathering_Description" 테이블의 기존 자료를 모두 삭제한다.
        # 아마도 "Foreign Key" 세팅으로 삭제가 안 되는 것 같은디, 그래서 그냥
        # "code"를 기준으로 먼저 찾게 하고, 없는 "품목"만 "Insert" 하게 한다.
        sql = "Delete From Gathering_EquipmentOfProduct"
        # Where code=%s"
        # value = '8000010001'
        # cursDict.execute(sql, value)
        cursDict.execute(sql)
        try:
            mySqlLocalDb.commit()
            print(" : Local 설비별 생산품 등록 테이블(EquipmentOfProduct)에서 모든 자료 삭제 성공 XXXXXXXXXXXXX! ")
            time.sleep(1)  # 10분 = 600
        except:
            mySqlLocalDb.rollback()
            print(" : Local 설비별 생산품 등록 테이블(EquipmentOfProduct)에서 모든 자료 삭제 실패 XXXXXXXXXXXXX! ")
            time.sleep(1)  # 10분 = 600
            sys.exit()

        # 2018.08.09 서버 "GoodsMaster.자산=제품 And 폐기 안된 제품"만 가져온다.
        # "From GoodsMaster INNER JOIN Description ON GoodsMaster.Description = Description.Id " \
        # "WHERE GoodsMaster.GoodsAssets = %s" \
        # "ORDER BY GoodsMaster.Description "
        # sql = "Select code,goods From goodsmaster Where goodsassets=%s And abolitiondate is NULL Order By code "
        # sql = "Select Code, PaCode, Process, Language3, Team From Groups Order By Code "
        sql = "Select Process, LineCode, Code, FaCode, BarcodeInfo, BeInUse, DescriptionEquipment, " \
              "CreatedUser, ModifiedUser From EquipmentOfProduct Order By Process, LineCode, Code "

        cursArrayServer.execute(sql)  # array_sets.execute() 아님에 주의.
        # cursDictServer.execute(sql, values)  # array_sets.execute() 아님에 주의.

        array_sets_server = cursArrayServer.fetchall()  # Dictionary based cursor, 선택한 "로우"가 1개 이상일 때.
        # print("array_sets_server : " + str(array_sets_server))

        row_count_server = len(array_sets_server)
        # print("서버 제품 마스터 총 수 : "+str(row_count_server))
        # sleep(1)  # 10분 = 600

        if row_count_server > 0:  # if array_sets_server is not None:

            r = 0
            for row in array_sets_server:
                r = r + 1
                # print("row_count_server : "+str(r)+", row : "+str(row))
                # print("row[0] :" + str(row[0]))
                # print("row[1] :" + str(row[1]))

                # code = row['code']
                # code = row[0]
                process = row[0]
                if process is not None:
                    process = process.strip()
                linecode = row[1]
                code = row[2]
                if code is not None:
                    code = code.strip()
                facode = row[3]
                if facode is not None:
                    facode = facode.strip()
                barcodeinfo = row[4]
                # print("1 barcodeinfo : ", barcodeinfo)
                if barcodeinfo is not None:
                    barcodeinfo = barcodeinfo.strip()
                    # print("2 barcodeinfo : ", barcodeinfo)
                beinuse = row[5]
                descriptionequipment = row[6]
                if descriptionequipment is not None:
                    descriptionequipment = descriptionequipment.strip()
                createduser = row[7]
                if createduser is not None:
                    createduser = createduser.strip()
                modifieduser = row[8]
                if modifieduser is not None:
                    modifieduser = modifieduser.strip()
                # print("code : "+str(code))
                # sleep(1)  # 10분 = 600

                # 로컬 자료 가져와서 검색.
                sql = "Select Process,LineCode,Code From Gathering_EquipmentOfProduct " \
                      "Where Process=%s AND LineCode=%s AND Code=%s Order By Process,LineCode,Code "

                values = (process, linecode, code)
                cursArray.execute(sql, values)  # "작업 일자"+"회사 코드"+"생산 라인"+"주야"+"제품 코드"+"일련 번호" 검색.
                # cursArray.execute(sql)
                # array_sets = cursArray.fetchone()  # 요넘 "fetchon()" 함수는 아래 "row_count = len(array_sets)"에서 에러가 발생한다. 오직 1개 이므로 의미가 "len()" 의미가 없다는 것 같다.
                array_sets = cursArray.fetchall()
                row_count = len(array_sets)
                # print("array_sets_server.count() : "+str(row_count))

                if row_count < 1:
                    # print("Insert Into Gathering_EquipmentOfProduct 시작합니다.")
                    sql = "Insert Into Gathering_EquipmentOfProduct " \
                          "(Process, LineCode, Code, FaCode, BarcodeInfo, BeInUse, DescriptionEquipment, " \
                          "CreatedUser, ModifiedUser) Values (%s,%s,%s,%s,%s, %s,%s,%s,%s)"
                    values = (process, linecode, code, facode, barcodeinfo, beinuse, descriptionequipment,
                              createduser, modifieduser)

                    cursArray.execute(sql, values)  # array_sets.execute() 아님에 주의.

                    try:
                        mySqlLocalDb.commit()
                        # print(process + "." + linecode + "." + code + " : 로컬 컴퓨터에 설비별 생산품 추가 성공!!! ")
                        # QMessageBox.about(self, 'Successfully Saved','Saved to Remote Server DB Successfully')
                        # sleep(1)  # 10분 = 600

                    except:
                        msSqlServerDb.rollback()
                        print(process + "." + linecode + "." + code + " : 로컬 컴퓨터에 설비별 생산품 추가 실패!!! ")
                        time.sleep(1)  # 10분 = 600
                        # QMessageBox.about(self, 'Failure Saved', 'Saved to Remote Server DB Failure')

            print(str(row_count_server) + " 전체 공정을 모두 로컬 컴퓨터에 성공적으로 추가하였습니다!!! ")
            return row_count_server


# if __name__ == '__main__':
#     try:
#         INFINITELOOP = 1
#
#         # 2019.03.02 Added. 사출 공정에 사용하는 투입 원료의 [재공 관련 정보] 관리 여부 변수.
#         PROCESSING_CONTROL_BEINUSE = False  # True
#
#         # INPUT_CODE_TYPE = "SELECT"
#
#         in_ok_pin = 23
#         ok_pin = 24
#         in_ng_pin = 20
#         ng_pin = 21
#         out_pin = 18
#         buzzer_pin = 4
#         humidity_temperature_pin = 16
#
#         ts_pin1 = 5
#         ts_pin2 = 6
#         ts_pin3 = 17
#
#         mySqlLocalDb, cursArray, cursDict = connectDB()
#
#     except:
#
#         print("\n\n")
#         # # print("now_utc : " + str(now_utc))
#         # print("current_date : " + str(current_date))
#         # print("modified_date : " + str(modified_date))
#         print("Main except :: 치명적 에러로 강제 종료 ! Completly.....")
#         print("\n\n")
#         sys.exit()  # 2019.07.16 Conclusion. 아래 명령어 "sys.exit(app.exec())"로는 프로그램이 단지 멈춰있을 뿐이다.
#         # sys.exit(app.exec())
