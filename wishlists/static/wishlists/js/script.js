// Display confirmation modal for deleting wishlist

const deleteWishlistBtn = document.querySelector(".delete-wishlist")
const modalCloseBtn = document.querySelector(".modal-close-btn")

function showDeleteWishlistModal() {
    const modal = document.querySelector("#delete-wishlist-modal")
    modal.classList.remove("none")
    const modalCloseBtn = document.querySelector(".modal-close-btn")
    modalCloseBtn.addEventListener("click", function() {
        modal.classList.add("none")
    })
}

deleteWishlistBtn.addEventListener("click", showDeleteWishlistModal)