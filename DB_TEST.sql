-- Insertar 20 permisos de ejemplo
INSERT INTO permisos (nombre_permiso, estado_permiso) VALUES
('Listar Usuarios', 'A'),
('Crear Usuarios', 'A'),
('Editar Usuarios', 'A'),
('Editar Rol Usuarios', 'A'),
('Editar Estado Usuarios', 'A'),
('Editar Perfil', 'A'),
('Eliminar Usuarios', 'A'),
('Listar Roles', 'A'),
('Crear Roles', 'A'),
('Editar Roles', 'A'),
('Editar Estado Roles', 'A'),
('Eliminar Roles', 'A'),
('Listar Permisos', 'A'),
-- ('Crear Permisos', 'A'),
('Editar Permisos', 'A'),
('Editar Estado Permisos', 'A'),
-- ('Eliminar Permisos', 'A'),
('Listar Productos', 'A'),
('Crear Productos', 'A'),
('Editar Productos', 'A'),
('Eliminar Productos', 'A'),
('Listar Tipo Productos', 'A'),
('Crear Tipo Productos', 'A'),
('Editar Tipo Productos', 'A'),
('Eliminar Tipo Productos', 'A'),
('Listar Servicios', 'A'),
('Crear Servicios', 'A'),
('Editar Servicios', 'A'),
('Eliminar Servicios', 'A'),
('Listar Tipo Servicios', 'A'),
('Crear Tipo Servicios', 'A'),
('Editar Tipo Servicios', 'A'),
('Eliminar Tipo Servicios', 'A'),
('Listar Pedidos', 'A'),
('Listar Mis Pedidos', 'A'),
('Crear Pedidos', 'A'),
('Editar Pedidos', 'A'),
('Editar Mis Pedidos', 'A'),
('Eliminar Pedidos', 'A'),
('Listar Reservas', 'A'),
('Listar Mis Reservas', 'A'),
('Crear Reservas', 'A'),
('Editar Reservas', 'A'),
('Editar Mis Reservas', 'A'),
('Eliminar Reservas', 'A'),
('Listar Ventas', 'A'),
('Crear Ventas', 'A'),
('Listar Mis Ventas', 'A');

-- Insertar roles
INSERT INTO roles (nombre_rol, estado_rol) VALUES
('Admin', 'A'),
('Cliente', 'A'),
('Moderador', 'I'),
('Analista', 'I'),
('Soporte Técnico', 'I');

-- Insertar permisos para el rol Admin
INSERT INTO roles_permisos (rol_id, permiso_id) 
SELECT r.id AS rol_id, p.id AS permiso_id 
FROM roles r 
CROSS JOIN permisos p 
WHERE r.nombre_rol = 'Admin'
AND NOT EXISTS (
    SELECT 1 FROM roles_permisos rp 
    WHERE rp.rol_id = r.id AND rp.permiso_id = p.id
);
-- Insertar permisos por rol para el rol de Cliente
INSERT INTO roles_permisos (rol_id, permiso_id) 
SELECT r.id AS rol_id, p.id AS permiso_id 
FROM roles r 
CROSS JOIN permisos p 
WHERE r.nombre_rol = 'Cliente'
AND (
    p.nombre_permiso LIKE '%Mis%' 
    OR p.nombre_permiso = 'Editar Perfil'
)
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
