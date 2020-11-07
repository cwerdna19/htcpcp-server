const url = 'http://localhost:8080';

// fetch(url).then(function(response){
//     return response.json();
// }).then(function(data){
//     console.log(data);
// }).catch(function() {
//     console.log("Booo");
// });

async function fetchAsync(url) {
    let response = await fetch(url, {
        headers : { 
            'Content-Type': 'application/json',
            'Accept': 'application/json'
           }
    });
    let data = await response.json();
    console.log(data)
    return data;
}