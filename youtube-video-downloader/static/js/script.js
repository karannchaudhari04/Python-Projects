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
        // Prompt user to choose download location
        const filename = "video.mp4";
        saveAs(blob, filename);
    })
    .catch(error => {
        alert(`Error: ${error.message}`);
    });
}
