export default class Currency {
  constructor(code, name) {
    this.name = name;
    this.code = code;
  }

  get code() {
    return this._code
  }

  set code(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Code must be a string');
    }
    this._code = this.code
  }

  get name() {
    return this._name
  }

  set name(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = this.name
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}