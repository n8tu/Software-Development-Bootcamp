function greet(name){
    if(name === "Count Dooku"){
        console.log("I'm coming for you, Dooku!");
    }else{
        console.log('Good day,',name + "!");
        const date = new Date();
        console.log(date.toUTCString());
    }
}

greet('Faisal');
greet('Count Dooku');