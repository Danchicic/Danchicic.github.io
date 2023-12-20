function create_card(card_index) {
  // create div
  const div = document.createElement("div");
  const img = document.createElement("img");

  const buttonAdd = document.createElement("button");
  const buttonDelete = document.createElement("button");

  const counter = document.createElement("span");
  const waste = document.createElement("div");

  waste.classList.add("counter_div");

  div.classList.add("cardDiv");

  // img settings
  img.setAttribute("src", "apples_img/" + card_index + ".jpg");
  img.classList.add("card");
  img.setAttribute("alt", "telephone");

  // button add
  buttonAdd.textContent = "add";
  buttonAdd.classList.add("button_plus");
  //button minus
  buttonDelete.textContent = "-";
  buttonDelete.classList.add("counting_button");
  buttonDelete.style.display = "none";

  //counter configure
  counter.classList.add("count");
  counter.textContent = 0;
  counter.style.display = "none";

  waste.appendChild(counter);
  div.appendChild(waste);

  div.appendChild(img);
  div.appendChild(buttonAdd);
  div.appendChild(buttonDelete);
  document.querySelector(".cards").appendChild(div);
}
document.addEventListener("DOMContentLoaded", function () {
  for (let i = 1; i < 17; i++) {
    create_card(i);
  }

  const cards = document.querySelectorAll(".cardDiv");
  cards.forEach((card) => {
    const addButton = card.querySelector(".button_plus");
    const buttonDelete = card.querySelector(".counting_button");
    const counterSpan = card.querySelector(".count");
    let count = 0;
    addButton.addEventListener("click", () => {
      count++;
      counterSpan.textContent = count;
      buttonDelete.style.display = "inline-block";
      counterSpan.style.display = "inline-block";
      addButton.textContent = "+";
    });
    buttonDelete.addEventListener("click", () => {
      if (count > 0) {
        count--;
        counterSpan.textContent = count;
      }
      if (count == 0) {
        buttonDelete.style.display = "none";
        counterSpan.style.display = "none";
        addButton.textContent = "add";
      }
    });
  });
});

