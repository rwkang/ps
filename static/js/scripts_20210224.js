/*!
    * Start Bootstrap - SB Admin v6.0.2 (https://startbootstrap.com/template/sb-admin)
    * Copyright 2013-2020 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-sb-admin/blob/master/LICENSE)
    */

(function($) {
    "use strict";

    // Add active state to sidbar nav links
    let path = window.location.href; // because the 'href' property of the DOM element is the absolute path
    console.log("path: ", path);

    // 2021.02.06 Conclusion. 여기는 진입부 모두 실행한 후, 실행한다. 여길 먼저 실행하지 않는다는 점에 주의...
    console.log("1111111111111js/script.js: ");
    $(document).ready(function () {
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
        console.log("시작 1일로 다시 세팅한 fromDateString 값:", fromDateString);

        // $("#toDate").datepicker('setDate', toDate); // *** 이건 정말 이상하네, [#fromDate]에서는 잘 되는데, 여기서는 안 되네...
        // $("#toDate").val(toDateString); // 이번 달 1일로 세팅...                : 이것도 잘 되고...

        // 2021.02.19 Conclusion. 아래 라인을 실행하게 되면, views.py로 갔다가 올 때, 다시 초기 값으로 세팅한다.
        // document.getElementById("toDate").value = toDateString; // 결론적으로 이렇게 사용하기로 한다. : 이것도 잘 되고...

        toDateString = document.getElementById("toDate").value;
        // console.log("오늘로 다시 세팅한 toDateString 값 typeof:", typeof toDateString);
        console.log("시작 오늘로 다시 세팅한 toDateString 값:", toDateString);

        // 2021.02.09 Added. [table.td.tr 행 수 또는 그 값 가져오기.
        let arrProcessCode = $("td#process-code");
        let arrProcessName = $("td#process-name");
        console.log("시작 arrProcessCode.length: ", arrProcessCode.length);
        console.log("시작 arrProcessName: ", arrProcessName);
        console.log("시작 typeof arrProcessName: ", typeof arrProcessName);
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
        console.log("보낼 processCode typeof:", typeof processCode);
        console.log("보낼 processCode: ", processCode);
        console.log("보낼 processCode: ", processCode);

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

    });

    // 2021.02.11 Added. [table > tr > td] 태그 클릭한 값 얻기 : http://jsfiddle.net/jscodedev/ukqqvL9h/1/
    // process-list : table 태그 id, 반드시 정의...
    // 혹시, 만약, [table > tr > td] 리스트에 [checkbox.체크 박스 컬럼]을 두고, 체크된 Row들을 핸들링하고 싶다면,
    // https://www.youtube.com/watch?v=FutMSTyDr3o : 여기 참조할 것...
    $("#process-list tr").click(function () {
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
        console.log("tdArr.length: ", tdArr.length); // tr 수가 아니고, td 수 임에 주의... 즉 Row 수가 아니고, 컬럼 수...
        console.log("tdArr: ", tdArr);

        // td.eq(index)를 통해 값을 가져올 수도 있다.
        // let processCode = td.eq(0).text();
        // let processName = td.eq(1).text();

        let processCode = td.eq(0).text();
        let processName = td.eq(1).text();
        console.log("processCode: ");
        console.log("#process-list tr processCode: ", processCode);
        console.log("#process-list tr processName: ", processName);

        // // 이걸 따로 processInfo.html 파일로 화면에 뿌려줄 수도 있다.
        // // table 태그 바로 아래에, <div id="process-info1"></div> 와 <div id="process-info2></div> 이렇게 2개의 <div> 태그를 두고...
        // str += "* 클릭한 Row tr 값 = No. : <font color='red'>" + no + "</font>" +
        //     ", 코드 : <font color='red'>" + processCode + "</font>" +
        //     ", 공정 : <font color='red'>" + processName + "</font>";
        // $("#process-info1").html("* 클릭한 Row의 모든 공정 데이터 = " + tr.text());
        // $("#process-info2").html(str);

        var fromDate = $("input#fromDate").val();
        var toDate = $("input#toDate").val();
        console.log("scripts.js #process-list 현재 찍혀있는 fromDate: ", fromDate);
        console.log("scripts.js #process-list 현재 찍혀있는 toDate: ", toDate);
        console.log("scripts.js #process-list 현재 찍혀있는 processCode: ", processCode);

        // 2021.02.18 Conclusion. ajax 방식이 아닌, form.submit 방식으로 3개 파라미터 값을 서버로 넘긴다.
        // let path;
        // let pathCurrent = window.location.href; // because the 'href' property of the DOM element is the absolute path
        // if (pathCurrent.indexOf("index")) {
        //     path = '/'
        // } else {
        //     path = "index/";
        // }
        let path = "/";
        let params = {"fromDate": fromDate, "toDate": toDate, "processCode": processCode};
        let method = "POST";

        sendPost(path, params, method);

        /*
        var action = 'inactive';
        var href = this.href;
        // console.log("scripts.js #process-list 현재 찍혀있는 href: ", href);
        $.ajax({
            // url: '/process/' + processCode + "/",
            url: '/process/',
            // url: '/index/',
            // url: this.href,
            method: 'POST',
            data: {fromDate: fromDate, toDate: toDate, processCode: processCode},
            // caches: false,
            success: function (response) {
                // alert(`00000 fromDate: ${fromDate}, toDate: ${toDate}, processCode: ${processCode}, action: ${action}`);
                // console.log("response: ", response); // 이건 [context] 자체, 엄청 크고 의미가 없다.
                // console.log("response[0]: ", response[0]); // 이건 에러는 없는데, 안 보인다. object는 index 값으로 못 본다.
                console.log("response['productsCount']: ", response['productsCount']);
                // console.log("response['ppDataPeriodProcesList'].length: ", response['ppDataPeriodProcessList'].length);
                console.log("response['ppDataPeriodProcesList']: ", response['ppDataPeriodProcessList']);
                console.log("response['LANGUAGE_NO']: ", response['LANGUAGE_NO']);
                if (response['productsCount'] === 0) {
                    console.log("response가 없습니다.!!!!")
                    $("#dataTable tr").remove(); // 테이블 데이터만 삭제...
                    $("#dataTable").empty(); // 테이블 헤드까지 삭제...
                    // for(var i = 1; i < table.rows.length;){
                    //     table.deleteRow(i);
                    // }
                    // $("#dataTable").submit(function (e) {
                    //     table.fnPageChange(0);
                    //     return false;
                    // })
                } else {
                    console.log("else!!!!!!!!!!!!!!!!!!!!!!!!")
                    console.log("response.processCode: ", response.processCode);
                    console.log("response.is_valid_post: ", response.is_valid_post);
                    // console.log("response: ", response);
                    console.log("typeof response: ", typeof response);
                    console.log("response.length: ", response.length);
                    console.log("response.pp_data: ", response.pp_data);
                    console.log("typeof response.pp_data: ", typeof response.pp_data);
                    console.log("response.pp_data.length: ", response.pp_data.length);
                    if (response.is_valid_post) {
                        // $('#dataTable tbody').html(response.context.pp_data) // 이건 에러...
                        $('#dataTable tbody').html(response.pp_data)
                    }
                    // console.log("response['ppDataPeriodProcesList'].length: ", response['ppDataPeriodProcessList'].length);
                    // console.log("response['ppDataPeriodProcesList']: ", response['ppDataPeriodProcessList']);
                    // $("#production-container").append(response['ppDataPeriodProcessList']);
                    // $("#dataTable").append(response['pp_data_period_process']);
                    // console.log("response['pp_data_period_process']: ", response['pp_data_period_process']);
                    // console.log("response['pp_data_period_process']: ", response['pp_data_period_process']);

                    // for (let i = 0; i < response['pp_data_period_process'].length; i++) {
                    //     // const table = document.getElementById("dataTable");
                    //     // const tr = document.getElementById("tr");
                    //     // const titleTd = document.getElementById("td");
                    //     const table = $("#dataTable");
                    //     const tr = $("#dataTable tr");
                    //     const titleTd = $("#dataTable tr td");
                    //     console.log("table: ", table);
                    //     console.log("tr: ", tr);
                    //     console.log("titleTd: ", titleTd);
                    //
                    //     // titleTd.innerText = articleResponse.data[i].title;
                    //     // commentCountTd.innerText = commentResponse.data.length;
                    //     // commentCountTd.style.textAlign = "center";
                    //     //
                    //     // tr.appendChild(titleTd);
                    //     // tr.appendChild(commentCountTd);
                    //     // list.appendChild(tr);
                    // }

                    // if (response['productsCount'] == 0) {
                    //     $("#more-data").html("<button type='button' class='btn btn-info'>No Post Found</button>");
                    //     action = 'active';
                    // } else {
                    //     $("more-data").html("<button type='button' class='btn btn-info'>Loading more post</button>");
                    //     action = 'inactive';
                    // }
                 }
            }
        })

        */

    });


    let rangeDate = 31; // set limit day
    let period;
    let setSdate, setEdate;
    $("#fromDate").datepicker({
        dateFormat: 'yy-mm-dd',
        // minDate: 0,
        onSelect: function(selectDate){
            let stxt = selectDate.split("-");
            stxt[1] = stxt[1] - 1;
            let sdate = new Date(stxt[0], stxt[1], stxt[2]);
            let edate = new Date(stxt[0], stxt[1], stxt[2]);
            edate.setDate(sdate.getDate() + rangeDate);
            $('#toDate').datepicker('option', {
                minDate: selectDate,
                beforeShow : function () {
                    $("#toDate").datepicker( "option", "maxDate", edate );
                    setSdate = selectDate;
                    console.log("부터, typeof setSdate: ", typeof setSdate);
                    console.log("부터, setSdate: ", setSdate);
                }});
            //to 설정
        }
        //from 선택되었을 때

    });

    $("#toDate").datepicker({
        dateFormat: 'yy-mm-dd',
        onSelect : function(selectDate){
            setEdate = selectDate;
            console.log("까지, setEdate: ", setEdate);
            console.log("까지, typeof setEdate: ", typeof setEdate);
            console.log("까지, setEdate: ", setEdate);

            // 2021.02.04 Conclusion. 여기서는 이벤트 발생을, 단지 [검색 기간]의 값을 서버에 전달하고, 그 값을 공유하고,
            // 반드시 [공정]에서 [보기] 버튼을 클릭했을 때, 서버 자료를 가져오도록 한다.
            // fetch('/period').then((res) => res.json()).then((results) => {
            //     console.log("results: ", results);
            //     const json_data = results.period;
            //     // const [labels, data] = [
            //     //     Object.keys(json_data),
            //     //     Object.values(json_data),
            //     // ];
            //     // // renderChart([data], [labels]);
            //     // renderChart((data), (labels));
            //     // // renderChart([], [])
            // });

        }
    });

    $("#period").on("click", function (e) {
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

        // console.log("typeof fromDate: ", typeof fromDate);
        // console.log("typeof toDate: ", typeof toDate);
        // console.log("typeof diff: ", typeof diff);
        // console.log("typeof currDay: ", typeof currDay);
        // console.log("fromDate: ", fromDate);
        // console.log("toDate: ", toDate);
        // console.log("diff: ", diff);
        // console.log("currDay: ", currDay);

        // alert("#period 333");

        if (Date.parse(diff / currDay) > rangeDate) {
            console.log("Date.parse(diff / currDay): ", Date.parse(diff / currDay));
            alert(`조회 기간은 ${rangeDate}일을 초과할 수 없습니다. 기간을 다시 확인하시오!`);
            return false;
        } else {
            fromDate = $("input#fromDate").val();
            toDate = $("input#toDate").val();
            console.log("scripts.js #period onClick else fromDate: ", fromDate);
            console.log("scripts.js #period onClick else toDate: ", toDate);

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
                    // console.log("index: ", index);
                    // console.log("itemProcessCode: ", itemProcessCode);
                    // console.log("processCode: ", processCode);
                    // console.log("typeof itemProcessCode: ", typeof itemProcessCode);
                });
            }
        }

        console.log("scripts.js #period onClick 보내는 processCode: ", processCode);

        // 2021.02.18 Conclusion. ajax 방식이 아닌, form.submit 방식으로 3개 파라미터 값을 서버로 넘긴다.
        // let path;
        // let pathCurrent = window.location.href; // because the 'href' property of the DOM element is the absolute path
        // if (pathCurrent.indexOf("index")) {
        //     path = '/'
        // } else {
        //     path = "index/";
        // }
        let path = "/";
        console.log("path: ", path);
        let params = {"fromDate": fromDate, "toDate": toDate, "processCode": processCode};
        let method = "POST";

        sendPost(path, params, method);

        // var xhttp = new XMLHttpRequest();
        // var csrf_token = $('[name=csrfmiddlewaretoken]').val();
        // xhttp.open(method, path, true);
        // xhttp.setRequestHeader('X-CSRFToken', csrf_token);
        // xhttp.send(params);


        // alert("#period 333");

        /*
        $.ajax({
            url: '/period/',
            // url: '/production/', // 2021.02.09 Conclusion. views.py.production() 여기는 삭제한다. 디버깅 완료...
            data: {'fromDate': fromDate, 'toDate': toDate, 'processCode': processCode},
            dataType: 'json',
            type: 'POST',
            // 2021.02.08 Added. ????? 그러니까...
            // 1. views.py.home()에서 넘긴 값, fromDate, toDate, processCode 값을, 여기서 어떻게 받느냐????
            success: function (data) {
                // alert("#period 222");
                // console.log("#period data: ", data);
                // console.log("#period typeof data: ", typeof data);
                // console.log("#period Object.keys(data).length: ", Object.keys(data).length); // ***** JSON Object 또는 일반 Object 갯수 확인... *****
                // console.log("#period data.length: ", data.length); // *** 배열의 갯수 확인... 전체 [data] 값은 큰 의미가 없다.***
                // console.log("#period data[0].[0]: ", data['process'][0]);
                // for (let i in data) {
                    // console.log("#period i: ", i);
                    // console.log(`#period i: ${i}`);
                    // console.log(`#period data[${i}]: ${data[i]}`);
                    // console.log(`#period data[${i}].length: ${Object.keys(data[i]).length}`);
                    // console.log(`#period data[${i}].length: ${data[i].length}`); 전체 [data]는 의미가 없음...
                    // console.log(`#period typeof data[${i}]: ${typeof data[i]}`);
                // }
                console.log("Object.keys(data['process']): ", Object.keys(data['process']));
                console.log("Object.keys(data['process']).length: ", Object.keys(data['process']).length);
                console.log("Object.keys(data['pp_data_period_process']): ", Object.keys(data['pp_data_period_process']));
                console.log("Object.keys(data['pp_data_period_process']).length: ", Object.keys(data['pp_data_period_process']).length);

                console.log("Object.values(data['pp_data_period_process']): ", Object.values(data['pp_data_period_process']));
                console.log("Object.values(data['pp_data_period_process']).length: ", Object.values(data['pp_data_period_process']).length);

                // console.log("#period :: data[1].length: ", data[1].length); // 여기는 에러...
                if (data['pp_data_period_process'].length === 0) { // if (data[1].length === 0) {
                    // console.log("Object.keys(data['process']).length: ", Object.keys(data['process']).length);
                    // console.log("Object.keys(data['pp_data_period_process']): ", Object.keys(data['pp_data_period_process']));
                    // console.log("Object.keys(data['pp_data_period_process']).length: ", Object.keys(data['pp_data_period_process']).length);
                    // $("table#dataTable").empty();
                    $("#dataTable").empty();
                } else {
                    // for (let i=0; i<Object.keys(data).length; i++) { // ******* 엄청 중요함. 여기 라인은 값을 못 가져온다. 모두 [undefined]로 찍힌다.
                    // for (let i in data) { // ******* 엄청 중요함. 반드시 여기 라인으로 처리해야 한다.
                        // console.log("i: ", i);
                        // console.log("Object.keys(data[i]): ", Object.keys(data[i])); // 여기는 [key] 값을 못 가져온다. 에러는 안 나고, 그냥 빈 값이 뿌려진다.
                        // console.log("data: ", data[i]);
                        // console.log(`#period data[${i}]: ${data[i]}`);
                        // console.log(`#pp_data_period_process data[${i}]: ${data[i]}`);
                        // console.log(`#pp_data_period_process typeof data[${i}]: ${typeof data[i]}`);
                    // }

                    var str = `<thead><br>`;
                    str += `<tr><th>생산 번호</th><th>제품 규격</th><th>양품량</th><th>공정</th></tr></thead><br>`;
                    str += `<tfoot><br><tr><br><th>생산 번호</th><th>제품 규격</th><th>양품량</th><th>공정</th></tr></tfoot><br>`;
                    str += `<tbody><br><tr>`;
                    for (let value of Object.values(data['pp_data_period_process'])) {
                        str += `<td>${value[1]}</td><td>${value[3]}</td><td align="right">${value[4]}</td><td>${value[5]}</td></tr><br>`;
                    }
                    console.log("str: ", str);
                    str += `</tbody><br>`;
                    console.log("str: ", str);

                    // $("#dataTable").html(str);
                    $("#tableBody").html(str);
                    // $("#tableBody").append(str);

                    $("#html").load("static/css/styles.css");
                    // $("#dataTable").load("./static/css/styles.css");
                    // $("#dataTable").load("../static/css/styles.css");

                    // $("#dataTable").DataTable();
                    // $(".table").DataTable();
                    // $("#dataTable > thead > tr > th").html();

                    // var tg = document.getElementById("dataTable");
                    // var tg = $("#dataTable");
                    // if (tg) {tg.href=("css/dataTables.bootstrap4.min.css")}

                    // var objLink = document.createElement("objLink");
                    // objLink.rel = "stylesheet";
                    // objLink.type = "text/css"
                    // objLink.href = "css/dataTables.bootstrap4.min.css";
                    // document.appendChild(objLink);

                    // var cssId = 'myCss';
                    // if (!document.getElementById(cssId)) {
                    //     var $head = $('head');
                    //     var link = document.createElement('link');
                    //     link.attr({
                    //         id: cssId,
                    //         rel: 'stylesheet',
                    //         type: 'text/css',
                    //         // href: 'css/styles.css',
                    //         href: 'css/dataTables.bootstrap4.min.css',
                    //         media: 'all'
                    //     });
                    //     $head.append(link);
                    //     // css/dataTables.bootstrap4.min.css
                    // }

                    // element.toggleClass('table');

                    // setInterval('location.reload()', 2000)
                    // setInterval('refreshPage()', 2000)


                    // self.close(); // 여기는 통신이 끊기면서, 브라우저 화면이 죽어 버리네...

                }

                console.log("Object.keys(data['pp_data_period_process']).length: ", Object.keys(data['pp_data_period_process']).length);

                // window.opener.location.reload();
                // $("#dataTable").load();
                // $("#dataTable").html(data['pp_data_period_process']);

                // $("#process_data").append(data.htmlresponse;)

            },

            error: function (xhr, status, error) {
                alert("서버 통신 실패!")
            },

            complete: function (xhr, status) {
                // $("#dataTable > thead > tr > th").html();
                // $("#dataTable > tfoot > tr > th").css('display','block');
                // $("#dataTable > tbody > tr > td").css('display','block');
                // $("#dataTable").css('display');
                // alert("통신 종료!")
            }

            // success: function (data, textStatus, xhr) {
            //     if (data === 'loginFail') {
            //         alert("전송에 실패하였습니다!")
            //     } else {
            //         window.location.href = 'index.html';
            //     }
            // },
            // error: function (request, status, error) {
            //     alert(`Error Code: ${request.status}, \n${error} error.`)
            // }
        });
        // console.log("data: ", data)

        */

    });

    ///*
    // 2021.02.22 Added. 차트 조정
    // 1. legend.레전드 전부 중간줄 긋기...
    // $("#myChart > option > title").on("click", function (e) {
    //     console.log("차트 클릭했나???");
    // });
    // $("#myChart > options > legend").on("click", function (e) {
    //     console.log("차트 레전드 클릭했나???");
    // });

    // 그래프를 그린다...

    // 데이터셋 세팅 : ppDataPeriodArr.length
    for (let i = 0; i < graphData.length; i++) {
        var color1 = Math.floor(Math.random() * 256);
        var color2 = Math.floor(Math.random() * 256);
        var color3 = Math.floor(Math.random() * 256);
        //console.log(`80: ${color1} ${color2} ${color3}`)
        var newDataset = {
            label: productsArrList[i], //'new Dataset' + config.data.datasets.length,
            backgroundColor: 'rgba(' + color1 + ', ' + color2 + ', ' + color3 + ', 1)',
            borderColor: 'rgba(' + color1 + ', ' + color2 + ', ' + color3 + ', 1)',
            // data: graphData[i],
            fill: false
        };
        // Chart에 newDataset 푸쉬
        // config.data.datasets.push(newDataset);
    }

        // {
        //         label: "My Second dataset",
        //         backgroundColor: color(chartColors.blue).alpha(0.2).rgbString(),
        //         borderColor: chartColors.blue,
        //         pointBackgroundColor: chartColors.blue,
        //         data: [
        //             randomScalingFactor(),
        //         ]
        //     }

    // console.log("productsArrList: ", productsArrList);
    // console.log("graphData: ", graphData);
    // console.log("newDataset: ", newDataset);


    // var ctx = document.getElementById('myChart');
    var ctx = document.getElementById('canvas');
    Chart.defaults.global.legend.labels.usePointStyle = true;
    var defaultLegendClickHandler = Chart.defaults.global.legend.onClick;

    var randomScalingFactor = function() {
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
    console.log("color: ", color);

    var config = {
        type: 'bar', //'radar',
        // data: newDataset, // 요래 하면 안되네...
        data: {
            labels: ppDataPeriodArrList,
            datasets: []
        },
        // data: {
        //     labels: [["Eating", "Dinner"], ["Drinking", "Water"], "Sleeping", ["Designing", "Graphics"], "Coding", "Cycling", "Running"],
        //     datasets: [{
        //         label: "My First dataset",
        //         backgroundColor: color(chartColors.red).alpha(0.2).rgbString(),
        //         borderColor: chartColors.red,
        //         pointBackgroundColor: chartColors.red,
        //         data: [
        //             randomScalingFactor(),
        //         ]
        //     }, {
        //         label: "My Second dataset",
        //         backgroundColor: color(chartColors.blue).alpha(0.2).rgbString(),
        //         borderColor: chartColors.blue,
        //         pointBackgroundColor: chartColors.blue,
        //         data: [
        //             randomScalingFactor(),
        //         ]
        //     }, {
        //         label: "My Third dataset",
        //         backgroundColor: color(chartColors.orange).alpha(0.2).rgbString(),
        //         borderColor: chartColors.orange,
        //         pointBackgroundColor: chartColors.orange,
        //         data: [
        //             randomScalingFactor(),
        //         ]
        //     },]
        // },
        options: {
            legend: {
                position: 'top',
                labels: {
                    // fontColor: 'rgb(255, 99, 132)'
                },
                onHover: function(event, legendItem) {
                    document.getElementById("canvas").style.cursor = 'pointer';
                },
                onClick: function(e, legendItem) {
                    var index = legendItem.datasetIndex;
                    var ci = this.chart;
                    var alreadyHidden = (ci.getDatasetMeta(index).hidden === null) ? false : ci.getDatasetMeta(index).hidden;

                    ci.data.datasets.forEach(function(e, i) {
                        var meta = ci.getDatasetMeta(i);

                        if (i !== index) {
                            if (!alreadyHidden) {
                                meta.hidden = meta.hidden === null ? !meta.hidden : null;
                            } else if (meta.hidden === null) {
                                meta.hidden = true;
                            }
                        } else if (i === index) {
                            meta.hidden = null;
                        }
                    });

                    ci.update();
                },
            },
            tooltips: {
                custom: function(tooltip) {
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
            // scale: {
            //     ticks: {
            //         beginAtZero: true
            //     }
            // }
        }
    };

    window.onload = function() {
        window.myChart = new Chart(document.getElementById("canvas"), config);
    };

    // 데이터셋 세팅 : ppDataPeriodArr.length
    for (let i = 0; i < graphData.length; i++) {
        var color1 = Math.floor(Math.random() * 256);
        var color2 = Math.floor(Math.random() * 256);
        var color3 = Math.floor(Math.random() * 256);
        // backgroundColor: color(chartColors.red).alpha(0.2).rgbString(),
        // borderColor: chartColors.red,
        // pointBackgroundColor: chartColors.red,
        //console.log(`80: ${color1} ${color2} ${color3}`)
        var newDataset = {
            label: productsArrList[i], //'new Dataset' + config.data.datasets.length,
            backgroundColor: 'rgba(' + color1 + ', ' + color2 + ', ' + color3 + ', 1)',
            borderColor: 'rgba(' + color1 + ', ' + color2 + ', ' + color3 + ', 1)',
            data: graphData[i],
            fill: false
        };
        // Chart에 newDataset 푸쉬
        config.data.datasets.push(newDataset);
    }

    // myChart.update(); // 차트 업데이트 // 2021.02.24 Conclusion. 이건 실행하면 에러 => myChart is not defined.


    /* 여기가 맨 처음 가져온 원본을 일부 수정한 것.
    var config = {
        type: 'bar', // 'pie',  //'radar',
        data: {
            labels: ppDataPeriodArrList, // [ ],
            datasets: []
        },
        option: {
            maintainAspectRatio: false,
            title: {
                display: true,
                //onClick: toggleLegend(),
                // text: '생산 실적 분석'
            },
            scales: {
                yAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: '차트'
                    }
                }]
            },
            legend: {
                display: true,
                // onHover: function(enent, legendItem) {
                //     document.getElementById("myChart").style.cursor = 'pointer';
                // },
                onClick: function(e, legendItem) {
                    let arc = this.myChart.getDatasetMeta(0).data[legendItem.index];
                    arc.hidden = !arc.hidden ? true : false;
                    this.myChart.update();
                },
                labels: {
                    fontColor: '#fff',
                    generateLabels: function(myChart) {
                        return myChart.data.labels.map(function(label, i) {
                            let arc = myChart.getDatasetMeta(0).data[i];
                            let value = myChart.config.data.datasets[arc._datasetIndex].data[arc._index];
                            return {
                                text: label + ': ' + value,
                                fillStyle: colorSet[i],
                                lineWidth: 1,
                                index: i
                            };
                        })
                    }
                },
                // onClick: function(event, legendItem) {
                //     var index = legendItem.datasetIndex;
                //     var ci = this.chart;
                //     var alreadyHidden = (ci.getDatasetMeta(index).hidden === null) ? false : ci.getDatasetMeta(index).hidden;
                //     var anyOthersAlreadyHidden = false;
                //     var allOthersHidden = true;
                //
                //     // figure out th current state of the labels
                //     ci.data.datasets.forEach(function (e, i) {
                //         var meta = ci.getDatasetMeta(i);
                //
                //         if (i !== index) {
                //             if (meta.hidden) {
                //                 anyOthersAlreadyHidden = true;
                //             } else {
                //                 allOthersHidden = false;
                //             }
                //         }
                //     });
                //
                //     // if the label we clicked is already hidden
                //     // then we now want to unhide (with any others already unhidden)
                //     if (alreadyHidden) {
                //         ci.getDatasetMeta(index).hidden = null;
                //     } else {
                //         // otherwise, lets figure out how to toggle visibility based upon the current state
                //         ci.data.datasets.forEach(function(e, i) {
                //             var meta = ci.getDatasetMeta(i);
                //
                //             if (i !== index) {
                //                 // handles logic when we click on visible hidden label and there is currently at least
                //                 // one other label that is visible and at least one other label already hidden
                //                 // (we want to keep those already hidden still hidden)
                //                 if (anyOthersAlreadyHidden && !allOthersHidden) {
                //                     meta.hidden = true;
                //                 } else {
                //                     // toggle visibility
                //                     meta.hidden = meta.hidden === null ? !meta.hidden : null;
                //                 }
                //             } else {
                //                 meta.hidden = null;
                //             }
                //         });
                //     }
                //
                //     ci.update();
                // },
            },
            // tooltips: {
            //     custom: function(tooltip) {
            //         if (!tooltip.opacity) {
            //             document.getElementById("canvas").style.cursor = 'default';
            //             return;
            //         }
            //     }
            // },
            // scale: {
            //     ticks: {
            //         beginAtZero: true
            //     }
            // }
        }
    };

    function toggleLegend() {
        //alert("레전드 클릭!!!");
        console.log("Legend Clicked!!!");
    }
    */

    // 레전드가 50개를 기준으로 화면 싸이즈를 조정한다.
    // 2021.02.24 Conclusion.
    //      1. #chartArea: 전체 차트 부분의 크기
    //      2. #canvas: 차트 부분 크기 ?? 아닌것 같은데...
    console.log("scripts.js productsArrList.length: ", productsArrList.length)
    let spaceAfterChart = 5;
    if (productsArrList.length > 0 && productsArrList.length < 25) {
        document.getElementById("chartArea").style.height = 300 + "px";
        // document.getElementById("chartLegend").style.height = 300 + "px";
        document.getElementById("canvas").height = 110;
        let chartAreaHeight = document.getElementById("chartArea").height;
        let canvasHeight = document.getElementById("canvas").height;
        // console.log("1 scripts.js chartAreaHeight: ", chartAreaHeight);
        // console.log("1 scripts.js canvasHeight: ", canvasHeight);
    } else if (productsArrList.length > 25 && productsArrList.length < 50) {
        spaceAfterChart = 7;
        document.getElementById("chartArea").style.height = 300 + "px";
        // document.getElementById("chartLegend").style.height = 300 + "px";
        document.getElementById("canvas").height = 130;
        let chartAreaHeight = document.getElementById("chartArea").height;
        let canvasHeight = document.getElementById("canvas").height;
        // console.log("2 scripts.js chartAreaHeight: ", chartAreaHeight);
        // console.log("2 scripts.js canvasHeight: ", canvasHeight)};
    } else if (productsArrList.length > 50 && productsArrList.length < 75) {
        spaceAfterChart = 8;
        document.getElementById("chartArea").style.height = 350 + "px";
        // document.getElementById("chartLegend").style.height = 300 + "px";
        document.getElementById("canvas").height = 150;
        let chartAreaHeight = document.getElementById("chartArea").height;
        let canvasHeight = document.getElementById("canvas").height;
        // console.log("3 scripts.js chartAreaHeight: ", chartAreaHeight);
        // console.log("3 scripts.js canvasHeight: ", canvasHeight);
    } else if (productsArrList.length > 50 && productsArrList.length < 100) {
        spaceAfterChart = 9;
        document.getElementById("chartArea").style.height = 450 + "px";
        // document.getElementById("chartLegend").style.height = 450 + "px";
        document.getElementById("canvas").height = 180;
        let chartAreaHeight = document.getElementById("chartArea").height;
        let canvasHeight = document.getElementById("canvas").height;
        // console.log("4 scripts.js chartAreaHeight: ", chartAreaHeight);
        // console.log("4 scripts.js canvasHeight: ", canvasHeight);
    } else if (productsArrList.length > 100 && productsArrList.length < 125) {
        spaceAfterChart = 10;
        document.getElementById("chartArea").style.height = 500 + "px";
        // document.getElementById("chartLegend").style.height = 550 + "px";
        document.getElementById("canvas").height = 200;
        let chartAreaHeight = document.getElementById("chartArea").height;
        let canvasHeight = document.getElementById("canvas").height;
        // console.log("5 scripts.js chartAreaHeight: ", chartAreaHeight);
        // console.log("5 scripts.js canvasHeight: ", canvasHeight);
    } else {
        spaceAfterChart = 11;
        document.getElementById("chartArea").style.height = 650 + "px";
        // document.getElementById("chartLegend").style.height = 650 + "px";
        document.getElementById("canvas").height = 230;
        let chartAreaHeight = document.getElementById("chartArea").height;
        let canvasHeight = document.getElementById("canvas").height;
        // console.log("6 scripts.js chartAreaHeight: ", chartAreaHeight);
        // console.log("6 scripts.js canvasHeight: ", canvasHeight);
    }

    // 2021.02.24 Added. 차트 범례를 고려한 차트 크기와, 차트 높이에 따른 차트와 표 사이의 공간 확보
    for (let i = 0; i < spaceAfterChart; i++) {
        let brSpace = document.createElement("br");
        document.getElementById("space-after-chart").appendChild(brSpace);
    }








    /*
    // 차트 그리기
    // var myChart = new Chart(ctx, config);

    // 데이터셋 세팅 : ppDataPeriodArr.length
    for (let i = 0; i < graphData.length; i++) {
        var color1 = Math.floor(Math.random() * 256);
        var color2 = Math.floor(Math.random() * 256);
        var color3 = Math.floor(Math.random() * 256);
        //console.log(`80: ${color1} ${color2} ${color3}`)
        var newDataset = {
            label: productsArrList[i], //'new Dataset' + config.data.datasets.length,
            backgroundColor: 'rgba(' + color1 + ', ' + color2 + ', ' + color3 + ', 1)',
            borderColor: 'rgba(' + color1 + ', ' + color2 + ', ' + color3 + ', 1)',
            data: graphData[i],
            fill: false
        };
        // Chart에 newDataset 푸쉬
        config.data.datasets.push(newDataset);
    }

    // myChart.options.title.display = true;
    // myChart.options.title.text = '생산 실적 분석';
    myChart.options.title.onClick = toggleLegend();
    // myChart.options.legend.display = true;
    myChart.options.animation.duration = 1;

    myChart.update(); // 차트 업데이트

    //*/



    /*
    // 2021.02.23 Added. 그라프의 전체 범례를 한 번에 보이게, 안 보이게...
    window.onload = function() {
        var ctx = $('#myChart').get(0).getContext("2d");
        window.myChart = new Chart(ctx, {
            type: 'bar',
            data: config.data,
            options: {
                legend: false,
                legendCallback: function(myChart){
                    return drawCustomLegend(myChart);
                }// 사용자 범례를 만들 때 쓰는 함수를 지정하거나 작성한다.
            }
        });
        $('#chartLegend').html(window.myChart.generateLegend());//사용자 범례 자리에 해당 차트에 대한 사용자 범례 코드를 넣는다.
    };

    $('#chartLegend').html(window.myChart.generateLegend()); // 사용자 범례 자리에 해당 차트에 대한 사용자 범례 코드를 넣는다.

    function drawCustomLegend(myChart){
        var text = [];
        text.push('<ul class="' + myChart.id + '-legend">');
        if(myChart.config.type == 'bar'){//막대차트, 막대라인차트일 경우
            var barIndex = myChart.data.datasets.length;
            for (var i = 0; i <myChart.data.datasets.length; i++) {
                if(myChart.data.datasets[i].type == 'line' == false){
                    barIndex = i;
                    break;
                }
            } //라인 형식 데이터셋이 어디까지인지 확인
            // -> 막대 형식의 데이터셋을 라인 형식의 데이터셋보다 앞에 둘 경우 라인이 막대에 묻히기 때문에 라인 형식이 먼저 올 수 밖에 없다.
            // 그러나 막대 형식의 데이터셋의 범례를 먼저 그리고 싶었기 때문에 해당 작업을 했다.
            for (var i = barIndex; i <myChart.data.datasets.length; i++) {
                if(!(myChart.data.datasets[i].hideLegend) && myChart.data.datasets[i].label){
                    text.push('<li datasetIndex="'+i+'"><span class="bar" style="background-color:' + myChart.data.datasets[i].backgroundColor + '" ></span>');
                    text.push('<span>'+myChart.data.datasets[i].label+'</span>');
                    text.push('</li>');
                }
            }//막대 형식 데이터셋의 범례를 먼저 그림
            for (var i = 0; i <barIndex; i++) {
                if(!(myChart.data.datasets[i].hideLegend) && myChart.data.datasets[i].label){
                    text.push('<li datasetIndex="'+i+'"><div class="line" style="background:' + myChart.data.datasets[i].borderColor + '"></div>');
                    text.push('<span>'+myChart.data.datasets[i].label+'</span>');
                    text.push('</li>');
                }
            }//막대 형식 데이터셋의 범례를 그린 후 라인 형식 데이터셋의 범례를 그림.
        } else if(myChart.config.type == 'line'){//라인 차트일 경우
            for (var i = 0; i <myChart.data.datasets.length; i++) {
                if(!(myChart.data.datasets[i].hideLegend) && myChart.data.datasets[i].label){
                    text.push('<li datasetIndex="'+i+'"><span class="line" style="background-color:' + myChart.data.datasets[i].borderColor + '"></span>');
                    text.push('<span>'+myChart.data.datasets[i].label+'</span>');
                    text.push('</li>');
                }
            }
        }
        text.push('</ul>');
        return text.join("");
    }
    */


    /* 요기 아래는 아직 안 되네... 좀 더 연구...
    window.onload = function() {
        // $("#chartLegend li").click(function(){
        $("#chartLegend").click(function(){
            updateDataset(event, $(this).attr("datasetIndex"), "myChart");
            if($(this).css("text-decoration").indexOf("line-through")<0){
                $(this).css("text-decoration", "line-through");
            } else{
                $(this).css("text-decoration", "none");
            }
        });
    };
    //범례 클릭시 해당 데이터셋이 숨김/보이기 토글 기능 함수
    function updateDataset(e, datasetIndex, chartId) {
        var index = datasetIndex;
        var ci = e.view[chartId];
        var meta = ci.getDatasetMeta(index);
        var scaleList = ci.options.scales["yAxes"];
        meta.hidden = meta.hidden === null? !ci.data.datasets[index].hidden : null;
        console.log("차트 레전드 클릭했나???");
        ci.update();
    }
    */

    // 출처: https://risha-lee.tistory.com/19?category=764955 [리샤의 개발 일지]

    /* 요기 아래는 아직 안 되네... 좀 더 연구...
    var defaultLegendClickHandler = Chart.defaults.global.legend.onClick;
    var newLegendClickHandler = function (e, legendItem) {
        var index = legendItem.datasetIndex;

        if (index > 1) {
            // Do the original logic
            defaultLegendClickHandler(e, legendItem);
        } else {
            let ci = this.chart;
            [
                ci.getDatasetMeta(0),
                ci.getDatasetMeta(1)
            ].forEach(function(meta) {
                meta.hidden = meta.hidden === null ? !ci.data.datasets[index].hidden : null;
            });
            ci.update();
            console.log("차트에 반영이 되었나?")
        }
    };

    var chart = new Chart(ctx, {
        type: 'line',
        data: data,
        options: {
            legend: {
                onClick: newLegendClickHandler
            }
        }
    });
    */

    // 2021.02.19 Conclusion. 아래 [path]는 맨 위로 올렸다. 전체에서 사용하기 위해...
    // Add active state to sidbar nav links
    // let path = window.location.href; // because the 'href' property of the DOM element is the absolute path
    // console.log("path: ", path);

    $("body").toggleClass("sb-sidenav-toggled");

    $("#layoutSidenav_nav .sb-sidenav a.nav-link").each(function() {
        if (this.href === path) {
            $(this).addClass("active");
            console.log("path1: ", path);
        }
    });

    // Toggle the side navigation
    $("#sidebarToggle").on("click", function(e) {
        e.preventDefault();
        $("body").toggleClass("sb-sidenav-toggled");
        console.log("path2: ", path);
    });
})(jQuery);


function getYyyyMmDdMmSsToString(date)
{
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
    var form = document.createElement("form");
    form.setAttribute("method", method);
    form.setAttribute("action", path);
    for (var key in params) {
        var hiddenField = document.createElement("input");
        hiddenField.setAttribute("type", "hidden");
        hiddenField.setAttribute("name", key);
        hiddenField.setAttribute("value", params[key]);
        form.appendChild(hiddenField);
        console.log("key: ", key)
        console.log("value: ", params[key])
        console.log("hiddenField: ", hiddenField)
    }
    // var hiddenField = document.createElement("input");
    // hiddenField.setAttribute("type", "hidden");
    // hiddenField.setAttribute("name", "_csrf");
    // hiddenField.setAttribute("value", "${_csrf.token}");

    // hiddenField.setAttribute("id", "csrfToken");
    // hiddenField.setAttribute("name", "${_csrf.parameterName}");
    // hiddenField.setAttribute("value", "${_csrf.token}");

    document.body.appendChild(form);
    form.submit();
}