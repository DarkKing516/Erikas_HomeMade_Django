START TRANSACTION;

-- Insertar 20 permisos de ejemplo
INSERT INTO permisos (nombre_permiso, estado_permiso) VALUES
('Listar Usuarios', 'activo'),
('Crear Usuarios', 'activo'),
('Editar Usuarios', 'activo'),
('Eliminar Usuarios', 'activo'),
('Listar Reservas', 'activo'),
('Listar Mis Reservas', 'activo'),
('Crear Reservas', 'activo'),
('Editar Reservas', 'activo'),
('Eliminar Reservas', 'activo');

-- Insertar roles
INSERT INTO roles (nombre_rol, estado_rol) VALUES
('Admin', 'A'),
('Cliente', 'A'),
('Moderador', 'I'),
('Analista', 'I'),
('Soporte Técnico', 'I');

-- Insertar permisos por rol
INSERT INTO roles_permisos (rol_id, permiso_id) 
SELECT r.id AS rol_id, p.id AS permiso_id 
FROM roles r 
CROSS JOIN permisos p 
WHERE r.nombre_rol = 'Admin'
AND NOT EXISTS (
    SELECT 1 FROM roles_permisos rp 
    WHERE rp.rol_id = r.id AND rp.permiso_id = p.id
);


-- Insertar usuarios de ejemplo
INSERT INTO `usuarios` (`nombre`, `telefono`, `documento`, `correo`, `usuario`, `contraseña`, `estado`, `idRol_id`) VALUES
('ADMINISTRADOR', '1234', '5678', 'admin@gmail.com', 'Admin UwU', 'pbkdf2_sha256$720000$6Ss3QHdg69DbXGaFcM7VwZ$A6OVIj5bW3zYIHcNv3aRv7pvBPNwqJdrN7cOxUzDV/0=', 'A', '1'),
('CLIENTE', '1234', '5678', 'cliente@gmail.com', 'Cliente UwU', 'pbkdf2_sha256$720000$6Ss3QHdg69DbXGaFcM7VwZ$A6OVIj5bW3zYIHcNv3aRv7pvBPNwqJdrN7cOxUzDV/0=', 'A', '2');

-- Insertar reservas de ejemplo
INSERT INTO `reservas` (`fecha`, `fecha_cita`, `descripcion`, `estado`, `usuario_id`) VALUES
('2024-05-05 15:36:33.000000', '2024-05-07 15:36:33.000000', 'Prueba 1', 'Completada', '1'),
('2024-05-05 15:36:33.000000', '2024-05-07 15:36:33.000000', 'Prueba 1', 'En Proceso', '2'),
('2024-05-05 15:36:33.000000', '2024-05-07 15:36:33.000000', 'Prueba 1', 'Completada', '1');


-- Insertar tipos de productos de ejemplo
INSERT INTO tipo_productos (nombre_producto, estado_producto) VALUES
('Electrónica', 'activo'),
('Ropa', 'activo'),
('Alimentos', 'activo'),
('Hogar', 'inactivo');

-- Insertar productos de ejemplo
INSERT INTO productos (nombre, descripcion, imagen, precio, estado_producto, estado_catalogo, cantidad, id_TipoProducto_id) VALUES
('Teléfono móvil', 'Teléfono móvil de última generación', 'telefono.jpg', 699.99, 'activo', 'disponible', 50, 1),
('Camiseta', 'Camiseta de algodón de color blanco', 'camiseta.jpg', 19.99, 'activo', 'disponible', 100, 2),
('Arroz', 'Arroz blanco de grano largo', 'arroz.jpg', 2.99, 'activo', 'disponible', 200, 3),
('Lámpara', 'Lámpara de mesa con pantalla de tela', 'lampara.jpg', 39.99, 'activo', 'disponible', 30, 4);

-- Pedidos
INSERT INTO pedidos (fechaCreacion_pedido, fecha_pedido, descripcion_pedido, subtotal, iva, total, evidencia_pago, estado_pedido, id_Usuario_id) VALUES
('2024-04-23 08:00:00', '2024-04-25', 'Pedido para Juan Perez', 1459.95, 0, 1459.95, 'comprobante_pago.jpg', 'pendiente', 1),
('2024-04-24 09:00:00', '2024-04-26', 'Pedido para María Lopez', 62.96, 0, 62.96, 'comprobante_pago2.jpg', 'pagado', 2);


-- Para la tabla detalle_pedido_productos:

INSERT INTO detalle_pedido_productos (cant_productos, nombre_productos, descripcion, precio_inicial_producto, subtotal_productos, idProducto_id, idPedido_id) VALUES
(2, 'Teléfono móvil', 'Teléfono móvil de última generación', 699.99, 1399.98, 1, 1),
(3, 'Camiseta', 'Camiseta de algodón de color blanco', 19.99, 59.97, 2, 1),
(1, 'Arroz', 'Arroz blanco de grano largo', 2.99, 2.99, 3, 2),
(2, 'Lámpara', 'Lámpara de mesa con pantalla de tela', 39.99, 79.98, 4, 2);

COMMIT;
