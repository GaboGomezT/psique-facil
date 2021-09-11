document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
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
                start: '2021-08-29T12:30:00',
                allDay: false
            },
            {
                title: 'event1.5',
                start: '2021-08-29T13:30:00',
                allDay: false
            },
            {
                title: 'event2',
                start: '2021-08-30T12:30:00',
                end: '2021-08-30T13:30:00',
                allDay: false
            },
            {
                title: 'event3',
                start: '2021-09-01T12:30:00',
                allDay: false // will make the time show
            }
        ]
    });
    calendar.render();
});
