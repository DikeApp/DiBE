var mongoose = require('mongoose');
var uniqueValidator = require('mongoose-unique-validator');
var bcrypt = require('bcrypt-nodejs')

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

userSchema.methods.comparePassword = function(inputPassword, callback) {
  bcrypt.compare(inputPassword, this.password, function(err, isMatch) {
    if (err) {
      return callback(err)
    }
    callback(null, isMatch);
  });
}

userSchema.plugin(uniqueValidator);

//Export model
module.exports = mongoose.model('User', userSchema);
