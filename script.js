function send() {
    let text = document.getElementById("input").value;

    if (!text) {
        alert("Please enter or speak an emergency!");
        return;
    }

    document.getElementById("output").innerHTML = "⏳ Analyzing...";

    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("output").innerHTML = `
            <b>⚠️ Emergency:</b> ${data.type} <br><br>
            <b>💡 Solution:</b> ${data.solution}
        `;
    })
    .catch(err => {
        document.getElementById("output").innerHTML = "❌ Error connecting to server";
    });
}

/* 🎤 VOICE FUNCTION */
function startVoice() {
    if (!('webkitSpeechRecognition' in window)) {
        alert("Your browser does not support voice recognition. Use Chrome.");
        return;
    }

    let recognition = new webkitSpeechRecognition();
    recognition.lang = "en-US";
    recognition.start();

    document.getElementById("output").innerHTML = "🎤 Listening...";

    recognition.onresult = function(event) {
        let speech = event.results[0][0].transcript;
        document.getElementById("input").value = speech;

        document.getElementById("output").innerHTML =
            "✅ Heard: " + speech;
    };

    recognition.onerror = function() {
        document.getElementById("output").innerHTML =
            "❌ Voice recognition failed";
    };
}