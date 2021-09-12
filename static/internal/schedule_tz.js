document.addEventListener('DOMContentLoaded', function () {
    var initialTimeZone = Intl.DateTimeFormat().resolvedOptions().timeZone;
    var timeZoneSelectorEl = document.getElementById('time-zone-selector');
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
}
)