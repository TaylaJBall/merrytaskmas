document.addEventListener("DOMContentLoaded", function () {
    const countdownElement = document.getElementById("countdown");
    if (!countdownElement) return;

    // Get the target date from the data attribute
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

            // Display the countdown
            countdownElement.innerHTML = `
                ${days} Days : ${hours} Hours : ${minutes} Minutes : ${seconds} Seconds
            `;
        } else {
            // When countdown is complete
            clearInterval(countdown);
            countdownElement.innerHTML = "Merry Christmas!";
        }
    }, 1000);
});
