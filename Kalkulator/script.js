const display = document.getElementById('display');

const symbols = ['-', '+', '/', '*'];

const addToDisplay = (value) => {
    const currentValue = display.value;
    const lastChar = currentValue[currentValue.length - 1];
    const secondLastChar = currentValue[currentValue.length - 2];

    if (!symbols.includes(value)) {
        return display.value += value
    }
    if (currentValue === '') {
        if (value != '-') return
        else { 
            return display.value += value
        }
    }
    else if (value == '*' && symbols.includes(lastChar)) {
        if (lastChar == '*' && secondLastChar == '*') return
        else if (lastChar != '*') return
        return display.value += value
    }
    else if (symbols.includes(lastChar) && value !== '*') {
        return
    } 
    else {
        display.value += value;
        return
    }
};

const clearDisplay = () => display.value = '';
const calc = () => display.value = eval(display.value);