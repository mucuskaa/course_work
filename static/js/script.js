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
const modalWindow = document.getElementById("modal-content");

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

    const isExpenseInvalid = isNaN(expense) || expense <= 0 || category === "" || expense > balance;

    // Перевірка валідності інпутів та керування видимістю помилок
    if (isExpenseInvalid) {
        expenseFormButton.disabled = true;

        if (expense > balance) {
            errorSpan.classList.remove("hidden");
            errorSpan.classList.add("visible");
            modalWindow.style.height = '423px';
            expenseAmount.style.border = 'solid 1px #c90000';
            expenseAmount.style.filter = 'drop-shadow(0px 0px 12px #c90000)';

        } else {
            errorSpan.classList.add("hidden");
            errorSpan.classList.remove("visible");
            modalWindow.style.height = '395px';
            expenseAmount.style.border = 'solid 1px #FFFFFF';
            expenseAmount.style.filter = 'none';
        }
    } else {
        expenseFormButton.disabled = false;
        errorSpan.classList.add("hidden");
        errorSpan.classList.remove("visible");
        modalWindow.style.height = '395px';
        expenseAmount.style.border = 'solid 1px #FFFFFF';
        expenseAmount.style.filter = 'none';
    }
}

// Обробники подій для перевірки валідності
incomeAmount.addEventListener("input", validateIncomeForm);
incomeCategory.addEventListener("change", validateIncomeForm);

expenseAmount.addEventListener("input", validateExpenseForm);
expenseCategory.addEventListener("change", validateExpenseForm);

// Ініціалізація з самого початку
validateIncomeForm();
validateExpenseForm();


(function() {
  const selectWrappers = document.querySelectorAll(".select-wrapper");

  selectWrappers.forEach((wrapper, index) => {
    const selElmnt = wrapper.querySelector("select");
    const selectedDisplay = document.createElement("div");
    selectedDisplay.className = "select-selected";
    selectedDisplay.textContent = selElmnt.options[selElmnt.selectedIndex].textContent;
    wrapper.appendChild(selectedDisplay);

    const selectItems = document.createElement("div");
    selectItems.className = "select-items select-hide"; // Список прихований за замовчуванням

    for (let j = 1; j < selElmnt.options.length; j++) {
      const optionDiv = document.createElement("div");
      optionDiv.textContent = selElmnt.options[j].textContent;

      optionDiv.addEventListener("click", function() {
        const select = this.parentNode.parentNode.querySelector("select");

        // Встановлюємо індекс вибраної опції
        const selectedIndex = Array.from(select.options).findIndex(
          option => option.textContent === this.textContent
        );

        // Оновлюємо значення `select`
        select.selectedIndex = selectedIndex;
        selectedDisplay.textContent = this.textContent; // Оновлюємо відображення вибраної опції

        // Відправляємо подію `change` для валідації
        select.dispatchEvent(new Event("change")); // Це важливо для активації валідації

        // Закриваємо випадаючий список після вибору
        selectItems.classList.add("select-hide");
        selectedDisplay.classList.remove("select-arrow-active");
      });

      selectItems.appendChild(optionDiv); // Додаємо опцію до списку
    }

    wrapper.appendChild(selectItems);

    selectedDisplay.addEventListener("click", function(e) {
      e.stopPropagation(); // Запобігає закриттю при натисканні
      closeAllSelect(this);
      selectItems.classList.toggle("select-hide"); // Відкриває/закриває список
      selectedDisplay.classList.toggle("select-arrow-active");
    });
  });

  function closeAllSelect(current) {
    const selectItems = document.querySelectorAll(".select-items");
    const selectedDisplays = document.querySelectorAll(".select-selected");

    selectItems.forEach((item, index) => {
      if (current !== selectedDisplays[index]) {
        item.classList.add("select-hide"); // Закриває всі інші списки
        selectedDisplays[index].classList.remove("select-arrow-active");
      }
    });
  }

  document.addEventListener("click", function() {
    closeAllSelect(); // Закриває всі списки при натисканні за межами
  });
})();



