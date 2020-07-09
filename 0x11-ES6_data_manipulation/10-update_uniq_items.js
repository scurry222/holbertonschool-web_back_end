export default function updateUniqueItems(map) {
    if (!(map instanceof Map)) throw Error('Cannot Process');

    for (let entry of map) if (entry[1] === 1) map.set(entry[0], 100);

    return map;
}