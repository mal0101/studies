document.getElementById('absolute').addEventListener('change', function() {
    document.getElementById('absoluteOptions').style.display = 'block';
});

document.getElementById('relative').addEventListener('change', function() {
    document.getElementById('absoluteOptions').style.display = 'none';
});

function applyChanges() {
    const calque = document.getElementById('calque');
    const form = document.getElementById('paramForm');

    calque.style.backgroundColor = form.color.value;
    calque.style.width = form.width.value + 'px';
    calque.style.height = form.height.value + 'px';
    calque.innerHTML = form.content.value;
    calque.style.opacity = form.opacity.value / 100;

    if (form.position.value === 'absolute') {
        calque.style.position = 'absolute';
        calque.style.top = form.top.value;
        calque.style.left = form.left.value;
    } else {
        calque.style.position = 'relative';
        calque.style.top = '0';
        calque.style.left = '0';
    }
}

function resetDefaults() {
    const calque = document.getElementById('calque');
    const form = document.getElementById('paramForm');

    calque.style.backgroundColor = '#ccc';
    calque.style.width = '200px';
    calque.style.height = '200px';
    calque.innerHTML = 'Texte par défaut';
    calque.style.opacity = '1';
    calque.style.position = 'relative';
    calque.style.top = '0';
    calque.style.left = '0';

    form.reset();
    document.getElementById('absoluteOptions').style.display = 'none';
}