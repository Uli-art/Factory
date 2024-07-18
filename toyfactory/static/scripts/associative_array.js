let authorizationDateElement  = document.getElementById('authorizationDate');
let numberOfReaderBookElement  = document.getElementById('numberOfReaderBook');
let nameElement  = document.getElementById('name');
let surnameElement  = document.getElementById('surname');
let patronymicElement  = document.getElementById('patronymic');
let readersTable = document.getElementById('readers');
let oldestReaderElement = document.getElementById('oldestReader');

let readersForm = document.getElementById("addReader");
function handleForm(event) { event.preventDefault(); }
readersForm.addEventListener('submit', handleForm);

let readers = new Map();

function AddReader() {
    let authorizationDate = new Date(authorizationDateElement.value);

    let numberOfReaderBook = numberOfReaderBookElement.value;
    let name = nameElement.value;
    let surname = surnameElement.value;
    let patronymic = patronymicElement.value;

    let key = surname.toString() + " " + name.toString() + " "  + patronymic.toString();
    let arr = readers.get(key);
    if (arr === undefined) {
        readers.set(key, [authorizationDate]);
    } else {
        alert("added existing reader");
        return;
    }
    authorizationDateElement.value = "";
    numberOfReaderBookElement.value = "";
    nameElement.value = "";
    surnameElement.value = "";
    patronymicElement.value = "";
    let authorizationDateFormat = authorizationDate.getFullYear() + "-" +  authorizationDate.getMonth() + "-" + authorizationDate.getDate();


    let newRow = readersTable.insertRow(readersTable.rows.length);
    let cell1 = newRow.insertCell(0);
    let cell2 = newRow.insertCell(1);
    let cell3 = newRow.insertCell(2);
    let cell4 = newRow.insertCell(3);
    let cell5 = newRow.insertCell(4);
    cell1.innerHTML = name;
    cell2.innerHTML = surname;
    cell3.innerHTML = patronymic;
    cell4.innerHTML = numberOfReaderBook.toString();
    cell5.innerHTML = authorizationDateFormat;
    console.log(readers);
    getOldestReader();
}

function getOldestReader() {
    oldestReaderElement.innerHTML = "";
    let oldestReader = [...readers.entries()].reduce((accumulator, element) => {
  return new Date(element[1]) < new Date(accumulator[1]) ? element : accumulator;});

    oldestReaderElement.innerHTML = oldestReader[0] + " Date: " + oldestReader[1][0].getFullYear() + "-" +  oldestReader[1][0].getMonth() + "-" + oldestReader[1][0].getDate();
}