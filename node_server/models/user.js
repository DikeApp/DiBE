var mongoose = require('mongoose');
var uniqueValidator = require('mongoose-unique-validator');

var Schema = mongoose.Schema;

userSchema = new Schema(
  {
    username: {
      type: String,
      required: true,
      maxLength: 100,
      minLength: 8,
      unique: true,
    },
    password: {
      type: String,
      required: true,
      maxLength: 50,
      minLength: 8,
    },
  }
);

userSchema.plugin(uniqueValidator);

//Export model
module.exports = mongoose.model('User', userSchema);
