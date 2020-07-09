export default function getStudentIdsSum(list) {
  if (!Array.isArray(list)) return [];

  return list.reduce((sum, item) => sum + item.id, 0);
}
