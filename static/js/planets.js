


let planetsData = fetch('https://swapi.co/api/planets/')
.then((response) => response.json())
.then((data) => {
    tableDisplay(data.results);
});



// let tableDisplay = document.getElementById('tbody');

let tableDisplay = function f(api_data) {
    for (let row of api_data){
        console.log(row)
    }
}