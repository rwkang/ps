const renderChart = (data, labels) => {
    var ctx = document.getElementById('myChartBarProcess').getContext('2d');
    var myChartBarProcess = new Chart(ctx, {
        type: 'bar', // 'line', 'doughnut', 'pie', 'bar',
        data: {
            labels: labels, // ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
            datasets: [
                {
                    label: '당월 공정별 진도 관리', //'# of Votes', : 그래프 내부 현재 datasets에 대한 타이틀...
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
                },
                {
                    label: 'test', //'# of Votes', : 그래프 내부 현재 datasets에 대한 타이틀...
                    data: data, // [12, 19, 3, 5, 2, 3, 20, 15],

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
    console.log("fetching..."); // for Debugging...
    // console.log("pp_process_analysis.js::data: ", data);

    // fetch('') : 여기 안에는, url 이름을 적어 준다. views 이름이나 namespace 이름이 아님에 주의.
    // ***** 또한 [pp_process_analysis]가 아님에 특히 주의... JSON 데이터를 보내 주는 [pp_process_summary]임에 주의...
    fetch('/pp_process_summary').then((res) => res.json()).then((results) => {

        console.log("results: ", results);

        const json_data = results.pp_period_process_sum;
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

document.onload = getChartData() // 반드시()를 써서, 함수를 부른다.

