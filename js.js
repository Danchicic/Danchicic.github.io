document.addEventListener("DOMContentLoaded", function () {
  function create_card(card_index) {
    // create div
    const div = document.createElement("div");
    const img = document.createElement("img");
    const buttonAdd = document.createElement("button");
    const buttonDelete = document.createElement("button");
    const counterText = document.createElement("p");
    const counter = document.createElement("span");
    const waste = document.createElement('div');

    waste.classList.add('counter_div')

    div.classList.add("cardDiv");

    // img settings
    img.setAttribute("src", "apples_img/" + card_index + ".jpg");
    img.classList.add("card");
    img.setAttribute("alt", "telephone");

    // button add
    buttonAdd.textContent = "add";
    buttonAdd.classList.add("button_plus");
    //button minus
    buttonDelete.textContent = "delete";
    buttonDelete.classList.add( "button_minus");

    //counter configure
    counterText.textContent = "Всего товаров: ";
    counter.classList.add("count");
    counter.textContent = 0;

    waste.appendChild(counterText);
    waste.appendChild(counter);
    div.appendChild(waste);

    div.appendChild(img);
    div.appendChild(buttonAdd);
    div.appendChild(buttonDelete);
    document.querySelector(".cards").appendChild(div);

    buttonAdd.addEventListener("click", function () {
      let count = parseInt(counter.textContent);
      count++;
     

      counter.textContent = count;
    });
    buttonDelete.addEventListener("click", function () {
      let count = parseInt(counter.textContent);
      if (count > 0) {
        count--;
        counter.textContent = count;
   
      }
    });
  }
  for (let i = 1; i < 18; i++) {
    create_card(i);
  }
});
