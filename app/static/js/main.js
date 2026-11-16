document.addEventListener("DOMContentLoaded", function () {
  var messages = document.querySelectorAll(".flash-success, .flash-info");
  messages.forEach(function (msg) {
    setTimeout(function () {
      msg.style.opacity = "0";
      setTimeout(function () { msg.remove(); }, 400);
    }, 6000);
  });
});
