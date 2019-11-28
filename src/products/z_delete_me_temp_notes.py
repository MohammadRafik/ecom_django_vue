



# # this class is used to find all catagorys in the database bring them
# # in, and check if a catagory is selected and load things accordingly


#     @classmethod
#     def generate_navigation_code(cls, category,f):
#         string_category = str(category)
#         f.write( '''<dropdown :trigger="'hover'" :align="'right'">''')
#         f.write( '''<template slot="btn"><a href="#" >'''+  string_category + '''</a></template>''' )
#         # f.write( '''<template slot="btn"><a href="#">category</a></template>''' )
#         f.write( '''<template slot="body">''' )
#         if category.sub_categories_list != None:
#             for child in category.sub_categories_list:
#                 cls.generate_navigation_code(child,f)
#         f.write( '</template>' )
#         f.write( '</dropdown>' )

#     def __init__(self, request):
#         # generate code to list all categories
#         self.all_categories = Category.update_sub_category_lists()
#         self.categories = Category.find_main_categories(self.all_categories)
#         path = os.getcwd() + '\src\products\\navigationString.txt'
#         try:
#             f= open(path,"w+")
#         except:
#             path = os.getcwd() + '\products\\navigationString.txt'
#             f= open(path,"w+")
#         if 'category' not in request.session:
#             f.write(''' 
#                         <nav class="col-md-2 d-none d-md-block bg-light sidebar">
#                         <div class="sidebar-sticky">
#                         <h5 class="sidebar-heading d-flex justify-content-between align-items-center px-3 mt-4 mb-1 text-muted">
#                         Navigation
#                         </h5>
#                         <ul class="nav flex-column">
#                     ''')
#             for cat in self.categories:
#                 self.generate_navigation_code(cat, f)
#             f.write(''' 
#                         </ul>
#                         </div>
#                         </nav> 
#                     ''')
#             f.close()
#         else:
#             f.write('''
#                         <nav class="col-md-2 d-none d-md-block bg-light sidebar">
#                         <div class="sidebar-sticky">
#                         <ul class="nav flex-column">
#                         <dropdown :trigger="'hover'" :align="'right'">
#                         <template slot="btn"><a href="#" >Catalog</a></template>
#                         <template slot="body">
#                     ''')
#             for cat in self.categories:
#                 self.generate_navigation_code(cat, f)
#             f.write('''
#                         </ul>
#                         </div>
#                         </nav>
#                         </template>
#                         </dropdown>
#                     ''')
#             f.close()


#         with open(path, 'r') as file:
#             self.massive_string = file.read().replace('\n', '')