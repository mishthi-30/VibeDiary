document.addEventListener("DOMContentLoaded", function () {

    const themeToggle = document.getElementById("theme-toggle");

    // Load saved theme
    const savedTheme = localStorage.getItem("theme");

    if (savedTheme === "dark") {
        document.body.classList.add("dark-mode");

        if (themeToggle) {
            themeToggle.textContent = "☀️ Light Mode";
        }
    }

    // Toggle theme
    if (themeToggle) {

        themeToggle.addEventListener("click", function () {

            document.body.classList.toggle("dark-mode");

            if (document.body.classList.contains("dark-mode")) {

                localStorage.setItem("theme", "dark");
                themeToggle.textContent = "☀️ Light Mode";

            } else {

                localStorage.setItem("theme", "light");
                themeToggle.textContent = "🌙 Dark Mode";

            }

        });

    }

});