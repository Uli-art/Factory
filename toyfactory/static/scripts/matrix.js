/*let form = document.getElementById("matrixForm");
function handleForm(event) { event.preventDefault(); }
form.addEventListener('submit', handleForm);*/

function makeLogging(obj, fnc) {
    return (...args) => {

        let start = performance.now();
        fnc.apply(obj, args);

        let time = performance.now() - start;
        console.log('Run function ' + fnc.name + " :" + time + " ms");
    }
}

class Matrix{
    constructor() {
        this.form = document.getElementById("matrixForm");
        this.newCountElement = document.getElementById('elementCount');
        this.newCount = this.newCountElement.value;
        this.maxSelectionsElement = document.getElementById('maxSelectedElements');
        this.newMatrix = document.getElementById('matrix');
        this.currentStateOfMatrix = [];
    }

    handleForm(event) {
        event.preventDefault();
    }

    changeColor (cell) {
        if (cell.classList.contains('selected')) {
            this.cleanCell(cell);
            return;
        }

        let maxSelections = parseInt(this.maxSelectionsElement.value);
        let selectedCellsInRow = document.querySelectorAll('.selected[data-row="' + cell.parentNode.rowIndex + '"]');
        let selectedCellsInCol = document.querySelectorAll('.selected[data-col="' + cell.cellIndex + '"]');

        if (selectedCellsInRow.length >= maxSelections || selectedCellsInCol.length >= maxSelections) {
            alert('Maximum selection limit');
            return;
        }

        let cellIndex = cell.cellIndex;
        let rowIndex = cell.parentNode.rowIndex;

        for (let selectedCell of selectedCellsInRow) {
            let selectedCellIndex = selectedCell.cellIndex;
            if (Math.abs(selectedCellIndex - cellIndex) === 1) {
                alert('Cannot select neighbors');
                return;
            }
        }

        for (let selectedCell of selectedCellsInCol) {
            let selectedRowIndex = selectedCell.parentNode.rowIndex;
            if (Math.abs(selectedRowIndex - rowIndex) === 1) {
                alert('Cannot select neighbors');
                return;
            }
        }

        cell.classList.add('selected');
        cell.setAttribute('data-row', rowIndex);
        cell.setAttribute('data-col', cellIndex);

        let num = parseInt(cell.innerHTML);
        if (num % 2 === 0) {
            cell.style.backgroundColor = "#ffdbf8"
        } else {
            cell.style.backgroundColor = "#cdffb9"
        }
    }

    changeCount() {
        this.newCountElement = document.getElementById('elementCount');
        this.newCount = this.newCountElement.value;

        while (this.newMatrix.rows.length > 0) {
            this.newMatrix.deleteRow(0);
        }
        this.currentStateOfMatrix = Array(this.newCount);

        for (let i = 0; i < this.newCount; ++i) {
            let row = this.newMatrix.insertRow(i);
            this.currentStateOfMatrix[i] = [];
            for (let j = 0; j < this.newCount; ++j) {
                let cell = row.insertCell(j);
                let tempValue = Math.floor(Math.random() * 10);
                cell.innerHTML = tempValue.toString();
                this.currentStateOfMatrix[i][j] = tempValue;
                cell.addEventListener('click', () => this.changeColor(cell));
            }
        }
    }

    transposeMatrix() {
        this.currentStateOfMatrix = this.currentStateOfMatrix[0].map(
            (col, i) => this.currentStateOfMatrix.map(row => row[i]));

        const newMatrix = document.getElementById('matrix');

        for (let i = 0; i < this.newCount; ++i) {
            for (let j = 0; j < this.newCount; ++j) {
                let cell = newMatrix.rows[i].cells[j];
                cell.innerHTML = this.currentStateOfMatrix[i][j].toString();
                this.cleanCell(cell);
            }
        }
    }

    cleanCell (cell) {
        if (cell.classList.contains('selected')) {
            cell.classList.remove('selected');
            cell.style.backgroundColor = '';
        }
    }

    addRowColumn() {
        let newArray = Array(this.newCount + 1);

        for (let i = 0; i <= this.newCount; ++i) {
            newArray[i] = [];
        }

        for (let i = 0; i < this.currentStateOfMatrix.length; i++) {
            newArray[i] = this.currentStateOfMatrix[i].slice();
        }

        this.currentStateOfMatrix = newArray;
        let newRow = this.newMatrix.insertRow(this.newMatrix.rows.length);
        this.currentStateOfMatrix[this.newMatrix.rows.length] = [];
        for (let i = 0; i < this.newMatrix.rows[0].cells.length; i++) {
            let cell = newRow.insertCell(i);
            let tempValue = Math.floor(Math.random() * 10);
            cell.innerHTML = tempValue.toString();
            this.currentStateOfMatrix[this.newMatrix.rows.length - 1][i] = tempValue;
            cell.addEventListener('click', () => this.changeColor(cell));
        }

        for (let i = 0; i < this.newMatrix.rows.length; i++) {
            let cell = this.newMatrix.rows[i].insertCell(this.newMatrix.rows[i].cells.length);

            let tempValue = Math.floor(Math.random() * 10);
            cell.innerHTML = tempValue.toString();
            this.currentStateOfMatrix[i][this.newMatrix.rows[i].cells.length - 1] = tempValue;

            cell.addEventListener('click', () => this.changeColor(cell));
        }
        ++this.newCount;
    }

}

class MatrixChanger extends Matrix {
     constructor() {
         super();
         this.transposeMatrix = makeLogging(this, this.transposeMatrix);
         this.changeColor = makeLogging(this, this.changeColor);
         this.form.addEventListener('submit', this.handleForm.bind(this));
         this.newCountElement.addEventListener('click', this.changeCount.bind(this));
         //this.maxSelectionsElement.addEventListener('click', this.transposeMatrix.bind(this.matrix));
         document.getElementById('transposeButton').addEventListener('click', this.transposeMatrix.bind(this));
         document.getElementById('addElements').addEventListener('click', this.addRowColumn.bind(this));
     }
}

const changer = new MatrixChanger();


/*
function Matrix() {
    this.form = document.getElementById("matrixForm");
    this.newCountElement = document.getElementById('elementCount');
    this.newCount = this.newCountElement.value;
    this.maxSelectionsElement = document.getElementById('maxSelectedElements');
    this.newMatrix = document.getElementById('matrix');
    this.currentStateOfMatrix = [];
}

Matrix.prototype.handleForm = function(event) {
        event.preventDefault();
}

Matrix.prototype.changeColor = function(cell) {
    if (cell.classList.contains('selected')) {
        this.cleanCell(cell);
        return;
    }

    let maxSelections = parseInt(this.maxSelectionsElement.value);
    let selectedCellsInRow = document.querySelectorAll('.selected[data-row="' + cell.parentNode.rowIndex + '"]');
    let selectedCellsInCol = document.querySelectorAll('.selected[data-col="' + cell.cellIndex + '"]');

    if (selectedCellsInRow.length >= maxSelections || selectedCellsInCol.length >= maxSelections) {
        alert('Maximum selection limit');
        return;
    }

    let cellIndex = cell.cellIndex;
    let rowIndex = cell.parentNode.rowIndex;

    for (let selectedCell of selectedCellsInRow) {
        let selectedCellIndex = selectedCell.cellIndex;
        if (Math.abs(selectedCellIndex - cellIndex) === 1) {
            alert('Cannot select neighbors');
            return;
        }
    }

    for (let selectedCell of selectedCellsInCol) {
        let selectedRowIndex = selectedCell.parentNode.rowIndex;
        if (Math.abs(selectedRowIndex - rowIndex) === 1) {
            alert('Cannot select neighbors');
            return;
        }
    }

    cell.classList.add('selected');
    cell.setAttribute('data-row', rowIndex);
    cell.setAttribute('data-col', cellIndex);

    let num = parseInt(cell.innerHTML);
    if (num % 2 === 0) {
        cell.style.backgroundColor = "#ffdbf8"
    } else {
        cell.style.backgroundColor = "#cdffb9"
    }
}

Matrix.prototype.changeCount = function() {
    this.newCountElement = document.getElementById('elementCount');
    this.newCount = this.newCountElement.value;

    while (this.newMatrix.rows.length > 0) {
        this.newMatrix.deleteRow(0);
    }
    this.currentStateOfMatrix = Array(this.newCount);

    for (let i = 0; i < this.newCount; ++i) {
        let row = this.newMatrix.insertRow(i);
        this.currentStateOfMatrix[i] = [];
        for (let j = 0; j < this.newCount; ++j) {
            let cell = row.insertCell(j);
            let tempValue = Math.floor(Math.random() * 10);
            cell.innerHTML = tempValue.toString();
            this.currentStateOfMatrix[i][j] = tempValue;
            cell.addEventListener('click', () => this.changeColor(cell));
        }
    }
}

Matrix.prototype.cleanCell = function (cell) {
    if (cell.classList.contains('selected')) {
        cell.classList.remove('selected');
        cell.style.backgroundColor = '';
    }
}

Matrix.prototype.transposeMatrix = function () {
    this.currentStateOfMatrix = this.currentStateOfMatrix[0].map(
        (col, i) => this.currentStateOfMatrix.map(row => row[i]));

    const newMatrix = document.getElementById('matrix');

    for (let i = 0; i < this.newCount; ++i) {
        for (let j = 0; j < this.newCount; ++j) {
            let cell = newMatrix.rows[i].cells[j];
            cell.innerHTML = this.currentStateOfMatrix[i][j].toString();
            this.cleanCell(cell);
        }
    }
}

Matrix.prototype.addRowColumn = function() {
    let newArray = Array(this.newCount + 1);

    for (let i = 0; i <= this.newCount; ++i) {
        newArray[i] = [];
    }

    for (let i = 0; i < this.currentStateOfMatrix.length; i++) {
        newArray[i] = this.currentStateOfMatrix[i].slice();
    }

    this.currentStateOfMatrix = newArray;
    let newRow = this.newMatrix.insertRow(this.newMatrix.rows.length);
    this.currentStateOfMatrix[this.newMatrix.rows.length] = [];
    for (let i = 0; i < this.newMatrix.rows[0].cells.length; i++) {
        let cell = newRow.insertCell(i);
        let tempValue = Math.floor(Math.random() * 10);
        cell.innerHTML = tempValue.toString();
        this.currentStateOfMatrix[this.newMatrix.rows.length - 1][i] = tempValue;
        cell.addEventListener('click', () => this.changeColor(cell));
    }

    for (let i = 0; i < this.newMatrix.rows.length; i++) {
        let cell = this.newMatrix.rows[i].insertCell(this.newMatrix.rows[i].cells.length);

        let tempValue = Math.floor(Math.random() * 10);
        cell.innerHTML = tempValue.toString();
        this.currentStateOfMatrix[i][this.newMatrix.rows[i].cells.length - 1] = tempValue;

        cell.addEventListener('click', () => this.changeColor(cell));
    }
    ++this.newCount;
}

function MatrixChanger() {
    Matrix.call(this);
}

MatrixChanger.prototype = Object.create(Matrix.prototype);
MatrixChanger.prototype.constructor = MatrixChanger;

MatrixChanger.prototype.initializer = function () {
    this.form.addEventListener('submit', this.handleForm.bind(this));
    this.newCountElement.addEventListener('click', this.changeCount.bind(this));
    //this.maxSelectionsElement.addEventListener('click', this.transposeMatrix.bind(this.matrix));
    document.getElementById('transposeButton').addEventListener('click', this.transposeMatrix.bind(this));
    document.getElementById('addElements').addEventListener('click', this.addRowColumn.bind(this));
};

const changer = new MatrixChanger();
changer.initializer();
*/







/*

function changeColor (cell) {
    if (cell.classList.contains('selected')) {
        cleanCell(cell);
        return;
    }

    let maxSelections = parseInt(maxSelectionsElement.value);
    let selectedCellsInRow = document.querySelectorAll('.selected[data-row="' + cell.parentNode.rowIndex + '"]');
    let selectedCellsInCol = document.querySelectorAll('.selected[data-col="' + cell.cellIndex + '"]');

    if (selectedCellsInRow.length >= maxSelections || selectedCellsInCol.length >= maxSelections) {
        alert('Maximum selection limit');
        return;
    }

    let cellIndex = cell.cellIndex;
    let rowIndex = cell.parentNode.rowIndex;

    for (let selectedCell of selectedCellsInRow) {
        let selectedCellIndex = selectedCell.cellIndex;
        if (Math.abs(selectedCellIndex - cellIndex) === 1) {
            alert('Cannot select neighbors');
            return;
        }
    }

    for (let selectedCell of selectedCellsInCol) {
        let selectedRowIndex = selectedCell.parentNode.rowIndex;
        if (Math.abs(selectedRowIndex - rowIndex) === 1) {
            alert('Cannot select neighbors');
            return;
        }
    }

    cell.classList.add('selected');
    cell.setAttribute('data-row', rowIndex);
    cell.setAttribute('data-col', cellIndex);

    let num = parseInt(cell.innerHTML);
    if (num % 2 === 0) {
        cell.style.backgroundColor = "#ffdbf8"
    } else {
        cell.style.backgroundColor = "#cdffb9"
    }
}

function changeCount() {
    newCountElement = document.getElementById('elementCount');
    newCount = newCountElement.value;

    while (newMatrix.rows.length > 0) {
        newMatrix.deleteRow(0);
    }
    currentStateOfMatrix = Array(newCount);

    for (let i = 0; i < newCount; ++i) {
        let row = newMatrix.insertRow(i);
        currentStateOfMatrix[i] = [];
        for (let j = 0; j < newCount; ++j) {
            let cell = row.insertCell(j);
            let tempValue = Math.floor(Math.random() * 10);
            cell.innerHTML = tempValue.toString();
            currentStateOfMatrix[i][j] = tempValue;
            cell.addEventListener('click', () => this.changeColor(cell));
        }
    }
}

function transposeMatrix(){
    currentStateOfMatrix = currentStateOfMatrix[0].map(
        (col, i) => currentStateOfMatrix.map(row => row[i]));

    const newMatrix = document.getElementById('matrix');

    for (let i = 0; i < newCount; ++i) {
        for (let j = 0; j < newCount; ++j) {
            let cell = newMatrix.rows[i].cells[j];
            cell.innerHTML = currentStateOfMatrix[i][j].toString();
            cleanCell(cell);
        }
    }
    console.log(currentStateOfMatrix);
}

function cleanCell (cell) {
    if (cell.classList.contains('selected')) {
        cell.classList.remove('selected');
        cell.style.backgroundColor = '';
    }
}

function addRowColumn() {
    let newArray = Array(newCount + 1);

    for (let i = 0; i <= newCount; ++i) {
        newArray[i] = [];
    }

    for (let i = 0; i < currentStateOfMatrix.length; i++) {
        newArray[i] = currentStateOfMatrix[i].slice();
    }
    console.log(currentStateOfMatrix);
    console.log(newArray);
    currentStateOfMatrix = newArray;
    let newRow = newMatrix.insertRow(newMatrix.rows.length);
    currentStateOfMatrix[newMatrix.rows.length] = [];
    for (let i = 0; i < newMatrix.rows[0].cells.length; i++) {
        let cell = newRow.insertCell(i);
        let tempValue = Math.floor(Math.random() * 10);
        cell.innerHTML = tempValue.toString();
        console.log(currentStateOfMatrix[newMatrix.rows.length][i]);
        currentStateOfMatrix[newMatrix.rows.length-1][i] = tempValue;
        console.log(currentStateOfMatrix[newMatrix.rows.length][i]);
        cell.addEventListener('click', () => this.changeColor(cell));
    }

     for (let i = 0; i < newMatrix.rows.length; i++) {
        let cell = newMatrix.rows[i].insertCell(newMatrix.rows[i].cells.length);

        let tempValue = Math.floor(Math.random() * 10);
        cell.innerHTML = tempValue.toString();
        console.log(currentStateOfMatrix[i][newMatrix.rows[i].cells.length]);
        currentStateOfMatrix[i][newMatrix.rows[i].cells.length-1] = tempValue;
        console.log(currentStateOfMatrix[i][newMatrix.rows[i].cells.length]);

        cell.addEventListener('click', () => this.changeColor(cell));
    }

    ++newCount;
    console.log(currentStateOfMatrix);
}
*/

