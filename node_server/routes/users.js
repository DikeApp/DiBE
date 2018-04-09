var express = require('express');
var router = express.Router();
var userController = require('../controllers/userController')

/* GET users listing. */
router.get('/', userController.user_list);

/* POST sign up new user */
router.post('/', userController.user_sign_up);

/* POST user log in */
router.post('/login', userController.user_log_in);

module.exports = router;
