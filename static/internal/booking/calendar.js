document.addEventListener('DOMContentLoaded', function () {
    var initialTimeZone = Intl.DateTimeFormat().resolvedOptions().timeZone;
    var timeZoneSelectorEl = document.getElementById('time-zone-selector');
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        nowIndicator: true,
        timeZone: initialTimeZone,
        locale: 'es',
        height: 650,
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek'
        },
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
        events: [
            {
                title: 'event1',
                start: '2021-09-11T12:30:00',
                allDay: false
            },
            {
                title: 'event1.5',
                start: '2021-09-11T13:30:00',
                allDay: false
            },
            {
                title: 'event2',
                start: '2021-09-12T12:30:00',
                end: '2021-09-12T13:30:00',
                allDay: false
            },
            {
                title: 'event3',
                start: '2021-09-14T12:30:00',
                allDay: false // will make the time show
            }
        ]
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
    });
});
