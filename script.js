document.getElementById('generateAudio').addEventListener('click', async () => {
    const text = document.getElementById('inputText').value;
    if (!text) {
        alert('Please enter some text!');
        return;
    }

    try {
        const response = await fetch('/generate-audio', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text })
        });

        if (!response.ok) throw new Error('Error generating audio');

        const blob = await response.blob();
        const audioUrl = URL.createObjectURL(blob);
        
        const audioPlayer = document.getElementById('audioPlayer');
        audioPlayer.src = audioUrl;
        audioPlayer.style.display = 'block';

        // Download link
        const downloadLink = document.createElement('a');
        downloadLink.href = audioUrl;
        downloadLink.download = 'output.mp3';
        downloadLink.click();
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to generate audio');
    }
});