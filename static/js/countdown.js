document.addEventListener("DOMContentLoaded", function () {
    const countdownElement = document.getElementById("countdown");
    const targetDate = new Date(countdownElement.dataset.targetDate).getTime();

    const daysElement = document.getElementById("days");
    const hoursElement = document.getElementById("hours");
    const minutesElement = document.getElementById("minutes");
    const secondsElement = document.getElementById("seconds");

    const countdown = setInterval(function () {
        const now = new Date().getTime();
        const timeRemaining = targetDate - now;

        if (timeRemaining > 0) {
            const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
            const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

            daysElement.textContent = days;
            hoursElement.textContent = hours;
            minutesElement.textContent = minutes;
            secondsElement.textContent = seconds;
        } else {
            clearInterval(countdown);
            countdownElement.innerHTML = "<h3>Merry Christmas!</h3>";
        }
    }, 1000);
});
