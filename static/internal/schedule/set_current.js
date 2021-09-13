document.addEventListener('DOMContentLoaded', function () {
    var days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    days.forEach((day) => {
        console.log(day)
        var dayContainer = document.getElementById(day + '_container');
        console.log(dayContainer)
        var hours_string = dayContainer.getAttribute("available-hours");
        console.log(hours_string)
        var availableHours = JSON.parse(hours_string);
        console.log(availableHours)

        availableHours.hours.forEach((hour) => {
            var hour_holder = document.createElement("div");

            // Append input element
            var input = document.createElement("input");
            input.type = "time";
            input.min = "08:00"
            input.max = "23:00"
            input.required = true;
            input.name = day + "_hour";
            input.value = hour
            hour_holder.appendChild(input);

            // Append delete action
            var delete_btn = document.createElement("a")
            delete_btn.innerHTML = "eliminar"
            delete_btn.href = "#"
            delete_btn.addEventListener("click", function () {
                hour_holder.parentNode.removeChild(hour_holder)
            })
            hour_holder.appendChild(delete_btn)

            // Append a line break 
            break_line = document.createElement("br")
            hour_holder.appendChild(break_line);
            dayContainer.appendChild(hour_holder)
        })

    })

})