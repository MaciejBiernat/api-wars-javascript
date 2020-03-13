


let planetsData = fetch('https://swapi.co/api/planets/')
.then((response) => response.json())
.then((data) => {
    tableDisplay(data.results);
});

const keys = [
    'name', 'diameter', 'climate', 'terrain', 'surface_water', 'population'
]

// let tableDisplay = document.getElementById('tbody');

let tableDisplay = function f(api_data) {
    for (let row of api_data) {
        for (key of keys) {
            console.log(row[key])
        }
    }
}

// let insertRow = function f(row) {
//     for (let key of row){
//         console.log(row[key])
//     }
// }

planetsData;
