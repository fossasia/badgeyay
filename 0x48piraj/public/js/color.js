function changeColor() {
  var col = document.getElementById("in").value;
  document.getElementById("wrapper").style.backgroundColor = col;
  document.getElementById("wrapper").style.transition = "all 3s";
}