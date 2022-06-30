function pizzaOven(crustType, sauceType, cheeses, toppings){
    var pizza = {};
    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    return pizza;
}

function randomPizza(){
    var pizzas = [
        ["deep dish", "traditional", ["mozzarella"],["pepperoni", "sausage"]],
        ["deep dish", "traditional", ["mozzarella"],["pepperoni", "sausage"]],
        ["hand tossed", "marinara", ["feta"],["mushrooms", "olives", "onions"]],
        ["hand tossed", "ranch", ["feta"],["olives"]],
        ["deep dish", "marinara", ["mozzarella", "feta"],["mushrooms", "olives"]],
        ["deep dish", "traditional", [] ,["pepperoni"]],
        ["hand tossed", "marinara", ["feta"],["olives", "onions"]],
        ["hand tossed", "ranch", [],["olives"]],
        ["deep dish", "marinara", ["mozzarella", "feta"],["mushrooms", "olives"]]
    ];

    var randomPizza = Math.floor(Math.random() * pizzas.length);
    return pizzaOven(
        pizzas[randomPizza][0],
        pizzas[randomPizza][1],
        pizzas[randomPizza][2],
        pizzas[randomPizza][3]
        );

}

var pizza1 = pizzaOven("deep dish", "traditional", ["mozzarella"],["pepperoni", "sausage"]);
var pizza2 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"],["mushrooms", "olives", "onions"]);
var pizza3 = pizzaOven("hand tossed", "ranch", ["mozzarella", "feta"],["olives"]);
var pizza4 = pizzaOven("deep dish", "marinara", ["mozzarella", "feta"],["mushrooms", "olives"]);
var pizza5 = randomPizza();

console.log(pizza5);

