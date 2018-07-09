# -*- coding: utf-8 -*-
# ----------------------------------
# Project : default
# Name    : browser
# Author  : 
# Version : 0.0.1
# Updata  : 2018/07/09 04:35:43
# ----------------------------------
    
gl  = r'G:/dev/git/skeleton_manager'
ver = '0.0.1'

class browserUI(object):
    def __init__(self):
        self.windowManageName = 'browserWindow'
        self.windowTitle      = 'browser'
        self.windowSize       = [200, 600]

    def checkWindowOverlap(self):
        if pm.window(self.windowManageName, ex=True):
            pm.deleteUI(self.windowManageName)


    def main(self):
        self.checkWindowOverlap()
        window = pm.window(self.windowManageName,
                           t  = self.windowTitle,
                           w  = self.windowSize[0],
                           h  = self.windowSize[1],
                           mb = True)
        # -- menu
        pm.menu(l='Help', hm=True )
        pm.menuItem(l='Maya 2016 HELP',
                    c='mc.showHelp("http://help.autodesk.com/view/MAYAUL/2016/JPN/", a=True)')

        # -- base form layout
        self.fmL00 = pm.formLayout(nd=100)
        with self.fmL00:
            self.sep00 = pm.separator()
            self.itb00 = pm.iconTextButton(st = 'iconOnly', 
                                           i1 = '{0}/img/browser/logo.png'.format(gl),
                                           l  = '')

            # -- tabLayout
            self.tbL10 = pm.tabLayout(imw=0, imh=0)
            with self.tbL10:
                # -- tabLayout - A
                self.fmL20 = pm.formLayout(nd=100)
                with self.fmL20:
                    self.scf20 = pm.scrollField(ed=True, ww=True)

                # -- tabLayout - B
                self.fmL21 = pm.formLayout(nd=100)
                with self.fmL21:
                    self.scf21 = pm.scrollField(ed=True, ww=True)

                # -- tabLayout - C
                self.fmL22 = pm.formLayout(nd=100)
                with self.fmL22:
                    self.scf22 = pm.scrollField(ed=True, ww=True)



        # -- Edit UI Layout
        pm.formLayout(self.fmL00, e=True,
               af = [(self.sep00, 'top',  0), (self.sep00, 'left', 0), (self.sep00, 'right', 0), 
                     (self.itb00, 'top',  5), (self.itb00, 'left', 3), 
                     (self.tbL10, 'top', 40), (self.tbL10, 'left', 0), (self.tbL10, 'right', 0), (self.tbL10, 'bottom', 0)
                    ])
        # -- tabLayout - A
        pm.formLayout(self.fmL20, e=True,
               af = [(self.scf20, 'top',  0), (self.scf20, 'left', 0), (self.scf20, 'right',  0), (self.scf20, 'bottom', 0)
                    ])
        # -- tabLayout - B
        pm.formLayout(self.fmL21, e=True,
               af = [(self.scf21, 'top', 40), (self.scf21, 'left', 6), (self.scf21, 'right',  6), (self.scf21, 'bottom', 5)
                    ])
        # -- tabLayout - C
        pm.formLayout(self.fmL22, e=True,
               af = [(self.scf22, 'top', 40), (self.scf22, 'left', 6), (self.scf22, 'right',  6), (self.scf22, 'bottom', 5)
                    ])
        pm.tabLayout(self.tbL10, tl=[(self.fmL20, 'creater'), 
                                    (self.fmL21, 'browser'),
                                    (self.fmL22, 'editor')], e=True)


        # -- dock control
        self.dock = pm.dockControl(aa  = ('left', 'right'), 
                                   a   = 'left', 
                                   fl  = False, 
                                   con = window,
                                   l   = 'skeleton manager {0}'.format(ver), 
                                   w   = 200)
        window.show()


def showUI():
    testIns = browserUI()
    testIns.main()


showUI()




#pm.deleteUI('browserWindow', wnd=True)












