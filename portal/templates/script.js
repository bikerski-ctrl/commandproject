function openModal(element) {
    var modal = document.getElementById("myModal");
    var modalImg = document.getElementById("img01");
    modal.style.display = "block";
    modalImg.src = element.src;
}

function closeModal() {
    var modal = document.getElementById("myModal");
    modal.style.display = "none";
}