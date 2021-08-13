datePicker.addEventListener("input", function (e) {
    console.log(this.value)
    var message = document.getElementById("my-script").getAttribute("message")
    console.log(message)
});