use twitter;
INSERT INTO tweets (tweet, user_id) VALUES ("Hello Ninja", 2);
SELECT * FROM tweets;
UPDATE tweets SET created_at = NOW(), updated_at = NOW() WHERE id=16;
DELETE FROM tweets WHERE id=17;