create table `budget` (
    `name`        varchar(32) not null unique,
    `daily_limit` integer not null
);

create table `category_type` (
    `id`          integer primary key autoincrement,
    `name`        varchar(32) not null unique,
    `description` text null
);

create table `category` (
    `id`               integer primary key autoincrement,
    `category_type_id` integer not null,
    `name`             varchar(32) not null unique,
    `description`      text null,
    foreign key (category_type_id) references `category_type` (id)
);

create table `expense` (
    `id`          integer primary key autoincrement,
    `category_id` integer not null,
    `amount`      integer not null,
    `comment`     text null,
    `created`     datetime not null,
    foreign key (category_id) references `category` (id)
);

insert into `category_type` (name, description) values (
    ('Повседневные', ''),
    ('Крупные', ''),
    ('Квартира', '')
);

insert into `category` (category_type_id, name, description) values (
    (0, 'Еда вне дома', 'Бизнес ланчи, перекусы, кофе с собой'),
    (0, 'Продукты', 'Покупки в супермаркетах и рынках'),
    (0, 'Бары и рестораны', 'Бары, рестораны, кафе, кальянные, бургерные'),
    (0, 'Транспорт', 'Общественный транспорт, такси'),
    (0, 'Подарки', 'Дни рождения, свадьбы, коллегам, мат. помощь'),
    (0, 'Здоровье', 'Мед услуги, средства гигиены, лекарства, спорт'),
    (0, 'Одежда', 'Покупка одежды, уход, химчистка'),
    (0, 'Развлечения', 'Кино, театры, музеи'),
    (0, 'Регулярные', 'Подписки на сервисы, мобильная связь, интернет'),
    (0, 'Прочее', 'Все остальное')
);

insert into `category` (category_type_id, name) values (
    (1, 'Путешествия'),
    (1, 'Одежда'),
    (1, 'Гаджеты'),
    (1, 'Праздики'),
    (1, 'Крастота и здоровье'),
    (1, 'Образование'),
    (2, 'Ремонт'),
    (2, 'Ипотека'),
    (2, 'ЖКХ'),
    (2, 'Все для дома'),
    (2, 'Аренда'),
    (2, 'Прочее'),
);

insert into `budget` values (
    'Повседневные', 350
);