export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) throw Error('Cannot process');

  for (const entry of map) if (entry[1] === 1) map.set(entry[0], 100);

  return map;
}
