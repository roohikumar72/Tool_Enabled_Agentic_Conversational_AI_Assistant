// function send() {
//   const message = document.getElementById("input").value;

//   fetch("http://127.0.0.1:5000/chat", {
//   method: "POST",
//   headers: { "Content-Type": "application/json" },
//   body: JSON.stringify({ message: userMessage })
// })
// .then(res => res.json())
// .then(data => {
//     document.getElementById("output").innerText =
//       JSON.stringify(data, null, 2);
//   });
// }
function send() {
  const message = document.getElementById("input").value;

  fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: message })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("output").innerText =
      data.reply;
  });

  document.getElementById("input").value = "";
}
