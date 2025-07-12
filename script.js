function detectEmotion() {
  const text = document.getElementById("textInput").value;

  fetch("/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: "text=" + encodeURIComponent(text),
  })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("result").innerHTML =
        "<strong>Predicted Emotion:</strong> " + data.emotion;
    })
    .catch((error) => {
      document.getElementById("result").innerHTML =
        "Error: Could not get prediction.";
    });
}
