export default function appendToEachArrayValue(array, appendString) {
  const newarray = [];
  for (const idx in array) {
    newarray.push(appendString + idx)
  }

  return array;
}
