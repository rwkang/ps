from django.db import models

from django.utils.translation import ugettext as _


# 2021.02.10 Added. 혹시나 사용할까 해서 만들어 본다.
# ProductionActual.생산 실적 자료를 [생산 분석]을 위한 자료르 수집한 후에, 여기 모델을 활용할 수 있을까 해서이다.
class ProductionPerformance(models.Model):
    code = models.CharField(max_length=100, blank=False, null=False)
    specification = models.CharField(max_length=1000, blank=False, null=False)
    d1 = models.IntegerField(blank=True, null=False, default=0)
    d2 = models.IntegerField(blank=True, null=False, default=0)
    d3 = models.IntegerField(blank=True, null=False, default=0)
    d4 = models.IntegerField(blank=True, null=False, default=0)
    d5 = models.IntegerField(blank=True, null=False, default=0)
    d6 = models.IntegerField(blank=True, null=False, default=0)
    d7 = models.IntegerField(blank=True, null=False, default=0)
    d8 = models.IntegerField(blank=True, null=False, default=0)
    d9 = models.IntegerField(blank=True, null=False, default=0)
    d10 = models.IntegerField(blank=True, null=False, default=0)
    d11 = models.IntegerField(blank=True, null=False, default=0)
    d12 = models.IntegerField(blank=True, null=False, default=0)
    d13 = models.IntegerField(blank=True, null=False, default=0)
    d14 = models.IntegerField(blank=True, null=False, default=0)
    d15 = models.IntegerField(blank=True, null=False, default=0)
    d16 = models.IntegerField(blank=True, null=False, default=0)
    d17 = models.IntegerField(blank=True, null=False, default=0)
    d18 = models.IntegerField(blank=True, null=False, default=0)
    d19 = models.IntegerField(blank=True, null=False, default=0)
    d20 = models.IntegerField(blank=True, null=False, default=0)
    d21 = models.IntegerField(blank=True, null=False, default=0)
    d22 = models.IntegerField(blank=True, null=False, default=0)
    d23 = models.IntegerField(blank=True, null=False, default=0)
    d24 = models.IntegerField(blank=True, null=False, default=0)
    d25 = models.IntegerField(blank=True, null=False, default=0)
    d26 = models.IntegerField(blank=True, null=False, default=0)
    d27 = models.IntegerField(blank=True, null=False, default=0)
    d28 = models.IntegerField(blank=True, null=False, default=0)
    d29 = models.IntegerField(blank=True, null=False, default=0)
    d30 = models.IntegerField(blank=True, null=False, default=0)
    d31 = models.IntegerField(blank=True, null=False, default=0)

    def __init__(self):
        return self.specification


class Subject(models.Model):
    name = models.CharField(max_length=50)
    number_credits = models.IntegerField()

    def __init__(self):
        return u'{}'.format(self.name)

class Student(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subject_student = models.ManyToManyField(Subject)

    def full_name(self):
        return u'{} {}'.format(self.name, self.last_name)

    class Mets:
        permissions = (
            ('is_teacher', _('Is Teacher')),
            ('is_student', _('Is Student')),
        )


class Log(models.Model):
    pass


class Count(models.Model):
    pass


class Category(models.Model):
    category = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.category


class ProductionActual(models.Model):
    # pk = models.AutoField()
    ppk = models.IntegerField(db_column='Ppk', blank=True, null=True)
    productionactualno = models.CharField(db_column='ProductionActualNo', primary_key=True, max_length=100)  # Field name made lowercase.
    lotno = models.CharField(db_column='LotNo', max_length=100)  # Field name made lowercase.
    revision = models.CharField(db_column='Revision', max_length=10)  # Field name made lowercase.
    workdate = models.DateTimeField(db_column='WorkDate')  # Field name made lowercase.
    # workdate = models.DateField(db_column='WorkDate')  # Field name made lowercase.
    workfrom = models.DateTimeField(db_column='Workfrom', blank=True, null=True)  # Field name made lowercase.
    workto = models.DateTimeField(blank=True, null=True)
    code = models.CharField(db_column='Code', max_length=100)  # Field name made lowercase.
    costcenter = models.CharField(db_column='CostCenter', max_length=10)  # Field name made lowercase.
    workcenter = models.CharField(db_column='WorkCenter', max_length=10)  # Field name made lowercase.
    machine = models.CharField(db_column='Machine', max_length=10)  # Field name made lowercase.
    groups = models.CharField(db_column='Groups', max_length=10)  # Field name made lowercase.
    facode = models.CharField(db_column='FACode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    producingorderno = models.CharField(db_column='ProducingOrderNo', max_length=100)  # Field name made lowercase.
    mp = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    ma = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    producingorder = models.DecimalField(db_column='ProducingOrder', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ap = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    aa = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    produced = models.DecimalField(db_column='Produced', max_digits=18, decimal_places=4)  # Field name made lowercase.
    beginninging = models.DecimalField(db_column='BeginningING', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    beginningstk = models.DecimalField(db_column='BeginningSTK', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    outgoingno = models.CharField(db_column='OutgoingNo', max_length=16, blank=True, null=True)  # Field name made lowercase.
    outgoing = models.DecimalField(db_column='Outgoing', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    spqty = models.DecimalField(db_column='SPQty', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    daywork = models.DecimalField(db_column='Daywork', max_digits=18, decimal_places=4)  # Field name made lowercase.
    daynight = models.CharField(db_column='DayNight', max_length=1)  # Field name made lowercase.
    incominglocation = models.IntegerField(db_column='IncomingLocation', blank=True, null=True)  # Field name made lowercase.
    incomingqty = models.DecimalField(db_column='IncomingQTY', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    goodness = models.DecimalField(db_column='Goodness', max_digits=18, decimal_places=4)  # Field name made lowercase.
    badness = models.DecimalField(db_column='Badness', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    badnessid = models.CharField(db_column='BadnessID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    badnesspro = models.DecimalField(db_column='BadnessPro', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    saleslocal = models.DecimalField(db_column='SalesLocal', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    salesexport = models.DecimalField(db_column='SalesExport', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    outgoinglocation = models.IntegerField(db_column='OutgoingLocation', blank=True, null=True)  # Field name made lowercase.
    outgoingqty = models.DecimalField(db_column='OutgoingQTY', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    outgoingsupplier = models.DecimalField(db_column='OutgoingSupplier', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rnd = models.DecimalField(db_column='RnD', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    iqc = models.DecimalField(db_column='IQC', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    afterservice = models.DecimalField(db_column='AfterService', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sample = models.DecimalField(db_column='Sample', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    disuse = models.DecimalField(db_column='Disuse', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    controlstock = models.DecimalField(db_column='ControlStock', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    movelocation = models.IntegerField(db_column='MoveLocation', blank=True, null=True)  # Field name made lowercase.
    movelocationqty = models.DecimalField(db_column='MoveLocationQty', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    finaling = models.DecimalField(db_column='FinalING', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    finalstk = models.DecimalField(db_column='FinalSTK', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    measuresqty = models.DecimalField(db_column='MeasuresQty', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    s_date = models.CharField(max_length=10)
    rateproduced = models.DecimalField(db_column='RateProduced', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    analysiscode = models.IntegerField(db_column='AnalysisCode', blank=True, null=True)  # Field name made lowercase.
    worker = models.DecimalField(max_digits=18, decimal_places=0)
    # id = models.CharField(max_length=50)
    sdmcperunit = models.DecimalField(db_column='SDMCPerUnit', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    admcperunit = models.DecimalField(db_column='ADMCPerUnit', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sdmc = models.DecimalField(db_column='SDMC', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    admc = models.DecimalField(db_column='ADMC', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qcdate = models.DateTimeField(db_column='QCDate', blank=True, null=True)  # Field name made lowercase.
    firstmodified = models.DateTimeField(db_column='FirstModified', blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
    modified = models.IntegerField(db_column='Modified', blank=True, null=True)  # Field name made lowercase.
    location = models.IntegerField(db_column='Location', blank=True, null=True)  # Field name made lowercase.
    outsourcingrecoveryno = models.CharField(db_column='OutsourcingRecoveryNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    incomingwarehouse = models.CharField(db_column='IncomingWarehouse', max_length=20, blank=True, null=True)  # Field name made lowercase.
    outgoingwarehouse = models.CharField(db_column='OutgoingWarehouse', max_length=20, blank=True, null=True)  # Field name made lowercase.
    movingwarehouse = models.CharField(db_column='MovingWarehouse', max_length=20, blank=True, null=True)  # Field name made lowercase.
    movingqty = models.DecimalField(db_column='MovingQty', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    requiredmeasured = models.DecimalField(db_column='RequiredMeasured', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    suboutgoingno = models.DecimalField(db_column='SubOutgoingNo', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    suboutgoing = models.DecimalField(db_column='SubOutgoing', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dischargeing = models.DecimalField(db_column='DischargeIng', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    badnessweightsuming = models.DecimalField(db_column='BadnessWeightSumIng', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    badnessqtying = models.DecimalField(db_column='BadnessQtyIng', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    badnessweighting = models.DecimalField(db_column='BadnessWeightIng', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    testqtying = models.DecimalField(db_column='TestQtyIng', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    testweighting = models.DecimalField(db_column='TestWeightIng', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    scrapweightuniting = models.DecimalField(db_column='ScrapWeightUnitIng', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    scrapweightsuming = models.DecimalField(db_column='ScrapWeightSumIng', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    requiredstandard = models.DecimalField(db_column='RequiredStandard', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    requiredtolerance = models.DecimalField(db_column='RequiredTolerance', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PRODUCTIONACTUAL'



# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models


class Asking(models.Model):
    # pk = models.CharField(primary_key=True, max_length=12)
    askingno = models.CharField(db_column='AskingNo', max_length=12, blank=True, null=True)  # Field name made lowercase.
    askingdate = models.DateTimeField(db_column='AskingDate', blank=True, null=True)  # Field name made lowercase.
    askinguserid = models.CharField(db_column='AskingUserId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    askingwarehouse = models.IntegerField(db_column='AskingWarehouse', blank=True, null=True)  # Field name made lowercase.
    movingwarehouse = models.IntegerField(db_column='MovingWarehouse', blank=True, null=True)  # Field name made lowercase.
    confirmstatus = models.IntegerField(db_column='ConfirmStatus', blank=True, null=True)  # Field name made lowercase.
    confirmdate = models.DateTimeField(db_column='ConfirmDate', blank=True, null=True)  # Field name made lowercase.
    confirmuserid = models.CharField(db_column='ConfirmUserId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    approvalex = models.CharField(db_column='ApprovalEx', max_length=10, blank=True, null=True)  # Field name made lowercase.
    approvalfi = models.CharField(db_column='ApprovalFi', max_length=10, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ASKING'


class Askingdata(models.Model):
    # pk = models.CharField(primary_key=True, max_length=16)
    askingno = models.CharField(db_column='AskingNo', max_length=12, blank=True, null=True)  # Field name made lowercase.
    askingwarehouse = models.IntegerField(db_column='AskingWarehouse', blank=True, null=True)  # Field name made lowercase.
    movingwarehouse = models.IntegerField(db_column='MovingWarehouse', blank=True, null=True)  # Field name made lowercase.
    confirmstatus = models.IntegerField(db_column='ConfirmStatus', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(max_length=20, blank=True, null=True)
    description = models.IntegerField(blank=True, null=True)
    steps = models.CharField(max_length=100, blank=True, null=True)
    askingqty = models.DecimalField(db_column='AskingQty', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    stock = models.DecimalField(db_column='Stock', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    movingqty = models.DecimalField(db_column='MovingQty', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    shortage = models.DecimalField(db_column='Shortage', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ASKINGDATA'


class Analysiscode(models.Model):
    language1 = models.CharField(max_length=50, blank=True, null=True)
    language2 = models.CharField(max_length=50, blank=True, null=True)
    language3 = models.CharField(max_length=50, blank=True, null=True)
    language4 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'AnalysisCode'


class Approvalhistoryasking(models.Model):
    iid = models.AutoField(primary_key=True)
    o_id = models.CharField(max_length=20, blank=True, null=True)
    id = models.CharField(max_length=20)
    cs = models.IntegerField(blank=True, null=True)
    language1 = models.CharField(max_length=50, blank=True, null=True)
    language2 = models.CharField(max_length=50, blank=True, null=True)
    language3 = models.CharField(max_length=50, blank=True, null=True)
    language4 = models.CharField(max_length=50, blank=True, null=True)
    responsibilities1 = models.CharField(max_length=50, blank=True, null=True)
    responsibilities2 = models.CharField(max_length=50, blank=True, null=True)
    responsibilities3 = models.CharField(max_length=50, blank=True, null=True)
    responsibilities4 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ApprovalHistoryAsking'


class Approvalline(models.Model):
    # pk = models.AutoField(primary_key=True)
    rqtano = models.CharField(db_column='RqtANo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    approvalcount = models.IntegerField(db_column='ApprovalCount', blank=True, null=True)  # Field name made lowercase.
    approvalcurrent = models.IntegerField(db_column='ApprovalCurrent', blank=True, null=True)  # Field name made lowercase.
    approvalid1 = models.CharField(db_column='ApprovalId1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    approvalid2 = models.CharField(db_column='ApprovalId2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    approvalid3 = models.CharField(db_column='ApprovalId3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    approvalid4 = models.CharField(db_column='ApprovalId4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    approvalid5 = models.CharField(db_column='ApprovalId5', max_length=20, blank=True, null=True)  # Field name made lowercase.
    approvalid6 = models.CharField(db_column='ApprovalId6', max_length=20, blank=True, null=True)  # Field name made lowercase.
    approvalid7 = models.CharField(db_column='ApprovalId7', max_length=20, blank=True, null=True)  # Field name made lowercase.
    approvalid8 = models.CharField(db_column='ApprovalId8', max_length=20, blank=True, null=True)  # Field name made lowercase.
    approvalid9 = models.CharField(db_column='ApprovalId9', max_length=20, blank=True, null=True)  # Field name made lowercase.
    approvalornot1 = models.CharField(db_column='ApprovalOrNot1', max_length=1, blank=True, null=True)  # Field name made lowercase.
    approvalornot2 = models.CharField(db_column='ApprovalOrNot2', max_length=1, blank=True, null=True)  # Field name made lowercase.
    approvalornot3 = models.CharField(db_column='ApprovalOrNot3', max_length=1, blank=True, null=True)  # Field name made lowercase.
    approvalornot4 = models.CharField(db_column='ApprovalOrNot4', max_length=1, blank=True, null=True)  # Field name made lowercase.
    approvalornot5 = models.CharField(db_column='ApprovalOrNot5', max_length=1, blank=True, null=True)  # Field name made lowercase.
    approvalornot6 = models.CharField(db_column='ApprovalOrNot6', max_length=1, blank=True, null=True)  # Field name made lowercase.
    approvalornot7 = models.CharField(db_column='ApprovalOrNot7', max_length=1, blank=True, null=True)  # Field name made lowercase.
    approvalornot8 = models.CharField(db_column='ApprovalOrNot8', max_length=1, blank=True, null=True)  # Field name made lowercase.
    approvalornot9 = models.CharField(db_column='ApprovalOrNot9', max_length=1, blank=True, null=True)  # Field name made lowercase.
    approvaldate1 = models.DateTimeField(db_column='ApprovalDate1', blank=True, null=True)  # Field name made lowercase.
    approvaldate2 = models.DateTimeField(db_column='ApprovalDate2', blank=True, null=True)  # Field name made lowercase.
    approvaldate3 = models.DateTimeField(db_column='ApprovalDate3', blank=True, null=True)  # Field name made lowercase.
    approvaldate4 = models.DateTimeField(db_column='ApprovalDate4', blank=True, null=True)  # Field name made lowercase.
    approvaldate5 = models.DateTimeField(db_column='ApprovalDate5', blank=True, null=True)  # Field name made lowercase.
    approvaldate6 = models.DateTimeField(db_column='ApprovalDate6', blank=True, null=True)  # Field name made lowercase.
    approvaldate7 = models.DateTimeField(db_column='ApprovalDate7', blank=True, null=True)  # Field name made lowercase.
    approvaldate8 = models.DateTimeField(db_column='ApprovalDate8', blank=True, null=True)  # Field name made lowercase.
    approvaldate9 = models.DateTimeField(db_column='ApprovalDate9', blank=True, null=True)  # Field name made lowercase.
    confirmcount = models.IntegerField(db_column='ConfirmCount', blank=True, null=True)  # Field name made lowercase.
    confirmcurrent = models.IntegerField(db_column='ConfirmCurrent', blank=True, null=True)  # Field name made lowercase.
    confirmid1 = models.CharField(db_column='ConfirmId1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    confirmid2 = models.CharField(db_column='ConfirmId2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    confirmid3 = models.CharField(db_column='ConfirmId3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    confirmid4 = models.CharField(db_column='ConfirmId4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    confirmid5 = models.CharField(db_column='ConfirmId5', max_length=20, blank=True, null=True)  # Field name made lowercase.
    confirmid6 = models.CharField(db_column='ConfirmId6', max_length=20, blank=True, null=True)  # Field name made lowercase.
    confirmid7 = models.CharField(db_column='ConfirmId7', max_length=20, blank=True, null=True)  # Field name made lowercase.
    confirmid8 = models.CharField(db_column='ConfirmId8', max_length=20, blank=True, null=True)  # Field name made lowercase.
    confirmid9 = models.CharField(db_column='ConfirmId9', max_length=20, blank=True, null=True)  # Field name made lowercase.
    confirmornot1 = models.CharField(db_column='ConfirmOrNot1', max_length=1, blank=True, null=True)  # Field name made lowercase.
    confirmornot2 = models.CharField(db_column='ConfirmOrNot2', max_length=1, blank=True, null=True)  # Field name made lowercase.
    confirmornot3 = models.CharField(db_column='ConfirmOrNot3', max_length=1, blank=True, null=True)  # Field name made lowercase.
    confirmornot4 = models.CharField(db_column='ConfirmOrNot4', max_length=1, blank=True, null=True)  # Field name made lowercase.
    confirmornot5 = models.CharField(db_column='ConfirmOrNot5', max_length=1, blank=True, null=True)  # Field name made lowercase.
    confirmornot6 = models.CharField(db_column='ConfirmOrNot6', max_length=1, blank=True, null=True)  # Field name made lowercase.
    confirmornot7 = models.CharField(db_column='ConfirmOrNot7', max_length=1, blank=True, null=True)  # Field name made lowercase.
    confirmornot8 = models.CharField(db_column='ConfirmOrNot8', max_length=1, blank=True, null=True)  # Field name made lowercase.
    confirmornot9 = models.CharField(db_column='ConfirmOrNot9', max_length=1, blank=True, null=True)  # Field name made lowercase.
    confirmdate1 = models.DateTimeField(db_column='ConfirmDate1', blank=True, null=True)  # Field name made lowercase.
    confirmdate2 = models.DateTimeField(db_column='ConfirmDate2', blank=True, null=True)  # Field name made lowercase.
    confirmdate3 = models.DateTimeField(db_column='ConfirmDate3', blank=True, null=True)  # Field name made lowercase.
    confirmdate4 = models.DateTimeField(db_column='ConfirmDate4', blank=True, null=True)  # Field name made lowercase.
    confirmdate5 = models.DateTimeField(db_column='ConfirmDate5', blank=True, null=True)  # Field name made lowercase.
    confirmdate6 = models.DateTimeField(db_column='ConfirmDate6', blank=True, null=True)  # Field name made lowercase.
    confirmdate7 = models.DateTimeField(db_column='ConfirmDate7', blank=True, null=True)  # Field name made lowercase.
    confirmdate8 = models.DateTimeField(db_column='ConfirmDate8', blank=True, null=True)  # Field name made lowercase.
    confirmdate9 = models.DateTimeField(db_column='ConfirmDate9', blank=True, null=True)  # Field name made lowercase.
    autoslip = models.CharField(max_length=1, blank=True, null=True)
    approvalname1 = models.CharField(db_column='ApprovalName1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    approvalname2 = models.CharField(db_column='ApprovalName2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    approvalname3 = models.CharField(db_column='ApprovalName3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    approvalname4 = models.CharField(db_column='ApprovalName4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    approvalname5 = models.CharField(db_column='ApprovalName5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    approvalname6 = models.CharField(db_column='ApprovalName6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    approvalname7 = models.CharField(db_column='ApprovalName7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    approvalname8 = models.CharField(db_column='ApprovalName8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    approvalname9 = models.CharField(db_column='ApprovalName9', max_length=50, blank=True, null=True)  # Field name made lowercase.
    confirmname1 = models.CharField(db_column='ConfirmName1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    confirmname2 = models.CharField(db_column='ConfirmName2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    confirmname3 = models.CharField(db_column='ConfirmName3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    confirmname4 = models.CharField(db_column='ConfirmName4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    confirmname5 = models.CharField(db_column='ConfirmName5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    confirmname6 = models.CharField(db_column='ConfirmName6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    confirmname7 = models.CharField(db_column='ConfirmName7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    confirmname8 = models.CharField(db_column='ConfirmName8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    confirmname9 = models.CharField(db_column='ConfirmName9', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True  # False
        db_table = 'ApprovalLine'


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Process(models.Model):
    # id = models.AutoField()
    code = models.CharField(db_column='Code', primary_key=True, max_length=20)  # Field name made lowercase.
    language1 = models.CharField(db_column='Language1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    language2 = models.CharField(db_column='Language2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    language3 = models.CharField(db_column='Language3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    language4 = models.CharField(db_column='Language4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    appliedstandard = models.CharField(db_column='AppliedStandard', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nextprocessst = models.CharField(db_column='NextProcessSt', max_length=1, blank=True, null=True)  # Field name made lowercase.
    skipvalue = models.CharField(db_column='SkipValue', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lotnobase = models.CharField(db_column='LotNoBase', max_length=1, blank=True, null=True)  # Field name made lowercase.
    registrationdate = models.DateTimeField(db_column='RegistrationDate')  # Field name made lowercase.
    registrationusercode = models.CharField(db_column='RegistrationUserCode', max_length=20)  # Field name made lowercase.
    obsoletecode = models.CharField(db_column='ObsoleteCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    previousprocess = models.CharField(db_column='PreviousProcess', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nextprocess = models.CharField(db_column='NextProcess', max_length=10, blank=True, null=True)  # Field name made lowercase.
    processsuperior = models.CharField(db_column='ProcessSuperior', max_length=10)  # Field name made lowercase.
    followupprocess = models.CharField(db_column='FollowUpProcess', max_length=10, blank=True, null=True)  # Field name made lowercase.
    leadtime = models.DecimalField(db_column='LeadTime', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    workingorderkey = models.CharField(db_column='WorkingOrderKey', max_length=1)  # Field name made lowercase.
    dayworklimitst = models.CharField(db_column='DayworkLimitSt', max_length=1)  # Field name made lowercase.
    beinuse = models.IntegerField(db_column='BeInUse')  # Field name made lowercase.
    warehousest = models.CharField(db_column='WarehouseSt', max_length=20)  # Field name made lowercase.
    colorst = models.CharField(db_column='ColorSt', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PROCESS'
        unique_together = (('code', 'processsuperior'),)


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )
    name = models.CharField(max_length=100)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)  # *** 반드시 여기 라인 위쪽에, [Tag] class가 있어야 한다...

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivery', 'Delivery'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)


class GoodsMaster(models.Model):
    # id = models.AutoField(db_column='ID')  # Field name made lowercase.
    code = models.CharField(db_column='Code', primary_key=True, max_length=20)  # Field name made lowercase.
    revisiondate = models.DateTimeField(db_column='RevisionDate', blank=True, null=True)  # Field name made lowercase.
    revisionmathercode = models.IntegerField(db_column='RevisionMatherCode', blank=True, null=True)  # Field name made lowercase.
    partno = models.CharField(db_column='PartNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    goods = models.CharField(db_column='Goods', max_length=100, blank=True, null=True)  # Field name made lowercase.
    goodsassets = models.IntegerField(db_column='GoodsAssets', blank=True, null=True)  # Field name made lowercase.
    goods0 = models.IntegerField(db_column='Goods0', blank=True, null=True)  # Field name made lowercase.
    goods1 = models.IntegerField(db_column='Goods1', blank=True, null=True)  # Field name made lowercase.
    goods2 = models.IntegerField(db_column='Goods2', blank=True, null=True)  # Field name made lowercase.
    goods3 = models.IntegerField(db_column='Goods3', blank=True, null=True)  # Field name made lowercase.
    goods4 = models.IntegerField(db_column='Goods4', blank=True, null=True)  # Field name made lowercase.
    goods5 = models.IntegerField(db_column='Goods5', blank=True, null=True)  # Field name made lowercase.
    description = models.IntegerField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    step1 = models.CharField(db_column='Step1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    step2 = models.CharField(db_column='Step2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    step3 = models.CharField(db_column='Step3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    step4 = models.CharField(db_column='Step4', max_length=50, blank=True, null=True)  # Field name made lowercase.
    step5 = models.CharField(db_column='Step5', max_length=50, blank=True, null=True)  # Field name made lowercase.
    step6 = models.CharField(db_column='Step6', max_length=50, blank=True, null=True)  # Field name made lowercase.
    step7 = models.CharField(db_column='Step7', max_length=50, blank=True, null=True)  # Field name made lowercase.
    step8 = models.CharField(db_column='Step8', max_length=50, blank=True, null=True)  # Field name made lowercase.
    step9 = models.CharField(db_column='Step9', max_length=100, blank=True, null=True)  # Field name made lowercase.
    color = models.IntegerField(db_column='Color', blank=True, null=True)  # Field name made lowercase.
    unit = models.IntegerField(db_column='Unit', blank=True, null=True)  # Field name made lowercase.
    unit_qty = models.DecimalField(db_column='Unit_Qty', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    supplydemand = models.IntegerField(db_column='SupplyDemand', blank=True, null=True)  # Field name made lowercase.
    abolitiondate = models.DateTimeField(db_column='AbolitionDate', blank=True, null=True)  # Field name made lowercase.
    confirmdate = models.DateTimeField(db_column='ConfirmDate', blank=True, null=True)  # Field name made lowercase.
    confirmname = models.CharField(db_column='ConfirmName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    standardtime = models.DecimalField(db_column='StandardTime', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    standardinferior = models.DecimalField(db_column='StandardInferior', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    special_flag = models.CharField(max_length=10, blank=True, null=True)
    parity = models.IntegerField(db_column='Parity', blank=True, null=True)  # Field name made lowercase.
    locationposition = models.CharField(db_column='LocationPosition', max_length=10, blank=True, null=True)  # Field name made lowercase.
    markingno = models.CharField(db_column='MarkingNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    process = models.CharField(db_column='Process', max_length=20, blank=True, null=True)  # Field name made lowercase.
    codeno = models.CharField(db_column='CodeNo', max_length=20)  # Field name made lowercase.
    companyid = models.IntegerField(db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    language1 = models.CharField(db_column='Language1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    language2 = models.CharField(db_column='Language2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    language3 = models.CharField(db_column='Language3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    language4 = models.CharField(db_column='Language4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=100, blank=True, null=True)  # Field name made lowercase.
    box_qty = models.DecimalField(db_column='Box_Qty', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    safe_qty = models.DecimalField(db_column='Safe_Qty', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    safe_day = models.IntegerField(db_column='Safe_Day', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100, blank=True, null=True)  # Field name made lowercase.
    use_yn = models.CharField(db_column='Use_Yn', max_length=1, blank=True, null=True)  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='Create_Date', blank=True, null=True)  # Field name made lowercase.
    create_user_id = models.CharField(db_column='Create_User_Id', max_length=100, blank=True, null=True)  # Field name made lowercase.
    last_user_id = models.CharField(db_column='Last_User_Id', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    location = models.IntegerField(db_column='Location', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'GOODSMASTER'
