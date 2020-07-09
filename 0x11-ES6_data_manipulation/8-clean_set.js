export default function cleanSet(set, startString) {
  if (!startString || !startString.length) return '';

  let res = '';
  set.forEach((item) => {
    if (item && item.startsWith(startString)) res += `${item.slice(startString.length)}-`;
  });

  return res.slice(0, res.length - 1);
}
