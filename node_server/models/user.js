var mongoose = require('mongoose');
var uniqueValidator = require('mongoose-unique-validator');

var Schema = mongoose.Schema;

userSchema = new Schema(
  {
    username: {
      type: String,
      required: true,
      maxlength: 100,
      minlength: [8, 'Username should be longer than 8 characters'],
      unique: true,
    },
    password: {
      type: String,
      required: true,
    },
  }
);

userSchema.plugin(uniqueValidator);

//Export model
module.exports = mongoose.model('User', userSchema);
