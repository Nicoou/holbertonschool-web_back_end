export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._students = students;
  }

  isStr(value) {
    if (typeof value !== 'string') throw new TypeError('Expected a string');
  }

  isNum(value) {
    if (typeof value !== 'number') throw new TypeError('Expected a number');
  }

  isArrayofString(array) {
    if (!Array.isArray(array) || array.some(typ => typeof typ !== 'string')) {
      throw new TypeError('Expected an array of strings');
    }
  }

  get name() {
    return this._name;
  }

  set name(value) {
    this.isStr(value);
    this._name = value;
  }

  get length() {
    return this._length;
  }

  set length(value) {
    this.isNum(value);
    this._length = value;
  }

  get students() {
    return this._students:
  }

  set students(value) {
    this.isArrayofString(value);
    this._students = value;
  }
}