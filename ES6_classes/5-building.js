export default class Building {
  constructor(sqft) {
    if (typeof sqft !== 'number') throw new TypeError('Square footage must be a number');
    this._sqft = sqft;

    if (new.target === Building) {
      throw new Error('Building is an abstract class and cannot be instantiated directly.');
    }
  }

  get sqft() {
    return this._sqft;
  }

  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}

// Example subclass
class OfficeBuilding extends Building {
  constructor(sqft, name) {
    super(sqft);
    this._name = name;
  }

  evacuationWarningMessage() {
    return `Evacuate the ${this._name} building immediately!`;
  }
}
