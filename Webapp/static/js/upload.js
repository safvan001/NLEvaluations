const dropContainer = document.getElementById('drop-container');
const fileInput = document.getElementById('file-input');

dropContainer.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropContainer.classList.add('drag-over');
});

dropContainer.addEventListener('dragleave', (e) => {
    e.preventDefault();
    dropContainer.classList.remove('drag-over');
});

dropContainer.addEventListener('drop', (e) => {
    e.preventDefault();
    dropContainer.classList.remove('drag-over');
    handleFiles(e.dataTransfer.files);
});

fileInput.addEventListener('change', (e) => {
    handleFiles(fileInput.files);
});

function handleFiles(files) {
    const imageType = /^image\//;

    for (const file of files) {
        if (imageType.test(file.type)) {
            const img = document.createElement('img');
            img.classList.add('preview-img');
            img.file = file;

            const reader = new FileReader();
            reader.onload = (function(aImg) {
                return function(e) {
                    aImg.src = e.target.result;
                    dropContainer.appendChild(aImg);
                };
            })(img);

            reader.readAsDataURL(file);
        }
    }
}
