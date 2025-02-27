CREATE TABLE IF NOT EXISTS `python`.`bot_users` (
    `id` int unsigned NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(50) DEFAULT NULL,
    `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB CHARSET=cp1251;