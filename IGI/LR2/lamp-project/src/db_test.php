<?php
$host = 'db';       // имя сервиса MySQL из docker-compose.yml
$user = 'user';     // пользователь из environment
$pass = 'userpass'; // пароль из environment
$db = 'appdb';      // имя БД

$conn = new mysqli($host, $user, $pass, $db);
if ($conn->connect_error) {
  die('Ошибка подключения: ' . $conn->connect_error);
}
echo 'Успешное подключение к MySQL!';
?>
