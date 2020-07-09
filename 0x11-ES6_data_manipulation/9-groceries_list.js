export default function groceriesList() {
    const groceriesArray = [
        ['Apples', 10],
        ['Tomatoes', 10],
        ['Pasta', 1],
        ['Rice', 1],
        ['Banana', 5],
    ];
    const groceriesMap = new Map();
    groceriesArray.forEach(item => groceriesMap.set(item[0], item[1]));
    return groceriesMap;
}