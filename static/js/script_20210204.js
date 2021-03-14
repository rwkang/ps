


(function($) {
    "use strict";

    // let today = new Date();
    // console.log('today: ', today);



    // Add active state to sidbar nav links : 사이드바 탐색 링크에 활성 상태 추가.
    // because the 'href' property of the DOM element is the absolute path : DOM 요소의 'href' 속성이 절대 경로이므로...
    var path = window.location.href; // because the 'href' property of the DOM element is the absolute path
    console.log('path: ', path);



    $("#layoutSidenav_nav .sb-sidenav a.nav-link").each(function() {
        $("body").toggleClass("sb-sidenav-toggled"); // 요기 라인을 추가함으로써,
        // 일단 사이드바를 [숨김]으로 출발할 수 있고, 사이드바 메뉴를 클릭했을 때도 디폴트 값이 숨김이므로,
        // 자동으로 사이드바의 어떤 메뉴를 클릭했을 때, 사이드바가 안 보이게 처리된다.
        // 마치 [숨김] 버튼을 클릭한 것과 같은 효과를 보인다.

        if (this.href === path) {
            // console.log("숨김, path: ", path);
            $(this).addClass("active");
            var current = $("body").className
            // console.log("current: ", current)
        }
    });

    // Toggle the side navigation : 사이드바 보이게 하기.
    $("#sidebarToggle").on("click", function(e) {
        e.preventDefault();
        // console.log("보임, path: ", path);
        $("body").toggleClass("sb-sidenav-toggled");
    });

    // // Toggle the side navigation : 사이드바 보이게 하기.
    // $("#sidebarToggle1").on("click", function(e) {
    //     e.preventDefault();
    //     console.log("보임, path: ", path);
    //     $("body").toggleClass("sb-nav-fixed");
    // });

})(jQuery);

function sidebarToggleClicked() {
    alert("클릭했네....");
    // var bodyClassCurrent = $('.sb-nav-fixed');
    // console.log("bodyClassCurrent: ", bodyClassCurrent);
    // if ('sb-sidenav-toggled' in bodyClassCurrent) {
    //     document.getElementsByTagName(body).classname === "sb-nav-fixed";
    // } else {
    //     document.getElementsByTagName(body).classname === "sb-nav-fixed sb-sidenav-toggled";
    // }
}


