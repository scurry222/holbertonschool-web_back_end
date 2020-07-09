export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
    console.log(this);
  }

  get size() {
    return this._size;
  }

  get location() {
    return this._location;
  }

  [Symbol.toPrimitive](hint) {
    if (hint === 'string') {
      return this.location;
    }
    if (hint === 'number') {
      return this.size;
    }
    return null;
  }
}
