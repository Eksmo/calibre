# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/preferences/look_feel.ui'
#
# Created: Sun Jul  8 22:37:51 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(820, 519)
        self.gridLayout_2 = QtGui.QGridLayout(Form)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_9 = QtGui.QGridLayout(self.tab)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_9.addWidget(self.label_7, 2, 0, 1, 1)
        self.opt_language = QtGui.QComboBox(self.tab)
        self.opt_language.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.opt_language.setMinimumContentsLength(20)
        self.opt_language.setObjectName(_fromUtf8("opt_language"))
        self.gridLayout_9.addWidget(self.opt_language, 2, 1, 1, 1)
        self.opt_systray_icon = QtGui.QCheckBox(self.tab)
        self.opt_systray_icon.setObjectName(_fromUtf8("opt_systray_icon"))
        self.gridLayout_9.addWidget(self.opt_systray_icon, 3, 0, 1, 1)
        self.label_17 = QtGui.QLabel(self.tab)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_9.addWidget(self.label_17, 1, 0, 1, 1)
        self.opt_gui_layout = QtGui.QComboBox(self.tab)
        self.opt_gui_layout.setMaximumSize(QtCore.QSize(250, 16777215))
        self.opt_gui_layout.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.opt_gui_layout.setMinimumContentsLength(20)
        self.opt_gui_layout.setObjectName(_fromUtf8("opt_gui_layout"))
        self.gridLayout_9.addWidget(self.opt_gui_layout, 1, 1, 1, 1)
        self.opt_disable_animations = QtGui.QCheckBox(self.tab)
        self.opt_disable_animations.setObjectName(_fromUtf8("opt_disable_animations"))
        self.gridLayout_9.addWidget(self.opt_disable_animations, 3, 1, 1, 1)
        self.opt_disable_tray_notification = QtGui.QCheckBox(self.tab)
        self.opt_disable_tray_notification.setObjectName(_fromUtf8("opt_disable_tray_notification"))
        self.gridLayout_9.addWidget(self.opt_disable_tray_notification, 4, 0, 1, 1)
        self.opt_show_splash_screen = QtGui.QCheckBox(self.tab)
        self.opt_show_splash_screen.setObjectName(_fromUtf8("opt_show_splash_screen"))
        self.gridLayout_9.addWidget(self.opt_show_splash_screen, 4, 1, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_8 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.opt_toolbar_icon_size = QtGui.QComboBox(self.groupBox_2)
        self.opt_toolbar_icon_size.setObjectName(_fromUtf8("opt_toolbar_icon_size"))
        self.gridLayout_8.addWidget(self.opt_toolbar_icon_size, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_8.addWidget(self.label_5, 0, 0, 1, 1)
        self.opt_toolbar_text = QtGui.QComboBox(self.groupBox_2)
        self.opt_toolbar_text.setObjectName(_fromUtf8("opt_toolbar_text"))
        self.gridLayout_8.addWidget(self.opt_toolbar_text, 1, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_8.addWidget(self.label_8, 1, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_2, 7, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem, 8, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.font_display = QtGui.QLineEdit(self.tab)
        self.font_display.setReadOnly(True)
        self.font_display.setObjectName(_fromUtf8("font_display"))
        self.horizontalLayout.addWidget(self.font_display)
        self.gridLayout_9.addLayout(self.horizontalLayout, 6, 0, 1, 1)
        self.change_font_button = QtGui.QPushButton(self.tab)
        self.change_font_button.setObjectName(_fromUtf8("change_font_button"))
        self.gridLayout_9.addWidget(self.change_font_button, 6, 1, 1, 1)
        self.label_widget_style = QtGui.QLabel(self.tab)
        self.label_widget_style.setObjectName(_fromUtf8("label_widget_style"))
        self.gridLayout_9.addWidget(self.label_widget_style, 0, 0, 1, 1)
        self.opt_ui_style = QtGui.QComboBox(self.tab)
        self.opt_ui_style.setObjectName(_fromUtf8("opt_ui_style"))
        self.gridLayout_9.addWidget(self.opt_ui_style, 0, 1, 1, 1)
        self.opt_book_list_tooltips = QtGui.QCheckBox(self.tab)
        self.opt_book_list_tooltips.setObjectName(_fromUtf8("opt_book_list_tooltips"))
        self.gridLayout_9.addWidget(self.opt_book_list_tooltips, 5, 0, 1, 1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("lt.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.gridLayout_12 = QtGui.QGridLayout(self.tab_4)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.groupBox = QtGui.QGroupBox(self.tab_4)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.field_display_order = QtGui.QListView(self.groupBox)
        self.field_display_order.setAlternatingRowColors(True)
        self.field_display_order.setObjectName(_fromUtf8("field_display_order"))
        self.gridLayout_3.addWidget(self.field_display_order, 0, 0, 3, 1)
        self.df_up_button = QtGui.QToolButton(self.groupBox)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(I("arrow-up.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.df_up_button.setIcon(icon1)
        self.df_up_button.setObjectName(_fromUtf8("df_up_button"))
        self.gridLayout_3.addWidget(self.df_up_button, 0, 1, 1, 1)
        self.df_down_button = QtGui.QToolButton(self.groupBox)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(I("arrow-down.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.df_down_button.setIcon(icon2)
        self.df_down_button.setObjectName(_fromUtf8("df_down_button"))
        self.gridLayout_3.addWidget(self.df_down_button, 2, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 1, 1, 1, 1)
        self.gridLayout_12.addWidget(self.groupBox, 1, 0, 2, 1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.label = QtGui.QLabel(self.tab_4)
        self.label.setObjectName(_fromUtf8("label"))
        self.hboxlayout.addWidget(self.label)
        self.opt_default_author_link = QtGui.QLineEdit(self.tab_4)
        self.opt_default_author_link.setObjectName(_fromUtf8("opt_default_author_link"))
        self.hboxlayout.addWidget(self.opt_default_author_link)
        self.gridLayout_12.addLayout(self.hboxlayout, 0, 0, 1, 1)
        self.opt_use_roman_numerals_for_series_number = QtGui.QCheckBox(self.tab_4)
        self.opt_use_roman_numerals_for_series_number.setChecked(True)
        self.opt_use_roman_numerals_for_series_number.setObjectName(_fromUtf8("opt_use_roman_numerals_for_series_number"))
        self.gridLayout_12.addWidget(self.opt_use_roman_numerals_for_series_number, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.tab_4)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_12.addWidget(self.label_3, 1, 1, 1, 1)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(I("book.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_4, icon3, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_10 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.opt_categories_using_hierarchy = EditWithComplete(self.tab_2)
        self.opt_categories_using_hierarchy.setObjectName(_fromUtf8("opt_categories_using_hierarchy"))
        self.gridLayout_10.addWidget(self.opt_categories_using_hierarchy, 3, 2, 1, 3)
        self.label_9 = QtGui.QLabel(self.tab_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_10.addWidget(self.label_9, 0, 0, 1, 2)
        self.opt_tags_browser_partition_method = QtGui.QComboBox(self.tab_2)
        self.opt_tags_browser_partition_method.setObjectName(_fromUtf8("opt_tags_browser_partition_method"))
        self.gridLayout_10.addWidget(self.opt_tags_browser_partition_method, 0, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.tab_2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_10.addWidget(self.label_10, 0, 3, 1, 1)
        self.opt_tags_browser_collapse_at = QtGui.QSpinBox(self.tab_2)
        self.opt_tags_browser_collapse_at.setMaximum(10000)
        self.opt_tags_browser_collapse_at.setObjectName(_fromUtf8("opt_tags_browser_collapse_at"))
        self.gridLayout_10.addWidget(self.opt_tags_browser_collapse_at, 0, 4, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(690, 252, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem2, 5, 0, 1, 5)
        self.label_8111 = QtGui.QLabel(self.tab_2)
        self.label_8111.setObjectName(_fromUtf8("label_8111"))
        self.gridLayout_10.addWidget(self.label_8111, 1, 2, 1, 1)
        self.opt_tag_browser_dont_collapse = EditWithComplete(self.tab_2)
        self.opt_tag_browser_dont_collapse.setObjectName(_fromUtf8("opt_tag_browser_dont_collapse"))
        self.gridLayout_10.addWidget(self.opt_tag_browser_dont_collapse, 1, 3, 1, 2)
        self.opt_show_avg_rating = QtGui.QCheckBox(self.tab_2)
        self.opt_show_avg_rating.setChecked(True)
        self.opt_show_avg_rating.setObjectName(_fromUtf8("opt_show_avg_rating"))
        self.gridLayout_10.addWidget(self.opt_show_avg_rating, 2, 0, 1, 5)
        self.label_81 = QtGui.QLabel(self.tab_2)
        self.label_81.setObjectName(_fromUtf8("label_81"))
        self.gridLayout_10.addWidget(self.label_81, 3, 0, 1, 1)
        self.opt_tag_browser_old_look = QtGui.QCheckBox(self.tab_2)
        self.opt_tag_browser_old_look.setObjectName(_fromUtf8("opt_tag_browser_old_look"))
        self.gridLayout_10.addWidget(self.opt_tag_browser_old_look, 4, 0, 1, 5)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(I("tags.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon4, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_11 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.opt_separate_cover_flow = QtGui.QCheckBox(self.tab_3)
        self.opt_separate_cover_flow.setObjectName(_fromUtf8("opt_separate_cover_flow"))
        self.gridLayout_11.addWidget(self.opt_separate_cover_flow, 0, 0, 1, 2)
        self.label_6 = QtGui.QLabel(self.tab_3)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_11.addWidget(self.label_6, 1, 0, 1, 1)
        self.opt_cover_flow_queue_length = QtGui.QSpinBox(self.tab_3)
        self.opt_cover_flow_queue_length.setObjectName(_fromUtf8("opt_cover_flow_queue_length"))
        self.gridLayout_11.addWidget(self.opt_cover_flow_queue_length, 1, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(690, 283, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem3, 4, 0, 1, 2)
        self.opt_cb_fullscreen = QtGui.QCheckBox(self.tab_3)
        self.opt_cb_fullscreen.setObjectName(_fromUtf8("opt_cb_fullscreen"))
        self.gridLayout_11.addWidget(self.opt_cb_fullscreen, 2, 0, 1, 2)
        self.fs_help_msg = QtGui.QLabel(self.tab_3)
        self.fs_help_msg.setStyleSheet(_fromUtf8("margin-left: 1.5em"))
        self.fs_help_msg.setWordWrap(True)
        self.fs_help_msg.setObjectName(_fromUtf8("fs_help_msg"))
        self.gridLayout_11.addWidget(self.fs_help_msg, 3, 0, 1, 2)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(I("cover_flow.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon5, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.label_7.setBuddy(self.opt_language)
        self.label_17.setBuddy(self.opt_gui_layout)
        self.label_5.setBuddy(self.opt_toolbar_icon_size)
        self.label_8.setBuddy(self.opt_toolbar_text)
        self.label_2.setBuddy(self.font_display)
        self.label_widget_style.setBuddy(self.opt_ui_style)
        self.label.setBuddy(self.opt_default_author_link)
        self.label_9.setBuddy(self.opt_tags_browser_partition_method)
        self.label_10.setBuddy(self.opt_tags_browser_collapse_at)
        self.label_8111.setBuddy(self.opt_tag_browser_dont_collapse)
        self.label_81.setBuddy(self.opt_categories_using_hierarchy)
        self.label_6.setBuddy(self.opt_cover_flow_queue_length)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.label_7.setText(_("Choose &language (requires restart):"))
        self.opt_systray_icon.setText(_("Enable system &tray icon (needs restart)"))
        self.label_17.setText(_("User Interface &layout (needs restart):"))
        self.opt_disable_animations.setToolTip(_("Disable all animations. Useful if you have a slow/old computer."))
        self.opt_disable_animations.setText(_("Disable &animations"))
        self.opt_disable_tray_notification.setText(_("Disable &notifications in system tray"))
        self.opt_show_splash_screen.setText(_("Show &splash screen at startup"))
        self.groupBox_2.setTitle(_("&Toolbar"))
        self.label_5.setText(_("&Icon size:"))
        self.label_8.setText(_("Show &text under icons:"))
        self.label_2.setText(_("Interface font:"))
        self.change_font_button.setText(_("Change &font (needs restart)"))
        self.label_widget_style.setText(_("User interface &style (needs restart):"))
        self.opt_book_list_tooltips.setText(_("Show &tooltips in the book list"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _("Main Interface"))
        self.groupBox.setTitle(_("Select displayed metadata"))
        self.df_up_button.setToolTip(_("Move up"))
        self.df_down_button.setToolTip(_("Move down"))
        self.label.setText(_("Default author link template:"))
        self.opt_default_author_link.setToolTip(_("<p>Enter a template to be used to create a link for\n"
"an author in the books information dialog. This template will\n"
"be used when no link has been provided for the author using\n"
"Manage Authors. You can use the values {author} and\n"
"{author_sort}, and any template function."))
        self.opt_use_roman_numerals_for_series_number.setText(_("Use &Roman numerals for series"))
        self.label_3.setText(_("Note that <b>comments</b> will always be displayed at the end, regardless of the position you assign here."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _("Book Details"))
        self.opt_categories_using_hierarchy.setToolTip(_("A comma-separated list of categories in which items containing\n"
"periods are displayed in the tag browser trees. For example, if\n"
"this box contains \'tags\' then tags of the form \'Mystery.English\'\n"
"and \'Mystery.Thriller\' will be displayed with English and Thriller\n"
"both under \'Mystery\'. If \'tags\' is not in this box,\n"
"then the tags will be displayed each on their own line."))
        self.label_9.setText(_("Tags browser category &partitioning method:"))
        self.opt_tags_browser_partition_method.setToolTip(_("Choose how tag browser subcategories are displayed when\n"
"there are more items than the limit. Select by first\n"
"letter to see an A, B, C list. Choose partitioned to\n"
"have a list of fixed-sized groups. Set to disabled\n"
"if you never want subcategories"))
        self.label_10.setText(_("&Collapse when more items than:"))
        self.opt_tags_browser_collapse_at.setToolTip(_("If a Tag Browser category has more than this number of items, it is divided\n"
"up into subcategories. If the partition method is set to disable, this value is ignored."))
        self.label_8111.setText(_("Categories not to partition:"))
        self.opt_tag_browser_dont_collapse.setToolTip(_("A comma-separated list of categories that are not to\n"
"be partitioned even if the number of items is larger than\n"
"the value shown above. This option can be used to\n"
"avoid collapsing hierarchical categories that have only\n"
"a few top-level elements."))
        self.opt_show_avg_rating.setText(_("Show &average ratings in the tags browser"))
        self.label_81.setText(_("Categories with &hierarchical items:"))
        self.opt_tag_browser_old_look.setText(_("Use &alternating row colors in the Tag Browser"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _("Tag Browser"))
        self.opt_separate_cover_flow.setText(_("Show cover &browser in a separate window (needs restart)"))
        self.label_6.setText(_("&Number of covers to show in browse mode (needs restart):"))
        self.opt_cb_fullscreen.setText(_("When showing cover browser in separate window, show it &fullscreen"))
        self.fs_help_msg.setText(_("You can press the %s keys to toggle full screen mode."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _("Cover Browser"))

from calibre.gui2.complete2 import EditWithComplete
