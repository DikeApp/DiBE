var mongoose = require('mongoose');

var Schema = mongoose.Schema;

userSchema = new Schema(
  {
    username: {type: String, required: true, max: 100, min: 8},
    password: {type: String, required: true, max: 50, min: 8},
  }
);

//Export model
module.exports = mongoose.model('User', userSchema);
