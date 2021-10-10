document.addEventListener('DOMContentLoaded', function () {
    var initialTimeZone = Intl.DateTimeFormat().resolvedOptions().timeZone;
    var timeZoneSelectorEl = document.getElementById('time-zone-selector');
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'timeGridWeek',
        nowIndicator: true,
        timeZone: initialTimeZone,
        locale: 'es',
        height: 650,
        buttonText: {
            today: 'hoy',
            month: 'mes',
            week: 'semana',
            day: 'día',
            list: 'lista',
        },
        views: {
            timeGrid: {
                allDaySlot: false,
                slotLabelFormat: {
                    hour: 'numeric',
                    minute: '2-digit',
                    omitZeroMinute: true,
                    meridiem: 'short',
                    hour12: true
                }
            },
        },
        eventSources: [
            {
                url: '/events',
                method: 'GET',
                extraParams: {
                    user_id: "1",
                    user_type: "therapist"
                },
                failure: function () {
                    alert('¡Hubo un error consiguendo los eventos!')
                }
            }
        ],
        eventClick: function (info) {
            therapist_id = 1
            window.location.href = "/agenda_sesion/therapist/" + therapist_id + "/date_time/" + info.event.startStr + "/time_zone/" + initialTimeZone.replace("/", "*");
        },
        eventMouseEnter: function (info) {
            info.el.style.backgroundColor = "#1e5c96";
            document.body.style.cursor = 'pointer';
            // #1e5c96
        },
        eventMouseLeave: function (info) {
            info.el.style.backgroundColor = "#3788D8";
            document.body.style.cursor = 'default';
            // #3788D8
        }
    });
    calendar.render();

    var opts = {
        method: 'GET',
        headers: {}
    };
    fetch('/timezones', opts).then(function (response) {
        return response.json();
    })
        .then(function (body) {
            body.timezones.forEach(function (timeZone) {
                var optionEl;

                optionEl = document.createElement('option');
                optionEl.value = timeZone;
                optionEl.innerText = timeZone;
                timeZoneSelectorEl.appendChild(optionEl);
            });

            timeZoneSelectorEl.value = initialTimeZone;
        });

    // when the timezone selector changes, dynamically change the calendar option
    timeZoneSelectorEl.addEventListener('change', function () {
        calendar.setOption('timeZone', this.value);
        initialTimeZone = this.value;
    });
});
