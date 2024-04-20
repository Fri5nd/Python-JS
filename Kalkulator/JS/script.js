const addToDisplay = (value) => document.getElementById('display').value += value
const clearDisplay = () => document.getElementById('display').value = ''

const calc = () => {
    document.getElementById('display').value = eval(document.getElementById('display').value)
}
