/***********************************************************/
--employees
/***********************************************************/
create table employees (
    employee_id bigint generated always as identity primary key,
    user_id varchar(100) not null unique,
    pw varchar(68) not null,
    active boolean not null,
    first_name varchar(100) not null,
    last_name varchar(100) not null,
	employment_type varchar(10) not null check (employment_type in ('salary', 'hourly')),
    salary numeric(10,2),
	hourly_wage numeric(10,2)
);

insert into employees (user_id, pw, active, first_name, last_name, employment_type, salary, hourly_wage) values
('bwayne', '', true, 'bruce', 'wayne', 'hourly', null, 17.50),
('dprince', '', true, 'diana', 'prince', 'hourly', null, 16.25),
('srogers', '', true, 'steve', 'rogers', 'hourly', null, 13.75),
('pparker', '', true, 'peter', 'parker', 'hourly', null, 13.75),
('tstark', '', true, 'tony', 'stark', 'salary', 120000.00, null),
('ejarvis', '', true, 'edwin', 'jarvis', 'salary', 80000.00, null);


/***********************************************************/
--roles
--	For implementing Spring Security
/***********************************************************/
create table roles (
    employee_id bigint not null,
    role varchar(100) not null,
    constraint roles_pk primary key (employee_id, role),
    constraint roles_fk foreign key (employee_id) references employees(employee_id)
);

insert into roles
values 
(1,'ROLE_EMPLOYEE'),
(2,'ROLE_EMPLOYEE'),
(3,'ROLE_EMPLOYEE'),
(4,'ROLE_EMPLOYEE'),
(5,'ROLE_EMPLOYEE'),
(5,'ROLE_ADMIN'),
(6,'ROLE_EMPLOYEE'),
(6,'ROLE_MANAGER');

/***********************************************************/
--customers
/***********************************************************/
create table customers (
    customer_id bigint generated always as identity primary key,
    first_name varchar(100) not null,
    last_name varchar(100) not null,
    email varchar(255) not null unique
);

/***********************************************************/
--pizzas
/***********************************************************/
create table pizzas (
    pizza_id bigint generated always as identity primary key,
	pizza_type varchar(50) not null,
	total_cost numeric(5,2),
	total_price numeric(5,2)
);

/***********************************************************/
--ingredients
/***********************************************************/
create table ingredients (
    ingredient_id bigint generated always as identity primary key,
    name varchar(100) not null unique,
	unit_cost numeric(5,2) not null,
    retail_price numeric(5,2) not null,
	initial_supply bigint,
	used_supply bigint,
	lost_supply bigint
);

insert into ingredients (name, unit_cost, retail_price, initial_supply, used_supply, lost_supply)
values
('crust', 0.85, 4.00, 100000, 0, 0),
('tomato sauce', 0.30, 4.00, 100000, 0, 0),
('mozzarella', 0.75, 4.00, 100000, 0, 0),
('pepperoni', 0.50, 1.50, 5000, 0, 0),
('sausage', 0.60, 1.50, 5000, 0, 0),
('bell peppers', 0.30, 0.35, 5000, 0, 0),
('black olives', 0.45, 0.50, 5000, 0, 0),
('mushrooms', 0.40, 0.45, 5000, 0, 0),
('onions', 0.20, 0.25, 5000, 0, 0),
('tomatoes', 0.20, 0.25, 5000, 0, 0);


/***********************************************************/
--pizza_ingredients
/***********************************************************/
create table pizza_ingredients (
    pizza_id bigint not null,
    ingredient_id bigint not null,
    constraint pizza_ingredients_pk primary key (pizza_id, ingredient_id),
    constraint pi_pizza_fk foreign key (pizza_id) references pizzas(pizza_id),
    constraint pi_ingredient_fk foreign key (ingredient_id) references ingredients(ingredient_id)
);

/***********************************************************/
--orders
/***********************************************************/
create table orders (
    order_id bigint generated always as identity primary key,
	pizza_id bigint not null unique,
    customer_id bigint not null,
    employee_id bigint,
    created_at timestamptz not null,
    fulfilled_at timestamptz,
	constraint orders_pizza_fk foreign key (pizza_id) references pizzas(pizza_id),
    constraint orders_customer_fk foreign key (customer_id) references customers(customer_id),
    constraint orders_employee_fk foreign key (employee_id) references employees(employee_id)
);

