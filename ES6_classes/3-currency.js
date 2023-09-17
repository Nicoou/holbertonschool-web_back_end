export default class Currency {
  constructor(code, name) {
    this.name = name;
    this.code = code;
  }

  get code() {
    return this._code
  }

  set code(value) {
    this._code = value
  }

  get name() {
    return this._name
  }

  set name(New) {
    this._name = value
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}