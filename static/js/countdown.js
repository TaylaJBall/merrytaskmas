document.addEventListener("DOMContentLoaded", function () {
    const countdownElement = document.getElementById("countdown");
    if (!countdownElement) return;

    // Get the target date
    const targetDate = new Date(countdownElement.dataset.targetDate).getTime();

    // Update the countdown every second
    const countdown = setInterval(function () {
        const now = new Date().getTime();
        const timeRemaining = targetDate - now;

        if (timeRemaining > 0) {
            // Calculate days, hours, minutes, and seconds
            const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
            const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

            // Update countdown display
            countdownElement.innerHTML = `
                <div class="row">
                    <div class="col-3"><strong>Days</strong><br>${days}</div>
                    <div class="col-3"><strong>Hours</strong><br>${hours}</div>
                    <div class="col-3"><strong>Minutes</strong><br>${minutes}</div>
                    <div class="col-3"><strong>Seconds</strong><br>${seconds}</div>
                </div>
            `;
        } else {
            // Stop the countdown and display the message
            clearInterval(countdown);
            countdownElement.innerHTML = "<h3>Merry Christmas!</h3>";
        }
    }, 1000);
});
