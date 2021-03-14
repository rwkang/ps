// 사용 변수
const GAME_TIME = 9;

let score = 0;
let time = GAME_TIME;
let isPlaying = false;
let timeInterval;
let checkInterval;
let words = [];

const wordInput = document.querySelector('.word-input');
const wordDisplay = document.querySelector('.word-display');
const scoreDisplay = document.querySelector('.score');
const timeDisplay = document.querySelector('.time');
const button = document.querySelector('.button');

// 초기 값으로 자동 실행되게 한다.
init();

function init(){
    buttonChange('게임 로딩중...');
    getWords();
    wordInput.addEventListener('input', checkMatch);
}

// 게임 실행
function run() {
    if (isPlaying) {
        return; // 게임 실행중에는 버튼이 안 눌러지게...
    }
    isPlaying = true; // init()에서 false로 세팅했기 때문에, run().게임시작 했을 때, isPlaying 값을 true로 변경...
    time = GAME_TIME;
    wordInput.focus(); // 게임시작 버튼 클릭시, 즉시 input 박스 안으로 커서를 이동 *****
    scoreDisplay.innerText = 0; // 점수 텍스트를 [0]으로 초기화...
    timeInterval = setInterval(countDown, 1000);
    checkInterval = setInterval(checkStatus, 50); // 50 마이크로 초마다, 게임 상태 체크...
    buttonChange('게임중'); // 버튼 텍스트를 '게임중'으로 변경...
}

function checkStatus() {
    if(!isPlaying && time === 0) {
        buttonChange('게임시작'); // 게임이 종료가 되면, 게임을 시작 할 수 있도록, 버튼 텍스트를 '게임시작'으로 변경해야 한다.
        clearInterval(checkInterval);
    }
}
// 단어 불러 오기
// 단어 불러 오는 랜덤 api site...[https://random-word-api.herokuapp.com/word?number=100] : number=100 : 100개 단어 불러오기.
// axios 라이브러리 활용 : 1. npn 설치, 2. CDN 링크 활용 : <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
// words = ['Hello', 'Banana', 'Apple', 'Cherry'];
function getWords() {
    axios.get("https://random-word-api.herokuapp.com/word?number=100")
        .then(function (response) {
            response.data.forEach((word) => {
                if (word.length < 10) {
                    words.push(word);
                }
            })
            buttonChange('게임시작');
        })
        .catch(function (error) {
            console.log(error);
        })
    // words = ['Hello', 'Banana', 'Apple', 'Cherry'];
}

// 단어 일치 체크
function checkMatch(){
    if(wordInput.value.toLowerCase() === wordDisplay.innerText.toLowerCase()){
        wordInput.value = "";
        if (!isPlaying) {
            return;
        }
        score++;
        scoreDisplay.innerText = score;
        time = GAME_TIME;
        const randomIndex = Math.floor(Math.random() * words.length); // floor : 소숫점 짜르기...
        wordDisplay.innerText = words[randomIndex]
    }
}

// wordInput.addEventListener('input', () => {
//     if(wordInput.value.toLowerCase() === wordDisplay.innerText.toLowerCase()){
//         score++;
//         scoreDisplay.innerText = score;
//         wordInput.value = "";
//     }
//})

// setInterval(countDown, 1000);
// buttonChange('게임시작') // 게임종료



function countDown() {
    // (조건) ? 참일 경우 : 거짓일 경우 :: 3항 연산자
    time > 0 ? time -- : isPlaying = false;
    if (!isPlaying){
        clearInterval(timeInterval) // 게임종료...
    }
    timeDisplay.innerText = time;
}


function buttonChange(text) {
    button.innerText = text;
    text === '게임시작' ? button.classList.remove('loading') : button.classList.add('loading')
}