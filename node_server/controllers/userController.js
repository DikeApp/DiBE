var User = require('../models/user');

// Display all user
exports.user_list = function(req, res, next) {

  User.find()
    .exec(function(err, user_list) {
      if (err) {
        return next(err);
      }
      res.send({
        success: True,
        code: 200,
        data: user_list,
      })
    });

}