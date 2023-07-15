
fetch('http://localhost:5000/api/data')
  .then(response => response.json())
  .then(data => {
    // Process the retrieved data
    console.log(data);

    const dataContainer = document.getElementById('data-container');
    
    // Clear existing content
    dataContainer.innerHTML = data.name;
    });