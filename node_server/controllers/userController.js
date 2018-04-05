var User = require('../models/user');

// Display all user
exports.user_list = function(req, res, next) {

  User.find()
    .exec(function(err, user_list) {
      if (err) {
        return next(err);
      }
      res.send({
        success: true,
        code: 200,
        data: user_list,
      })
    });
  // res.send('User list');
}

exports.user_sign_up = function(req, res, next) {

  var newUser = new User(
    {
      username: req.body.username,
      password: req.body.password,
    }
  );

  newUser.validate(function(err) {
    if (err) {
      res.send({
        success: false,
        code: 402,
        err: err,
      });
      return false;
    } else {
      newUser.save(function(err) {
        if (err) {
          res.send({
            success: false,
            code: 400,
            err: err,
          });
          return next(err);
        }
        res.send({
          success: true,
          code: 200,
          user_id: newUser._id,
        });
      });
    }
  });
}
