create table `budget` (
    `name`        varchar(32) not null unique,
    `daily_limit` integer not null
);

create table `category` (
    `id`               integer primary key autoincrement,
    `name`             varchar(32) not null,
    `description`      text null,
    `is_limit`         boolean not null
);

create table `expense` (
    `id`               integer primary key autoincrement,
    `category_id`      integer not null,
    `amount`           integer not null,
    `comment`          text null,
    `created`          datetime not null,
    foreign key (category_id) references `category` (id)
);

create view `my_expense` as select cat.name as category, e.amount, e.comment, e.created from `expense` as e 
	inner join `category` as cat on cat.id = e.category_id;

insert into `category` (name, description, is_limit) values 
    ('🍔 Еда вне дома', '🍔 Бизнес ланчи, перекусы, кофе с собой', false),
    ('🥗 Продукты', '🥗 Покупки в супермаркетах и рынках', true),
    ('🍽 Бары и рестораны', '🍽 Бары, рестораны, кафе, кальянные, бургерные', false),
    ('🚎 Транспорт', '🚎 Общественный транспорт, такси, метро', true),
    ('🎁 Подарки', '🎁 Дни рождения, свадьбы, коллегам, мат. помощь', false),
    ('❤️ Здоровье', '❤️ Мед услуги, средства гигиены, лекарства, спорт', false),
    ('👕 Одежда', '👕 Покупка одежды, уход, химчистка', false),
    ('🎳 Развлечения', '🎳 Кино, театры, музеи', false),
    ('Образование', 'Книги, курсы, сертифицирование', false),
    ('Квартира', 'Аренда, Ипотека, ЖКХ, Все для дома', true),
    ('📱 Регулярные', '📱 Подписки на сервисы, мобильная связь, интернет', true),
    ('🛒 Прочее', '🛒 Все остальное', false);

insert into `budget` values (
    'Повседневные', 350
);