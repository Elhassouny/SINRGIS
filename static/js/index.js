/*searchBar events*/
document.addEventListener("DOMContentLoaded", function() {
    const searchBar = document.querySelector("#searchbar");

    searchBar.addEventListener("keyup", function(e) {
        const searchQuery = e.target.value.toLowerCase();
        const boxes = document.querySelectorAll(".box");

        boxes.forEach(box => {
            const title = box.querySelector(".text h3").textContent.toLowerCase();
            if (title.includes(searchQuery)) {
                box.style.display = "block";
            } else {
                box.style.display = "none";
            }
        });
    });
});



