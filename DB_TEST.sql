START TRANSACTION;

-- Insertar 20 permisos de ejemplo
INSERT INTO permisos (nombre_permiso, estado_permiso) VALUES
('Crear usuarios', 'activo'),
('Eliminar usuarios', 'activo'),
('Modificar configuración', 'inactivo'),
('Leer correos electrónicos', 'activo'),
('Generar reportes', 'inactivo'),
('Enviar mensajes', 'activo'),
('Eliminar mensajes', 'inactivo'),
('Ver estadísticas', 'activo'),
('Descargar archivos', 'inactivo'),
('Modificar perfiles', 'activo'),
('Crear grupos', 'activo'),
('Eliminar grupos', 'inactivo'),
('Gestionar permisos', 'activo'),
('Actualizar base de datos', 'inactivo'),
('Ejecutar scripts', 'activo'),
('Configurar notificaciones', 'inactivo'),
('Crear tareas', 'activo'),
('Asignar tareas', 'inactivo'),
('Cerrar sesión', 'activo'),
('Ver historial de actividad', 'inactivo');

-- Insertar roles
INSERT INTO roles (nombre_rol, estado_rol) VALUES
('Administrador', 'activo'),
('Cliente', 'activo'),
('Moderador', 'activo'),
('Analista', 'activo'),
('Soporte Técnico', 'inactivo');


-- Insertar usuarios de ejemplo
INSERT INTO usuarios (nombre, telefono, documento, correo, usuario, contraseña, estado, idRol_id) VALUES
('Juan Perez', '123456789', '1234567890', 'juan@example.com', 'juanperez', 'contraseña123', 'activo', 1),
('María Lopez', '987654321', '0987654321', 'maria@example.com', 'marialopez', 'contraseña456', 'activo', 1),
('Carlos García', '456789012', '4567890123', 'carlos@example.com', 'carlosgarcia', 'contraseña789', 'inactivo', 2),
('Ana Martínez', '789012345', '7890123456', 'ana@example.com', 'anamartinez', 'contraseñaabc', 'activo', 3);

-- Insertar reservas de ejemplo
INSERT INTO reservas (fecha, fecha_cita, descripcion, estado, usuario_id) VALUES
('2024-04-23', '2024-04-25 10:00:00', 'Reunión de trabajo', 'pendiente', 1),
('2024-04-24', '2024-04-26 15:00:00', 'Entrevista de empleo', 'confirmada', 2),
('2024-04-25', '2024-04-27 09:30:00', 'Consulta médica', 'pendiente', 3);

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
