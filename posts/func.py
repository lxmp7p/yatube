from .models import Group

def get_group_list(title=None):
    if title:
        titleList = []
        title = Group.objects.all()
        for i in title:
            titleList.append(i.title)
        return(titleList)

def get_id_group_on_slug(slug):
    idGroup = Group.objects.filter(slug=slug)[:1]
    return (idGroup[0].id)

def get_name_gropu_on_slug(slug):
    idGroup = get_id_group_on_slug(slug)
    groupName = idGroup[0].title
    return (groupName)
