from django.urls import path
# from .views import Index
# from .views import PeriodView
from ppp import views


urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.home, name='home'),

    path('ppp_process/', views.ppp_process, name='ppp_process'),
    path('ppp_month/', views.ppp_month, name='ppp_month'),
    path('ppp_capacity/', views.ppp_capacity, name='ppp_capacity'),
    path('ppp_monitoring/', views.ppp_monitoring, name='ppp_monitoring'),
    path('ppp_current/', views.ppp_current, name='ppp_current'),

    # path('index_sudoku/', views.sudoku, name="sudoku"),

    path('productionPerformance/', views.productionPerformance, name="productionPerformance"),

    # path('', Index.as_view(), name="index"),
    # path('index/', Index.as_view(), name="index"),
    # path('index/', PeriodView.as_view(), name="period"),

    # path('period/', views.period, name='period'),
    # path('production/', views.production, name='production'),

    path('goodsmasters/', views.goodsmasters, name='goodsmasters'),
    # path('process_all/', views.process_all, name='process-all'),
    # path('process/<str:process_code>/', views.process_selected, name='process-selected'),
    # path('process/', views.process, name='process'),

    # 아래와 같이 2개 이용하는 것은, 별도 html 파일을 만들어, 그쪽으로 웹 페이지 자체가 완전히 옮겨 가는 것이다.
    # 설명하자면,
    # 1. sidebar.html 파일에서, [생산 분석-공정별 분석] 메뉴를 클릭하면, [pp-process-analysis]의 링크를 타고,
    # 2. pp_process_analysis.html 파일이 실행된다. *** pp-process-summary.html 파일은 없다는 것에 주의...
    # 3. pp_process_analysis.html 파일에서, [Chart.차트 보기] 버튼을 클릭하면, [name='pp-process-summary'] 이것의 링크를 타고
    # 4. views.pp_process_summary 함수가 실행되는 것이다.
    # 5. 만약, sidebar.html 파일에서, [생산 분석-공정별 분석] 메뉴를 클릭했을 때, 그 화면에서 바로 그라프를 뿌려주게 하려면,
    # 6. [생산 분석-공정별 분석] 메뉴 링크를 [pp-process-summary]로 직접 걸어 주고,

    # path('pp_process_summary/', views.pp_process_summary, name='pp-process-summary'),
    # path('pp_process_analysis/', views.pp_process_analysis, name='pp-process-analysis'),
    #
    # path('pp_product_summary/', views.pp_product_summary, name='pp-product-summary'),
    # path('pp_product_analysis/', views.pp_product_analysis, name='pp-product-analysis'),
]

