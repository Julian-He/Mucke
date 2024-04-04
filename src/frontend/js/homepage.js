const navElements = [
    document.getElementById("libraryNav"),
    document.getElementById("reviewDropdownNav"),
    document.getElementById("friendsNav")
]

for (i=0; i<=navElements.length; i++) {
    navElements[i].ariaDisabled = false
    navElements[i].classList.remove("disabled")
}