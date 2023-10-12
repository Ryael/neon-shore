/* Profile Sidebar */

window.addEventListener("load", event => {

    // Expand Left Side
    var icon = document.querySelector('.profile-hamburger'),
        left = document.querySelector('.profile-navigation');


    icon.addEventListener('click', expand);

    function expand() {
        if (left.classList.contains('show')) {
            left.classList.remove('show')
        } else {
            left.classList.add('show')
        }
    }
});
