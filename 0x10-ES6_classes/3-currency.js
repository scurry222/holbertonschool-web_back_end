export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  set code(code) {
    this.code = code;
  }

  get code() {
    return this.code;
  }

  set name(name) {
    this.name = name;
  }

  get name() {
    return this.name;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
