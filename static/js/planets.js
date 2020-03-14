
const keys = [
    'name', 'diameter', 'climate', 'terrain', 'surface_water', 'population', 'residents'
];

let tableInsert = document.getElementById('tbody');
let tr = '<tr>';
let endTr = '</tr>';



let insertData = function (cell) {
    tableInsert.innerHTML += `<td>${cell}</td>`
};


let displayRow = function f(apiData) {
    apiData.forEach(row => {

        for (i = 0; i < keys.length; i++){
            tr += `<td> ${row[keys[i]]} </td>`;

        }
        tr+=endTr
    });
    tableInsert.innerHTML += tr + endTr
    };

let planetsData = fetch('https://swapi.co/api/planets/')
.then((response) => response.json())
.then((data) => {
    displayRow(data.results);
});

planetsData;











//
// let tableDisplay = function f(apiData) {
//     for (let row in apiData) {
//         console.log(row);
//         insertRow(row);
//         tableInsert.innerHTML += tr + endTr;
//     }
// };
// //
// let insertRow = function f(row){
//     for (i = 0; i < keys.length; i++){
//         tr += `<td> ${row[keys[i]]} </td>`;
//         console.log(tr)
//     }
// };


// let insertRow = function f(row) {
//     for (let key of keys){
//         tr += `<td> ${row[key]} </td>`;
//     }
//     tableInsert.innerHTML += tr + endTr;
// }
