
const keys = [
    'name', 'diameter', 'climate', 'terrain', 'surface_water', 'population', 'residents', 'vote'
];

const charKeys = [
    "name", "height", "mass", "hair_color", "skin_color", "eye_color", "birth_year", "gender"
];

const tableInsert = document.getElementById('tbody');
let tr = '<tr>';
let endTr = '</tr>';


let displayPage = function f(planetsData) {
    planetsData.forEach(row => {
        for (i = 0; i < keys.length; i++){
            if (keys[i] === 'vote'){
                tr += `<td> <button class="btn btn-secondary vote" type="button"> Vote </button></td>`;;
            }
            else if (keys[i] != 'residents') {
                tr += `<td> ${row[keys[i]]} </td>`;
            }
            else if (row['residents'] != '') {
                tr += `<td> <button class="btn btn-primary residents" data-api-inputs="${row['residents']}" type="button">Residents ${row['residents'].length} </button></td>`;
            }
            else {
                tr += `<td> ${row[keys[i]]} </td>`
            }
        }
        tr+=endTr
    });
    tableInsert.innerHTML += tr + endTr
    };




let inputApi = 'https://swapi.co/api/planets/';
let nextInputApi = "";
let prevInputApi = "";

let planetsData = function (inputApi){
    fetch(inputApi)
        .then((response) => response.json())
        .then((data) => {
            nextInputApi = data.next;
            prevInputApi = data.previous;
            displayPage(data.results);
            showResidents()
        })
};

planetsData(inputApi);

// add to main


let nextButton = document.getElementById('next');
let prevButton = document.getElementById('prev');

nextButton.addEventListener('click', function (event) {
       for (i=0; i<10; i++) {
           document.getElementById("tbody").deleteRow(-1);
           tr = '<tr>';
       }
    planetsData(nextInputApi)
});

prevButton.addEventListener('click', function (event) {
    tableInsert.innerHTML = "";
    tr = '<tr>';
    planetsData(prevInputApi)
});


let showResidents = function () {
    let residents = document.querySelectorAll('.residents');
    residents.forEach(item => {
        item.addEventListener('click', function (event) {
            document.getElementById('modalbody').innerHTML = ''; //clearing content inmodal
            let charApi = this.dataset.apiInputs.split(',');
            charApi.forEach( input => {
                addToModalTable(input)
            });
            $('#myModal').modal('show')
        })
    })
};


let addToModalTable = function (inputApi){
    fetch(inputApi)
        .then((response) => response.json())
        .then((data) => {
            displayModal(data);
        })
};q

let displayModal = function (charData) {
    let trModal = `<tr>`;
    let trEndModal = `</tr>`;
    for (i=0; i<charKeys.length; i++){
        trModal += `<td>${charData[charKeys[i]]}</td>`
    }
    document.getElementById('modalbody').innerHTML += trModal + trEndModal;
};




