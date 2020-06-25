/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 80019
Source Host           : localhost:3306
Source Database       : message_board_db

Target Server Type    : MYSQL
Target Server Version : 80019
File Encoding         : 65001

Date: 2020-06-25 21:34:37
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for message_board
-- ----------------------------
DROP TABLE IF EXISTS `message_board`;
CREATE TABLE `message_board` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '留言序号',
  `content` varchar(511) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '留言内容',
  `username` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '留言人姓名',
  `time` datetime NOT NULL COMMENT '留言创建/更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=140 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of message_board
-- ----------------------------
INSERT INTO `message_board` VALUES ('90', 'odk，mahay来了我看见了。', '不淡定的但丁', '2020-06-19 12:42:41');
INSERT INTO `message_board` VALUES ('91', '什么什么', '不淡定的但丁', '2020-06-19 21:19:08');
INSERT INTO `message_board` VALUES ('92', 'odk', '不淡定的但丁', '2020-06-19 21:19:13');
INSERT INTO `message_board` VALUES ('94', '我是mahay，mahayhay', '赵鹏飞', '2020-06-19 21:42:35');
INSERT INTO `message_board` VALUES ('95', '我是WOWspring', '姚鹏飞', '2020-06-19 21:43:19');
INSERT INTO `message_board` VALUES ('96', '大家好，我是WOWspring', '姚鹏飞', '2020-06-19 21:43:56');
INSERT INTO `message_board` VALUES ('97', 'test', '王帆', '2020-06-19 22:31:59');
INSERT INTO `message_board` VALUES ('99', 'new window', '王帆', '2020-06-19 22:44:37');
INSERT INTO `message_board` VALUES ('101', 'odk，mahay来了我看见了。', '不淡定的但丁', '2020-06-20 13:02:53');
INSERT INTO `message_board` VALUES ('102', '这是\r\n修改后的留言', '不淡定的但丁', '2020-06-20 16:10:49');
INSERT INTO `message_board` VALUES ('104', '最多换行 3次，\r\n也就是说最多显示四行。', '不淡定的但丁', '2020-06-20 16:18:00');
INSERT INTO `message_board` VALUES ('106', '大家好，我是mahay', '赵鹏飞', '2020-06-20 16:50:28');
INSERT INTO `message_board` VALUES ('109', 'mahay, mayiyahay', '赵鹏飞', '2020-06-23 17:49:31');
INSERT INTO `message_board` VALUES ('110', '我ypf也要发言', '姚鹏飞', '2020-06-20 16:52:03');
INSERT INTO `message_board` VALUES ('112', '我不配拥有姓名吗', '王子轩', '2020-06-20 18:42:10');
INSERT INTO `message_board` VALUES ('114', '我是大号[旺柴]', 'b5dx', '2020-06-20 18:47:15');
INSERT INTO `message_board` VALUES ('116', '大家好，我是b5dx', '王子轩', '2020-06-20 21:16:11');
INSERT INTO `message_board` VALUES ('118', '你好', '王嘉承', '2020-06-21 12:06:18');
INSERT INTO `message_board` VALUES ('119', '拍了拍', '王嘉承', '2020-06-21 12:06:36');
INSERT INTO `message_board` VALUES ('124', '行啊', '王子轩', '2020-06-21 12:08:42');
INSERT INTO `message_board` VALUES ('129', 'hallo，再来最后一波测试吧。\r\n现在所有代码已经修缮完毕了。', '王子轩', '2020-06-21 15:51:58');
INSERT INTO `message_board` VALUES ('132', '完活，我提交了，我好了', '王子轩', '2020-06-21 16:01:46');

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `user_id` int unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '登录用，不可重复',
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '用md5加密过的密码',
  `register_date` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES ('1', '不淡定的但丁', '61ea443736739b55cd4190848cf6f84f', '2020-06-07 22:15:39');
INSERT INTO `users` VALUES ('2', '赵鹏飞', '7f8c42a7ead3b65ad24d27d2bd64c6d7', '2020-06-09 23:23:27');
INSERT INTO `users` VALUES ('3', '姚鹏飞', '7f8c42a7ead3b65ad24d27d2bd64c6d7', '2020-06-11 12:40:02');
INSERT INTO `users` VALUES ('5', '王帆', 'e10adc3949ba59abbe56e057f20f883e', '2020-06-19 21:46:37');
INSERT INTO `users` VALUES ('6', '王子轩', '547ed8d0d02ed089ad277c18c72868af', '2020-06-23 18:55:24');
INSERT INTO `users` VALUES ('8', 'b5dx', '61ea443736739b55cd4190848cf6f84f', '2020-06-20 18:43:20');
INSERT INTO `users` VALUES ('9', '王嘉承', 'e10adc3949ba59abbe56e057f20f883e', '2020-06-21 12:06:01');
INSERT INTO `users` VALUES ('11', 'mahay', '7f8c42a7ead3b65ad24d27d2bd64c6d7', '2020-06-25 15:26:11');
