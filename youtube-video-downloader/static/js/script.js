function startDownload() {
    const videoLink = document.getElementById("video-link").value;
    if (!videoLink) {
        alert("Please enter a valid YouTube video link.");
        return;
    }

    fetch("/download", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body: `url=${encodeURIComponent(videoLink)}`,
    })
    .then(response => {
        if (response.ok) {
            const contentDisposition = response.headers.get('Content-Disposition');
            const filename = contentDisposition.split('filename=')[1].split(';')[0].replace(/"/g, '');
            return response.blob().then(blob => {
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = filename;
                document.body.appendChild(a);
                a.click();
                a.remove();
            });
        } else {
            return response.text().then(error => {
                alert(`Error: ${error}`);
            });
        }
    })
    .catch(error => {
        alert(`Error: ${error}`);
    });
}