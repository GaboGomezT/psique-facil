document.addEventListener('DOMContentLoaded', function () {
    var timeZoneSelectorEl = document.getElementById('time-zone-selector');
    var retrieved_timezone = timeZoneSelectorEl.getAttribute("timezone")
    var initialTimeZone = retrieved_timezone ? retrieved_timezone : Intl.DateTimeFormat().resolvedOptions().timeZone;

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