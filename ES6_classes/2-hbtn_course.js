export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'String') throw new TypeError('Name must be a String');
    if (typeof length !== 'Number') throw new TypeError('Length must be a Number');
    if (!Array.isArray(students)) throw new TypeError('Students must be an Array');
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  get students() {
    return this._students;
  }

  set name(name) {
    if (typeof name !== 'String') throw new TypeError('Name must be a String');
    this._name = name;
  }

  set length(length) {
    if (typeof length !== 'Number') throw new TypeError('Length must be a Number');
    this._length = length;
  }

  set students(students) {
    if (!Array.isArray(students)) throw new TypeError('Students must be an Array');
    this._students = students;
  }
}
