/*!
    * Start Bootstrap - SB Admin v6.0.2 (https://startbootstrap.com/template/sb-admin)
    * Copyright 2013-2020 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-sb-admin/blob/master/LICENSE)
    */

(function($) {
    "use strict";

    showWindow();

    // 2021.02.25 Added. 진행바 팝업창 자동 닫힘 방지.
    // $('#pleaseWaitDialog').modal({backdrop: 'static'});
    // $('#pleaseWaitDialog').modal({keyboard: false});

    // Add active state to sidbar nav links
    let path = window.location.href; // because the 'href' property of the DOM element is the absolute path
    console.log("read(function) 실행 전 path: ", path);
    let pathList = path.split("/");
    console.log("read(function) 실행 전 pathList: ", pathList);

    let pathAdded = false;
    let i = pathList.indexOf("ppp_");
    if (i > 0) {
        let pathAdded = true;
    }


    // 2021.02.06 Conclusion. 여기는 진입부 모두 실행한 후, 실행한다. 여길 먼저 실행하지 않는다는 점에 주의...
    // console.log("1111111111111js/script.js: ");
    $(document).ready(function () {

        showWindow();
        $('#wait').show();
        // alert("00showWindow() 실행???");

        // 2021.03.05 Added. NavBar에서 [시스템 제목.PSC 제조 관리] 클릭하면, 메뉴가 보이게...
        $(document).on("click", "#navBarAll", function (e) {
            e.preventDefault();
            $("body").toggleClass("sb-sidenav-toggled");

            // let ele = document.getElementById("sidebarToggle");
            // console.log("sidebarToggle 메뉴가 보입니다. ele: ", ele);
            // ele.dispatchEvent(new CustomEvent("mouseclicked"))
            // console.log("sidebarToggle 메뉴가 보입니다.");
        });

        // 2021.02.04 Conclusion. ***** 자바스크립트에서는, 달은 [0]부터 [11]까지이고, [0]이 1월임,
        // 날짜는 [1]부터 시작하는데, ***** 만약 날짜 값을 [0]을 주면, 그 달의 [마지막 날]을 돌려준다.*****
        let thisDate = new Date();
        let firstDay = 1; // 이건 이번 달, 지난 달, 다음 달 구분 없이, 무조건 [1]
        // console.log("thisDate: ", thisDate);
        let thisDateString = getYyyyMmDdMmSsToString(thisDate);
        // console.log("thisDateString: ", thisDateString);

        let nextMonth = thisDate.getMonth() + 1; // 숫자로 5, 또는 11.
        // console.log("nextMonth: ", nextMonth);
        // var firstDateNextMonth = new Date(thisDate.getFullYear(), nextMonth, firstDay); // 이런 식으로 계산할 필요가 없다.
        // console.log("firstDateNextMonth: ", firstDateNextMonth);
        let lastDateThisMonth = new Date(thisDate.getFullYear(), thisDate.getMonth(), 0); // 날짜 값을 [0]을 주면, 마지막 날짜를 돌려 준다.
        // console.log("lastDateThisMonth: ", lastDateThisMonth);
        let lastDayThisMonth = lastDateThisMonth.getDate();
        // console.log("lastDayThisMonth: ", lastDayThisMonth); // 숫자로 마지막 날짜 값을 얻는다.

        var fromDate = new Date(thisDate.getFullYear(), thisDate.getMonth(), firstDay);
        // console.log("typeof fromDate: ", typeof fromDate);
        // console.log("fromDate: ", fromDate);
        var fromDateString = getYyyyMmDdMmSsToString(fromDate);
        // console.log("typeof fromDateString: ", typeof fromDateString);
        // console.log("fromDateString: ", fromDateString);

        var toDate = thisDate;
        var toDateString = getYyyyMmDdMmSsToString(toDate); // new Date(); // 반드시 여기서 선언을 해 주어야 한다.

        fromDate = dateToYYYYMMDD(fromDate);
        toDate = dateToYYYYMMDD(toDate);
        // console.log("fromDate typeof:", typeof fromDate);
        // console.log("변환 후 fromDate 값:", fromDate);
        // console.log("변환 후 toDate 값:", toDate);

        // $("#fromDate").datepicker('setDate', fromDate); // 이건 이상하게도, 요기서는 잘 되는데, [#toDate] 세팅이 안 되네...
        // $("#fromDate").val(fromDateString); // 이번 달 1일로 세팅...                : 이것도 잘 되고...

        // 2021.02.19 Conclusion. 아래 라인을 실행하게 되면, views.py로 갔다가 올 때, 다시 초기 값으로 세팅한다.
        // document.getElementById("fromDate").value = fromDateString; // 결론적으로 이렇게 사용하기로 한다. : 이것도 잘 되고...

        fromDateString = document.getElementById("fromDate").value;
        // console.log("1일로 다시 세팅한 fromDateString 값 typeof:", typeof fromDateString);
        // console.log("시작 1일로 다시 세팅한 fromDateString 값:", fromDateString);

        // $("#toDate").datepicker('setDate', toDate); // *** 이건 정말 이상하네, [#fromDate]에서는 잘 되는데, 여기서는 안 되네...
        // $("#toDate").val(toDateString); // 이번 달 1일로 세팅...                : 이것도 잘 되고...

        // 2021.02.19 Conclusion. 아래 라인을 실행하게 되면, views.py로 갔다가 올 때, 다시 초기 값으로 세팅한다.
        // document.getElementById("toDate").value = toDateString; // 결론적으로 이렇게 사용하기로 한다. : 이것도 잘 되고...

        toDateString = document.getElementById("toDate").value;
        // console.log("오늘로 다시 세팅한 toDateString 값 typeof:", typeof toDateString);
        // console.log("시작 오늘로 다시 세팅한 toDateString 값:", toDateString);

        // let processCode = getProcess();

        // 2021.02.09 Added. [table.td.tr 행 수 또는 그 값 가져오기.
        let arrProcessCode = $("td#process-code");
        let arrProcessName = $("td#process-name");
        // console.log("시작 arrProcessCode.length: ", arrProcessCode.length);
        // console.log("시작 arrProcessName: ", arrProcessName);
        // console.log("시작 typeof arrProcessName: ", typeof arrProcessName);
        let processCode;
        // 2021.02.09 Added. 만약 2개 이상의 공정 자료가 있을 때는, 모든 공정의 자료를 가져오게 한다.
        if (arrProcessCode.length === 0 || arrProcessCode.length > 1) {
            processCode = "all";
        } else {
            $.each(arrProcessCode, function (index, item) { // ***** 여기는 로우 1개씩 그 값을 가져와서 뿌린다.***** [index]는 [0]부터 시작함에 주의...
                let itemProcessCode = $(item).text();
                if (index === 0) {
                    processCode = itemProcessCode;
                }
            });
        }
        // console.log("보낼 processCode typeof:", typeof processCode);
        // console.log("보낼 processCode: ", processCode);
        // console.log("보낼 processCode: ", processCode);


        var action = 'inactive';
        var href = this.href;
        // console.log("보낼 href: ", href);

        // alert(`111 fromDate: ${fromDate}, toDate: ${toDate}, processCode: ${processCode}, action: ${action}`);

        // function getProduction(fromDate, toDate, processCode) {
        //     $.ajax({
        //         // url: 'period/',
        //         url: 'process/' + processCode + "/",
        //         method: 'POST',
        //         data: {
        //             fromDate: fromDate,
        //             toDate: toDate,
        //             processCode: processCode
        //         },
        //         caches: false,
        //         success: function (response) {
        //             console.log("처음에 받아 온 response['productsCount']: ", response['productsCount']);
        //             action = 'inactive';
        //             $("#production-container").append(response);
        //             alert(`000 fromDate: ${fromDate}, toDate: ${toDate}, processCode: ${processCode}, action: ${action}`);
        //             alert(`response: ${response}`);
        //             // if (response == '') {
        //             //     $("#more-data").html("<button type='button' class='btn btn-info'>No Post Found</button>");
        //             //     action = 'active';
        //             // } else {
        //             //     $("more-data").html("<button type='button' class='btn btn-info'>Loading more post</button>");
        //             //     action = 'inactive';
        //             // }
        //         }
        //     })
        // }

        // // alert(`222 fromDate: ${fromDate}, toDate: ${toDate}, processCode: ${processCode}, action: ${action}`);
        // if (action == 'inactive') {
        //     action = 'active';
        //     getProduction(fromDate, toDate, processCode);
        // }



        // 2021.03.03 Added. [table.생산 실적 수량]을 [page]별로 합산. 서버에서 자료를 어떠한 형태로든 가져오면 무조건 수행...
        var ppQtyTotal = dataTableReset();
        // console.log("ppQtyTotal: ", ppQtyTotal);

        // 2021.03.03 Added. [pagination.각 페이지] 클릭했을 때, [table.생산 실적 수량]을 [page]별로 합산.
        // $("#dataTable").on("click", ".page-link", function () { 이건 안 되네...
        $(document).on("click", ".page-link", function () {
            // console.log(".page-link 클릭!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ");
            var ppQtyTotal = dataTableReset();
        });

        // 2021.03.04 Added. [table.show entries] 수량을 변경하면, 역시 [table.생산 실적 수량]을 [page]별로 합산.
        $(document).on("click", ".custom-select", function () {
            console.log(".custom-select 클릭!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ");
            var ppQtyTotal = dataTableReset();
        });

        console.log("로딩 완 디버깅 11 processTotal: ", processTotal);
        hideWindow();

    });

    $("#process-list tr").click(function () {

        // alert("50showWindow() 실행 w전");
        showWindow();
        // alert("51showWindow() 실행 후");

        var str ="";
        var tdArr = new Array();

        // 현재 클릭한 Row(<tr>)
        var tr = $(this);
        var td = tr.children();

        // tr.text()는 클릭한 Row, 즉 tr에 있는 모든 값을 가져온다.
        var trCurrent = tr.text();
        // console.log("trCurrent: ", trCurrent); // 엄청 넓은 높이로 찍어 주네...

        // 반복문으로 배열에 값을 담을 수 있다.
        td.each(function (i) {
            tdArr.push(td.eq(i).text());
        });
        // console.log("tdArr.length: ", tdArr.length); // tr 수가 아니고, td 수 임에 주의... 즉 Row 수가 아니고, 컬럼 수...
        // console.log("tdArr: ", tdArr);

        // td.eq(index)를 통해 값을 가져올 수도 있다.
        // let processCode = td.eq(0).text();
        // let processName = td.eq(1).text();

        let processCode = td.eq(0).text();
        let processName = td.eq(1).text();
        // console.log("processCode: ");
        console.log("#process-list tr processCode: ", processCode);
        // console.log("#process-list tr processName: ", processName);

        // // 이걸 따로 processInfo.html 파일로 화면에 뿌려줄 수도 있다.
        // // table 태그 바로 아래에, <div id="process-info1"></div> 와 <div id="process-info2></div> 이렇게 2개의 <div> 태그를 두고...
        // str += "* 클릭한 Row tr 값 = No. : <font color='red'>" + no + "</font>" +
        //     ", 코드 : <font color='red'>" + processCode + "</font>" +
        //     ", 공정 : <font color='red'>" + processName + "</font>";
        // $("#process-info1").html("* 클릭한 Row의 모든 공정 데이터 = " + tr.text());
        // $("#process-info2").html(str);

        var fromDate = $("input#fromDate").val();
        var toDate = $("input#toDate").val();
        // console.log("scripts.js #process-list 현재 찍혀있는 fromDate: ", fromDate);
        // console.log("scripts.js #process-list 현재 찍혀있는 toDate: ", toDate);
        // console.log("scripts.js #process-list 현재 찍혀있는 processCode: ", processCode);

        // 2021.02.18 Conclusion. ajax 방식이 아닌, form.submit 방식으로 3개 파라미터 값을 서버로 넘긴다.
        // let path;
        // let pathCurrent = window.location.href; // because the 'href' property of the DOM element is the absolute path
        // if (pathCurrent.indexOf("index")) {
        //     path = '/'
        // } else {
        //     path = "index/";
        // }
        if (pathAdded) {
            let path = "/";
        } else {
            let path = "ppp_process/";
        }
        // let path = "ppp_process/";
        let params = {"fromDate": fromDate, "toDate": toDate, "processCode": processCode};
        let method = "POST";

        showWindow();
        sendPost(path, params, method);
        // alert("55showWindow() 실행???");

        // progressPopup2();

        // // 2021.03.03 Added. [table.생산 실적 수량]을 [page]별로 합산 : 여기 찍으면, 찍은 후에 다시 지워지네...
        // var ppQtyTotal = dataTableReset();
        // console.log("ppQtyTotal: ", ppQtyTotal);

        console.log("로딩 완 디버깅 22 processTotal: ", processTotal);
        //hideWindow();

    });

    /*
        * 달력 생성기
        * @param sDate 파라미터만 넣으면 1개짜리 달력 생성
        * @example   datePickerSet($("#datepicker"));
        *
        *
        * @param sDate,
        * @param eDate 2개 넣으면 연결달력 생성되어 서로의 날짜를 넘어가지 않음
        * @example   datePickerSet($("#datepicker1"), $("#datepicker2"));
        */

    let rangeDate = 366; // set limit day
    let period;
    let setSdate, setEdate;
    let lang;

    if (languageNo === 1042) {
        lang = 'ko';
    } else if (languageNo === 1033) {
        lang = 'en';
    } else {
        lang = 'cs';
    }
    console.log("languageNo: ", languageNo);
    console.log("lang: ", lang);
    datePickerSet($("#fromDate"), $("#toDate"), true); //다중은 시작하는 달력 먼저, 끝달력 2번째

    function datePickerSet(sDate, eDate, flag) {

        //시작 ~ 종료 2개 짜리 달력 datepicker
        if (!isValidStr(sDate) && !isValidStr(eDate) && sDate.length > 0 && eDate.length > 0) {
            var sDay = sDate.val();
            var eDay = eDate.val();

            if (flag && !isValidStr(sDay) && !isValidStr(eDay)) { //처음 입력 날짜 설정, update...
                var sdp = sDate.datepicker().data("datepicker");
                sdp.selectDate(new Date(sDay.replace(/-/g, "/")));  //익스에서는 그냥 new Date하면 -을 인식못함 replace필요

                var edp = eDate.datepicker().data("datepicker");
                edp.selectDate(new Date(eDay.replace(/-/g, "/")));  //익스에서는 그냥 new Date하면 -을 인식못함 replace필요
            }

            //시작일자 세팅하기 날짜가 없는경우엔 제한을 걸지 않음
            if (!isValidStr(eDay)) {
                sDate.datepicker({
                    maxDate: new Date(eDay.replace(/-/g, "/"))
                });
            }
            sDate.datepicker({
                language: lang, //'ko',
                autoClose: true,
                onSelect: function () {
                    datePickerSet(sDate, eDate);
                }
            });

            //종료일자 세팅하기 날짜가 없는경우엔 제한을 걸지 않음
            if (!isValidStr(sDay)) {
                eDate.datepicker({
                    minDate: new Date(sDay.replace(/-/g, "/"))
                });
            }
            eDate.datepicker({
                language: lang, //'ko',
                autoClose: true,
                onSelect: function () {
                    datePickerSet(sDate, eDate);
                }
            });

            //한개짜리 달력 datepicker
        } else if (!isValidStr(sDate)) {
            var sDay = sDate.val();
            if (flag && !isValidStr(sDay)) { //처음 입력 날짜 설정, update...
                var sdp = sDate.datepicker().data("datepicker");
                sdp.selectDate(new Date(sDay.replace(/-/g, "/"))); //익스에서는 그냥 new Date하면 -을 인식못함 replace필요
            }

            sDate.datepicker({
                language: lang, //'ko',
                autoClose: true
            });
        }


        function isValidStr(str) {
            if (str == null || str == undefined || str == "")
                return true;
            else
                return false;
        }
    }


    $("#period").on("click", function (e) {

        showWindow();
        // alert("70showWindow() 실행???");

        if ($('input#fromDate').val() === '') {
            alert("기간 시작일을 입력하시요!");
            $('input#fromDate').focus();
            return false;
        } else if ($('input#toDate').val() === '') {
            alert("기간 종료일을 입력하시오!");
            $('input#toDate').focus();
            return false;
        }
        // 위의 공백 확인을 이렇게도 할 수 있다. 위도 실행하고 여기도 실행해도 상관없고...
        if (!$('input#fromDate').val() || !$('input#toDate').val()) {
            alert("기간을 확인하시오!");
            $('input#fromDate').focus();
            return false;
        }

        // let processSelected = $('a#processSelected');
        let fromDateString = $('input#fromDate').val().split("-");
        let toDateString = $('input#toDate').val().split("-");
        // fromDateString = document.getElementById("fromDate").innerText;
        // toDateString = document.getElementById("toDate").innerText;

        let fromDate = new Date(fromDateString[0], fromDateString[1] - 1, fromDateString[2]);
        let toDate = new Date(toDateString[0], toDateString[1] - 1, toDateString[2]);
        let diff = toDate - fromDate;
        let currDay = 24 * 60 * 60 * 1000;
        let diffDay = diff / (24 * 60 * 60 * 1000);
        diffDay = Math.floor(diffDay);

        // console.log("typeof fromDate: ", typeof fromDate);
        // console.log("typeof toDate: ", typeof toDate);
        // console.log("typeof diff: ", typeof diff);
        // console.log("typeof currDay: ", typeof currDay);
        // console.log("fromDate: ", fromDate);
        // console.log("toDate: ", toDate);
        // console.log("diff: ", diff);
        // console.log("currDay: ", currDay);

        // 년도, 월도, 날짜, 요일 뽑아내기
        let year = fromDate.getFullYear();
        let month = fromDate.getMonth();
        let date = fromDate.getDate();
        let day = fromDate.getDay();

        let fromDateThis = fromDate.getDate();
        let toDateThis = toDate.getDate();

        // alert("#period 333");

        // if (Date.parse(diff / currDay) > rangeDate) {
        //     console.log("Date.parse(diff / currDay): ", Date.parse(diff / currDay));
        if (diffDay > rangeDate) {
            console.log("rangeDate: ", rangeDate);
            console.log("diffDay: ", diffDay);
            alert(`조회 기간 ${diffDay}일은 ${rangeDate}일을 초과할 수 없습니다. 기간을 다시 확인하시오!`);
            return false;
        } else {
            fromDate = $("input#fromDate").val();
            toDate = $("input#toDate").val();
            console.log("scripts.js #period onClick else fromDate: ", fromDate);
            console.log("scripts.js #period onClick else toDate: ", toDate);

            // var processCode = getProcess();

            var processCode;
            // 2021.02.09 Added. [table.td.tr 행 수 또는 그 값 가져오기.
            // let processCode1 = $("#process-code")[0].childNodes[0].nodeValue; // 이건 첫번째 값은 가져오는데, 두번째는 에러가 나네...
            let arrProcessCode = $("td#process-code");
            console.log("arrProcessCode.length: ", arrProcessCode.length);
            // 2021.02.09 Added. 만약 2개 이상의 공정 자료가 있을 때는, 모든 공정의 자료를 가져오게 한다.
            if (arrProcessCode.length === 0 || arrProcessCode.length > 1) {
                processCode = "all";
            } else {
                $.each(arrProcessCode, function (index, item) { // ***** 여기는 로우 1개씩 그 값을 가져와서 뿌린다.***** [index]는 [0]부터 시작함에 주의...
                    let itemProcessCode = $(item).text();
                    if (index === 0) {
                        processCode = itemProcessCode;
                    }
                });
            }

        }

        console.log("scripts.js #period onClick 보내는 processCode: ", processCode);

        // 2021.02.18 Conclusion. ajax 방식이 아닌, form.submit 방식으로 3개 파라미터 값을 서버로 넘긴다.
        if (pathAdded) {
            let path = "/";
        } else {
            let path = "ppp_process/";
        }
        // let path = "ppp_process/";
        console.log("scripts.js #period onClick path: ", path);
        let params = {"fromDate": fromDate, "toDate": toDate, "processCode": processCode};
        let method = "POST";

        showWindow();
        sendPost(path, params, method);
        // alert("77showWindow() 실행???");

        // progressPopup2();

        // // 2021.03.03 Added. [table.생산 실적 수량]을 [page]별로 합산 : 여기 찍으면, 찍은 후에 다시 지워지네...
        // var ppQtyTotal = dataTableReset();
        // console.log("ppQtyTotal: ", ppQtyTotal);

        // setChart(); 2021.02.24 Conclusion. 여기서는 전체 공정 자료에 대한 그라프를 그리지 않는다.

        // var xhttp = new XMLHttpRequest();
        // var csrf_token = $('[name=csrfmiddlewaretoken]').val();
        // xhttp.open(method, path, true);
        // xhttp.setRequestHeader('X-CSRFToken', csrf_token);
        // xhttp.send(params);

    });


    // 2021.02.24 Added. 그라프 그리는 것을 통째로 함수화한다.

    // 그래프를 그린다...
    console.log("script_processCodeCurrent: ", processCodeCurrent);
    console.log("script_processCodeCurrent.length: ", processCodeCurrent.length);

    // 2021.02.24 Added. 공정이 지정이 안 되어 있어, [processCode == "all"] 이면, 그라프를 뿌리지 말자...
    // let processCode = getProcess();

    console.log("script_그라프 그리기 바로 전 processCodeCurrent: ", processCodeCurrent);

    if (processCodeCurrent === "all") {
        console.log("script_그라프를 그리는 의미가 없어 그리지 않습니다.");
    } else {
        console.log("실적 합계 찍기 전에 productsArrList.length: ", productsArrList.length);
        if (productsArrList.length > 0) {
            setChart(processCodeCurrent);
        }
    }

    // console.log("script_그라프를 그립니다. processCodeCurrent: ", processCodeCurrent);
    // $('#pleaseWaitDialog, .window').hide();
    // $('#pleaseWaitDialog').modal('hide');
    // e.target === modal ? modal.classList.remove('show-modal') : false


    // 2021.02.19 Conclusion. 아래 [path]는 맨 위로 올렸다. 전체에서 사용하기 위해...
    // Add active state to sidbar nav links
    // let path = window.location.href; // because the 'href' property of the DOM element is the absolute path
    // console.log("path: ", path);

    $("body").toggleClass("sb-sidenav-toggled");

    $("#layoutSidenav_nav .sb-sidenav a.nav-link").each(function() {

        showWindow();
        // alert("88showWindow() 실행???");

        if (this.href === path) {
            // $(this).addClass("active"); // 사이드 메뉴를 보인다???
            console.log("#layoutSidenav_nav .sb-sidenav a.nav-link.each(function() path1: ", path);
        }
        // $('#pleaseWaitDialog').modal('hide');
        // $('#pleaseWaitDialog, .window').hide();
    });

    // Toggle the side navigation
    $("#sidebarToggle").on("click", function(e) {
        e.preventDefault();
        $("body").toggleClass("sb-sidenav-toggled");
        console.log("path2: ", path);
    });

    // // 2021.02.25 Added. progressPopup1();
    // $(function () {
    //     var pleaseWait = $('#pleaseWaitDialog');
    //
    //     var showPleaseWait = function () {
    //         pleaseWait.modal('show');
    //     };
    //
    //     var hidePleaseWait = function () {
    //         pleaseWait.modal('hide');
    //     };
    //
    //     showPleaseWait();
    // });

    // 2021.02.25 Added. 진행바 팝업창 자동 닫힘 방지.
    // $('#pleaseWaitDialog').modal({backdrop: 'static'});
    // $('#pleaseWaitDialog').modal({keyboard: false});
    // e.target === modal ? modal.classList.remove('show-modal') : false
    // $('#pleaseWaitDialog, .window').hide();

})(jQuery);


















function getYyyyMmDdMmSsToString(date) {
    var dd = date.getDate();
    var mm = date.getMonth()+1; //January is 0!

    var yyyy = date.getFullYear();
    if(dd<10){dd='0'+dd} if(mm<10){mm='0'+mm}

    yyyy = yyyy.toString();
    mm = mm.toString();
    dd = dd.toString();

    var m = date.getHours();
    var s = date.getMinutes();

    if(m<10){m='0'+m} if(s<10){s='0'+s}
    m = m.toString();
    s = s.toString();

    // var s1 = yyyy+"-"+mm+"-"+dd+" "+m+":"+s;
    var s1 = yyyy+"-"+mm+"-"+dd;
    return s1;
}

//date객체 YYYY-MM-DD 변환함수
function dateToYYYYMMDD(date){
    function pad(num) {
        num = num + '';
        return num.length < 2 ? '0' + num : num;
    }
    return date.getFullYear() + '-' + pad(date.getMonth()+1) + '-' + pad(date.getDate());
}

// 2021.02.18 Conclusion. ajax 방식이 아닌, form.submit 방식으로 3개 파라미터 값을 서버로 넘긴다.
function sendPost(path, params, method) {

    // alert("sendPost 33 showWindow() 실행 전");
    showWindow();
    // alert("sendPost 33 showWindow() 실행 후");

    var form = document.createElement("form");
    form.setAttribute("method", method);
    form.setAttribute("action", path);
    for (var key in params) {
        var hiddenField = document.createElement("input");
        hiddenField.setAttribute("type", "hidden");
        hiddenField.setAttribute("name", key);
        hiddenField.setAttribute("value", params[key]);
        form.appendChild(hiddenField);
        // console.log("key: ", key);
        // console.log("value: ", params[key]);
        // console.log("hiddenField: ", hiddenField);
    }
    // var hiddenField = document.createElement("input");
    // hiddenField.setAttribute("type", "hidden");
    // hiddenField.setAttribute("name", "_csrf");
    // hiddenField.setAttribute("value", "${_csrf.token}");

    // hiddenField.setAttribute("id", "csrfToken");
    // hiddenField.setAttribute("name", "${_csrf.parameterName}");
    // hiddenField.setAttribute("value", "${_csrf.token}");

    document.body.appendChild(form);
    // alert("sendPost 44 showWindow() 실행 후");
    form.submit();
    // alert("sendPost 44 showWindow() 실행 후");

    // waitingDialog.show('Please wait',{rtl:false});
    // progressPopup1();

}

// 2021.02.24 Added. 차트 그리기 통째로 함수화...
function  setChart(processCode) {
    // var ctx = document.getElementById('myChart');
    var ctx = document.getElementById('canvas');
    Chart.defaults.global.legend.labels.usePointStyle = true;
    var defaultLegendClickHandler = Chart.defaults.global.legend.onClick;

    var config = {
        type: 'bar', //'radar',
        // data: newDataset, // 요래 하면 안되네...
        data: {
            labels: ppDataPeriodArrList,
            datasets: []
        },
        options: {
            legend: {
                position: 'top',
                // labels: {
                // fontColor: 'rgb(255, 99, 132)'
                // },
                onHover: function (event, legendItem) {
                    document.getElementById("canvas").style.cursor = 'pointer';
                },
                onClick: function (e, legendItem) {
                    var ci = this.chart;
                    var index = legendItem.datasetIndex;

                    var indexRest = index % 2; // 0: 생산 실적, 1: 생산 Volume, 2: 불량...
                    // console.log("setChart 내부 legend onClick 이벤트 index: ", index);
                    // console.log("setChart 내부 legend onClick 이벤트 length: ", length);
                    // console.log("setChart 내부 legend onClick 이벤트 legendTextCurrent: ", legendTextCurrent);
                    // console.log("setChart 내부 legend onClick 이벤트 indexRest: ", indexRest);
                    if (indexRest === 0) { // legend 2개가 한쌍으로 되었을 때, 첫번째 legend 만 클릭 이벤트 반응하게 한다.

                        // 2021.02.20 Added. legend 2개를 1개 처럼 표시한다. 만약 3개를 표시하려면, 3줄 작성한다. index + 1
                        var alreadyHidden = (ci.getDatasetMeta(index).hidden === null) ? false : ci.getDatasetMeta(index).hidden;
                        var alreadyHidden1 = (ci.getDatasetMeta(index + 1).hidden === null) ? false : ci.getDatasetMeta(index + 1).hidden;

                        ci.data.datasets.forEach(function (e, i) {
                            var meta = ci.getDatasetMeta(i);

                            if (i === index || i === index + 1) {
                                meta.hidden = null;
                                // console.log("setChart 내부 legend onClick 이벤트 현재 legend 만 뿌려 준다.");
                            } else {
                                if (!alreadyHidden) {
                                    meta.hidden = meta.hidden === null ? !meta.hidden : null;
                                    // console.log("setChart 내부 legend onClick 이벤트 모두 뿌려 준다.");
                                } else if (meta.hidden === null) {
                                    meta.hidden = true;
                                    // console.log("setChart 내부 legend onClick 이벤트 모두 숨긴다.");
                                }
                            }
                        });
                    }

                    var legendLength = ci.controller.chart.legend.legendItems.length; // 현재 legendLength...
                    // console.log("legendLength: ", legendLength);

                    // 2021.03.02 Added. 아래 [ci.update();] 명령을 수행 전에 여기서 아래 값을 불러오면, 절대 안 된다. 틀린다.
                    // if (legendLength > 0) {
                    //     var legendStatusIndex = ci.controller.chart.legend.legendItems[index].hidden; // 현재 legend 상태...
                    //     var legendStatusIndex1 = ci.controller.chart.legend.legendItems[index+1].hidden; // 현재 legend 상태...
                    //     var legendStatusFirst = ci.controller.chart.legend.legendItems[0].hidden; // 현재 legend 상태...
                    //     var legendStatusLast = ci.controller.chart.legend.legendItems[legendLength - 1].hidden; // 현재 legend 상태...
                    // }
                    // console.log("legendStatusIndex: ", legendStatusIndex);
                    // console.log("legendStatusIndex1: ", legendStatusIndex1);
                    // console.log("legendStatusFirst: ", legendStatusFirst);
                    // console.log("legendStatusLast: ", legendStatusLast);

                    // // 여기 아래가 원본임...
                    // var alreadyHidden = (ci.getDatasetMeta(index).hidden === null) ? false : ci.getDatasetMeta(index).hidden;
                    // ci.data.datasets.forEach(function (e, i) {
                    //     var meta = ci.getDatasetMeta(i);
                    //
                    //     if (i !== index) {
                    //         if (!alreadyHidden) {
                    //             meta.hidden = meta.hidden === null ? !meta.hidden : null;
                    //         } else if (meta.hidden === null) {
                    //             meta.hidden = true;
                    //         }
                    //     } else if (i === index) {
                    //         meta.hidden = null;
                    //     }
                    // });

                    ci.update();

                    // 2021.03.02 Added. 반드시 위의 [ci.update();]를 수행한 후에, 그 값을 불러와야, 그 값이 정확하다.
                    if (legendLength > 0) {
                        var legendStatusIndex = ci.controller.chart.legend.legendItems[index].hidden; // 현재 legend 상태...
                        var legendStatusIndex1 = ci.controller.chart.legend.legendItems[index+1].hidden; // 현재 legend 상태...
                        var legendStatusFirst = ci.controller.chart.legend.legendItems[0].hidden; // 현재 legend 상태...
                        var legendStatusLast = ci.controller.chart.legend.legendItems[legendLength - 1].hidden; // 현재 legend 상태...
                    }
                    // console.log("legendStatusIndex: ", legendStatusIndex);
                    // console.log("legendStatusIndex1: ", legendStatusIndex1);
                    // console.log("legendStatusFirst: ", legendStatusFirst);
                    // console.log("legendStatusLast: ", legendStatusLast);

                    // 2021.03.02 Added. 클릭한 legend 값을, 아래 table.표의 Search: 텍스트에 찍어준다. 1개라도 [true]이면.
                    // 위의 legendStatus... 개 모두가 [false]이면, Search: 텍스트를 모두 지운다.
                    // var legendTextCurrentTemp = ci.getDatasetMeta(index).controller.chart.legend.legendItems[index].text;
                    var legendTextCurrent = ci.controller.chart.legend.legendItems[index].text; // 위의 라인과 같은 값...
                    // console.log("legendTextCurrent: ", legendTextCurrent);
                    // legendTextCurrent = legendTextCurrent.substring(1,9);
                    // var temIndex = legendTextCurrent.indexOf(" "); // 첫번째 [공백]까지는 [차종명]이고, 그 이후부터 [Code.품번] 열자리인데, 문제는 <table>에는 [12345-67890], 이런식으로 중간에 [-]가 있다.
                    // temIndex = temIndex + 5; // 그러므로 [코드] 중에서, [앞 5 자리]까지만 담는다. ===> 아니다. [-]만 없앤다.
                    // legendTextCurrent = legendTextCurrent.substring(1, temIndex); // 첫문자가 작은 따옴표['] 임에 주의... ===> 아니다. [-]만 없앤다.
                    legendTextCurrent = legendTextCurrent.replace(/-/g,""); // 그러므로 [코드] 중에서, [앞 5 자리]까지만 담는다. ===> 아니다. [-]만 없앤다.
                    legendTextCurrent = legendTextCurrent.substring(1); // 첫문자가 작은 따옴표['] 임에 주의... ===> 아니다. [-]만 없앤다.
                    console.log("legendTextCurrent: ", legendTextCurrent);

                    // var searchCurrent = $('.form-control form-control-sm').val();
                    var searchCurrent =  document.getElementById('dataTable_filter').getElementsByClassName('form-control')[0];
                    // console.log("searchCurrent: ", searchCurrent);

                    // var searchCurrentValue =  document.getElementById('dataTable_filter').getElementsByClassName('form-control')[0].val();
                    var searchCurrentValue =  document.getElementById('dataTable_filter').getElementsByClassName('form-control')[0].value;
                    // console.log("전 searchCurrentValue: ", searchCurrentValue);

                    if (legendStatusIndex || legendStatusIndex1 || legendStatusFirst || legendStatusLast) {
                        document.getElementById('dataTable_filter').getElementsByClassName('form-control')[0].value = legendTextCurrent;
                        var searchCurrentValue =  document.getElementById('dataTable_filter').getElementsByClassName('form-control')[0].value;
                        // console.log("후 searchCurrentValue: ", searchCurrentValue);
                    } else {
                        legendTextCurrent = "";
                        document.getElementById('dataTable_filter').getElementsByClassName('form-control')[0].value = legendTextCurrent;
                        var searchCurrentValue =  document.getElementById('dataTable_filter').getElementsByClassName('form-control')[0].value;
                        // console.log("후 빈칸 searchCurrentValue: ", searchCurrentValue);
                    }

                    let ele = document.getElementById('dataTable_filter').getElementsByClassName('form-control')[0];
                    // console.log("ele: ", ele);

                    // 2021.03.03 Conclusion. 아래와 2줄로 이벤트를 트리거 할 수 있는데,
                    // 더 정확한 방법은, 현재 사용하고 있는 CustomEvent()를 사용하는 것이다.
                    // let event = new Event("keyup");
                    // document.getElementById('dataTable_filter').getElementsByClassName('form-control')[0].dispatchEvent(event);

                    // ele.addEventListener("keyup", function (event) { alert(event.detail.name); });
                    ele.dispatchEvent(new CustomEvent("keyup", {detail: {name: legendTextCurrent}}));


                    // 2021.03.03 Added. [table.생산 실적 수량]을 [page]별로 합산.
                    var ppQtyTotal = dataTableReset();
                    // console.log("ppQtyTotal: ", ppQtyTotal);

                },
            },
            tooltips: {
                custom: function (tooltip) {
                    if (!tooltip.opacity) {
                        document.getElementById("canvas").style.cursor = 'default';
                        return;
                    }
                }
            },
            title: {
                // display: true,
                // text: 'Chart.js Radar Chart'
            },
            // 여기 아래 [scale] [radar] 그라프에서만 사용하는 options 임에 주의.
            // scale: {
            //     ticks: {
            //         beginAtZero: true
            //     }
            // }
        }
    };

    window.onload = function () {
        window.myChart = new Chart(document.getElementById("canvas"), config);
    };

    // 2021.02.24 Conclusion. 차트를 3단계로 나눠서,
    // 1. 차트의 [config]를 1차 구정하고,
    // 2. window.myChart = new Chart()로 그리고,
    // 3. dynamic하게 동적으로 진행하는 것들을 아래와 같이 push 한다.
    // 4. 추가로 더 할 것들은, myChart.update() 해 준다.

    // 데이터셋 세팅 : ppDataPeriodArr.length
    // console.log("graphData.length: ", graphData.length);
    // console.log("graphData2.length: ", graphData2.length);
    // console.log("graphData.length * 2: ", graphData.length * 2);
    let j = 0;
    let k = 0;
    for (let i = 0; i < (graphData.length * 2); i++) {
        // backgroundColor: color(chartColors.red).alpha(0.2).rgbString(),
        // borderColor: chartColors.red,
        // pointBackgroundColor: chartColors.red,
        //console.log(`80: ${color1} ${color2} ${color3}`)
        var indexRest = i % 2;
        // console.log("j: ", j, "i: ", i);
        // console.log("indexRest: ", indexRest);

        if (indexRest === 0) {
            var color1 = Math.floor(Math.random() * 256);
            var color2 = Math.floor(Math.random() * 256);
            var color3 = Math.floor(Math.random() * 256);
            // console.log("color1: ", color1);
            // console.log("color2: ", color2);
            // console.log("color3: ", color3);
        }

        if (indexRest === 0) {
            var newDataset = { // 생산 실적
                type: 'line', // 2021.02.25 Conclusion. 만약 [label=legend]별로 그라프 형식을 지정하고 싶으면, 여기서 처리...
                label: productsArrList[j], //'new Dataset' + config.data.datasets.length,
                backgroundColor: 'rgba(' + color1 + ', ' + color2 + ', ' + color3 + ', 1)',
                borderColor: 'rgba(' + color1 + ', ' + color2 + ', ' + color3 + ', 1)',
                data: graphData2[j],
                fill: false
            };
        } else if (indexRest === 1) { // 생산 Volume
            var newDataset = {
                type: 'bar', // 2021.02.25 Conclusion. 만약 [label=legend]별로 그라프 형식을 지정하고 싶으면, 여기서 처리...
                label: '', //productsArrList[j], // String(i),//productsArrList[i], //'new Dataset' + config.data.datasets.length,
                backgroundColor: 'rgba(' + color1 + ', ' + color2 + ', ' + color3 + ', 1)',
                borderColor: 'rgba(' + color1 + ', ' + color2 + ', ' + color3 + ', 1)',
                data: graphData[j],
                fill: false
            };
            j += 1;
        } else {
            var newDataset = { // 생산 불량
                type: 'bar', // 2021.02.25 Conclusion. 만약 [label=legend]별로 그라프 형식을 지정하고 싶으면, 여기서 처리...
                label: '', // String(i), //'new Dataset' + config.data.datasets.length,
                // backgroundColor: 'rgba(' + color1 + ', ' + color2 + ', ' + color3 + ', 1)',
                // borderColor: 'rgba(' + color1 + ', ' + color2 + ', ' + color3 + ', 1)',
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: graphData[j],
                fill: false
            };
        }

        // Chart에 newDataset 푸쉬
        config.data.datasets.push(newDataset);

    }

    // myChart.update(); // 차트 업데이트 // 2021.02.24 Conclusion. 이건 실행하면 에러 => myChart is not defined.


    // 레전드가 50개를 기준으로 화면 싸이즈를 조정한다.
    // 2021.02.24 Conclusion.
    //      1. #chartArea: 전체 차트 부분의 크기
    //      2. #canvas: 차트 부분 크기 ?? 아닌것 같은데...
    console.log("scripts.js 높이 조정 productsArrList.length: ", productsArrList.length);
    let spaceAfterChart = 15;
    console.log("scripts.js spaceAfterChart: ", spaceAfterChart);
    if (productsArrList.length === 0) {
        document.getElementById("chartArea").style.height = 50 + "px";
        // document.getElementById("chartLegend").style.height = 300 + "px";
        document.getElementById("canvas").height = 40;
        let chartAreaHeight = document.getElementById("chartArea").height;
        let canvasHeight = document.getElementById("canvas").height;
        console.log("0 scripts.js chartAreaHeight: ", chartAreaHeight);
        console.log("0 scripts.js canvasHeight: ", canvasHeight);
    } else if (productsArrList.length > 0 && productsArrList.length < 25) {
        // spaceAfterChart = 15;
        document.getElementById("chartArea").style.height = 280 + "px";
        // document.getElementById("chartLegend").style.height = 300 + "px";
        // document.getElementById("canvas").height = 130;
        document.getElementById("canvas").height = 110;
        let chartAreaHeight = document.getElementById("chartArea").height;
        let canvasHeight = document.getElementById("canvas").height;
        // console.log("2 scripts.js chartAreaHeight: ", chartAreaHeight);
        // console.log("2 scripts.js canvasHeight: ", canvasHeight)};
    } else if (productsArrList.length > 25 && productsArrList.length < 50) {
        // spaceAfterChart = 15;
        document.getElementById("chartArea").style.height = 400 + "px";
        // document.getElementById("chartLegend").style.height = 300 + "px";
        document.getElementById("canvas").height = 120;
        let chartAreaHeight = document.getElementById("chartArea").height;
        let canvasHeight = document.getElementById("canvas").height;
        console.log("2 scripts.js chartAreaHeight: ", chartAreaHeight);
        console.log("2 scripts.js canvasHeight: ", canvasHeight);
    } else if (productsArrList.length > 50 && productsArrList.length < 75) {
        // spaceAfterChart = 15;
        document.getElementById("chartArea").style.height = 500 + "px";
        // document.getElementById("chartLegend").style.height = 300 + "px";
        document.getElementById("canvas").height = 150;
        let chartAreaHeight = document.getElementById("chartArea").height;
        let canvasHeight = document.getElementById("canvas").height;
        // console.log("3 scripts.js chartAreaHeight: ", chartAreaHeight);
        // console.log("3 scripts.js canvasHeight: ", canvasHeight);
    } else if (productsArrList.length > 75 && productsArrList.length < 100) {
        // spaceAfterChart = 15;
        document.getElementById("chartArea").style.height = 500 + "px";
        // document.getElementById("chartLegend").style.height = 450 + "px";
        document.getElementById("canvas").height = 150;
        let chartAreaHeight = document.getElementById("chartArea").height;
        let canvasHeight = document.getElementById("canvas").height;
        console.log("4 scripts.js chartAreaHeight: ", chartAreaHeight);
        console.log("4 scripts.js canvasHeight: ", canvasHeight);
    } else if (productsArrList.length > 100 && productsArrList.length < 125) {
        // spaceAfterChart = 15;
        document.getElementById("chartArea").style.height = 500 + "px";
        // document.getElementById("chartLegend").style.height = 550 + "px";
        document.getElementById("canvas").height = 150;
        let chartAreaHeight = document.getElementById("chartArea").height;
        let canvasHeight = document.getElementById("canvas").height;
        // console.log("5 scripts.js chartAreaHeight: ", chartAreaHeight);
        // console.log("5 scripts.js canvasHeight: ", canvasHeight);
    } else {
        // spaceAfterChart = 15;
        document.getElementById("chartArea").style.height = 650 + "px";
        // document.getElementById("chartLegend").style.height = 1500 + "px";
        document.getElementById("canvas").height = 150;
        let chartAreaHeight = document.getElementById("chartArea").height;
        let canvasHeight = document.getElementById("canvas").height;
        console.log("6 scripts.js chartAreaHeight: ", chartAreaHeight);
        console.log("6 scripts.js canvasHeight: ", canvasHeight);
    }

    // 2021.02.24 Added. 차트 범례를 고려한 차트 크기와, 차트 높이에 따른 차트와 표 사이의 공간 확보
    for (let i = 0; i < spaceAfterChart; i++) {
        let brSpace = document.createElement("br");
        document.getElementById("space-after-chart").appendChild(brSpace);
    }
}

// 2020.02.24 가져온 그라프 참고 자료...
function setRefChart() {
    Chart.defaults.global.legend.labels.usePointStyle = true;

    var randomScalingFactor = function () {
        return Math.round(Math.random() * 100);
    };

    var chartColors = {
        red: 'rgb(255, 99, 132)',
        orange: 'rgb(255, 159, 64)',
        yellow: 'rgb(255, 205, 86)',
        green: 'rgb(75, 192, 192)',
        blue: 'rgb(54, 162, 235)',
        purple: 'rgb(153, 102, 255)',
        grey: 'rgb(231,233,237)'
    };

    var color = Chart.helpers.color;
    var config = {
        type: 'bar', // 'radar',
        data: {
            labels: [["Eating", "Dinner"], ["Drinking", "Water"], "Sleeping", ["Designing", "Graphics"], "Coding", "Cycling", "Running"],
            datasets: [{
                type: 'bar',
                label: "My First dataset",
                backgroundColor: color(chartColors.red).alpha(0.2).rgbString(),
                borderColor: chartColors.red,
                pointBackgroundColor: chartColors.red,
                data: [
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor()
                ],
            }, {
                type: 'line',
                label: "2",
                backgroundColor: color(chartColors.blue).alpha(0.2).rgbString(),
                borderColor: chartColors.blue,
                pointBackgroundColor: chartColors.blue,
                data: [
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor()
                ]
            }, {
                type: 'bar',
                label: "My 3 dataset",
                backgroundColor: color(chartColors.blue).alpha(0.2).rgbString(),
                borderColor: chartColors.blue,
                pointBackgroundColor: chartColors.blue,
                data: [
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor()
                ]
            }, {
                type: 'line',
                label: "4",
                backgroundColor: color(chartColors.blue).alpha(0.2).rgbString(),
                borderColor: chartColors.blue,
                pointBackgroundColor: chartColors.blue,
                data: [
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor()
                ]
            }, {
                type: 'bar',
                label: "My 5 dataset",
                backgroundColor: color(chartColors.blue).alpha(0.2).rgbString(),
                borderColor: chartColors.blue,
                pointBackgroundColor: chartColors.blue,
                data: [
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor()
                ]
            }, {
                type: 'line',
                label: "6",
                backgroundColor: color(chartColors.orange).alpha(0.2).rgbString(),
                borderColor: chartColors.orange,
                pointBackgroundColor: chartColors.orange,
                data: [
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor(),
                    randomScalingFactor()
                ]
            },]
        },
        options: {
            legend: {
                position: 'top',
                labels: {
                    fontColor: 'rgb(255, 99, 132)'
                },
                onHover: function (event, legendItem) {
                    document.getElementById("canvas").style.cursor = 'pointer';
                },
                onClick: function (e, legendItem) {
                    console.log("e: ", e);
                    console.log("legendItem: ", legendItem);
                    var index = legendItem.datasetIndex;
                    console.log("index: ", index);
                    var ci = this.chart;

                    indexFirst = index % 2; // 2로 나누든, 3으로 나누던... indexSecond...
                    console.log("indexFirst: ", indexFirst);
                    if (indexFirst === 0) {
                        var alreadyHidden = (ci.getDatasetMeta(index).hidden === null) ? false : ci.getDatasetMeta(index).hidden;
                        var alreadyHidden = (ci.getDatasetMeta(index + 1).hidden === null) ? false : ci.getDatasetMeta(index + 1).hidden;
                        // console.log("바로 다음 index: ", index);
                        // console.log("바로 다음 indexEven: ", indexEven);
                    } else {
                        var alreadyHidden = (ci.getDatasetMeta(index).hidden === null) ? false : ci.getDatasetMeta(index).hidden;
                        // console.log("일반 index: ", index);
                        // console.log("일반 indexEven: ", indexEven);
                    }

                    ci.data.datasets.forEach(function (e, i) {

                        var meta = ci.getDatasetMeta(i);

                        if (i === index || i === index+1) {
                            meta.hidden = null;
                        } else {
                            if (!alreadyHidden) {
                                meta.hidden = meta.hidden === null ? !meta.hidden : null;
                            } else if (meta.hidden === null) {
                                meta.hidden = true;
                            }
                        }

                        // 여기 아래가 원본임...
                        // var meta = ci.getDatasetMeta(i);
                        //
                        // if (i+1 !== index) {
                        //     if (!alreadyHidden) {
                        //         meta.hidden = meta.hidden === null ? !meta.hidden : null;
                        //     } else if (meta.hidden === null) {
                        //         meta.hidden = true;
                        //     }
                        // } else if (i === index) {
                        //     meta.hidden = null;
                        // }

                    });

                    ci.update();
                },
            },
            tooltips: {
                custom: function (tooltip) {
                    if (!tooltip.opacity) {
                        document.getElementById("canvas").style.cursor = 'default';
                        return;
                    }
                }
            },
            title: {
                display: true,
                text: 'Chart.js Radar Chart'
            },
            // 여기 아래 [scale] [radar] 그라프에서만 사용하는 options 임에 주의.
            // scale: {
            //     ticks: {
            //         beginAtZero: true
            //     }
            // }
        },
    };

    // window.onload = function () {
    //     window.myRadar = new Chart(document.getElementById("canvas"), config);
    // };
    window.onload = function () {
        var ctx = document.getElementById("canvas").getContext('2d');
        window.myRadar = new Chart(ctx, config);
    };



    // 2021.02.24 Added. 차트 범례를 고려한 차트 크기와, 차트 높이에 따른 차트와 표 사이의 공간 확보
    let spaceAfterChart = 5;
    for (let i = 0; i < spaceAfterChart; i++) {
        let brSpace = document.createElement("br");
        document.getElementById("space-after-chart").appendChild(brSpace);
    }
}

// 2021.02.24 Added. 진행 바...
function move1(){
    var ele=document.getElementById('progressing');
    var width = 5;
    var id =setInterval(frame, 45);
    function frame(){
        if(width>=100){
            clearInterval(id);
        }else{
            width ++;
            ele.style.width=width+"%";
            ele.innerHTML=width+"%";
        }
    }
}

function move2() {
    var elem = document.getElementById("myBar");
    var width = 10;
    var id = setInterval(frame, 10);
    function frame() {
        if (width >= 100) {
            clearInterval(id);
        } else {
            width++;
            elem.style.width = width + '%';
            document.getElementById("label").innerHTML = width * 1  + '%';
        }
    }
}

/**
 *
 *  @author abdennour.toumi[AT]gmail.com
 *
 */
window.simple=function(){
    waitingDialog.show('Please Wait');
    setTimeout(function () {
        waitingDialog.hide();
    }, 2000);
};

window.animateText=function(){
    waitingDialog.show('Please Wait');
    var animation=waitingDialog.animate();
    setTimeout(function () {
        waitingDialog.hide();
        waitingDialog.stopAnimate(animation);
    }, 5000);
};

window.adv_animateText = function () {
    waitingDialog.show('');
    console.log("window.adv_animateText 함수로 들어는 왔네...")
    var animation = waitingDialog.animate(function (container) {
        container.html(new Date());
    }, 1000);
    setTimeout(function () {
        waitingDialog.stopAnimate(animation);
        waitingDialog.hide();

    }, 6000);
};

window.progress=function(){
    waitingDialog.show();
    //---------------------------------
    waitingDialog.progress(0);
    setTimeout(function(){
        waitingDialog.progress(10);
        waitingDialog.message('Initialize your ENV..')
    },1000);
    //------------------------------------------
    var mocks=[{message:'Initialize your ENV..',prog:10},{message:'Upload required info...',prog:30},{message:'Please wait..',prog:40},{prog:50},{prog:55},{prog:56},{prog:57},{prog:61},{prog:70},{prog:75},{prog:77},{prog:80},{prog:88},{prog:89},{prog:91},{prog:92},{prog:94},{prog:95},{prog:96},{prog:99},{prog:100}] ;
    mocks.forEach(function(e,i){
        setTimeout(function(){
            if(e.message){
                waitingDialog.message(e.message)
            }else{
                waitingDialog.message(e.prog+'% ...')
            }
            waitingDialog.progress(e.prog);
        },(i+1)*2000)
    });

    setTimeout(function () {

        waitingDialog.hide();

    }, (mocks.length+0.5)*2000);

};

// progressPopup1();
function progressPopup2() {
    $(function () {
        var pleaseWait = $('#pleaseWaitDialog');

        var showPleaseWait = function () {
            // pleaseWait.modal('show');
        };

        var hidePleaseWait = function () {
            // pleaseWait.modal('hide');
        };

        showPleaseWait();
    });
}

// 2021.03.03 Added. [table.생산 실적 수량]을 [page]별로 합산.
function dataTableReset() {
    /*
    if (aa === undefined){....}
    만약 따옴표를 넣고 체크를 할꺼라면
    if (typeof aa == "undefined"){....}
    if (aa == null) {.....}
    이렇게 해도 되겠지만 좀더 정확하게 Null을 체크하려면 아래가 젤 좋다. 값 뿐만 아니라 type.타입까지도 체크해 주기 때문...
    if (aa === null) {.....}
    if (isNan(ppQty)) {.....} // [NaN === Not a Number]
    */
    var $dataRows = $("#dataTable tr:not('.titlerow')");
    let currentPageTotal = 0;
    let i = 0;
    // console.log("$dataRows: ", $dataRows);
    $dataRows.each(function () {
        i++;
        // console.log("i: ", i);
        // var ppQty = $(this).find('.ppQty'); // 이건 object 자체를 가져오네...
        var currentRowQty = $(this).find('.currentRowQty').html();
        if (currentRowQty === undefined) {
            currentRowQty = 0;
        } else if (typeof currentRowQty === 'string' || currentRowQty instanceof String){
            // console.log("String 전 ppQty: ", ppQty);
            currentRowQty = currentRowQty.replace(/[,\{\}\[\]\(\)\'\"\?\*]/gi,""); // 여기서 반드시 [,] 컴마를 빼 주고, 숫자로 변환해야 되네...  [빽슬러쉬+특수문자] 형태로 적어줘야 한다...
            currentRowQty = parseInt(currentRowQty);
            console.log("String 후 currentRowQty: ", currentRowQty);
            // ppQty = Number(ppQty);
        } else {
            currentRowQty = 0
        }
        // console.log("ppQty: ", ppQty);
        // console.log("typeof ppQty: ", typeof ppQty);
        // // currentPageTotal += parseInt(ppQty.html()); // 이런식으로 처리하면 에러 발생 가능성이 많다...
        currentPageTotal += parseInt(currentRowQty);
        // console.log("currentPageTotal: ", currentPageTotal);
        // console.log("typeof currentPageTotal: ", typeof currentPageTotal);
    });
    // console.log("실적 합계 currentPageTotal: ", currentPageTotal);
    // let currentPageTotalString = String(currentPageTotal);
    // document.getElementById("currentPageTotal").innerHTML = String(currentPageTotal);
    if (languageNo === 1042) {
        document.getElementById("currentPageTotal").innerHTML = currentPageTotal.toLocaleString('ko-KR');
        document.getElementById("processTotal").innerHTML = goodnessTotal.toLocaleString('ko-KR');
    } else if (languageNo === 1033) {
        document.getElementById("currentPageTotal").innerHTML = currentPageTotal.toLocaleString('en-US');
        document.getElementById("processTotal").innerHTML = goodnessTotal.toLocaleString('en-US');
    } else {
        document.getElementById("currentPageTotal").innerHTML = currentPageTotal.toLocaleString('zh-CN');
        document.getElementById("processTotal").innerHTML = goodnessTotal.toLocaleString('zh-CN');
    }
    // document.getElementById("currentPageTotal").HTML = currentPageTotalString; // 이건 확실히 아니네...

    return currentPageTotal

    /* 여긴 에러는 안 나는데, 경고 창이 뜨면서 안 되네...
    // 2021.03.03 Added. [table.생산 실적 수량]을 [page]별로 합산.
    $('#dataTable').DataTable( {
        "footerCallback": function ( row, data, start, end, display ) {
            paging: false;
            var api = this.api(), data;

            // Remove the formatting to get integer data for summation
            var intVal = function ( i ) {
                return typeof i === 'string' ?
                    i.replace(/[\$,]/g, '')*1 :
                    typeof i === 'number' ?
                        i : 0;
            };

            // Total over all pages
            var total = api
                .column( 2 )
                .data()
                .reduce( function (a, b) {
                    return intVal(a) + intVal(b);
                }, 0 );

            // Total over this page
            var pageTotal = api
                .column( 2, { page: 'current'} )
                .data()
                .reduce( function (a, b) {
                    return intVal(a) + intVal(b);
                }, 0 );

            // Update footer
            $( api.column( 2 ).footer() ).html(
                '$'+pageTotal +' ( $'+ total +' total)'
            );
        }
    } );
     */
}


function showWindow() {
    // console.log("로딩 완 디버깅 99 showWindow() 막 들어왔다.");
    $('#wait').show();
    // console.log("로딩 완 디버깅 99 showWindow() wait show.");

    $('#process-container').hide();

    $('body').hide();
    // console.log("로딩 완 디버깅 99 showWindow() html body 숨겼다.");

    // stop scroll
    // $('html body').css('overflow', 'hidden');
    // auto hide after 5s
    // stopAutoHide = setTimeout(hideWindow, 5000);
}

function hideWindow() {
    $('#wait').hide();
    $('#process-container').show();
    $('body').show();
    // on scroll
    // $('html body').css('overflow', 'scroll');
}

// // close after click
// $('#close-btn').click(function () {
//     hideWindow();
//     clearTimeout(stopAutoHide);
// });

// console.log("로딩 완 디버깅 99 processTotal: ", processTotal);
