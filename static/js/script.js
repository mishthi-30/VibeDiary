document.addEventListener("DOMContentLoaded", function () {

    const darkModeButton = document.getElementById("darkModeToggle");

    // Apply saved theme when page loads
    const savedTheme = localStorage.getItem("theme");

    if (savedTheme === "dark") {
        document.body.classList.add("dark-mode");

        if (darkModeButton) {
            darkModeButton.innerHTML = "☀️ Light Mode";
        }
    }

    // Dark mode button
    if (darkModeButton) {

        darkModeButton.addEventListener("click", function () {

            document.body.classList.toggle("dark-mode");

            if (document.body.classList.contains("dark-mode")) {

                localStorage.setItem("theme", "dark");
                darkModeButton.innerHTML = "☀️ Light Mode";

            } else {

                localStorage.setItem("theme", "light");
                darkModeButton.innerHTML = "🌙 Dark Mode";

            }

        });

    }

});