var counter = 0
monday_adder.addEventListener("click", function () {
    var container = document.getElementById("monday_container");
    var hour_holder = document.createElement("div");
    var input = document.createElement("input");
    input.type = "time";
    input.min = "08:00"
    input.max = "23:00"
    input.required = true;
    input.name = "monday_hour" + counter;
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
    container.appendChild(hour_holder)
    counter++
});

tuesday_adder.addEventListener("click", function () {
    var container = document.getElementById("tuesday_container");
    var hour_holder = document.createElement("div");
    var input = document.createElement("input");
    input.type = "time";
    input.min = "08:00"
    input.max = "23:00"
    input.required = true;
    input.name = "tuesday_hour" + counter;
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
    container.appendChild(hour_holder)
    counter++
});

wednesday_adder.addEventListener("click", function () {
    var container = document.getElementById("wednesday_container");
    var hour_holder = document.createElement("div");
    var input = document.createElement("input");
    input.type = "time";
    input.min = "08:00"
    input.max = "23:00"
    input.required = true;
    input.name = "wednesday_hour" + counter;
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
    container.appendChild(hour_holder)
    counter++
});

thursday_adder.addEventListener("click", function () {
    var container = document.getElementById("thursday_container");
    var hour_holder = document.createElement("div");
    var input = document.createElement("input");
    input.type = "time";
    input.min = "08:00"
    input.max = "23:00"
    input.required = true;
    input.name = "thursday_hour" + counter;
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
    container.appendChild(hour_holder)
    counter++
});

friday_adder.addEventListener("click", function () {
    var container = document.getElementById("friday_container");
    var hour_holder = document.createElement("div");
    var input = document.createElement("input");
    input.type = "time";
    input.min = "08:00"
    input.max = "23:00"
    input.required = true;
    input.name = "friday_hour" + counter;
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
    container.appendChild(hour_holder)
    counter++
});
saturday_adder.addEventListener("click", function () {
    var container = document.getElementById("saturday_container");
    var hour_holder = document.createElement("div");
    var input = document.createElement("input");
    input.type = "time";
    input.min = "08:00"
    input.max = "23:00"
    input.required = true;
    input.name = "saturday_hour" + counter;
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
    container.appendChild(hour_holder)
    counter++
});
sunday_adder.addEventListener("click", function () {
    var container = document.getElementById("sunday_container");
    var hour_holder = document.createElement("div");
    var input = document.createElement("input");
    input.type = "time";
    input.min = "08:00"
    input.max = "23:00"
    input.required = true;
    input.name = "sunday_hour" + counter;
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
    container.appendChild(hour_holder)
    counter++
});