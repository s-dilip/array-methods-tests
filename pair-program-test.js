// imports
import {
  assertEquals,
  assertStringIncludes,
} from "https://deno.land/std/testing/asserts.ts";
import { arrReduce, findFruit, getNames, priceFilter } from "./pair-program.js";

const basket = [
  { name: "Apple", priceInPence: 50, quantity: 4 },
  { name: "Orange", priceInPence: 80, quantity: 2 },
  { name: "Carrots", priceInPence: 20, quantity: 10 },
  { name: "Strawberries", priceInPence: 150, quantity: 1 },
];

Deno.test("Calculates the total quantity of items", () => {
  assertEquals(arrReduce(basket), 17);
});

Deno.test("Checks if there are grapes in the basket", () => {
  assertEquals(findFruit(basket), false);
});

Deno.test("Gets all the Names of the items in Basket", () => {
  assertEquals(getNames(basket), [
    "Apple",
    "Orange",
    "Carrots",
    "Strawberries",
  ]);
});

Deno.test("Filters items whose price is either £1 or Under", () => {
  assertEquals(priceFilter(basket), [
    { name: "Apple", priceInPence: 50, quantity: 4 },
    { name: "Orange", priceInPence: 80, quantity: 2 },
    { name: "Carrots", priceInPence: 20, quantity: 10 },
  ]);
});
