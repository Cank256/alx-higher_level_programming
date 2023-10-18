-- List privileges for user_0d_1
SELECT host, user, db, select_priv, insert_priv, update_priv, delete_priv, create_priv, drop_priv, alter_priv
FROM mysql.user
WHERE user = 'user_0d_1';

-- List privileges for user_0d_2
SELECT host, user, db, select_priv, insert_priv, update_priv, delete_priv, create_priv, drop_priv, alter_priv
FROM mysql.user
WHERE user = 'user_0d_2';
