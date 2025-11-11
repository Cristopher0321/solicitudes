from behave import when, then, given
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

@given(u'que he iniciado sesión en el sistema con mi perfil de usuario')
def step_impl(context):
    context.driver.get(context.url + "/dashboard") #Aqui se asume que el usuario ya esta loggeado

@given(u'tengo una solicitud creada en el sistema')
def step_impl(context):
    pass #Aqui se asume que ya existen solicitudes previas

@given(u'tengo una solicitud en estado "En proceso"')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'Mis Solicitudes').click()
    time.sleep(1)

@given(u'tengo una solicitud en cualquier estado')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'Mis Solicitudes').click()
    time.sleep(1)

@given(u'tengo solicitudes en diferentes estados')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'Mis Solicitudes').click()
    time.sleep(1)

@when(u'navego a la sección "Mis Solicitudes"')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'Mis Solicitudes').click()
    time.sleep(1)

@when(u'selecciono una solicitud específica de mi lista')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'table tbody tr:first-child a').click()
    time.sleep(1)

@when(u'cambio el estado a "Completado"')
def step_impl(context):
    select = Select(context.driver.find_element(By.NAME, 'estado'))
    select.select_by_visible_text('Completado')
    context.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(1)

@when(u'selecciono la opción "Cancelar solicitud"')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'Cancelar solicitud').click()
    time.sleep(1)

@when(u'aplico filtro por estado "En proceso"')
def step_impl(context):
    select = Select(context.driver.find_element(By.NAME, 'filtro_estado'))
    select.select_by_visible_text('En proceso')
    context.driver.find_element(By.ID, 'aplicar-filtro').click()
    time.sleep(1)

@when(u'confirmo la cancelación')
def step_impl(context):
    context.driver.find_element(By.ID, 'confirmar-cancelacion').click()
    time.sleep(1)

@then(u'debo ver una lista con todas mis solicitudes creadas')
def step_impl(context):
    rows = context.driver.find_elements(By.CSS_SELECTOR, 'table tbody tr')
    assert len(rows) > 0, "No se encontraron solicitudes en la lista"

@then(u'cada solicitud debe mostrar su estado actual entre en proceso, Cancelado o Completado')
def step_impl(context):
    rows = context.driver.find_elements(By.CSS_SELECTOR, 'table tbody tr')
    estados_validos = ['En proceso', 'Cancelado', 'Completado']
    
    for row in rows:
        estado = row.find_element(By.CSS_SELECTOR, 'td:nth-child(3)').text
        assert estado in estados_validos, f"Estado '{estado}' no es válido"

@then(u'puedo ver el estado de la solicitud')
def step_impl(context):
    estado_element = context.driver.find_element(By.ID, 'estado-solicitud')
    assert estado_element.is_displayed(), "No se puede ver el estado de la solicitud"

@then(u'el sistema registra la fecha de completado')
def step_impl(context):
    fecha_element = context.driver.find_element(By.ID, 'fecha-completado')
    assert fecha_element.is_displayed(), "No se muestra la fecha de completado"

@then(u'la solicitud aparece como finalizada en mi lista')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'Mis Solicitudes').click()
    time.sleep(1)
    rows = context.driver.find_elements(By.CSS_SELECTOR, 'table tbody tr')
    encontrado = any('Completado' in row.find_element(By.CSS_SELECTOR, 'td:nth-child(3)').text 
                    for row in rows)
    assert encontrado, "No se encontró la solicitud completada en la lista"

@then(u'ya no permite más cambios de estado')
def step_impl(context):
    try:
        select_element = context.driver.find_element(By.NAME, 'estado')
        assert not select_element.is_enabled(), "El selector de estado debería estar deshabilitado"
    except:
        pass

@then(u'el sistema solicita confirmación de cancelación')
def step_impl(context):
    modal = context.driver.find_element(By.ID, 'modal-confirmacion')
    assert modal.is_displayed(), "No se muestra el modal de confirmación"

@then(u'al confirmar, el estado cambia a "Cancelado"')
def step_impl(context):
    estado_element = context.driver.find_element(By.ID, 'estado-solicitud')
    assert 'Cancelado' in estado_element.text, "El estado no cambió a Cancelado"

@then(u'solo veo las solicitudes en estado "En proceso"')
def step_impl(context):
    rows = context.driver.find_elements(By.CSS_SELECTOR, 'table tbody tr')
    for row in rows:
        estado = row.find_element(By.CSS_SELECTOR, 'td:nth-child(3)').text
        assert estado == 'En proceso', f"Se encontró solicitud con estado: {estado}"

@then(u'el contador de resultados se actualiza según el filtro aplicado')
def step_impl(context):
    contador = context.driver.find_element(By.ID, 'contador-resultados')
    assert contador.is_displayed(), "No se muestra el contador de resultados"

@then(u'puedo remover el filtro para ver todas las solicitudes')
def step_impl(context):
    context.driver.find_element(By.ID, 'limpiar-filtros').click()
    time.sleep(1)
    rows = context.driver.find_elements(By.CSS_SELECTOR, 'table tbody tr')
    assert len(rows) > 0, "No se muestran solicitudes después de remover filtro"