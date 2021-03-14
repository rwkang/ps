/*!
    * Start Bootstrap - SB Admin v6.0.2 (https://startbootstrap.com/template/sb-admin)
    * Copyright 2013-2020 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-sb-admin/blob/master/LICENSE)
    */

// console.log("00000js/script.js: ");
// let from_date = document.getElementById("fromDate").innerText;
// let to_date = $("#toDate");
// console.log("00000js/script.js from_date: ", from_date);
// console.log("00000js/script.js to_date: ", to_date);

(function($) {
    "use strict";

    // 2021.02.06 Conclusion. 여기는 진입부 모두 실행한 후, 실행한다. 여길 먼저 실행하지 않는다는 점에 주의...
    $(document).ready(function () {
        console.log("1111111111111js/script.js: ");

        let processCode; // = "all";

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

        let fromDate = new Date(thisDate.getFullYear(), thisDate.getMonth(), firstDay);
        // console.log("typeof fromDate: ", typeof fromDate);
        // console.log("fromDate: ", fromDate);
        let fromDateString = getYyyyMmDdMmSsToString(fromDate);
        // console.log("typeof fromDateString: ", typeof fromDateString);
        // console.log("fromDateString: ", fromDateString);

        let toDate = thisDate;
        let toDateString = getYyyyMmDdMmSsToString(toDate); // new Date(); // 반드시 여기서 선언을 해 주어야 한다.

        fromDate = dateToYYYYMMDD(fromDate);
        toDate = dateToYYYYMMDD(toDate);
        // console.log("fromDate typeof:", typeof fromDate);
        // console.log("변환 후 fromDate 값:", fromDate);
        // console.log("변환 후 toDate 값:", toDate);

        // $("#fromDate").datepicker('setDate', fromDate); // 이건 이상하게도, 요기서는 잘 되는데, [#toDate] 세팅이 안 되네...
        // $("#fromDate").val(fromDateString); // 이번 달 1일로 세팅...                : 이것도 잘 되고...
        document.getElementById("fromDate").value = fromDateString; // 결론적으로 이렇게 사용하기로 한다. : 이것도 잘 되고...
        fromDateString = document.getElementById("fromDate").value;
        // console.log("1일로 다시 세팅한 fromDateString 값 typeof:", typeof fromDateString);
        console.log("시작 1일로 다시 세팅한 fromDateString 값:", fromDateString);

        // $("#toDate").datepicker('setDate', toDate); // *** 이건 정말 이상하네, [#fromDate]에서는 잘 되는데, 여기서는 안 되네...
        // $("#toDate").val(toDateString); // 이번 달 1일로 세팅...                : 이것도 잘 되고...
        document.getElementById("toDate").value = toDateString; // 결론적으로 이렇게 사용하기로 한다. : 이것도 잘 되고...
        toDateString = document.getElementById("toDate").value;
        // console.log("오늘로 다시 세팅한 toDateString 값 typeof:", typeof toDateString);
        console.log("시작 오늘로 다시 세팅한 toDateString 값:", toDateString);

        // 2021.02.09 Added. [table.td.tr 행 수 또는 그 값 가져오기.
        let arrProcessCode = $("td#process-code");
        console.log("시작 arrProcessCode.length: ", arrProcessCode.length);
        // 2021.02.09 Added. 만약 2개 이상의 공정 자료가 있을 때는, 모든 공정의 자료를 가져오게 한다.
        if (arrProcessCode.length > 1) {
            processCode = "all";
        } else {
            $.each(arrProcessCode, function (index, item) { // ***** 여기는 로우 1개씩 그 값을 가져와서 뿌린다.***** [index]는 [0]부터 시작함에 주의...
                let itemProcessCode = $(item).text();
                if (index === 0) {
                    processCode = itemProcessCode;
                }
            });
        }
        console.log("시작 processCode typeof:", typeof processCode);
        console.log("시작 processCode: ", processCode);

        $.ajax({
            url: '/',
            data: {'fromDate': fromDate, 'toDate': toDate, 'processCode': processCode},
            dataType: 'json',
            type: 'POST',
            // 2021.02.08 Conclusion. 여기 위에서, url 값 [/] 즉, views.py.home()으로 가서, 처리할 것을 처리하고,
            // 이쪽으로 오는 것이 아니라, 바로 views.py.home() 맨 아래쪽 return 에서, [ppp.index.html]로 바로 이동한다.
            // 그러므로 이 아래쪽으로는 전혀 실행할 수가 없다.
            // 만약 이 아래쪽을 실행하게 하려면, views.py.home() return 값을, return JsonResponse(context, safe=False)...
            success: function (data) {
                console.log("이쪽으로 들어 오나??? data: " + data);
                console.log("#시작 typeof data: ", typeof data);
                console.log("#시작 Object.keys(data).length: ", Object.keys(data).length); // ***** JSON Object 또는 일반 Object 갯수 확인... *****
                // console.log("#period data.length: ", data.length); // *** 배열의 갯수 확인... ***
                console.log("#시작 data[0].[0]: ", data['process'][0]);
                // alert("data: ");
                for (let i in data) {
                    console.log("#시작 i: ", i);
                    console.log(`#시작 i: ${i}`);
                    console.log(`#시작 data[${i}]: ${data[i]}`);
                    console.log(`#시작 data[${i}].length: ${Object.keys(data[i]).length}`);
                    // console.log(`#시작 data[${i}].length: ${data[i].length}`);
                    console.log(`#시작 typeof data[${i}]: ${typeof data[i]}`);
                }
                alert("#시작 222");
                console.log("#시작 222 data: ", data)
                if (data['pp_data_period_process'].length === 0) { // if (data[1].length === 0) {
                    console.log("시작 Object.keys(data['process']).length: ", Object.keys(data['process']).length);
                    console.log("시작 Object.keys(data['pp_data_period_process']).length: ", Object.keys(data['pp_data_period_process']).length);
                    console.log("시작 Object.keys(data['total_pp_data_count']).length: ", Object.keys(data['total_pp_data_count']).length);
                    // console.log("시작 Object.keys(data['pp_data_period_process']).length: ", Object.keys(data['pp_data_period_process']).length);
                    // $("table#dataTable").empty();
                    $("#dataTable").empty();
                }
                alert("#시작 333");
                // for (let i=0; i<Object.keys(data).length; i++) { // ******* 엄청 중요함. 여기 라인은 값을 못 가져온다. 모두 [undefined]로 찍힌다.
                for (let i in data) { // ******* 엄청 중요함. 반드시 여기 라인으로 처리해야 한다.
                    console.log("i: ", i);
                    // console.log("Object.keys(data[i]): ", Object.keys(data[i])); // 여기는 [key] 값을 못 가져온다. 에러는 안 나고, 그냥 빈 값이 뿌려진다.
                    console.log("시작 data: ", data[i]);
                    console.log(`#시작 data[${i}]: ${data[i]}`);
                }

                alert("#시작 444");
                let total_pp_data_count = Object.keys(data['total_pp_data_count']).length;

                alert("시작 data:: total_pp_data_count: " + total_pp_data_count);
                // $("#process_data").append(data.htmlresponse;)
            }

        });

            // .done( function (data) {
            //     console.log("서버에서 받은 data 값:", data);
            //     // console.log("서버에서 받은 fromDate 값:", fromDate);
            //     // console.log("서버에서 받은 toDate 값:", toDate);
            //     // console.log("서버에서 받은 process_code 값 typeof:", typeof process_code);
            //     // console.log("서버에서 받은 process_code 값:", process_code);
            // })
    });

    // 2021.02.09 Conclusion. 이쪽 아래 로직이 완료되면, 여기를 기준으로 위쪽 부분은 모두 삭제해야 한다.
    $("#process-selected").on("click", function (e) {
        alert("#process-selected 555");
        async function loadProduction() {
            const fromDate = document.getElementById("input#fromDate").value;
            const toDate = document.getElementById("input#toDate").value;
            const processCode = document.getElementById("tr#processCode").value;
            console.log("loadProduction fromDate: ", fromDate);
            console.log("loadProduction toDate: ", toDate);
            console.log("loadProduction processCode: ", processCode);
            alert("loadProduction processCode" + fromDate + " " + toDate + processCode);
            // const articleResponse = await axios.get("https://jsonplaceholder.typicode.com/posts?userId=" + UserId);
            // const ppResponse = await axios.get("/period");
            // for (let i = 0; i < ppResponse.data.length; i++) {
            //     const commentResponse = await axios.get("https://jsonplaceholder.typicode.com/comments?postId=" + articleResponse.data[i].id);
            //     const table = document.getElementById("list");
            //     const tr = document.getElementById("tr");
            //     const titleTd = document.getElementById("td");
            //
            //     titleTd.innerText = articleResponse.data[i].title;
            //     commentCountTd.innerText = commentResponse.data.length;
            //     commentCountTd.style.textAlign = "center";
            //
            //     tr.appendChild(titleTd);
            //     tr.appendChild(commentCountTd);
            //     list.appendChild(tr);
            // }
        }

        let processSelected;
        processSelected = $("#process-selected").val();
        console.log("processSelected: ", processSelected);
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
            if (arrProcessCode.length > 1) {
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

        alert("#period 333");

        $.ajax({
            url: '/period/',
            // url: '/production/', // 2021.02.09 Conclusion. views.py.production() 여기는 삭제한다. 디버깅 완료...
            data: {'fromDate': fromDate, 'toDate': toDate, 'processCode': processCode},
            dataType: 'json',
            type: 'POST',
            // 2021.02.08 Added. ????? 그러니까...
            // 1. views.py.home()에서 넘긴 값, fromDate, toDate, processCode 값을, 여기서 어떻게 받느냐????
            success: function (data) {
                alert("#period 222");
                console.log("#period data: ", data);
                console.log("#period typeof data: ", typeof data);
                console.log("#period Object.keys(data).length: ", Object.keys(data).length); // ***** JSON Object 또는 일반 Object 갯수 확인... *****
                // console.log("#period data.length: ", data.length); // *** 배열의 갯수 확인... ***
                console.log("#period data[0].[0]: ", data['process'][0]);
                for (let i in data) {
                    console.log("#period i: ", i);
                    console.log(`#period i: ${i}`);
                    console.log(`#period data[${i}]: ${data[i]}`);
                    console.log(`#period data[${i}].length: ${Object.keys(data[i]).length}`);
                    // console.log(`#period data[${i}].length: ${data[i].length}`);
                    console.log(`#period typeof data[${i}]: ${typeof data[i]}`);
                }
                console.log("Object.keys(data['process']).length: ", Object.keys(data['process']).length);
                console.log("Object.keys(data['ppData']).length: ", Object.keys(data['ppData']).length);
                console.log("Object.keys(data['total_pp_data_count']).length: ", Object.keys(data['total_pp_data_count']).length);
                console.log("Object.keys(data['pp_data_period_process']).length: ", Object.keys(data['pp_data_period_process']).length);
                // console.log("#period :: data[1].length: ", data[1].length); // 여기는 에러...
                if (data['ppData'].length === 0) { // if (data[1].length === 0) {
                    console.log("Object.keys(data['process']).length: ", Object.keys(data['process']).length);
                    console.log("Object.keys(data['ppData']).length: ", Object.keys(data['ppData']).length);
                    console.log("Object.keys(data['total_pp_data_count']).length: ", Object.keys(data['total_pp_data_count']).length);
                    console.log("Object.keys(data['pp_data_period_process']).length: ", Object.keys(data['pp_data_period_process']).length);
                    // $("table#dataTable").empty();
                    $("#dataTable").empty();
                }
                // for (let i=0; i<Object.keys(data).length; i++) { // ******* 엄청 중요함. 여기 라인은 값을 못 가져온다. 모두 [undefined]로 찍힌다.
                for (let i in data) { // ******* 엄청 중요함. 반드시 여기 라인으로 처리해야 한다.
                    console.log("i: ", i);
                    // console.log("Object.keys(data[i]): ", Object.keys(data[i])); // 여기는 [key] 값을 못 가져온다. 에러는 안 나고, 그냥 빈 값이 뿌려진다.
                    console.log("data: ", data[i]);
                    console.log(`#period data[${i}]: ${data[i]}`);
                }

                let total_pp_data_count = Object.keys(data['total_pp_data_count']).length;

                alert("data:: total_pp_data_count: " + total_pp_data_count);
                // $("#process_data").append(data.htmlresponse;)

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
    });




    // Add active state to sidbar nav links
    let path = window.location.href; // because the 'href' property of the DOM element is the absolute path
    console.log("path: ", path);

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

