from django.urls import path
from myapp import views

urlpatterns = [

    path('login/', views.Login),
    path('login_post/', views.login_post),
    path('logout/', views.logout),


    # --------------------------------Admin-------------------

    path('adminhome/',views.adminhome),

    path('changepassword/',views.changepassword),
    path('changepassword_post/', views.changepassword_post),

    path('viewapproveddoctor/',views.viewapproveddoctor),
    path('viewapproveddoctor_post/', views.viewapproveddoctor_post),

    path('viewdoctors/',views.viewdoctors),
    path('dctr_approve/<id>',views.dctr_approve),
    path('dctr_reject/<id>',views.dctr_reject),

    path('viewdoctor_post/', views.viewdoctor_post),

    path('viewrejecteddoctors/',views.viewrejecteddoctor),
    path('viewrejecteddoctor_post/', views.viewrejecteddoctor_post),

    path('viewreviews/',views.viewreviews),
    path('viewreviews_post/', views.viewreviews_post),

    path('viewusers/',views.viewusers),
    path('viewuser_post/', views.viewuser_post),

    #-------------------------------doctor------------------------

    path('doctorhome/',views.doctorhome),

    path('signup/', views.dr_signup),
    path('dr_signup_post/', views.dr_signup_post),

    path('addprescription/<id>',views.dr_addprescription),
    path('dr_addprescription_post/', views.dr_addprescription_post),

    path('addschedule/', views.dr_addschedule),
    path('addschedule_post/', views.addschedule_post),

    path('dr_changepassword/', views.dr_changepassword),
    path('dr_changepassword_post/', views.dr_changepassword_post),

    path('dr_editprofile/', views.dr_editprofile),
    path('dr_editprofile_post/', views.dr_editprofile_post),

    path('editschedule/<id>', views.dr_editschedule),
    path('dr_editschedule_post/', views.dr_editschedule_post),

    path('viewappointment/', views.dr_viewappoinment),
    path('dr_viewappoinment_post/', views.dr_viewappoinment_post),

    path('druploadimage/', views.druploadimage),
    path('druploadimage_post/', views.druploadimage_post),

    path('dr_viewprofile/', views.dr_viewprofile),
    # path('dr_viewprofile_post/', views.dr_viewprofile_post),

    path('viewschedule/', views.dr_viewschedule),
    path('dr_viewschedule_post/', views.dr_viewschedule_post),

    path('delete_schedule/<id>',views.delete_schedule),

    #---------------------------------user--------------------------

    path('userhome/', views.userhome),

    path('us_changepassword/', views.us_changepassword),
    path('us_changepassword_post/', views.us_changepassword_post),

    path('us_editprofile/', views.us_editprofile),
    path('us_editprofile_post/', views.us_editprofile_post),

    path('Signup/', views.us_signup),
    path('us_signup_post/', views.us_signup_post),

    path('us_viewdoctors/', views.us_viewdoctors),
    path('us_viewdoctors_post/', views.us_viewdoctors_post),

    path('viewhistory/', views.us_viewhistory),
    path('us_viewhistory_post/', views.us_viewhistory_post),

    path('us_viewprofile/', views.us_viewprofile),
    # path('us_viewprofile_post/', views.us_viewprofile_post),

    path('us_viewschedule/<id>', views.us_viewschedule),
    path('us_viewschedule_post/', views.us_viewschedule_post),
    path('makeappointment/<id>', views.makeappointment),
    path('uploadimage/', views.uploadimage),
    path('uploadimage_post/', views.uploadimage_post),

]
