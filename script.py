# coding: utf-8
#
import uiautomator2 as u2
import time

d = u2.connect()

#+
d(resourceId="com.ichi2.anki.debug:id/fab_main").click()
#create
d(resourceId="com.ichi2.anki.debug:id/add_deck_action").click()
#a
d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_1_0"]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.TextView[1]').click()
#确定
d(resourceId="com.ichi2.anki.debug:id/md_button_positive").click()
#+
d(resourceId="com.ichi2.anki.debug:id/fab_main").click()
#create
d(resourceId="com.ichi2.anki.debug:id/add_deck_action").click()
#b
d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_2_5"]/android.widget.TextView[1]').click()
#确定
d(resourceId="com.ichi2.anki.debug:id/md_button_positive").click()
#+
d(resourceId="com.ichi2.anki.debug:id/fab_main").click()
#create
d(resourceId="com.ichi2.anki.debug:id/add_deck_action").click()
#c
d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_2_3"]/android.widget.TextView[1]').click()
#确定
d(resourceId="com.ichi2.anki.debug:id/md_button_positive").click()

#+
d(resourceId="com.ichi2.anki.debug:id/fab_main").click()
#+card
d(resourceId="com.ichi2.anki.debug:id/fab_main").click()

#切换deck
d(resourceId="com.ichi2.anki.debug:id/id_note_editText", description="Front").click()
#选择deck-a
d(resourceId="com.ichi2.anki.debug:id/deck_picker_dialog_list_item_value", text="a").click()
#切换deck后点击front输入框
d(resourceId="android:id/text1", text="Default").click()
#A
d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_1_0"]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.TextView[1]').click()
#create_card按钮
d(resourceId="com.ichi2.anki.debug:id/action_save").click()
#B
d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_2_5"]/android.widget.TextView[1]').click()
#create_card按钮
d(resourceId="com.ichi2.anki.debug:id/action_save").click()
#C
d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_2_3"]/android.widget.TextView[1]').click()
#create_card按钮
d(resourceId="com.ichi2.anki.debug:id/action_save").click()
#切换deck
d(resourceId="com.ichi2.anki.debug:id/id_note_editText", description="Front").click()
#选择deck-b
d(resourceId="com.ichi2.anki.debug:id/deck_picker_dialog_list_item_value", text="b").click()
#切换deck后点击front输入框
d(resourceId="android:id/text1", text="Default").click()
#D
d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_1_2"]/android.widget.TextView[1]').click()
#create_card按钮
d(resourceId="com.ichi2.anki.debug:id/action_save").click()
#切换deck
d(resourceId="com.ichi2.anki.debug:id/id_note_editText", description="Front").click()
#选择deck-c
d(resourceId="com.ichi2.anki.debug:id/deck_picker_dialog_list_item_value", text="c").click()
#切换deck后点击front输入框
d(resourceId="android:id/text1", text="Default").click()
#E
d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_0_2"]/android.widget.TextView[1]').click()
#create_card按钮
d(resourceId="com.ichi2.anki.debug:id/action_save").click()
#F
d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_1_3"]/android.widget.TextView[1]').click()
#create_card按钮
d(resourceId="com.ichi2.anki.debug:id/action_save").click()
#返回
d(description="Navigate up").click()

#deck-a统计信息
d.xpath('//*[@resource-id="com.ichi2.anki.debug:id/files"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[2]').click()
time.sleep(2)
#返回
d(description="Navigate up").click()
#deck-b统计信息
d.xpath('//*[@resource-id="com.ichi2.anki.debug:id/files"]/android.widget.RelativeLayout[2]/android.widget.LinearLayout[2]').click()
time.sleep(2)
#返回
d(description="Navigate up").click()
#deck-c统计信息
d.xpath('//*[@resource-id="com.ichi2.anki.debug:id/files"]/android.widget.RelativeLayout[3]/android.widget.LinearLayout[2]').click()
time.sleep(2)