const basket = [
  { name: "Apple", priceInPence: 50, quantity: 4 },
  { name: "Orange", priceInPence: 80, quantity: 2 },
  { name: "Carrots", priceInPence: 20, quantity: 10 },
  { name: "Strawberries", priceInPence: 150, quantity: 1 },
];

export function arrReduce(basket) {
  const total = basket.reduce((currentTotal, item) => {
    return item.quantity + currentTotal;
  }, 0);

  return total;
}

export function findFruit(basket) {
  const fruitNames = basket.map((item) => {
    return item.name;
  });

  const fruitBool = fruitNames.includes("Grapes");

  return fruitBool;
}

export function getNames(basket) {
  const fruitNames = basket.map((item) => {
    return item.name;
  });

  return fruitNames;
}

export function priceFilter(basket) {
  const filteredFruits = basket.filter((fruit) => {
    return fruit.priceInPence <= 100;
  });

  return filteredFruits;
}

//console.log(arrReduce(basket));
console.log(priceFilter(basket));
