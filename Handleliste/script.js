const ul = document.getElementById('itemList')
const input = document.getElementById('itemInput')

let itemsArray = localStorage.getItem('items') ? 
JSON.parse(localStorage.getItem('items')) : []

function addTask(text) {
    const li = document.createElement('li')
    li.textContent = text
    
    const deleteButton = document.createElement('button')
    deleteButton.textContent = 'Remove'
    deleteButton.addEventListener('click', () => removeItem(text))
    
    li.appendChild(deleteButton)
    ul.appendChild(li)
}

itemsArray.forEach(addTask)

function addItem() {
    const newItem = input.value.trim()
    if (newItem !== '') {
        itemsArray.push(newItem)
        localStorage.setItem('items', JSON.stringify(itemsArray))
        addTask(newItem)
        input.value = ''
    }
}

function removeItem(itemText) {
    const index = itemsArray.indexOf(itemText);
    if (index !== -1) {
        itemsArray.splice(index, 1);
        localStorage.setItem('items', JSON.stringify(itemsArray));
        refreshList();
    }
}

function refreshList() {
    ul.innerHTML = '';
    itemsArray.forEach(addTask);
}

const clearList = () => {
    localStorage.clear();
    ul.innerHTML = '';
    itemsArray = [];
}
