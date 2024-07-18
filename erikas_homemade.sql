-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-07-2024 a las 23:34:20
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `erikas_homemade`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add permiso', 7, 'add_permiso'),
(26, 'Can change permiso', 7, 'change_permiso'),
(27, 'Can delete permiso', 7, 'delete_permiso'),
(28, 'Can view permiso', 7, 'view_permiso'),
(29, 'Can add rol', 8, 'add_rol'),
(30, 'Can change rol', 8, 'change_rol'),
(31, 'Can delete rol', 8, 'delete_rol'),
(32, 'Can view rol', 8, 'view_rol'),
(33, 'Can add usuario', 9, 'add_usuario'),
(34, 'Can change usuario', 9, 'change_usuario'),
(35, 'Can delete usuario', 9, 'delete_usuario'),
(36, 'Can view usuario', 9, 'view_usuario'),
(37, 'Can add reserva', 10, 'add_reserva'),
(38, 'Can change reserva', 10, 'change_reserva'),
(39, 'Can delete reserva', 10, 'delete_reserva'),
(40, 'Can view reserva', 10, 'view_reserva'),
(41, 'Can add tipo servicio', 11, 'add_tiposervicio'),
(42, 'Can change tipo servicio', 11, 'change_tiposervicio'),
(43, 'Can delete tipo servicio', 11, 'delete_tiposervicio'),
(44, 'Can view tipo servicio', 11, 'view_tiposervicio'),
(45, 'Can add servicio', 12, 'add_servicio'),
(46, 'Can change servicio', 12, 'change_servicio'),
(47, 'Can delete servicio', 12, 'delete_servicio'),
(48, 'Can view servicio', 12, 'view_servicio'),
(49, 'Can add tipo producto', 13, 'add_tipoproducto'),
(50, 'Can change tipo producto', 13, 'change_tipoproducto'),
(51, 'Can delete tipo producto', 13, 'delete_tipoproducto'),
(52, 'Can view tipo producto', 13, 'view_tipoproducto'),
(53, 'Can add producto', 14, 'add_producto'),
(54, 'Can change producto', 14, 'change_producto'),
(55, 'Can delete producto', 14, 'delete_producto'),
(56, 'Can view producto', 14, 'view_producto'),
(57, 'Can add pedido', 15, 'add_pedido'),
(58, 'Can change pedido', 15, 'change_pedido'),
(59, 'Can delete pedido', 15, 'delete_pedido'),
(60, 'Can view pedido', 15, 'view_pedido'),
(61, 'Can add detalle pedido producto', 16, 'add_detallepedidoproducto'),
(62, 'Can change detalle pedido producto', 16, 'change_detallepedidoproducto'),
(63, 'Can delete detalle pedido producto', 16, 'delete_detallepedidoproducto'),
(64, 'Can view detalle pedido producto', 16, 'view_detallepedidoproducto'),
(65, 'Can add detalle pedido servicio', 17, 'add_detallepedidoservicio'),
(66, 'Can change detalle pedido servicio', 17, 'change_detallepedidoservicio'),
(67, 'Can delete detalle pedido servicio', 17, 'delete_detallepedidoservicio'),
(68, 'Can view detalle pedido servicio', 17, 'view_detallepedidoservicio'),
(69, 'Can add venta', 18, 'add_venta'),
(70, 'Can change venta', 18, 'change_venta'),
(71, 'Can delete venta', 18, 'delete_venta'),
(72, 'Can view venta', 18, 'view_venta');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_pedido_productos`
--

CREATE TABLE `detalle_pedido_productos` (
  `idDetalle_Pedido_Productos` int(11) NOT NULL,
  `cant_productos` int(11) NOT NULL,
  `nombre_productos` varchar(50) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `precio_inicial_producto` decimal(10,2) NOT NULL,
  `subtotal_productos` decimal(10,2) NOT NULL,
  `idProducto_id` int(11) NOT NULL,
  `idPedido_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `detalle_pedido_productos`
--

INSERT INTO `detalle_pedido_productos` (`idDetalle_Pedido_Productos`, `cant_productos`, `nombre_productos`, `descripcion`, `precio_inicial_producto`, `subtotal_productos`, `idProducto_id`, `idPedido_id`) VALUES
(1, 3, 'Muñeco Mario panadero', 'Muñeco de Mario versión panadero', 50000.00, 150000.00, 5, 8),
(2, 1, 'Caballerito Crochet', 'Manualidad De Hollow knight Caballerito de crochet', 100000.00, 100000.00, 24, 8),
(3, 1, 'Muñeca vestido verde', 'Muñeca con vestido verde para niños pendejos', 25000.00, 25000.00, 6, 9),
(4, 1, 'Moño perlas', 'Moño color negro con perlas incrustadas', 5000.00, 5000.00, 11, 9),
(5, 1, 'Muñeco Mario panadero', 'Muñeco de Mario versión panadero', 50000.00, 50000.00, 5, 10),
(6, 1, 'Mantel Crochet', 'Mantel para mesa redonda tejido a mano tamaño 1m de diámetro', 40000.00, 40000.00, 9, 10),
(7, 1, 'Caballerito Crochet', 'Manualidad De Hollow knight Caballerito de crochet', 100000.00, 100000.00, 24, 10),
(8, 2, 'Luffy Crochet', 'Manualidad de one piece personaje Monkey D Luffy', 100000.00, 200000.00, 23, 10),
(9, 1, 'Muñeco de costura', 'Muñeco con costura remarcada', 10000.00, 10000.00, 7, 11),
(10, 1, 'Muñeco Mario panadero', 'Muñeco de Mario versión panadero', 50000.00, 50000.00, 5, 11);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_pedido_servicios`
--

CREATE TABLE `detalle_pedido_servicios` (
  `idDetalle_Pedido_Servicio` int(11) NOT NULL,
  `cantidad_servicios` int(11) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `precio_inicial_servicio` decimal(10,2) NOT NULL,
  `subtotal_servicios` decimal(10,2) NOT NULL,
  `idPedido_id` int(11) NOT NULL,
  `idServicio_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `detalle_pedido_servicios`
--

INSERT INTO `detalle_pedido_servicios` (`idDetalle_Pedido_Servicio`, `cantidad_servicios`, `descripcion`, `precio_inicial_servicio`, `subtotal_servicios`, `idPedido_id`, `idServicio_id`) VALUES
(1, 1, 'Short para mujer, todas las tallas y todos los colores. DETALLAR LA TALLA Y EL COLOR EN LA PASARELA DE PAGO', 50000.00, 50000.00, 8, 7),
(2, 2, 'Short para mujer, todas las tallas y todos los colores. DETALLAR LA TALLA Y EL COLOR EN LA PASARELA DE PAGO', 50000.00, 100000.00, 10, 7),
(3, 2, 'Camisetas personalizadas Todas las tallas y todos los diseños. DETALLAR LA TALLA Y EL COLOR EN LA PASARELA DE PAGO', 50000.00, 100000.00, 10, 8);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(16, 'pedidos', 'detallepedidoproducto'),
(17, 'pedidos', 'detallepedidoservicio'),
(15, 'pedidos', 'pedido'),
(14, 'pedidos', 'producto'),
(12, 'pedidos', 'servicio'),
(13, 'pedidos', 'tipoproducto'),
(11, 'pedidos', 'tiposervicio'),
(10, 'reservas', 'reserva'),
(6, 'sessions', 'session'),
(7, 'usuarios', 'permiso'),
(8, 'usuarios', 'rol'),
(9, 'usuarios', 'usuario'),
(18, 'ventas', 'venta');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-05-15 19:44:36.261594'),
(2, 'auth', '0001_initial', '2024-05-15 19:44:36.610392'),
(3, 'admin', '0001_initial', '2024-05-15 19:44:36.697634'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-05-15 19:44:36.706392'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-05-15 19:44:36.716389'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-05-15 19:44:36.773002'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-05-15 19:44:36.816040'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-05-15 19:44:36.831863'),
(9, 'auth', '0004_alter_user_username_opts', '2024-05-15 19:44:36.841532'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-05-15 19:44:36.881234'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-05-15 19:44:36.896235'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-05-15 19:44:36.915237'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-05-15 19:44:36.935238'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-05-15 19:44:36.951925'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-05-15 19:44:36.969538'),
(16, 'auth', '0011_update_proxy_permissions', '2024-05-15 19:44:36.980540'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-05-15 19:44:37.000438'),
(18, 'usuarios', '0001_initial', '2024-05-15 19:44:37.130403'),
(19, 'usuarios', '0002_rename_permiso_rolxpermiso_idpermiso_and_more', '2024-05-15 19:44:37.649731'),
(20, 'usuarios', '0003_alter_permiso_table_alter_rol_table_and_more', '2024-05-15 19:44:37.696503'),
(21, 'usuarios', '0004_alter_permiso_table_alter_rol_table_and_more', '2024-05-15 19:44:37.739243'),
(22, 'pedidos', '0001_initial', '2024-05-15 19:44:37.797191'),
(23, 'pedidos', '0002_tipoproducto_producto', '2024-05-15 19:44:37.855288'),
(24, 'pedidos', '0003_pedido_detallepedidoproducto', '2024-05-15 19:44:37.982455'),
(25, 'pedidos', '0004_detallepedidoservicio', '2024-05-15 19:44:38.066659'),
(26, 'pedidos', '0005_alter_producto_estado_catalogo_and_more', '2024-05-15 19:44:38.136334'),
(27, 'pedidos', '0006_alter_tiposervicio_estado_tiposervicio', '2024-05-15 19:44:38.149577'),
(28, 'pedidos', '0007_alter_pedido_estado_pedido_and_more', '2024-05-15 19:44:38.178406'),
(29, 'pedidos', '0008_remove_pedido_id_cliente', '2024-05-15 19:44:38.193408'),
(30, 'pedidos', '0009_alter_pedido_fechacreacion_pedido_and_more', '2024-05-15 19:44:38.235929'),
(31, 'pedidos', '0010_alter_pedido_evidencia_pago', '2024-05-15 19:44:38.277195'),
(32, 'pedidos', '0011_alter_pedido_evidencia_pago', '2024-05-15 19:44:38.307978'),
(33, 'pedidos', '0012_alter_pedido_evidencia_pago', '2024-05-15 19:44:38.371516'),
(34, 'pedidos', '0013_alter_pedido_evidencia_pago', '2024-05-15 19:44:38.438176'),
(35, 'pedidos', '0014_alter_pedido_evidencia_pago', '2024-05-15 19:44:38.476374'),
(36, 'pedidos', '0015_alter_pedido_evidencia_pago', '2024-05-15 19:44:38.535137'),
(37, 'pedidos', '0016_alter_pedido_evidencia_pago', '2024-05-15 19:44:38.544137'),
(38, 'reservas', '0001_initial', '2024-05-15 19:44:38.599767'),
(39, 'reservas', '0002_alter_reserva_table', '2024-05-15 19:44:38.621775'),
(40, 'reservas', '0003_alter_reserva_estado', '2024-05-15 19:44:38.651510'),
(41, 'reservas', '0004_alter_reserva_fecha', '2024-05-15 19:44:38.664556'),
(42, 'reservas', '0005_alter_reserva_fecha', '2024-05-15 19:44:38.670920'),
(43, 'reservas', '0006_alter_reserva_fecha', '2024-05-15 19:44:38.679922'),
(44, 'sessions', '0001_initial', '2024-05-15 19:44:38.706107'),
(45, 'usuarios', '0005_alter_permiso_table_alter_rol_table_and_more', '2024-05-15 19:44:38.756240'),
(46, 'usuarios', '0006_alter_usuario_idrol', '2024-05-15 19:44:38.890307'),
(47, 'usuarios', '0007_rol_permisos', '2024-05-15 19:44:38.983901'),
(48, 'usuarios', '0008_delete_rolxpermiso', '2024-05-15 19:44:38.993575'),
(49, 'usuarios', '0009_alter_usuario_idrol', '2024-05-15 19:44:39.116542'),
(50, 'usuarios', '0010_alter_usuario_correo', '2024-05-15 19:44:39.135546'),
(51, 'ventas', '0001_initial', '2024-05-15 19:44:39.186377'),
(52, 'pedidos', '0017_alter_servicio_estado_catalogo', '2024-05-21 20:23:43.646056'),
(53, 'pedidos', '0018_alter_servicio_estado_catalogo_and_more', '2024-05-28 19:23:52.375376'),
(54, 'pedidos', '0019_alter_producto_estado_catalogo', '2024-05-28 19:23:52.431542'),
(55, 'usuarios', '0011_usuario_imagen', '2024-05-30 19:28:44.903664'),
(56, 'pedidos', '0020_pedido_productos_pedido_servicios', '2024-06-07 21:20:06.167601'),
(57, 'reservas', '0007_alter_reserva_descripcion', '2024-07-11 19:54:27.852080');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0ow27q273m15kkqcgy3dgogimr7uf0kv', '.eJxdkMFqwkAQhl9F5hwM9JhTRXIo2CJFexFZ1uw0jGR3wkxSD-K7O4lW0952vvl2-f89A2rnA0MBC8hAuLHTsiFMHdpMwY3oJYMWJZKyQrGDMlDnZbZG-abGtBXpML-TGgsUzMp-pb9wYn6iovz4f-qETtwvy2Nsn0GvvRdiR2FMlTgeBN2dDtlXb-XHpoSH-ewz2562xisWQZ5cqW7r1zp6auYVx6F49DUm194aFpBHq-Dz3sK5cac5VZxYUYnT_NjWw8teOvue_eUKWlV0fA:1sIEud:v6EmCbr0_kpqvVH_JRWXbYigkKeVMoFL_9o6y_VhSa4', '2024-06-28 21:56:47.312062'),
('2nobz2457itw37ip6h8eqnpx45u8jhkb', '.eJxdj00LwjAMQP_KyLl48LiTID0IU0Q2LyKjrlEC7SLppgfxv9vNr-oxLy_wcgNhBznMHWHbISggW49oquCM4ilwgHwH2lJnJFujHMlFraAwzEsKkVmy0VJv6Rcm5gYDysX8qQlN3G3siWyvoA-9EeKa7FjVsj8I1i86tBcLvSo1fMzvP1l1rSJvWAQ5OWme69nJG3KThj3cH3j3Wkg:1s7Kc2:N6nA_CrUZ71nwCPFZLZRYm9yndxgNLka7MkmXJGOvMg', '2024-05-29 19:48:30.580024'),
('3r5snl87iqw8jua2tdetxpqm2siouxcv', '.eJxtk01PwzAMhv_K5HOFxHUnJrbDJAZTt3JBqCpNmCylzeS0cED8d9LhpG7Tox83j9_m4wfIGljDRjXYQgaoyhu4z-CqqUFnHazf4AldV9GqcH1F6FEGj6SnYKewWyS5NQt054XKLjSOmj7RDLVBn2mq5BxeqccQoRrn6XRQpMEaACuP4W9lkBlhlWiExWRVX3diYyQJPolCCglZdsarXTAmmLUpD-6kwwNOmr6wlscoCWsnKBgllGlTY4Jl2kV30okHo1BJcEAnIG93rOPhzcB01bj_c3uunc9QzeYJynduBOHaJWS2cLx5yYhX3XZCHkuRgNl7Bv3_cyhR3Z5pa5sP0iXT4SlvD_vn_emcb7YvOcTvwyNfFd-Fp7Ul0lYsq4bmw6Wp0NzVtoHfP3bcaaU:1s9W2W:8xQalRWH-gb8sQ0TI8uzLtSFh4dGg3C2RRBEZ3Jy5EA', '2024-06-04 20:24:52.368643'),
('7d4d0xs2e5e09kzkrat0r5kwpniv3mpz', '.eJxtk01PwzAMhv_K5HOFxHUnJrbDJAZTt3JBqCpNmCylzeS0cED8d9LhpG7Tox83j9_m4wfIGljDRjXYQgaoyhu4z-CqqUFnHazf4AldV9GqcH1F6FEGj6SnYKewWyS5NQt054XKLjSOmj7RDLVBn2mq5BxeqccQoRrn6XRQpMEaACuP4W9lkBlhlWiExWRVX3diYyQJPolCCglZdsarXTAmmLUpD-6kwwNOmr6wlscoCWsnKBgllGlTY4Jl2kV30okHo1BJcEAnIG93rOPhzcB01bj_c3uunc9QzeYJynduBOHaJWS2cLx5yYhX3XZCHkuRgNl7Bv3_cyhR3Z5pa5sP0iXT4SlvD_vn_emcb7YvOcTvwyNfFd-Fp7Ul0lYsq4bmw6Wp0NzVtoHfP3bcaaU:1s7KYp:fTPZQFyhNLVCWNaQeHGC7BF3NEzDcQrZmc68ljNtNpo', '2024-05-29 19:45:11.716386'),
('928zlmjurgz9pn55ca2ru006qnnuds1e', '.eJxdkDELwjAQhf9KuTk4OHYSJINQRcS6iJTYnHKQ9OTS6iD-d2NbNHa8731vePcEYQc5LB1h0yIoIFv1aK7ghuIpcID8CNpSayTbolzIRa2gMN6DohJjQnQ0LafBWF5TiNSSTe1_mJg7DCh3M1ETmriHOCayk4IudEaIK7L9pIb9WbAa6Wd4sdKbvYav-XtGVj7KyGsWQU4q9RAvrt6Qm9Xs4fUG49dvjw:1s7KYf:3vTmyoMixvNMWSNBepP3tNXaEZDvbSLO7mkMnUlh9v0', '2024-05-29 19:45:01.543988'),
('9h1zjweljqsl0qgvtgy5w0jbq284kl02', '.eJxdkMFqwzAMhl8l6Gwa2DGnjrLbNkqhu4xi1FgLGrEVpGSXsXevknZbtpv1-bP5f30C2YhJoIF7CKDS-2nXM5WRfOYUF3QXYCDNbGLQvMJD4hG12pO-ce_aI9s8P7E5S5zcCt_SX7gyD2SkH_hPXdGV--J5nJ0CTDahskROS6oi-awUb9SzPy-g2utEZ4Qf_7dVdbyRAK2okqwet1dl22XkftNKnleQsaMSh2vXBursZbCePGZc7qzmVooYGUvZvA_d_DPq6Is6fV0Ahf95IQ:1sLRoO:kc223R-NqF_mVKrsDEaWxGVGsazHblqibqr2-LrmnpM', '2024-07-07 18:19:36.676148'),
('bdaxa4iosgz8yvdjq9e04md2xpfzzp5r', '.eJxdkDELwjAQhf9KuTk4OHYSJINQRcS6iJTYnHKQ9OTS6iD-d2NbNHa8731vePcEYQc5LB1h0yIoIFv1aK7ghuIpcID8CNpSayTbolzIRa2gMN6DohJjQnQ0LafBWF5TiNSSTe1_mJg7DCh3M1ETmriHOCayk4IudEaIK7L9pIb9WbAa6Wd4sdKbvYav-XtGVj7KyGsWQU4q9RAvrt6Qm9Xs4fUG49dvjw:1s7KYf:3vTmyoMixvNMWSNBepP3tNXaEZDvbSLO7mkMnUlh9v0', '2024-05-29 19:45:01.182958'),
('bylpqfqx35zbf2xyi7cox0d3qw7rq2l9', '.eJxtlMFugzAMhl-lyhm12rWnVWsPldatou0uU4Uy4lWeCEYJbIdp775AEzCEG_6Mf_84Mb8CbC0VibXYiEQYKtonpbF0EaqsAw-JqMBotGTF-l08oysxi4ttpEGHEvFkYAx2CutZklIxQ3edh5nEEcwnFm1coPM0lvQ-nCQMJkI09IO4UU-DagBe8hi-lhuZEC_FEqHYkGrymg2Gk6DHUXDBoRc7Y0UzihH2sjEP2lHGNziB-cacHyMnXnaEgiKH3G2sGGHudlY7yvQHo1BxcEDLoB93H_eHNwHjqmH-U_UUrPMgJ_0Y9XduAOHaRWRSONy8qMUblDUT70PmwLNrIpr7OmSoujUtSX8YyDxtV3l72L_sT-d0s31NRf9-WPLF5efiaE7GALEy2SYfb1piscxJt_8CLW9QZtV9Iddipd2w5Kpx7rMuZ1eYU0kWLFK5_Kpura40tftjXP_-AWydg9k:1sFh8I:f70qJ6yjJbqpggwb0wwHkCXis--arLCoTE0gc8WNsys', '2024-06-21 21:28:22.560855'),
('feo7ph66aobeabg0e74xfu6zy24ik7jm', '.eJxdkMFqwzAMhl8l6Gwa2DGnjrLbNkqhu4xi1FgLGrEVpGSXsXevknZbtpv1-bP5f30C2YhJoIF7CKDS-2nXM5WRfOYUF3QXYCDNbGLQvMJD4hG12pO-ce_aI9s8P7E5S5zcCt_SX7gyD2SkH_hPXdGV--J5nJ0CTDahskROS6oi-awUb9SzPy-g2utEZ4Qf_7dVdbyRAK2okqwet1dl22XkftNKnleQsaMSh2vXBursZbCePGZc7qzmVooYGUvZvA_d_DPq6Is6fV0Ahf95IQ:1sLSE2:GsqFeoP3CW0Vv0i0mtpvTLTCtky2ANE8nK_xLt0Z-EM', '2024-07-07 18:46:06.115826'),
('fyznt84cyullkimft2p2f8zebcjekxbf', '.eJxdkMFqwzAMhl8l6Gwa2DGnjrLbNkqhu4xi1FgLGrEVpGSXsXevknZbtpv1-bP5f30C2YhJoIF7CKDS-2nXM5WRfOYUF3QXYCDNbGLQvMJD4hG12pO-ce_aI9s8P7E5S5zcCt_SX7gyD2SkH_hPXdGV--J5nJ0CTDahskROS6oi-awUb9SzPy-g2utEZ4Qf_7dVdbyRAK2okqwet1dl22XkftNKnleQsaMSh2vXBursZbCePGZc7qzmVooYGUvZvA_d_DPq6Is6fV0Ahf95IQ:1sLTfu:4MRssrTCWNPJQ5OOAQFlfDYc26BxNFrid4AHanpsb0o', '2024-07-07 20:18:58.275174'),
('gaj29kofujp89kggs1obkb2hcxd5wkm3', '.eJxdkDELwjAQhf9KuTk4OHYSJINQRcS6iJTYnHKQ9OTS6iD-d2NbNHa8731vePcEYQc5LB1h0yIoIFv1aK7ghuIpcID8CNpSayTbolzIRa2gMN6DohJjQnQ0LafBWF5TiNSSTe1_mJg7DCh3M1ETmriHOCayk4IudEaIK7L9pIb9WbAa6Wd4sdKbvYav-XtGVj7KyGsWQU4q9RAvrt6Qm9Xs4fUG49dvjw:1s7KYf:3vTmyoMixvNMWSNBepP3tNXaEZDvbSLO7mkMnUlh9v0', '2024-05-29 19:45:01.704000'),
('hjawsdl5k6594vb97pxmogtlbm6btcf9', '.eJx9lE1vwjAMhv8KyrkC7cppCDgg7QMB22VCVWiyylOTVEmLNE3770tKkrpN2a1-bL92Etc_hJuGMkWWZEUyolXlvpgAaS1geQceMlJzLcAoQ5Yf5Alsip69mZZqsCgja82HYMugmSQHVU3QbdfDhGPP9SdUzq7A9jSU9H1YSd43Eay-Hk8LRRpUA_CS-3DanmjF2qJBp8UkdItRkMbQi52gVhOKCfayKQ_aiccXOHJ9hQK_DSZedoCCIoa421QxwbjbSe3EE2-bAcPgGQyC_rqjHUdjBIZZYTi4sQXpSBxRPzU9CIOTkFFiPztJiXcuGyQeTdRBZMPBTA61vQLjsgA64bql3JuaoHjXs6YNrVQ5mkQqLmBjdoKWXP7nmnh6Lxw8scLdCHLOSHv7oXNg3aKRSlw0zz11y2jzvHvZHU-H1eb1QGJ8WFMz0X7P7AOAq1IorblCydSFPJaCQjUvlHA7res-r2-LZUkWwt4rXbRWIu98ZgGFkspwA0rOv-rS6VLd2M13_v0DauLKaA:1sLVjr:qG7cGrvFtw75rquZc9FsgklREAH8xSHKrjIa4S35_DM', '2024-07-07 22:31:11.875785'),
('j375f0t1esihzivm0v4nn7ik54or7ns4', '.eJxtk01PwzAMhv_K5HOFxHUnJrbDJAZTt3JBqCpNmCylzeS0cED8d9LhpG7Tox83j9_m4wfIGljDRjXYQgaoyhu4z-CqqUFnHazf4AldV9GqcH1F6FEGj6SnYKewWyS5NQt054XKLjSOmj7RDLVBn2mq5BxeqccQoRrn6XRQpMEaACuP4W9lkBlhlWiExWRVX3diYyQJPolCCglZdsarXTAmmLUpD-6kwwNOmr6wlscoCWsnKBgllGlTY4Jl2kV30okHo1BJcEAnIG93rOPhzcB01bj_c3uunc9QzeYJynduBOHaJWS2cLx5yYhX3XZCHkuRgNl7Bv3_cyhR3Z5pa5sP0iXT4SlvD_vn_emcb7YvOcTvwyNfFd-Fp7Ul0lYsq4bmw6Wp0NzVtoHfP3bcaaU:1s7h7Y:3-Y0GwmbLM7YSOfR6xGRDVfkWKfzU9hX5398rFR-56w', '2024-05-30 19:50:32.234621'),
('kqzuf3dwddf7m0ll820s9tovlv9fxkys', '.eJxdkMFqwkAQhl9F5hwM9JhTRXIo2CJFexFZ1uw0jGR3wkxSD-K7O4lW0952vvl2-f89A2rnA0MBC8hAuLHTsiFMHdpMwY3oJYMWJZKyQrGDMlDnZbZG-abGtBXpML-TGgsUzMp-pb9wYn6iovz4f-qETtwvy2Nsn0GvvRdiR2FMlTgeBN2dDtlXb-XHpoSH-ewz2562xisWQZ5cqW7r1zp6auYVx6F49DUm194aFpBHq-Dz3sK5cac5VZxYUYnT_NjWw8teOvue_eUKWlV0fA:1sHqHF:gNlZ69-UvehdBYQcYFgKKDxD_u4B6j_OmFXUtduCgrs', '2024-06-27 19:38:29.837468'),
('l0uudw26i87mbljp9kfci11nib1jlelz', '.eJxdkDELwjAQhf9KuTk4OHYSJINQRcS6iJTYnHKQ9OTS6iD-d2NbNHa8731vePcEYQc5LB1h0yIoIFv1aK7ghuIpcID8CNpSayTbolzIRa2gMN6DohJjQnQ0LafBWF5TiNSSTe1_mJg7DCh3M1ETmriHOCayk4IudEaIK7L9pIb9WbAa6Wd4sdKbvYav-XtGVj7KyGsWQU4q9RAvrt6Qm9Xs4fUG49dvjw:1s7KYf:3vTmyoMixvNMWSNBepP3tNXaEZDvbSLO7mkMnUlh9v0', '2024-05-29 19:45:01.324971'),
('mfa2ojwvo5wg03q64nms0t29dssqa0vb', '.eJx9lE1rwzAMhv_K8Dm0sA8GOW10PQw6KPu6jBLU2A0ajh3spIeN_fc5iZ2ocdpb_LzSK9kR-mXC1sA1S9kjS5jRsv1SINFhB5BnHbtNWCVMiVZbln6xTSubqw_bgEGHErYy4hSsOdaz5FXLGbru2pgRtsIcULqzr-nSxVgwnEZvEZsOVGKJioR5y2242TSRCCHUaN7kNbkyJaFlikJNCr3ZO1Z6xjHC3jbmwTtSfIE3YY6Y0x9Eibc9QcGRQtpt7Bhh2u2sd6QMv4Ejp-AFLYH-uYfzMB8TcJoVpkZYVxAm5oT6cRpBmKiITBLHoYpKfApVE_PhSDqYhFyYxMkt10fkQuUIM1Kfcm6MguNZZQU1SF1MRhPKPbqY5xIKoS5JM7PgjYMyVDgbwXYJa_pVkCFn6U3ClC73RmSeui31BAqldi9oCjBwtdGV-GFDWh-QGzjUDubaGKFJMu-Sj33u9d39Q1ECykWuy3bpdRfJqn7zpGxZuieGZeP-b9Zpdom5VtoKi1otvquiLQGmdqtx9_cPzJ7YKA:1sRfSd:H3UIdKSZhvyBeLC-Tw5MZyYrTduw5VkNzUBLbuZA1lM', '2024-07-24 22:06:51.481008'),
('pe8noj4uyrz9sytzlvopi7alkk12zac0', '.eJxtlMFugzAMhl-lyhm12rWnVWsPldatou0uU4Uy4lWeCEYJbIdp775AEzCEG_6Mf_84Mb8CbC0VibXYiEQYKtonpbF0EaqsAw-JqMBotGTF-l08oysxi4ttpEGHEvFkYAx2CutZklIxQ3edh5nEEcwnFm1coPM0lvQ-nCQMJkI09IO4UU-DagBe8hi-lhuZEC_FEqHYkGrymg2Gk6DHUXDBoRc7Y0UzihH2sjEP2lHGNziB-cacHyMnXnaEgiKH3G2sGGHudlY7yvQHo1BxcEDLoB93H_eHNwHjqmH-U_UUrPMgJ_0Y9XduAOHaRWRSONy8qMUblDUT70PmwLNrIpr7OmSoujUtSX8YyDxtV3l72L_sT-d0s31NRf9-WPLF5efiaE7GALEy2SYfb1piscxJt_8CLW9QZtV9Iddipd2w5Kpx7rMuZ1eYU0kWLFK5_Kpura40tftjXP_-AWydg9k:1sJHkG:a0NG0w1tWEWyI9WbRHrM6EgSaoLXYN1omz_4_55pLEs', '2024-07-01 19:10:24.760985'),
('rt0j39jmulyw9r3gfxr093y30ua92kmj', '.eJx9lMtqwzAQRX-laG0S6IOCVy1pFoUUQvrYlGIUSzFT9DCSnUVL_72yLdkTyclOOldzZ0Ya9Eu4bSjTJCePJCNGi26lqACHHQBW9Ow2IzU3Eqy2JP8km042V--2pQYcysjK8FOwZtDMkp0WM3TdlzEjbLk5gOj2AiSoU0tfh7PkUxFhN-XjaaKRBtcAvOU2dBsHIiEcNZq1ZYOuAZPQBkYhJ4be7A1qPeOYYG-b8uCdKD7BKzdHKPGjYeJtT1BwxBBXmzomGFc7650o4zMwYBi8gEXQX_e4H2cmAqdR0_3H7jtuXQ00yoeon7AJhCFLSBQ4zVmS4oOrBpmPW1RBdOTCcEaNr4_AuCqBzkhDyLnJCo5nlRVtqNBVNK1U7sGdeZa04uqSNDMe3jgoY4azJ-abmZy_MtIOn0UBjOQ3GVFa7g0vPHV_3RNVILS7YFNRQ682uuY_ZAwbDpSGHhoHS20M1yiY9cHHIfb67v6hkhTEotSy-zr7Pot6-L9yspTuBeiydc9f9JpdQqmVttyCVovvuiJ__1UP7Z0:1sUAIP:_kP4ZxVF4EWPMSZkUvdhmwMhzL_qRuEHHpPH8nd5v0k', '2024-07-31 19:26:37.048294'),
('wn8nx0gpuv3qoa3xsbiibud529zwvowc', '.eJxdjz0LwkAMhv9KyVwcHDsp0kGoImJdRMrZixK4ayTX6iD-d9P6dbrlffIE3twAQ2ssQwZTSEHY6TRzhE2LmslWAxqncEbxFDhAtoPcUmskWaEcyalWUOjzgoIyS1at9C39wshcY0C5mD81opG71T7K9il0oTNCXJEdWjXsD4LVi_bdi3m-3OTwMb__JOW1VF6zCHJ0Uj_Xk5M35EY1e7g_AGzQXfc:1sCPCa:29Sm9ReUdWQwQ4mKdJchGyttskUSkaDoEBQrShBY1HA', '2024-06-12 19:43:12.244106'),
('xfh7giiqv29zpzoqu7xn5ob1qbu75uqi', '.eJxdkMFKxEAMhl9lyXnYwooIPSnqbQXx4EVkiJ1syTIzKUm7B8V3N9uqVG-Tb74f_uQDyEZMAi3cQACV7K_bzFRH8plTnNEuwEBa2MSgfYH7xCPq5pH0wNm1Pdt5fmBzlji5FX6kv3BlPpGRnvCfuqIr99n7OHsNMNmEyhI5QXsRoEp5U4rf1LvfYeUsHtAeFTd7GegdfmOL0CkeRoedqJKswmkOn5bs7vLqui_IedtJOd-iYE81DsvSLTTFt8Jm8r5x_rOGO6liZCx1exx6-PwC-3Z5DQ:1sJKbN:Y1G3G8VIYBzzQYmG8ElIbFEqVpqfeDk_kc3D9U_mj_w', '2024-07-01 22:13:25.741545'),
('yihqhfmrqvbaajim8wkpf5slnh0wqzxh', '.eJxtk01vgzAMhv9K5TOqtGtPq9YeKq1bRcsu04QY8SpLQCoHusO0_77AkmAIt_px8_glHz-Api2Uhg1sIQHWVf9L1dTYilQ-gIcEbsg1GW1g8w7PZJfwKjNdwWRRAk-MU7BX1C6SVFcLdD9kWGickL-o6uuKbKap0uWwShxD-Gqch_GgQL3VA6c8-a-VQWbEqUTDL2aturIVGyOJ90nkU0joZBe66QVjhJ025t4dddyAM_KdSnmMkjjtBHmjhDJtbIywTLvojjrhYBQpCY5kBHTbHepweDMwXTXu_9yeorEZitk8Qd2dG4G_dhGZLRxvXjTiDZtWyEMpEjj2kUD3_xxyUsMzbXT9yZg72j_l3fHwcjhf0u3uNYXwf__IV9l3ZmmpmVGLZUXffLzWBVXrUtfw-we2-W1U:1sC2Su:gAs_UmOg_UM1p7fD1L0tpwlMCTb1urWkUkNH-34iJrU', '2024-06-11 19:26:32.160632'),
('zdr0uesxlk0g3f5nmpry0ztm0pd8zrmc', '.eJxdkE1PwzAMhv_K5HO0jkkMqSfQ4MKHhDhwQVMUGtN6JHFlt1wQ_x23gCjc7CdPrNd-B9QhRIYaLsCBcLJqnwjLgNZT9DPaOuhRMikr1E9wFWkIsrpHeaFk2i3p1N-RGosUzXI_0l-4MB9QUd7CP3VBF-6j5TF2cDDqGITYU4R656Bwfhb039SyX3dc7EvTBUyrPZdBUOZpv8plkNcbKu3pyc54wyLIiwnHjnOgs812c95akdYN5-kUObRYfP-1cw1VtqVCNVpcP79pRQ0XVlTisj727TQ8yGAHO3x8AucFeq4:1sKmJz:UXxhQebc_SGfURo50aCEl_b6ScO7ljUEhOYksvWjhYI', '2024-07-05 22:01:27.927395');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedidos`
--

CREATE TABLE `pedidos` (
  `idPedido` int(11) NOT NULL,
  `fechaCreacion_pedido` datetime(6) NOT NULL,
  `fecha_pedido` datetime(6) NOT NULL,
  `descripcion_pedido` varchar(255) NOT NULL,
  `subtotal` decimal(10,2) NOT NULL,
  `iva` decimal(10,2) NOT NULL,
  `total` decimal(10,2) NOT NULL,
  `evidencia_pago` varchar(100) NOT NULL,
  `estado_pedido` varchar(80) NOT NULL,
  `id_Usuario_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pedidos`
--

INSERT INTO `pedidos` (`idPedido`, `fechaCreacion_pedido`, `fecha_pedido`, `descripcion_pedido`, `subtotal`, `iva`, `total`, `evidencia_pago`, `estado_pedido`, `id_Usuario_id`) VALUES
(8, '2024-06-17 22:13:25.716010', '2024-08-06 05:00:00.000000', 'Enumerar cada muñeco del 1 al 4', 300000.00, 57000.00, 357000.00, 'pedidos/comprobante_prueba.png', 'Por hacer', 3),
(9, '2024-06-21 21:45:38.948645', '2024-07-03 05:00:00.000000', 'quiero que el moño sea morado', 30000.00, 5700.00, 35700.00, 'pedidos/74d25d5f-0b96-48cb-a1f8-55bfa66d2154', 'Entregado', 2),
(10, '2024-06-23 18:33:51.043874', '2024-07-12 05:00:00.000000', 'quiero que el  muñeco de costura sea azul', 560000.00, 106400.00, 666400.00, 'pedidos/images.jpeg', 'Por hacer', 6),
(11, '2024-07-10 22:02:50.785832', '2024-07-31 05:00:00.000000', 'quiero que el mario sea verde', 60000.00, 11400.00, 71400.00, 'pedidos/Captura_de_pantalla_2024-02-04_224354.png', 'Entregado', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `permisos`
--

CREATE TABLE `permisos` (
  `id` bigint(20) NOT NULL,
  `nombre_permiso` varchar(50) NOT NULL,
  `estado_permiso` varchar(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `permisos`
--

INSERT INTO `permisos` (`id`, `nombre_permiso`, `estado_permiso`) VALUES
(1, 'Listar Usuarios', 'A'),
(2, 'Crear Usuarios', 'A'),
(3, 'Editar Usuarios', 'A'),
(4, 'Editar Rol Usuarios', 'A'),
(5, 'Editar Estado Usuarios', 'A'),
(6, 'Editar Perfil', 'A'),
(7, 'Eliminar Usuarios', 'A'),
(8, 'Listar Roles', 'A'),
(9, 'Crear Roles', 'A'),
(10, 'Editar Roles', 'A'),
(11, 'Editar Estado Roles', 'A'),
(12, 'Eliminar Roles', 'A'),
(13, 'Listar Permisos', 'A'),
(14, 'Editar Permisos', 'I'),
(15, 'Editar Estado Permisos', 'A'),
(16, 'Listar Productos', 'A'),
(17, 'Crear Productos', 'A'),
(18, 'Editar Productos', 'A'),
(19, 'Eliminar Productos', 'A'),
(20, 'Listar Tipo Productos', 'A'),
(21, 'Crear Tipo Productos', 'A'),
(22, 'Editar Tipo Productos', 'A'),
(23, 'Eliminar Tipo Productos', 'A'),
(24, 'Listar Servicios', 'A'),
(25, 'Crear Servicios', 'A'),
(26, 'Editar Servicios', 'A'),
(27, 'Eliminar Servicios', 'A'),
(28, 'Listar Tipo Servicios', 'A'),
(29, 'Crear Tipo Servicios', 'A'),
(30, 'Editar Tipo Servicios', 'A'),
(31, 'Eliminar Tipo Servicios', 'A'),
(32, 'Listar Pedidos', 'A'),
(33, 'Listar Mis Pedidos', 'A'),
(34, 'Crear Pedidos', 'A'),
(35, 'Editar Pedidos', 'A'),
(36, 'Editar Mis Pedidos', 'A'),
(37, 'Eliminar Pedidos', 'A'),
(38, 'Listar Reservas', 'A'),
(39, 'Listar Mis Reservas', 'A'),
(40, 'Crear Reservas', 'A'),
(41, 'Editar Reservas', 'A'),
(42, 'Editar Mis Reservas', 'A'),
(43, 'Eliminar Reservas', 'A'),
(44, 'Listar Ventas', 'A'),
(45, 'Crear Ventas', 'A'),
(46, 'Listar Mis Ventas', 'A'),
(47, 'Crear Permisos', 'A'),
(48, 'Eliminar Permisos', 'I'),
(49, 'Editar Estado Pedidos', 'A'),
(50, 'Editar Evidencia Pedidos', 'A'),
(51, 'Editar Estado Tipo Productos', 'A'),
(52, 'Editar Estado Productos', 'A'),
(53, 'Editar Estado Catalogo Productos', 'A'),
(54, 'Cambiar Imagen Productos', 'A'),
(55, 'Cambiar Imagen Servicios', 'A'),
(56, 'Editar Estado Servicio Catalogo', 'A'),
(57, 'Editar Estado Servicio', 'A'),
(58, 'Editar Estado Tipo Servicios', 'A');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `idProducto` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `imagen` varchar(100) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `estado_producto` varchar(1) NOT NULL,
  `estado_catalogo` varchar(1) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `id_TipoProducto_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`idProducto`, `nombre`, `descripcion`, `imagen`, `precio`, `estado_producto`, `estado_catalogo`, `cantidad`, `id_TipoProducto_id`) VALUES
(5, 'Muñeco Mario panadero', 'Muñeco de Mario versión panadero', 'producto_imgs/mario.png', 50000.00, 'A', 'A', 1, 1),
(6, 'Muñeca vestido verde', 'Muñeca con vestido verde para niños pendejos', 'producto_imgs/muñecaverde.jpg', 25000.00, 'A', 'A', 0, 1),
(7, 'Muñeco de costura', 'Muñeco con costura remarcada', 'producto_imgs/muñecocostura.jpg', 10000.00, 'A', 'A', 0, 1),
(8, 'Tendido crochet', 'Tendido tejido a mano con estilo crochet', 'producto_imgs/tendidocrochet.jpg', 60000.00, 'A', 'A', 10, 2),
(9, 'Mantel Crochet', 'Mantel para mesa redonda tejido a mano tamaño 1m de diámetro', 'producto_imgs/mantelcrochet.jpg', 40000.00, 'A', 'A', 4, 2),
(10, 'Individuales crochet', 'individuales para mesa familiar 20cm de diámetro 4 unidades', 'producto_imgs/individualescrochet.jpg', 20000.00, 'A', 'A', 10, 2),
(11, 'Moño perlas', 'Moño color negro con perlas incrustadas', 'producto_imgs/moñoperlas.jfif', 5000.00, 'A', 'A', 19, 3),
(12, 'Arete dorado', 'Arete dorado para niña y mujer', 'producto_imgs/aretes.jfif', 4000.00, 'A', 'A', 12, 3),
(13, 'Collar perlado', 'Collar de perlas ajustable', 'producto_imgs/collarperlas.jfif', 4000.00, 'A', 'A', 5, 3),
(14, 'Vestido Verde', 'Vestido verde talla S', 'producto_imgs/vestidoverde.jfif', 50000.00, 'A', 'A', 5, 4),
(15, 'Vestido negro', 'Vestido negro talla S', 'producto_imgs/vestidonegro.jfif', 50000.00, 'A', 'A', 5, 4),
(16, 'Vestido Blanco', 'Vestido blanco talla S', 'producto_imgs/vestidoblanco.jfif', 55000.00, 'A', 'A', 5, 4),
(17, 'Uniforme Medico de hombre', 'Uniforme de medico para hombre talla M Color azul claro', 'producto_imgs/Uniforme_azul_claro.jfif', 70000.00, 'A', 'A', 2, 5),
(18, 'Uniforme Medico Mujer', 'Uniforme medicina para mujer, talla S, Color rosado', 'producto_imgs/UniformeRosadomujer.jfif', 70000.00, 'A', 'A', 5, 5),
(19, 'Uniforme de preescolar niño', 'Uniforme para niños de preescolar', 'producto_imgs/Uniformepreescolar.jfif', 40000.00, 'A', 'A', 10, 5),
(20, 'Camisa Negra', 'Camisa para hombre color negro, talla M', 'producto_imgs/CamisaNegra.jfif', 30000.00, 'A', 'A', 15, 6),
(21, 'Camisa Rosa', 'Camisa rosa para hombres', 'producto_imgs/CamisaRosa.jfif', 30000.00, 'A', 'A', 12, 6),
(22, 'Camisa mujer', 'Camisa para mujer color beige', 'producto_imgs/CamisaMujer.jfif', 25000.00, 'A', 'A', 7, 6),
(23, 'Luffy Crochet', 'Manualidad de one piece personaje Monkey D Luffy', 'producto_imgs/luffycrochet.jfif', 100000.00, 'A', 'A', 14, 2),
(24, 'Caballerito Crochet', 'Manualidad De Hollow knight Caballerito de crochet', 'producto_imgs/CaballeritoCrochet.jfif', 100000.00, 'A', 'A', 15, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservas`
--

CREATE TABLE `reservas` (
  `id` bigint(20) NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `fecha_cita` datetime(6) NOT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  `estado` varchar(80) NOT NULL,
  `usuario_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `reservas`
--

INSERT INTO `reservas` (`id`, `fecha`, `fecha_cita`, `descripcion`, `estado`, `usuario_id`) VALUES
(5, '2024-06-21 21:57:12.679182', '2024-06-22 23:00:00.000000', 'quiero arreglar el cierre de un pantalon', 'Cancelada', 2),
(6, '2024-06-23 20:13:10.446564', '2024-06-29 22:30:00.000000', 'quiero reunirme con la dueña para cotizar un vestido de bodas', 'Pendiente', 6),
(7, '2024-07-10 21:53:12.139201', '2024-07-19 21:53:00.000000', 'quiero ver a la linda de Erika', 'Pendiente', 3),
(8, '2024-07-17 19:27:13.378365', '2024-07-20 19:30:00.000000', 'www', 'Pendiente', 3),
(9, '2024-07-17 19:27:56.913528', '2024-07-22 19:30:00.000000', 'h', 'Pendiente', 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `id` bigint(20) NOT NULL,
  `nombre_rol` varchar(50) NOT NULL,
  `estado_rol` varchar(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`id`, `nombre_rol`, `estado_rol`) VALUES
(1, 'Admin', 'A'),
(2, 'Cliente', 'A'),
(3, 'Moderador', 'I'),
(4, 'Analista', 'A');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles_permisos`
--

CREATE TABLE `roles_permisos` (
  `id` bigint(20) NOT NULL,
  `rol_id` bigint(20) NOT NULL,
  `permiso_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `roles_permisos`
--

INSERT INTO `roles_permisos` (`id`, `rol_id`, `permiso_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 1, 4),
(5, 1, 5),
(6, 1, 6),
(7, 1, 7),
(8, 1, 8),
(9, 1, 9),
(10, 1, 10),
(11, 1, 11),
(12, 1, 12),
(13, 1, 13),
(16, 1, 16),
(17, 1, 17),
(18, 1, 18),
(19, 1, 19),
(20, 1, 20),
(21, 1, 21),
(22, 1, 22),
(23, 1, 23),
(24, 1, 24),
(25, 1, 25),
(26, 1, 26),
(27, 1, 27),
(28, 1, 28),
(29, 1, 29),
(30, 1, 30),
(31, 1, 31),
(32, 1, 32),
(33, 1, 33),
(34, 1, 34),
(35, 1, 35),
(36, 1, 36),
(38, 1, 38),
(39, 1, 39),
(40, 1, 40),
(41, 1, 41),
(42, 1, 42),
(43, 1, 43),
(44, 1, 44),
(45, 1, 45),
(46, 1, 46),
(134, 1, 49),
(135, 1, 50),
(136, 1, 51),
(137, 1, 52),
(138, 1, 53),
(139, 1, 54),
(140, 1, 55),
(141, 1, 56),
(142, 1, 57),
(64, 2, 6),
(68, 2, 33),
(69, 2, 36),
(70, 2, 39),
(71, 2, 42),
(72, 2, 46),
(151, 4, 1),
(152, 4, 2),
(153, 4, 3),
(154, 4, 4),
(155, 4, 5),
(196, 4, 6),
(156, 4, 7),
(82, 4, 8),
(85, 4, 9),
(86, 4, 10),
(200, 4, 11),
(201, 4, 12),
(183, 4, 13),
(185, 4, 15),
(157, 4, 16),
(158, 4, 17),
(159, 4, 18),
(160, 4, 19),
(164, 4, 20),
(166, 4, 21),
(167, 4, 22),
(168, 4, 23),
(169, 4, 24),
(172, 4, 25),
(173, 4, 26),
(174, 4, 27),
(176, 4, 28),
(180, 4, 29),
(181, 4, 30),
(182, 4, 31),
(187, 4, 32),
(188, 4, 33),
(189, 4, 34),
(190, 4, 35),
(191, 4, 36),
(192, 4, 37),
(195, 4, 38),
(197, 4, 39),
(198, 4, 40),
(199, 4, 41),
(202, 4, 42),
(203, 4, 43),
(204, 4, 44),
(205, 4, 45),
(206, 4, 46),
(184, 4, 47),
(193, 4, 49),
(194, 4, 50),
(165, 4, 51),
(163, 4, 52),
(161, 4, 53),
(162, 4, 54),
(170, 4, 55),
(171, 4, 56),
(175, 4, 57),
(186, 4, 58);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `servicios`
--

CREATE TABLE `servicios` (
  `idServicio` int(11) NOT NULL,
  `nombre_servicio` varchar(50) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `precio_servicio` decimal(10,2) NOT NULL,
  `estado_servicio` varchar(1) NOT NULL,
  `estado_catalogo` varchar(1) NOT NULL,
  `img` varchar(100) NOT NULL,
  `id_TipoServicio_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `servicios`
--

INSERT INTO `servicios` (`idServicio`, `nombre_servicio`, `descripcion`, `precio_servicio`, `estado_servicio`, `estado_catalogo`, `img`, `id_TipoServicio_id`) VALUES
(2, 'Hacer Camisa Hombre', 'Camisas para hombres, todas las tallas y todos los colores.\r\nDETALLAR LA TALLA Y EL COLOR EN LA PASARELA DE PAGO', 40000.00, 'A', 'A', 'servicio_imgs/camisasvarias.jfif', 1),
(3, 'Hacer Camisas Mujer', 'Camisas de mujer, todas las tallas, todos los colores\r\nDETALLAR LA TALLA Y EL COLOR EN LA PASARELA DE PAGO', 40000.00, 'A', 'A', 'servicio_imgs/Camisasmujervarias.jfif', 1),
(4, 'Pantalón hombre', 'Pantalón para hombres, todas las tallas y todos los colores. DETALLAR LA TALLA Y EL COLOR EN LA PASARELA DE PAGO', 90000.00, 'A', 'A', 'servicio_imgs/pantalon_hombre.jfif', 1),
(5, 'Pantalón mujer', 'Pantalón para mujer, todas las tallas y todos los colores. DETALLAR LA TALLA Y EL COLOR EN LA PASARELA DE PAGO', 90000.00, 'A', 'A', 'servicio_imgs/pantalonmujer.jfif', 1),
(6, 'Short Para hombre', 'Short para hombres, todas las tallas y todos los colores. DETALLAR LA TALLA Y EL COLOR EN LA PASARELA DE PAGO', 50000.00, 'A', 'A', 'servicio_imgs/pantaloneta_hombre.jfif', 1),
(7, 'Short para mujer', 'Short para mujer, todas las tallas y todos los colores. DETALLAR LA TALLA Y EL COLOR EN LA PASARELA DE PAGO', 50000.00, 'A', 'A', 'servicio_imgs/descargar.jfif', 1),
(8, 'Camisetas personalizadas', 'Camisetas personalizadas Todas las tallas y todos los diseños. DETALLAR LA TALLA Y EL COLOR EN LA PASARELA DE PAGO', 50000.00, 'A', 'A', 'servicio_imgs/sena.jfif', 1),
(9, 'Chaquetas', 'chaquetas unisex, todas las tallas y todos los colores. DETALLAR LA TALLA Y EL COLOR EN LA PASARELA DE PAGO', 150000.00, 'A', 'A', 'servicio_imgs/chaquetas.jfif', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_productos`
--

CREATE TABLE `tipo_productos` (
  `idTipo_Producto` int(11) NOT NULL,
  `nombre_producto` varchar(50) NOT NULL,
  `estado_producto` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tipo_productos`
--

INSERT INTO `tipo_productos` (`idTipo_Producto`, `nombre_producto`, `estado_producto`) VALUES
(1, 'Muñecos', 'Activo'),
(2, 'Manualidades', 'Activo'),
(3, 'Accesorios', 'Activo'),
(4, 'Vestidos', 'Activo'),
(5, 'Uniformes', 'Activo'),
(6, 'camisas', 'Activo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_servicios`
--

CREATE TABLE `tipo_servicios` (
  `idTipo_Servicio` int(11) NOT NULL,
  `nombre_tipoServicio` varchar(50) NOT NULL,
  `estado_tipoServicio` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tipo_servicios`
--

INSERT INTO `tipo_servicios` (`idTipo_Servicio`, `nombre_tipoServicio`, `estado_tipoServicio`) VALUES
(1, 'Hacer Prendas', 'Activo'),
(2, 'Hacer Manualidades', 'Activo'),
(3, 'Hacer Arreglo', 'Activo'),
(4, 'Coser Prenda', 'Activo'),
(5, 'Hacer uniforme', 'Activo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `documento` varchar(15) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `usuario` varchar(20) NOT NULL,
  `contraseña` varchar(255) NOT NULL,
  `estado` varchar(1) NOT NULL,
  `idRol_id` bigint(20) NOT NULL,
  `imagen` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `telefono`, `documento`, `correo`, `usuario`, `contraseña`, `estado`, `idRol_id`, `imagen`) VALUES
(1, 'ADMINISTRADOR', '1234', '5678', 'admin@gmail.com', 'Admin muy serio', 'pbkdf2_sha256$720000$6Ss3QHdg69DbXGaFcM7VwZ$A6OVIj5bW3zYIHcNv3aRv7pvBPNwqJdrN7cOxUzDV/0=', 'A', 1, 'user_images/iconosesion.jpg'),
(2, 'Nombre Prueba', '1234123412', '1254235132', 'cliente@gmail.com', 'Cliente Usuario', 'pbkdf2_sha256$720000$6Ss3QHdg69DbXGaFcM7VwZ$A6OVIj5bW3zYIHcNv3aRv7pvBPNwqJdrN7cOxUzDV/0=', 'A', 2, 'user_images/iconosesion.jpg'),
(3, 'Danilo Vergara Lopez', '3177099118', '1025884970', 'danilovergara257@gmail.com', 'Dancraft', 'pbkdf2_sha256$720000$Zb8dKoUJWg74VSt7JmGNZw$7lWonzHtMmXRNECJykpGZtKTj9STpNZKPU7pLN6F448=', 'A', 4, 'user_images/iconosesion.jpg'),
(4, 'Nelson Valencia Álzate', '3146060549', '1000898565', 'valenciaalzatenelsondavid@gmail.com', 'MurciaFeroz<3', 'pbkdf2_sha256$720000$lWBEdbkgEXpGKXYszZPoMb$uId0QrK7rsRRyjrzu0HQrwZ5UOE5aO7P9ztlZIb/bdg=', 'A', 2, 'user_images/iconosesion.jpg'),
(5, 'Emmanuel Sanchez Herrera', '3203097136', '1033487380', 'sanchez252901@gmail.com', 'ikaed', 'pbkdf2_sha256$720000$6IcaA4RSeFsVfCrvmdVmb6$U7Q2Qu4hcQYOBQgTjnbS3YtLHBjKfCD53a8OkOzwPeA=', 'A', 2, 'user_images/iconosesion.jpg'),
(6, 'Jhon Michael Contreras', '3213309428', '1091163415', 'jhomai7020@gmail.com', 'DarkKing516', 'pbkdf2_sha256$720000$3Ttqx0o2jBfBwAZTlfSmxY$K7mUe1sJ2t/BzBuP/9QE0+vYwdOXMJt/Z/9MegRoVcM=', 'A', 4, 'user_images/iconosesion.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas_venta`
--

CREATE TABLE `ventas_venta` (
  `idVenta` int(11) NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `metodo_pago` varchar(50) NOT NULL,
  `subtotal` decimal(10,2) NOT NULL,
  `descuento` decimal(10,2) NOT NULL,
  `iva` decimal(10,2) NOT NULL,
  `total` decimal(10,2) NOT NULL,
  `idPedido_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ventas_venta`
--

INSERT INTO `ventas_venta` (`idVenta`, `fecha`, `metodo_pago`, `subtotal`, `descuento`, `iva`, `total`, `idPedido_id`) VALUES
(13, '2024-06-21 21:52:03.301319', 'efectivo', 30000.00, 5700.00, 5700.00, 30000.00, 9),
(14, '2024-07-10 22:03:56.928559', 'nequi', 60000.00, 400.00, 11400.00, 71000.00, 11);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `detalle_pedido_productos`
--
ALTER TABLE `detalle_pedido_productos`
  ADD PRIMARY KEY (`idDetalle_Pedido_Productos`),
  ADD KEY `detalle_pedido_produ_idProducto_id_70926325_fk_productos` (`idProducto_id`),
  ADD KEY `detalle_pedido_produ_idPedido_id_1c6b705c_fk_pedidos_i` (`idPedido_id`);

--
-- Indices de la tabla `detalle_pedido_servicios`
--
ALTER TABLE `detalle_pedido_servicios`
  ADD PRIMARY KEY (`idDetalle_Pedido_Servicio`),
  ADD KEY `detalle_pedido_servi_idPedido_id_2444ae22_fk_pedidos_i` (`idPedido_id`),
  ADD KEY `detalle_pedido_servi_idServicio_id_d2c5e8af_fk_servicios` (`idServicio_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  ADD PRIMARY KEY (`idPedido`),
  ADD KEY `pedidos_id_Usuario_id_40ef4da9_fk_usuarios_usuario_id` (`id_Usuario_id`);

--
-- Indices de la tabla `permisos`
--
ALTER TABLE `permisos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`idProducto`),
  ADD KEY `productos_id_TipoProducto_id_7cf748bb_fk_tipo_prod` (`id_TipoProducto_id`);

--
-- Indices de la tabla `reservas`
--
ALTER TABLE `reservas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `reservas_reserva_usuario_id_531da18c_fk_usuarios_usuario_id` (`usuario_id`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `roles_permisos`
--
ALTER TABLE `roles_permisos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `roles_permisos_rol_id_permiso_id_daf91080_uniq` (`rol_id`,`permiso_id`),
  ADD KEY `roles_permisos_permiso_id_ff70f233_fk_permisos_id` (`permiso_id`);

--
-- Indices de la tabla `servicios`
--
ALTER TABLE `servicios`
  ADD PRIMARY KEY (`idServicio`),
  ADD KEY `servicios_id_TipoServicio_id_5b2b5147_fk_tipo_serv` (`id_TipoServicio_id`);

--
-- Indices de la tabla `tipo_productos`
--
ALTER TABLE `tipo_productos`
  ADD PRIMARY KEY (`idTipo_Producto`);

--
-- Indices de la tabla `tipo_servicios`
--
ALTER TABLE `tipo_servicios`
  ADD PRIMARY KEY (`idTipo_Servicio`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `usuarios_correo_02971567_uniq` (`correo`),
  ADD KEY `usuarios_idRol_id_9e7b1754_fk_roles_id` (`idRol_id`);

--
-- Indices de la tabla `ventas_venta`
--
ALTER TABLE `ventas_venta`
  ADD PRIMARY KEY (`idVenta`),
  ADD KEY `ventas_venta_idPedido_id_b18bdd00_fk_pedidos_idPedido` (`idPedido_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=73;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `detalle_pedido_productos`
--
ALTER TABLE `detalle_pedido_productos`
  MODIFY `idDetalle_Pedido_Productos` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `detalle_pedido_servicios`
--
ALTER TABLE `detalle_pedido_servicios`
  MODIFY `idDetalle_Pedido_Servicio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=58;

--
-- AUTO_INCREMENT de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  MODIFY `idPedido` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `permisos`
--
ALTER TABLE `permisos`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=59;

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `idProducto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT de la tabla `reservas`
--
ALTER TABLE `reservas`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `roles_permisos`
--
ALTER TABLE `roles_permisos`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=207;

--
-- AUTO_INCREMENT de la tabla `servicios`
--
ALTER TABLE `servicios`
  MODIFY `idServicio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `tipo_productos`
--
ALTER TABLE `tipo_productos`
  MODIFY `idTipo_Producto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `tipo_servicios`
--
ALTER TABLE `tipo_servicios`
  MODIFY `idTipo_Servicio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `ventas_venta`
--
ALTER TABLE `ventas_venta`
  MODIFY `idVenta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `detalle_pedido_productos`
--
ALTER TABLE `detalle_pedido_productos`
  ADD CONSTRAINT `detalle_pedido_produ_idPedido_id_1c6b705c_fk_pedidos_i` FOREIGN KEY (`idPedido_id`) REFERENCES `pedidos` (`idPedido`),
  ADD CONSTRAINT `detalle_pedido_produ_idProducto_id_70926325_fk_productos` FOREIGN KEY (`idProducto_id`) REFERENCES `productos` (`idProducto`);

--
-- Filtros para la tabla `detalle_pedido_servicios`
--
ALTER TABLE `detalle_pedido_servicios`
  ADD CONSTRAINT `detalle_pedido_servi_idPedido_id_2444ae22_fk_pedidos_i` FOREIGN KEY (`idPedido_id`) REFERENCES `pedidos` (`idPedido`),
  ADD CONSTRAINT `detalle_pedido_servi_idServicio_id_d2c5e8af_fk_servicios` FOREIGN KEY (`idServicio_id`) REFERENCES `servicios` (`idServicio`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `pedidos`
--
ALTER TABLE `pedidos`
  ADD CONSTRAINT `pedidos_id_Usuario_id_40ef4da9_fk_usuarios_usuario_id` FOREIGN KEY (`id_Usuario_id`) REFERENCES `usuarios` (`id`);

--
-- Filtros para la tabla `productos`
--
ALTER TABLE `productos`
  ADD CONSTRAINT `productos_id_TipoProducto_id_7cf748bb_fk_tipo_prod` FOREIGN KEY (`id_TipoProducto_id`) REFERENCES `tipo_productos` (`idTipo_Producto`);

--
-- Filtros para la tabla `reservas`
--
ALTER TABLE `reservas`
  ADD CONSTRAINT `reservas_reserva_usuario_id_531da18c_fk_usuarios_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`);

--
-- Filtros para la tabla `roles_permisos`
--
ALTER TABLE `roles_permisos`
  ADD CONSTRAINT `roles_permisos_permiso_id_ff70f233_fk_permisos_id` FOREIGN KEY (`permiso_id`) REFERENCES `permisos` (`id`),
  ADD CONSTRAINT `roles_permisos_rol_id_5daf3c70_fk_roles_id` FOREIGN KEY (`rol_id`) REFERENCES `roles` (`id`);

--
-- Filtros para la tabla `servicios`
--
ALTER TABLE `servicios`
  ADD CONSTRAINT `servicios_id_TipoServicio_id_5b2b5147_fk_tipo_serv` FOREIGN KEY (`id_TipoServicio_id`) REFERENCES `tipo_servicios` (`idTipo_Servicio`);

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_idRol_id_9e7b1754_fk_roles_id` FOREIGN KEY (`idRol_id`) REFERENCES `roles` (`id`);

--
-- Filtros para la tabla `ventas_venta`
--
ALTER TABLE `ventas_venta`
  ADD CONSTRAINT `ventas_venta_idPedido_id_b18bdd00_fk_pedidos_idPedido` FOREIGN KEY (`idPedido_id`) REFERENCES `pedidos` (`idPedido`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
