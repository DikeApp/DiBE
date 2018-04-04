var express = require('express');
var router = express.Router();
var userController = require('../controllers/userController')

/* GET users listing. */
router.get('/', userController.user_list);

/* POST sign up new user */
router.post('/', userController.user_sign_up);

module.exports = router;
