document.addEventListener("DOMContentLoaded", () => {
    const findBedLink = document.getElementById("find-bed");
    const dropdown = document.getElementById("district-dropdown");
    findBedLink.onclick = event => {
        event.preventDefault();
        dropdown.classList.add("show")
    }
});

window.onclick = function (event) {
    if (!event.target.matches('#find-bed')) {
        console.log("here")
        var dropdowns = document.getElementsByClassName("district-dropdown");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}