from django.urls import path

from cunstruction import views

urlpatterns=[
    path('',views.main,name='main'),
    path('usr_registration', views.usr_registration, name='usr_registration'),
    path('userReg', views.userReg, name='userReg'),
    path('cntrct_registration', views.cntrct_registration, name='cntrct_registration'),
    path('cntrctorRegistration', views.cntrctorRegistration, name='cntrctorRegistration'),
    path('log',views.log,name='log'),
    path('forgotPass',views.forgotPass,name='forgotPass'),
    path('forgot_password',views.forgot_password,name='forgot_password'),
    path('logout',views.logout,name='logout'),
    #Admin
    path('adminHome', views.adminHome, name='adminHome'),
    path('block_contractors', views.block_contractors, name='block_contractors'),
    path('blockContractor/<int:id>', views.blockContractor, name='blockContractor'),
    path('UnBlockContractor/<int:id>', views.UnBlockContractor, name='UnBlockContractor'),
    path('block_worker', views.block_worker, name='block_worker'),
    path('blockWorker/<int:id>', views.blockWorker, name='blockWorker'),
    path('UnBlockWorker/<int:id>', views.UnBlockWorker, name='UnBlockWorker'),
    path('viewUsrCompSentRep', views.viewUsrCompSentRep, name='viewUsrCompSentRep'),
    path('usrReply/<int:id>', views.usrReply, name='usrReply'),
    path('userCompReply', views.userCompReply, name='userCompReply'),
    path('verifyContractor', views.verifyContractor, name='verifyContractor'),
    path('acceptContractor/<int:id>', views.acceptContractor, name='acceptContractor'),
    path('rejectContractor/<int:id>', views.rejectContractor, name='rejectContractor'),
    path('veiwCustomerRevRat', views.veiwCustomerRevRat, name='veiwCustomerRevRat'),
    path('viewUser', views.viewUser, name='viewUser'),
    path('viewWorkerDetail', views.viewWorkerDetail, name='viewWorkerDetail'),
    path('viewWorkerRevRat', views.viewWorkerRevRat, name='viewWorkerRevRat'),
    path('view_worker_rev_rat', views.view_worker_rev_rat, name='view_worker_rev_rat'),
    path('viewWrkerCompSentRep', views.viewWrkerCompSentRep, name='viewWrkerCompSentRep'),
    path('view_Wrkr_Comp_Sent_rep', views.view_Wrkr_Comp_Sent_rep, name='view_Wrkr_Comp_Sent_rep'),
    path('workerRep/<int:id>', views.workerRep, name='workerRep'),
    path('workerReply', views.workerReply, name='workerReply'),
    path('manageVideo', views.manageVideo, name='manageVideo'),
    path('addVideo', views.addVideo, name='addVideo'),
    path('add_video', views.add_video, name='add_video'),


    #contractor
    path('contractorHome', views.contractorHome, name='contractorHome'),
    path('editContratorProfile', views.editContratorProfile, name='editContratorProfile'),
    path('updateContractorProfile', views.updateContractorProfile, name='updateContractorProfile'),
    path('update_con_prof', views.update_con_prof, name='update_con_prof'),
    path('addWorker', views.addWorker, name='addWorker'),
    path('add_jobs', views.add_jobs, name='add_jobs'),
    path('assignWorkToWorker', views.assignWorkToWorker, name='assignWorkToWorker'),
    path('assign_wrk_worker', views.assign_wrk_worker, name='assign_wrk_worker'),
    path('manageJobs', views.manageJobs, name='manageJobs'),
    path('editJobs/<int:id>', views.editJobs, name='editJobs'),
    path('delJobs/<int:id>', views.delJobs, name='delJobs'),
    path('updateJobs', views.updateJobs, name='updateJobs'),
    path('addjobs', views.addjobs, name='addjobs'),
    path('viewCustomerReqApprvl', views.viewCustomerReqApprvl, name='viewCustomerReqApprvl'),
    path('userReqAccept/<int:id>', views.userReqAccept, name='userReqAccept'),
    path('userReqReject/<int:id>', views.userReqReject, name='userReqReject'),
    path('viewWorker', views.viewWorker, name='viewWorker'),
    path('add_Worker', views.add_Worker, name='add_Worker'),
    path('wrkrExistChk', views.wrkrExistChk, name='wrkrExistChk'),
    path('view_contractor_work', views.view_contractor_work, name='view_contractor_work'),
    path('post_contractor_work', views.post_contractor_work, name='post_contractor_work'),
    path('postWorks', views.postWorks, name='postWorks'),
    path('viewVideo', views.viewVideo, name='viewVideo'),

    #User
    path('userHome', views.userHome, name='userHome'),
    path('editUserProfile', views.editUserProfile, name='editUserProfile'),
    path('updateUserProfile', views.updateUserProfile, name='updateUserProfile'),
    path('update_u_prof', views.update_u_prof, name='update_u_prof'),
    path('addUserComp', views.addUserComp, name='addUserComp'),
    path('sentUserFeedback', views.sentUserFeedback, name='sentUserFeedback'),
    path('sentFeedUser', views.sentFeedUser, name='sentFeedUser'),
    path('sntUsrCompViewReply', views.sntUsrCompViewReply, name='sntUsrCompViewReply'),
    path('add_user_comp', views.add_user_comp, name='add_user_comp'),
    path('srchCntrctrSentWrkReq', views.srchCntrctrSentWrkReq, name='srchCntrctrSentWrkReq'),
    path('viewContractorStatus', views.viewContractorStatus, name='viewContractorStatus'),
    path('srchAndViewCOntractor', views.srchAndViewCOntractor, name='srchAndViewCOntractor'),
    path('sendWorkReqToCon/<int:id>', views.sendWorkReqToCon, name='sendWorkReqToCon'),

    #worker
    path('workerHome', views.workerHome, name='workerHome'),
    path('updateWorkerProfile', views.updateWorkerProfile, name='updateWorkerProfile'),
    path('editWorkerProfile', views.editWorkerProfile, name='editWorkerProfile'),
    path('update_worker_pro', views.update_worker_pro, name='update_worker_pro'),
    path('postComplaint', views.postComplaint, name='postComplaint'),
    path('post_complaint_wrkr', views.post_complaint_wrkr, name='post_complaint_wrkr'),
    path('postCompViewRep', views.postCompViewRep, name='postCompViewRep'),
    path('sendContractorFeedback', views.sendContractorFeedback, name='sendContractorFeedback'),
    path('sendFeedbackCon', views.sendFeedbackCon, name='sendFeedbackCon'),
    path('viewAssignWork', views.viewAssignWork, name='viewAssignWork'),
    path('viewAssignWork', views.viewAssignWork, name='viewAssignWork'),
    path('viewVideoWorker', views.viewVideoWorker, name='viewVideoWorker'),

]