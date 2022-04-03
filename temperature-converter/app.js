var celsius = document.getElementById("celsius");
var fahrenheit = document.getElementById("fahrenheit");

function cCalc() {
    var result = (parseFloat(celsius.value) * 9/5 ) + 32;
    fahrenheit.value = parseFloat(result.toFixed(2));
}

function fCalc() {
    var result = (parseFloat(fahrenheit.value) - 32) * 5/9;
    celsius.value = parseFloat(result.toFixed(2));
}