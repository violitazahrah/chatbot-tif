const inputName = document.getElementById("fname");
const inputTingkatan = document.getElementById("Tingkatan");
const inputKelas = document.getElementById("Kelas");
const inputDate = document.getElementById("tglisifeedback");
const inputFeedback = document.getElementById("feedback");
const btnSubmit = document.getElementById("btnSubmit");

btnSubmit.onclick = function () {
  console.log(inputName.value);
  console.log(inputTingkatan.value);
  console.log(inputKelas.value);
  console.log(inputDate.value);
  console.log(inputFeedback.value);
  setValue();
};

function setValue() {
  localStorage.setItem("nama", inputName.value);
  localStorage.setItem("tingkatan", inputTingkatan.value);
  localStorage.setItem("kelas", inputKelas.value);
  localStorage.setItem("tanggal", inputDate.value);
  localStorage.setItem("feedback", inputFeedback.value);
}
