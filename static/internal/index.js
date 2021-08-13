datePicker.addEventListener("input", function (e) {
    console.log(this.value)
    var message = document.getElementById("my-script").getAttribute("message")
    var available_dates_str = document.getElementById("my-script").getAttribute("available_dates")
    var available_dates = JSON.parse(available_dates_str);
    console.log(message)
    console.log(available_dates)
    console.log(typeof available_dates)
    dates_open = available_dates[this.value]
    console.log(dates_open)
    user_message = dates_open ? "Sí hay citas abiertas para este día" : "No hay horas disponible"
    console.log(user_message)
});