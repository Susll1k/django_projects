from django import template

register = template.Library()

@register.filter
def custom_add(value,text):           
    return value + ' ' + text


@register.filter
def back_title(value):

    symbols = []

    for symbol in value:
        symbols += symbol

    result=''  
    for i in symbols:
        if i == symbols[-1]:
            i=i.upper()
        else:
            i=i.lower()
        result += i
    return result

 
 
@register.inclusion_tag('tags/ulist.html') 
def add_hello(*args): 
    return {'items': args}