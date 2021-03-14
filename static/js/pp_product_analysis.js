const renderChart = (data, labels) => {
    var ctx = document.getElementById('myChartBarProduct').getContext('2d');
    var myChartBarProduct = new Chart(ctx, {
        type: 'bar', // 'line', 'doughnut', 'pie', 'bar',
        data: {
            labels: labels, // ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
            datasets: [{
                label: '당월 제품별 진도 관리', //'# of Votes', : 그래프 내부 현재 datasets에 대한 타이틀...
                data: data,  // [12, 19, 3, 5, 2, 3],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            title: {
                display: false, //true, // 현재 공간만 차지하니, 타이틀은 뿌리지 말자...
                // text: "생산 실적 분석", // 그래프 내부 타이틀...
            }
        }
        // options: {
        //     scales: {
        //         yAxes: [{
        //             ticks: {
        //                 beginAtZero: true
        //             }
        //         }]
        //     }
        // }
    });
}

const getChartData=() => {
    // console.log("fetching..."); // for Debugging...
    // console.log("pp_product_analysis.js::data: ", data);

    // fetch('') : 여기 안에는, url 이름을 적어 준다. views 이름이나 namespace 이름이 아님에 주의.
    // ***** 또한 [pp_product_analysis]가 아님에 특히 주의... JSON 데이터를 보내 주는 [pp_product_summary]임에 주의...
    // var para = `/process/${process.code}` // 이건 에러...
    // var para = document.location.href.split("?");
    // var protocol = window.location.protocol;
    // var host = window.location.host;
    // var href = window.location.href;
    // var para1 = window.location.href.split("?");
    // var pathArry = window.location.pathname.split('/');
    // var secondLevelLocation = pathArry[0];
    // var newPathName = "";
    // for (i = 0; i < pathArry.length; i++) {
    //     if (pathArry[i].length > 0) {
    //         newPathName += "/";
    //     }
    //     newPathName += pathArry[i];
    // }
    // console.log("para: ", para);
    // console.log("protocol: ", protocol);
    // console.log("host: ", host);
    // console.log("href: ", href);
    // console.log("para1: ", para1);
    // console.log("pathArry: ", pathArry);

    // console.log("3 rsListSum.0.0.2: ", '{{ rsListSum.0.0.2 }}')


    // fetch('/process_selected').then((res) => res.json()).then((results) => {
    fetch('/pp_product_summary').then((res) => res.json()).then((results) => {

    // fetch(para).then((res) => res.json()).then((results) => {

        // console.log("results: ", results);

        const json_data = results.ppData;
        const [labels, data] = [
            Object.keys(json_data),
            Object.values(json_data),
        ];
        // renderChart([data], [labels]);
        renderChart((data), (labels));
        // renderChart([], [])
    });
};

// $("body").toggleClass("sb-sidenav-toggled");

document.onload = getChartData(); // 반드시()를 써서, 함수를 부른다.

