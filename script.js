document.getElementById('inputForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const nextInputValue = document.getElementById('nextInput').value;
    document.getElementById('output').innerText = `You entered: ${nextInputValue}`;
});

