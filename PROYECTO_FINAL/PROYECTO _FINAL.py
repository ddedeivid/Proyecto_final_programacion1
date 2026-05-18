class Cliente:
    def __init__(self, nombre_empresa, nombre_contacto_principal,
                 correo_del_contacto, telefono, area_empresarial):
        self.nombre_empresa = nombre_empresa
        self.nombre_contacto_principal = nombre_contacto_principal
        self.correo_del_contacto = correo_del_contacto
        self.telefono = telefono
        self.area_empresarial = area_empresarial
 
 
class Usuario:
    def __init__(self, nombres, apellidos, correo, cargo):
        self.nombres = nombres
        self.apellidos = apellidos
        self.correo = correo
        self.cargo = cargo
 
 
class Proyecto:
    def __init__(self, titulo, descripcion, fecha_inicio,
                 fecha_fin, cliente, lider_del_proyecto):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.cliente = cliente                        # Instancia de Cliente
        self.lider_del_proyecto = lider_del_proyecto  # Instancia de Usuario
 
 
class Tarea:
    def __init__(self, titulo, descripcion, usuario_responsable,
                 proyecto, categoria, prioridad, estado,
                 fecha_de_entrega, comentario):
        self.titulo = titulo
        self.descripcion = descripcion
        self.usuario_responsable = usuario_responsable  # Instancia de Usuario
        self.proyecto = proyecto                        # Instancia de Proyecto
        self.categoria = categoria
        self.prioridad = prioridad
        self.estado = estado
        self.fecha_de_entrega = fecha_de_entrega
        self.comentario = comentario
 
 
class SubTarea:
    def __init__(self, titulo, descripcion, usuario_responsable,
                 categoria, prioridad, estado, tarea_principal,
                 fecha_de_entrega, comentario):
        self.titulo = titulo
        self.descripcion = descripcion
        self.usuario_responsable = usuario_responsable  # Instancia de Usuario
        self.categoria = categoria
        self.prioridad = prioridad
        self.estado = estado
        self.tarea_principal = tarea_principal          # Instancia de Tarea
        self.fecha_de_entrega = fecha_de_entrega
        self.comentario = comentario
 
 
class Notificacion:
    def __init__(self, asunto, descripcion, detalle, fecha_y_hora):
        self.asunto = asunto
        self.descripcion = descripcion
        self.detalle = detalle
        self.fecha_y_hora = fecha_y_hora
 
 
class NotificacionCorreo(Notificacion):
    def __init__(self, asunto, descripcion, detalle, fecha_y_hora, direccion_correo):
        super().__init__(asunto, descripcion, detalle, fecha_y_hora)
        self.direccion_correo = direccion_correo
 
 
class NotificacionSMS(Notificacion):
    def __init__(self, asunto, descripcion, detalle, fecha_y_hora, numero_de_celular):
        super().__init__(asunto, descripcion, detalle, fecha_y_hora)
        self.numero_de_celular = numero_de_celular
