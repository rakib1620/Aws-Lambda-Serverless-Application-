
const apiUrl = 'https://srax773kwi.execute-api.us-east-1.amazonaws.com/prod/myresource';


document.getElementById('feedbackForm').addEventListener('submit', function(e) {
    e.preventDefault(); 

  
    const name = document.getElementById('name').value;
    const feedback = document.getElementById('feedback').value;

 
    const data = {
        name: name,
        feedback: feedback
    };


    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data) 
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        alert('Feedback submitted successfully!');
        console.log('Success:', data);
     
        document.getElementById('feedbackForm').reset();
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('Failed to submit feedback. Please check console for details.');
    });
});