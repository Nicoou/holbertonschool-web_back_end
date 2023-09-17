export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof value !== 'string') {
      throw TypeError('Name must be a string');
    }

    if (typeof value !== 'number') {
      throw TypeError('Length must be a number');
    }

    if (!Array.isArray(value)) {
      throw TypeError('Students must be a array of strings');
    }

    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value !== 'string') {
      throw TypeError('Name must be a string');
    }
    else {
      this._name = value;
    }
  }

  get length() {
    return this._length;
  }

  set length(value) {
    if (typeof value !== 'number') {
      throw TypeError('Length must be a number');
    }
    else {
      this._length = value;
    }
  }

  get students() {
    return this._students;
  }

  set students(value) {
    if (!Array.isArray(value)) {
      throw TypeError('Students must be a array of strings');
    }
    else {
      this._students = value;
    }
  }
}
