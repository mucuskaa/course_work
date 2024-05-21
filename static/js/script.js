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

openIncomeModalButton.addEventListener("click", () => {
    incomeModal.style.display = "block";
    validateIncomeForm();
});

openExpenseModalButton.addEventListener("click", () => {
    expenseModal.style.display = "block";
    validateExpenseForm();
});

closeIncomeModalButton.addEventListener("click", () => {
    incomeModal.style.display = "none";
});

closeExpenseModalButton.addEventListener("click", () => {
    expenseModal.style.display = "none";
});

window.addEventListener("click", (event) => {
    if (event.target === incomeModal) {
        incomeModal.style.display = "none";
    }
    if (event.target === expenseModal) {
        expenseModal.style.display = "none";
    }
});

function validateIncomeForm() {
    const amount = parseFloat(incomeAmount.value);
    const category = incomeCategory.value;

    if (isNaN(amount) || amount <= 0 || category === "") {
        incomeFormButton.disabled = true;
    } else {
        incomeFormButton.disabled = false;
    }
}

function validateExpenseForm() {
    const expense = parseFloat(expenseAmount.value);
    wall = wallet.textContent.replace(',','.');
    const balance = parseFloat(wall);
    const category = expenseCategory.value;

    const isExpenseInvalid = isNaN(expense) || expense <= 0 || category === "" || expense > balance;

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

incomeAmount.addEventListener("input", validateIncomeForm);
incomeCategory.addEventListener("change", validateIncomeForm);

expenseAmount.addEventListener("input", validateExpenseForm);
expenseCategory.addEventListener("change", validateExpenseForm);

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
    selectItems.className = "select-items select-hide";

    for (let j = 1; j < selElmnt.options.length; j++) {
      const optionDiv = document.createElement("div");
      optionDiv.textContent = selElmnt.options[j].textContent;

      optionDiv.addEventListener("click", function() {
        const select = this.parentNode.parentNode.querySelector("select");

        const selectedIndex = Array.from(select.options).findIndex(
          option => option.textContent === this.textContent
        );

        select.selectedIndex = selectedIndex;
        selectedDisplay.textContent = this.textContent;

        select.dispatchEvent(new Event("change"));

        selectItems.classList.add("select-hide");
        selectedDisplay.classList.remove("select-arrow-active");
      });

      selectItems.appendChild(optionDiv);
    }

    wrapper.appendChild(selectItems);

    selectedDisplay.addEventListener("click", function(e) {
      e.stopPropagation();
      closeAllSelect(this);
      selectItems.classList.toggle("select-hide");
      selectedDisplay.classList.toggle("select-arrow-active");
    });
  });

  function closeAllSelect(current) {
    const selectItems = document.querySelectorAll(".select-items");
    const selectedDisplays = document.querySelectorAll(".select-selected");

    selectItems.forEach((item, index) => {
      if (current !== selectedDisplays[index]) {
        item.classList.add("select-hide");
        selectedDisplays[index].classList.remove("select-arrow-active");
      }
    });
  }

  document.addEventListener("click", function() {
    closeAllSelect();
  });
})();

const swiper = new Swiper('.swiper', {
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },

  slidesPerView: 1,
  slidesPerGroup: 1,
});
