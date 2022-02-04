-- 2. Пусть задан некоторый пользователь. 
-- Из всех друзей этого пользователя найдите человека, который больше всех общался с нашим пользователем.

SELECT
    from_user_id, COUNT(*) as send 
FROM messages 
WHERE to_user_id=1 
GROUP BY from_user_id
ORDER BY send DESC;

-- 3. Подсчитать общее количество лайков, которые получили 10 самых молодых пользователей.

SELECT COUNT(*) as 'Likes' 
FROM profiles 
WHERE (YEAR(NOW())-YEAR(birthday)) <= 10;

-- 4. Определить кто больше поставил лайков (всего) - мужчины или женщины?

SELECT gender, COUNT(*) as 'Likes' 
FROM profiles 
GROUP BY gender;

-- 5. Найти 10 пользователей, которые проявляют наименьшую активность в использовании социальной сети.

