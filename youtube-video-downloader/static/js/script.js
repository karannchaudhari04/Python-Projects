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
            return response.blob();
        } else {
            throw new Error(`Server responded with ${response.status}`);
        }
    })
    .then(blob => {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = "video.mp4"; // Set default filename
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    })
    .catch(error => {
        alert(`Error: ${error.message}`);
    });
}
