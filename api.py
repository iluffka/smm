import vk
import json

session = vk.Session(access_token='')
vk_api = vk.API(session)
# r = vk_api.users.get(user_ids='screen_name', v=5.95)
# print(r)
print('------------------------------------')
g = vk_api.groups.getCatalogInfo(extended=1, subcategories='1', v=5.95)
print(g['categories'])

catalog = vk_api.groups.getCatalog(category_id=10, subcategories=1, v=5.95)
print(catalog)
