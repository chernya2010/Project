from django import template
from django.utils.safestring import mark_safe
from mainapp.models import Smartphone

register = template.Library()

TABLE_HEAD = """
             <table class="table table-sm" style="width: 500px; margin-left: 155px;">
               <tbody>
             """

TABLE_TAIL = """
                 </tbody>
             </table>
             """

TABLE_CONTENT = """
                <tr>
                  <td>{name}</td>
                  <td>{value}</td>
                </tr>
                """

PRODUCT_SPEC = {
    'smartphone': {
        'Диагональ': 'diagonal',
        'Тип дисплея': 'display',
        'Разрешение экрана': 'resolution',
        'Объем батареи': 'accum_volume',
        'Оперативная память': 'ram',
        'Наличие слота для SD карты': 'sd',
        'Макcимальный объем SD карты': 'sd_volume_max',
        'Главная камера': 'main_cam_mp',
        'Фронтальная камера': 'frontal_cam_mp'
    },
    'notebook': {
        'Диагональ': 'diagonal',
        'Тип дисплея': 'display',
        'Частота процессора': 'processor_freq',
        'Оперативная память': 'ram',
        'Видеокарта': 'video',
        'Время работы аккумулятора': 'time_without_charge'
    }
}

# Rendering a table with characteristics
def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content

# Displaying the sd_volume_max field only if the sd checkbox is active
@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    if isinstance(product, Smartphone):
        if not product.sd:
            PRODUCT_SPEC['smartphone'].pop('Макcимальный объем SD карты')
        else:
            PRODUCT_SPEC['smartphone']['Макcимальный объем SD карты'] = 'sd_volume_max'
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)

    pass