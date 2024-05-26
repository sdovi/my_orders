document.addEventListener("DOMContentLoaded", function() {
    const profileCube = document.querySelector(".profile__cube");
    const modalOverlay = document.getElementById("modalOverlay");
    const modalContent = document.getElementById("modalContent");
    const editProductForm = document.getElementById("editProductForm");

    profileCube.addEventListener("click", function() {
        modalOverlay.style.display = "block";
        modalContent.style.display = "block";
    });

    modalOverlay.addEventListener("click", function() {
        modalOverlay.style.display = "none";
        modalContent.style.display = "none";
    });

    editProductForm.addEventListener("submit", function(event) {
        event.preventDefault();

        const formData = new FormData(editProductForm);
        const productData = {};
        formData.forEach((value, key) => {
            productData[key] = value;
        });

        fetch("http://localhost:3000/products", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(productData)
        })
        .then(response => response.json())
        .then(data => {
            console.log("Успех:", data);
            modalOverlay.style.display = "none";
            modalContent.style.display = "none";
        })
        .catch(error => {
            console.error("Ошибка:", error);
        });
    });
});