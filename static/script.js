function sendToPython() {
    let text = document.getElementById("inputText").value;

    fetch("/hitung", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerHTML =
            "<b>Input:</b> " + data.input + "<br>" +
            "<b>Jumlah Vokal:</b> " + data.vokal;
    })
    .catch(err => {
        document.getElementById("result").innerHTML =
            "⚠ Error: Backend Python belum dijalankan!";
    });
}
