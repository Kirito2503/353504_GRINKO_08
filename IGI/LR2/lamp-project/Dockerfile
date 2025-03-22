FROM php:8.2-apache

# Устанавливаем зависимости и расширения PHP
RUN apt-get update && apt-get install -y \
    libpng-dev \
    libzip-dev \
    && docker-php-ext-install mysqli pdo pdo_mysql \
    && docker-php-ext-enable mysqli

# Включаем модуль Apache rewrite (опционально)
RUN a2enmod rewrite