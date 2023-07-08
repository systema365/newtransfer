document.addEventListener('DOMContentLoaded', () => {
    const dropArea = document.getElementById('drop-area');
  
    // Prevent default behaviors when dragging files over the drop area
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
      dropArea.addEventListener(eventName, preventDefaults, false);
    });
  
    // Highlight drop area when a file is dragged over it
    ['dragenter', 'dragover'].forEach(eventName => {
      dropArea.addEventListener(eventName, highlight, false);
    });
  
    // Remove highlighting when a file is dragged outside the drop area
    ['dragleave', 'drop'].forEach(eventName => {
      dropArea.addEventListener(eventName, unhighlight, false);
    });
  
    // Handle file drop event
    dropArea.addEventListener('drop', handleDrop, false);
  });
  
  function preventDefaults(event) {
    event.preventDefault();
    event.stopPropagation();
  }
  
  function highlight() {
    const dropArea = document.getElementById('drop-area');
    dropArea.classList.add('highlight');
  }
  
  function unhighlight() {
    const dropArea = document.getElementById('drop-area');
    dropArea.classList.remove('highlight');
  }
  
  function handleDrop(event) {
    const fileInput = document.getElementById('file-input');
    const file = event.dataTransfer.files[0];
    fileInput.files = event.dataTransfer.files;
  
    // Display the file name or perform any desired validation
  
    // You can also access the file using fileInput.files[0] in the submit handler
  
    // Example: Display the file name
    const dropArea = document.getElementById('drop-area');
    const p = document.createElement('p');
    p.textContent = file.name;
    dropArea.appendChild(p);
  }
  