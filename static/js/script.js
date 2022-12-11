const inputName = document.getElementById("fname");
const inputTingkatan = document.getElementById("Tingkatan");
const inputKelas = document.getElementById("Kelas");
const inputDate = document.getElementById("tglisifeedback");
const inputFeedback = document.getElementById("feedback");
const btnSubmit = document.getElementById("btnSubmit");

function setValue() {
  localStorage.setItem("nama", inputName.value);
  localStorage.setItem("tingkatan", inputTingkatan.value);
  localStorage.setItem("kelas", inputKelas.value);
  localStorage.setItem("feedback", inputFeedback.value);
}

function postData() {
  fetch("https://6394605a4df9248eada048fe.mockapi.io/feedBack", {
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      nama: localStorage.getItem("nama"),
      tingkatan: localStorage.getItem("tingkatan"),
      kelas: localStorage.getItem("kelas"),
      feedback: localStorage.getItem("feedback"),
    }),
  });
  localStorage.clear();
}

function clearData() {
  inputName.value = "";
  inputTingkatan.value = "";
  inputKelas.value = "";
  inputDate.value = "";
  inputFeedback.value = "";
  return alert("Feedback kamu berhasil dikirim");
}

btnSubmit.onclick = function () {
  setValue();
  postData();
  return clearData();
};
