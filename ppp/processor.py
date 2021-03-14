import locale
import ctypes
from datetime import time

# String gs_SqlServerInstalledInstance="SQLEXPRESS"//"MSSQLSERVER14"//"SQLEXPRESS2012"/*현재 SQL SERVER 설치된 인스턴스*/ => 2017.01.09 현재 확인 결과 의미 없는 변수 임.
# String g_HostName/*내 컴퓨터 이름 : 사용자 정의 보고서 용*/,gs_HostFullName=g_HostName+"\"+gs_SqlServerInstalledInstance
# String gs_Host[] /*w_Trans_Data_DB_TB에서... 전환 하려는 HOST의  모든 이름...*/,gs_HostPass[]
# String gs_ServerTransfer /*w_Trans_Data_DB_TB에서... 전환 하려는 HOST 이름...*/,gs_ServerReceiver
# String g_Server,gs_RegistryKeySection/*2019.05.25 Added. 레지스트리 저장 섹션*/
# String gs_Database_Name_Default="PowErpPsc" // 2019.05.25 Added. 시스템 기본 디폴트 Database 값 적용.
# String gs_Server_Default="" // 2019.05.25 Added. 시스템 기본 디폴트 gs_Server_Default 값 적용. : 마지막 접속한 Server 컴퓨터 이름 또는 IP.
#
# TRANSACTION SQLCA0,SQLCA1,SQLCA2,SQLCA3,SQLCA4,SQLCA5,SQLCA6,SQLCA7,SQLCA8,SQLCA9,SQLCA10 //10=gs_DatabaseAccess
# Window gw_Window
#
# uo_db_control guo_db_control // Ms Sql
# uo_db_control_my guo_db_control_my // My Sql
#
# //nvo_encode gFun
# str_system str_sys
# str_Menu gstr_MenuParm
# Boolean gb_PrintFirstPaperTry,g_admin,gb_PbCommThread // 2017.08.01 Added. 닫기 버튼 클릭시에... 프로그램 종료 안 하게 해 볼려고...
# Boolean gb_PrintSettingOk // w_PrintDialog.cb_pSetup. 즉시 인쇄할 프린터를 세팅 완료 했음...
# Int g_int_count, g_int_row,gi_MenuDivisionId,gi_Return
# //2018.03.26 Modified. 기본 값을 "99"로 미리 주고, "guo_db_control" 에서 연결이 정상적으로 되면... "gi_SqlCode 값이 "0"으로 변경된다. 물론 연결이 안 되었다면... "-1" ...
# Int gi_SQLCode=99
#
# String gs_BarcodeFileName/*2018.01.01 바코드 생성시 파일 경로 포함한 파일 이름.*/,gs_BarcodeImagePath
# String gs_ServerNo,gs_DSN//,gs_CurrentDir
# String g_RegistryKeyName//="PowERP2012"//"PowerERP"//여기를 바꾸고, init_db()에서 Select 문에서 바꿔준다.
# String g_Language, g_Corp/*회사명*/
# String gs_DatabaseName[],gs_DatabaseFrom,gs_DatabaseTo//w_Trans_Database_Table.ddlb_1.SelectionChanged.f_SetTransactionDataWindow()
# String g_Database/*="PowERP"*/,g_Database0="PowerERP",g_Database1,g_Database5/*="PowERPHoucheng"*/,g_Database6/*="PowERPFine"*/
# String g_Database2/*="PWMS"*/,g_Database3/*="PERP1"*/,g_Database4,g_Database7/*="TMS"*/,g_Database8,g_Database9
# String gs_DatabaseAccess // w_i_Barcode_Product (="Test_Data")
# String g_UserId,g_UserName,g_User,g_menu_code,g_Responsibility,g_Authority
# String g_bq /*시스템 년월:BenQi*/,gs_YearMonth,g_Year, g_c_month,g_Pass,gs_Pass_Default,g_SysConWay,g_Driver/*="C"*/
# String gs_CurrentDirectory,g_sd,g_cc	/* 사업부 단위의 원가 관리 여부 변수*/
# String gs_AccessFirstYesNo/*현재 실행 윈도우가 첫번째 실행인지*/
# String gs_WindowName,gs_WinParm,gs_MenuSuperiorOrigin,gs_MenuCodeOrigin
# String gs_SortDirection[10],gs_Column[10],gs_DataWindowObjectName,gs_DataWindowSortFields
# String gs_EditMaster_GoodsMasterCode="XXXXX-XXXXXXXXXX",gs_EditMaster_WarehouseCode="XX-XX-XX-XX"
# String gs_EditMaster_ReceivingOrderNo="XXXX-XX-XXXX",gs_EditMaster_ReceivingOrderDataNo="XXXX-XX-XXXX-XXXX"
# String gs_EditMaster_ShippingNo="XXXX-XX-XXXX-XXXX-XXXX",gs_EditMask_ProductionActualNo="XXXXXX-XXXXXX-XX-X-XXXXX-XXXXXXXXXX"
# String gs_EditMask_ProducingOrderNo="XXXXXX-XXXXXX-XX-X-XXXXX-XXXXXXXXXX",gs_EditMask_GatheringNo="XXXXXX-XXXXXX-XX-X-XXXXX-XXXXXXXXXXXXXXX"
# String gs_EditMask_MarkingNo="XX-XXXXXXXXXX",gs_EditMask_Code_MultiLine="XXXXX~nXXXXX~nXXXXX"
# //Long gi_ModifiedYesNo // 2020.06.26 Added. 각종 텍스트 항목 등을 최근 번역했는지 여부.
# Long gl_UserId //13.12.16 추가 : 숫자형 id 값 자동 증가 번호.
# //,g_ct  // 2008.02.02 g_ct 변수 삭제코저 함. 혹시 다른 루틴에 영향이 있을 수 있으므로 임시 유지,
# // powerp 어프리케이션에 CodeName 테이블 id=77을 치환한 알 수 없는 변수이므로.
# DateTime gdt_WorkDate//,g_workdate // 2015.02.27 수정. 변수명 수정 차원에서 수정, 다른 의미 없음.
# Date gdate_CwDate // from w_cw_config.cb_3.Clicked // 2015.02.27 수정. 변수명 수정 차원에서 수정, 다른 의미 없음.
# // g_bq:   , g_sd :    , g_c_month
# //string gs_flag = "DES"
# //2011.10.26 Added.
# Double gd_dec0=0,gd_dec2=2,gd_dec4=4,gd_dec6=6
# //Long gl_CurrentRow
# Time gt_NightClosingTime // w_Login.cb_1.Clicked() = 08:30:00 // 여기서 상수 값을 정하지 않고 (회사마다 값이 상이) w_Monitoring_Equipment_Pi에서 처리한다. // 야간조 퇴근 시간 : 모니터링할 때 날짜 변경 시간 조정을 위함.
# Time gt_DayClosingTime // w_Login.cb_1.Clicked() =20:30:00 // 주간조 퇴근 시간 : 모니터링할 때 날짜 변경 시간 조정을 위함.
# Time gt_DayLunchTime // 2018.12.07 Added. 주간 점심 시작 시간
# Time gt_NightLunchTime // 2018.12.07 Added. 야간 점심 시작 시간
# Time gt_DayWorkStartTime=Time("08:00:00") // 2019.09.05 주간 작업 시간 : gt_NightClosingTime 값과 동일할 있으나, 주간만 생산하는 회사인 경우에는, gt_NightClosingTime 값을 "00:00:00"을 줄 수 있으므로, gt_DayWorkStartTime 변수를 새로 두고, 진짜 주간 작업 시간을 지정하게 한다.
# Time gt_NightWorkStartTime=Time("00:00:01") // 2019.09.05 야간 작업 시간

# class GetGlobal():
def getGlobal(request):
    global LANGUAGE_NO, LANGUAGE_CODE, DAY_WORK_START_TIME, NIGHT_WORK_START_TIME

    windll = ctypes.windll.kernel32
    LANGUAGE_NO = windll.GetUserDefaultUILanguage()  # 1033, 1042 : int 숫자형...
    LANGUAGE_CODE = locale.windows_locale[windll.GetUserDefaultUILanguage()]  # "en_US", "ko_KR" : 문자형
    DAY_WORK_START_TIME = time(8, 0)
    NIGHT_WORK_START_TIME = time(20, 0)
    # print("LANGUAGE_NO: ", LANGUAGE_NO, ", LANGUAGE_NO: ", LANGUAGE_NO)
    # print("type(LANGUAGE_NO): ", type(LANGUAGE_NO), ", type(LANGUAGE_NO): ", type(LANGUAGE_NO))
    context = {
        # 'email_count': request.user.email_count(),
        'LANGUAGE_NO': LANGUAGE_NO,
        'LANGUAGE_CODE': LANGUAGE_CODE,
        'DAY_WORK_START_TIME': DAY_WORK_START_TIME,
        'NIGHT_WORK_START_TIME': NIGHT_WORK_START_TIME
    }
    return context  #, LANGUAGE_NO, LANGUAGE_CODE, DAY_WORK_START_TIME, NIGHT_WORK_START_TIME
