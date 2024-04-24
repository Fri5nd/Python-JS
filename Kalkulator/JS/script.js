const display = document.getElementById('display')

const addToDisplay = (value) => display.value += value
const clearDisplay = () => display.value = ''
const calc = () => display.value = eval(display.value)