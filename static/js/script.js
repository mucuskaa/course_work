// Вибір елементів
const openIncomeModalButton = document.getElementById("open-income-modal");
const openExpenseModalButton = document.getElementById("exp-btn");

const incomeModal = document.getElementById("income-modal");
const expenseModal = document.getElementById("expense-modal");

const closeIncomeModalButton = document.getElementById("close-income-modal");
const closeExpenseModalButton = document.getElementById("close-expense-modal");

const wallet = document.getElementById("wallet");

const expenseAmount = document.getElementById("expense-amount");
const expenseCategory = document.getElementById("expense-category");

const incomeAmount = document.getElementById("income-amount");
const incomeCategory = document.getElementById("income-category");

const incomeFormButton = document.querySelector("#income-modal .form-btn");
const expenseFormButton = document.querySelector("#expense-modal .form-btn");

const errorSpan = document.getElementById("error");

// Відкриття модальних вікон
openIncomeModalButton.addEventListener("click", () => {
    incomeModal.style.display = "block";
    validateIncomeForm(); // Перевірка, чи активна кнопка під час відкриття модального вікна
});

openExpenseModalButton.addEventListener("click", () => {
    expenseModal.style.display = "block";
    validateExpenseForm(); // Перевірка, чи активна кнопка під час відкриття модального вікна
});

// Закриття модальних вікон
closeIncomeModalButton.addEventListener("click", () => {
    incomeModal.style.display = "none";
});

closeExpenseModalButton.addEventListener("click", () => {
    expenseModal.style.display = "none";
});

// Закриття при натисканні поза модальним вікном
window.addEventListener("click", (event) => {
    if (event.target === incomeModal) {
        incomeModal.style.display = "none";
    }
    if (event.target === expenseModal) {
        expenseModal.style.display = "none";
    }
});

// Функція для перевірки валідності інпутів для прибутків
function validateIncomeForm() {
    const amount = parseFloat(incomeAmount.value);
    const category = incomeCategory.value;

    if (isNaN(amount) || amount <= 0 || category === "") {
        incomeFormButton.disabled = true;
    } else {
        incomeFormButton.disabled = false;
    }
}

// Функція для перевірки валідності інпутів для витрат
function validateExpenseForm() {
    const expense = parseFloat(expenseAmount.value);
    const balance = parseFloat(wallet.textContent);
    const category = expenseCategory.value;

    if (isNaN(expense) || expense <= 0 || category === "" || expense > balance) {
        expenseFormButton.disabled = true;
        if (expense > balance) {
            errorSpan.style.display = "block";
        }
    } else {
        expenseFormButton.disabled = false;
        errorSpan.style.display = "none";
    }
}

// Додамо обробники подій для перевірки валідності
incomeAmount.addEventListener("input", validateIncomeForm);
incomeCategory.addEventListener("change", validateIncomeForm);

expenseAmount.addEventListener("input", validateExpenseForm);
expenseCategory.addEventListener("change", validateExpenseForm);

// Ініціалізація з самого початку
validateIncomeForm();
validateExpenseForm();
