let newWindow;

        function openWindow() {
            const url = document.getElementById('adr').value;
            const width = document.getElementById('width').value || 600;
            const height = document.getElementById('height').value || 400;

            if (newWindow && !newWindow.closed) {
                newWindow.location.href = url;
            } else {
                newWindow = window.open(url, '_blank', `width=${width},height=${height}`);
            }
        }

        function closeWindow() {
            const url = document.getElementById('adr').value;
            if (newWindow && !newWindow.closed) {
                if (confirm('Are you sure you want to close the window?')) {
                    newWindow.close();
                }
            } else {
                alert('No window is open.');
            }
        }