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
INSERT INTO roles (id, nombre_rol, estado_rol) VALUES
(0, 'Administrador', 'activo'),
(1, 'Cliente', 'activo'),
(2, 'Moderador', 'activo'),
(3, 'Analista', 'activo'),
(4, 'Soporte Técnico', 'inactivo');