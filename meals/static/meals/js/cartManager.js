function updateCart(mealPk = false) {
  // Retrieve the cart in the localStorage
  let localStorageCart = localStorage.getItem("cart");
  // Parse it into JSON to get a JS object we can work on
  let cart = JSON.parse(localStorageCart);
  if (cart && mealPk) {
    cart.push(mealPk);
  } else if (mealPk) {
    cart = [mealPk];  // only for cart init
  }
  // Only save unique values
  cart = [...new Set(cart)];
  // Save the cart in the localStorage
  localStorage.setItem("cart", JSON.stringify(cart));
  return cart;
}

function updateCartBadge() {
  let cart = updateCart();
  let cartBadge = document.getElementById("cart-badge");
  if (cart.length > 0) {
    cartBadge.innerHTML = String(cart.length);
  }
  return cartBadge;
}

function updateCartLink() {
  let cart = updateCart();
  let cartLink = document.getElementById("cart-link");
  let cartLinkHref = cartLink.getAttribute("href").split("?")[0];
  cart.forEach((element, index) => {
    if (index === 0) {
      cartLinkHref = cartLinkHref + "?meal=" + element;
    } else {
      cartLinkHref = cartLinkHref + "&meal=" + element;
    }
  });
  cartLink.setAttribute("href", cartLinkHref);
  return cartLink;
}

function emptyCart() {
  localStorage.removeItem("cart");
  updateCartLink();
  updateCartBadge();
  window.location.replace('/');
}

function addToCart(mealPk) {
  updateCart(mealPk);
  // Now update the DOM
  updateCartBadge();
  updateCartLink()
}

function checkElement(element) {
  element.firstElementChild.checked = !element.firstElementChild.checked;
}

window.onload = function() {
  dragula(
   [
    document.querySelector('#left'),
    document.querySelector('#monday'),
    document.querySelector('#tuesday'),
    document.querySelector('#wednesday'),
    document.querySelector('#thursday'),
    document.querySelector('#friday'),
    document.querySelector('#saturday'),
    document.querySelector('#sunday'),
   ]
  );
  updateCartBadge();
  updateCartLink();
}
