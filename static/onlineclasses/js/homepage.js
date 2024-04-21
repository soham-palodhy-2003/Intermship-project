
function changeButtonColor() {
    const buttons = document.querySelectorAll('.btn');

    buttons.forEach((button) => {
        button.addEventListener('mouseover', () => {
            button.style.backgroundColor = '#e6b800';
        });

        button.addEventListener('mouseout', () => {
            button.style.backgroundColor = 'orangered';
        });
    });
}

window.addEventListener('load', changeButtonColor);
