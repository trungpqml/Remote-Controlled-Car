document.onkeydown = function (event) {
    const key_press = String.fromCharCode(event.keyCode);
    //document.getElementById('kp').innerHTML = key_press;

    const key_code = event.keyCode;
    //document.getElementById('kc').innerHTML = key_code;

    const status = document.getElementById('status');
    //status.innerHTML = "DOWN Event Fired For : " + key_press;

    if (key_code === 38 || key_press === "W") moveUp();
    else if (key_code === 37 || key_press === "A") moveLeft();
    else if (key_code === 40 || key_press === "S") moveDown();
    else if (key_code === 39 || key_press === "D") moveRight();
    else if (key_code === 16 || key_press === "X") moveStop();
    console.log(key_press);
};

function moveUp() {
    const request = new XMLHttpRequest();
    request.open("GET", "/forward", true);
    request.send();
    console.log("Forward");
}

function moveDown() {
    const request = new XMLHttpRequest();
    request.open("GET", "/backward", true);
    request.send();
    console.log("Backward");
}

function moveLeft() {
    const request = new XMLHttpRequest();
    request.open("GET", "/left", true);
    request.send();
    console.log("Left");
}

function moveRight() {
    const request = new XMLHttpRequest();
    request.open("GET", "/right", true);
    request.send();
    console.log("Right");
}

function moveStop() {
    let request = new XMLHttpRequest();
    request.open("GET", "/stop", true);
    request.send();
    console.log("Stop");
}


// $(document).ready(distance());

// $(function () {
//     $('a#process_input').bind('click', function () {
//         $.getJSON('/background_process', {
//             proglang: $('input[name="proglang"]').val(),
//         }, function (data) {
//             $("#result").text(data.result);
//         });
//         return false;
//     });
// });

const sleep = (milliseconds) => {
    return new Promise(resolve => setTimeout(resolve, milliseconds))
};

// print distance with 1 sec sleep
let i=0, runTime = 100, range = 15;
function loopDistance() {
    setTimeout(function () {
        $(document).ready(function() {
            $.get("/get_dist",
                function (data) {
                    if (data.result>range) $('#dist').text("Object spotted");
                    else $('#dist').text("READY");
                    console.log(data.result);
                })
        });
        i++;
        if(i<runTime) loopDistance();
    }, 1000);
}
loopDistance(); //call the function for the first run

$('#dist').text("READY");

// Client must have a loop to send request (Get)
// The server receives and returns the distance accordingly
//
// Loop to print the distance
// for (let i = 0; i < 10; i++) {
//     $('#dist').click(function () {
//         $.get("/get_dist",
//             function (data) {
//                 $('#result').text(data.result);
//                 console.log(data.result);
//             })
//     });
// }