-- Insertar 20 permisos de ejemplo
INSERT INTO permisos (nombre_permiso, estado_permiso) VALUES
('Listar Usuarios', 'activo'),
('Crear Usuarios', 'activo'),
('Editar Usuarios', 'activo'),
('Editar Perfil', 'activo'),
('Eliminar Usuarios', 'activo'),
('Listar Roles', 'activo'),
('Crear Roles', 'activo'),
('Editar Roles', 'activo'),
('Eliminar Roles', 'activo'),
('Listar Permisos', 'activo'),
('Crear Permisos', 'activo'),
('Editar Permisos', 'activo'),
('Eliminar Permisos', 'activo'),
('Listar Productos', 'activo'),
('Crear Productos', 'activo'),
('Editar Productos', 'activo'),
('Eliminar Productos', 'activo'),
('Listar Tipo Productos', 'activo'),
('Crear Tipo Productos', 'activo'),
('Editar Tipo Productos', 'activo'),
('Eliminar Tipo Productos', 'activo'),
('Listar Servicios', 'activo'),
('Crear Servicios', 'activo'),
('Editar Servicios', 'activo'),
('Eliminar Servicios', 'activo'),
('Listar Tipo Servicios', 'activo'),
('Crear Tipo Servicios', 'activo'),
('Editar Tipo Servicios', 'activo'),
('Eliminar Tipo Servicios', 'activo'),
('Listar Pedidos', 'activo'),
('Listar Mis Pedidos', 'activo'),
('Crear Pedidos', 'activo'),
('Editar Pedidos', 'activo'),
('Editar Mis Pedidos', 'activo'),
('Eliminar Pedidos', 'activo'),
('Listar Reservas', 'activo'),
('Listar Mis Reservas', 'activo'),
('Crear Reservas', 'activo'),
('Editar Reservas', 'activo'),
('Editar Mis Reservas', 'activo'),
('Eliminar Reservas', 'activo'),
('Listar Ventas', 'activo'),
('Crear Ventas', 'activo'),
('Listar Mis Ventas', 'activo');

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
