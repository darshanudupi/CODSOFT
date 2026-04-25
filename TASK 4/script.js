let cart = [];

function addToCart(item) {
  cart.push(item);
  displayCart();
}

function displayCart() {
  let cartList = document.getElementById("cartItems");

  // Prevent jumping
  cartList.innerHTML = "";

  cart.forEach(product => {
    let li = document.createElement("li");
    li.innerText = product;
    cartList.appendChild(li);
  });
}