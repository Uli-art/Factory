const newBirthDate = document.getElementById('birthDay');

function changeDate() {
  let now = new Date();
  let today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
  let birthDate = new Date(newBirthDate.value);
  let age = today.getFullYear() - birthDate.getFullYear();
  console.log(today)
  if (today < birthDate) {
    --age;
  }
  if (age >= 18) {
    let day = getWeekDay(birthDate);
    alert(`Age: ${age}. Day of a week: ${day}`)
    document.querySelector('#submitButton').disabled = false;
  }
  else {
    alert('You need your parents\' permission!')
    document.querySelector('#submitButton').disabled = true;
  }

}

function getWeekDay(date) {
  let days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
  return days[date.getDay()];
}
