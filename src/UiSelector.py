#!/usr/bin/env python
""" generated source for module UiSelector """
from __future__ import print_function
# 
#  * Copyright (C) 2012 The Android Open Source Project
#  *
#  * Licensed under the Apache License, Version 2.0 (the "License");
#  * you may not use this file except in compliance with the License.
#  * You may obtain a copy of the License at
#  *
#  *      http://www.apache.org/licenses/LICENSE-2.0
#  *
#  * Unless required by applicable law or agreed to in writing, software
#  * distributed under the License is distributed on an "AS IS" BASIS,
#  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  * See the License for the specific language governing permissions and
#  * limitations under the License.
#  
# package: com.llxx.nodefinder
# 
#  * Specifies the elements in the layout hierarchy for tests to target, filtered
#  * by properties such as text value, content-description, class name, and state
#  * information. You can also target an element by its location in a layout
#  * hierarchy.
#  * @since API Level 16
#  
class UiSelector(object):
    """ generated source for class UiSelector """
    SELECTOR_NIL = 0
    SELECTOR_TEXT = 1
    SELECTOR_START_TEXT = 2
    SELECTOR_CONTAINS_TEXT = 3
    SELECTOR_CLASS = 4
    SELECTOR_DESCRIPTION = 5
    SELECTOR_START_DESCRIPTION = 6
    SELECTOR_CONTAINS_DESCRIPTION = 7
    SELECTOR_INDEX = 8
    SELECTOR_INSTANCE = 9
    SELECTOR_ENABLED = 10
    SELECTOR_FOCUSED = 11
    SELECTOR_FOCUSABLE = 12
    SELECTOR_SCROLLABLE = 13
    SELECTOR_CLICKABLE = 14
    SELECTOR_CHECKED = 15
    SELECTOR_SELECTED = 16
    SELECTOR_ID = 17
    SELECTOR_PACKAGE_NAME = 18
    SELECTOR_CHILD = 19
    SELECTOR_CONTAINER = 20
    SELECTOR_PATTERN = 21
    SELECTOR_PARENT = 22
    SELECTOR_COUNT = 23
    SELECTOR_LONG_CLICKABLE = 24
    SELECTOR_TEXT_REGEX = 25
    SELECTOR_CLASS_REGEX = 26
    SELECTOR_DESCRIPTION_REGEX = 27
    SELECTOR_PACKAGE_NAME_REGEX = 28
    SELECTOR_RESOURCE_ID = 29
    SELECTOR_CHECKABLE = 30
    SELECTOR_RESOURCE_ID_REGEX = 31
    mSelectorAttributes = SparseArray()

    # 
    #      * @since API Level 16
    #      
    @overloaded
    def __init__(self):
        """ generated source for method __init__ """

    @__init__.register(object, UiSelector)
    def __init___0(self, selector):
        """ generated source for method __init___0 """
        self.mSelectorAttributes = selector.cloneSelector().mSelectorAttributes

    # 
    #      * @since API Level 17
    #      
    def cloneSelector(self):
        """ generated source for method cloneSelector """
        ret = UiSelector()
        ret.mSelectorAttributes = self.mSelectorAttributes.clone()
        if hasChildSelector():
            ret.mSelectorAttributes.put(self.SELECTOR_CHILD, UiSelector(getChildSelector()))
        if hasParentSelector():
            ret.mSelectorAttributes.put(self.SELECTOR_PARENT, UiSelector(getParentSelector()))
        if hasPatternSelector():
            ret.mSelectorAttributes.put(self.SELECTOR_PATTERN, UiSelector(getPatternSelector()))
        return ret

    @classmethod
    @overloaded
    def patternBuilder(cls, selector):
        """ generated source for method patternBuilder """
        if not selector.hasPatternSelector():
            return UiSelector().patternSelector(selector)
        return selector

    @classmethod
    @patternBuilder.register(object, UiSelector, UiSelector)
    def patternBuilder_0(cls, container, pattern):
        """ generated source for method patternBuilder_0 """
        return UiSelector(UiSelector().containerSelector(container).patternSelector(pattern))

    def text(self, text):
        """ generated source for method text """
        return buildSelector(self.SELECTOR_TEXT, text)

    def textMatches(self, regex):
        """ generated source for method textMatches """
        return buildSelector(self.SELECTOR_TEXT_REGEX, Pattern.compile(regex))

    def textStartsWith(self, text):
        """ generated source for method textStartsWith """
        return buildSelector(self.SELECTOR_START_TEXT, text)

    def textContains(self, text):
        """ generated source for method textContains """
        return buildSelector(self.SELECTOR_CONTAINS_TEXT, text)

    @overloaded
    def className(self, className):
        """ generated source for method className """
        return buildSelector(self.SELECTOR_CLASS, className)

    def classNameMatches(self, regex):
        """ generated source for method classNameMatches """
        return buildSelector(self.SELECTOR_CLASS_REGEX, Pattern.compile(regex))

    @className.register(object, Class)
    def className_0(self, type_):
        """ generated source for method className_0 """
        return buildSelector(self.SELECTOR_CLASS, type_.__name__)

    def description(self, desc):
        """ generated source for method description """
        return buildSelector(self.SELECTOR_DESCRIPTION, desc)

    def descriptionMatches(self, regex):
        """ generated source for method descriptionMatches """
        return buildSelector(self.SELECTOR_DESCRIPTION_REGEX, Pattern.compile(regex))

    def descriptionStartsWith(self, desc):
        """ generated source for method descriptionStartsWith """
        return buildSelector(self.SELECTOR_START_DESCRIPTION, desc)

    def descriptionContains(self, desc):
        """ generated source for method descriptionContains """
        return buildSelector(self.SELECTOR_CONTAINS_DESCRIPTION, desc)

    def resourceId(self, id):
        """ generated source for method resourceId """
        return buildSelector(self.SELECTOR_RESOURCE_ID, id)

    def resourceIdMatches(self, regex):
        """ generated source for method resourceIdMatches """
        return buildSelector(self.SELECTOR_RESOURCE_ID_REGEX, Pattern.compile(regex))

    def index(self, index):
        """ generated source for method index """
        return buildSelector(self.SELECTOR_INDEX, index)

    def instance_(self, instance_):
        """ generated source for method instance_ """
        return buildSelector(self.SELECTOR_INSTANCE, instance_)

    def enabled(self, val):
        """ generated source for method enabled """
        return buildSelector(self.SELECTOR_ENABLED, val)

    def focused(self, val):
        """ generated source for method focused """
        return buildSelector(self.SELECTOR_FOCUSED, val)

    def focusable(self, val):
        """ generated source for method focusable """
        return buildSelector(self.SELECTOR_FOCUSABLE, val)

    def scrollable(self, val):
        """ generated source for method scrollable """
        return buildSelector(self.SELECTOR_SCROLLABLE, val)

    def selected(self, val):
        """ generated source for method selected """
        return buildSelector(self.SELECTOR_SELECTED, val)

    def checked(self, val):
        """ generated source for method checked """
        return buildSelector(self.SELECTOR_CHECKED, val)

    def clickable(self, val):
        """ generated source for method clickable """
        return buildSelector(self.SELECTOR_CLICKABLE, val)

    def checkable(self, val):
        """ generated source for method checkable """
        return buildSelector(self.SELECTOR_CHECKABLE, val)

    def longClickable(self, val):
        """ generated source for method longClickable """
        return buildSelector(self.SELECTOR_LONG_CLICKABLE, val)

    def childSelector(self, selector):
        """ generated source for method childSelector """
        return buildSelector(self.SELECTOR_CHILD, selector)

    def patternSelector(self, selector):
        """ generated source for method patternSelector """
        return buildSelector(self.SELECTOR_PATTERN, selector)

    def containerSelector(self, selector):
        """ generated source for method containerSelector """
        return buildSelector(self.SELECTOR_CONTAINER, selector)

    def fromParent(self, selector):
        """ generated source for method fromParent """
        return buildSelector(self.SELECTOR_PARENT, selector)

    def packageName(self, name):
        """ generated source for method packageName """
        return buildSelector(self.SELECTOR_PACKAGE_NAME, name)

    def packageNameMatches(self, regex):
        """ generated source for method packageNameMatches """
        return buildSelector(self.SELECTOR_PACKAGE_NAME_REGEX, Pattern.compile(regex))

    def buildSelector(self, selectorId, selectorValue):
        """ generated source for method buildSelector """
        selector = UiSelector(self)
        if selectorId == self.SELECTOR_CHILD or selectorId == self.SELECTOR_PARENT:
            selector.getLastSubSelector().mSelectorAttributes.put(selectorId, selectorValue)
        else:
            selector.mSelectorAttributes.put(selectorId, selectorValue)
        return selector

    def getChildSelector(self):
        """ generated source for method getChildSelector """
        selector = self.mSelectorAttributes.get(UiSelector.SELECTOR_CHILD, None)
        if selector != None:
            return UiSelector(selector)
        return None

    def getPatternSelector(self):
        """ generated source for method getPatternSelector """
        selector = self.mSelectorAttributes.get(UiSelector.SELECTOR_PATTERN, None)
        if selector != None:
            return UiSelector(selector)
        return None

    def getContainerSelector(self):
        """ generated source for method getContainerSelector """
        selector = self.mSelectorAttributes.get(UiSelector.SELECTOR_CONTAINER, None)
        if selector != None:
            return UiSelector(selector)
        return None

    def getParentSelector(self):
        """ generated source for method getParentSelector """
        selector = self.mSelectorAttributes.get(UiSelector.SELECTOR_PARENT, None)
        if selector != None:
            return UiSelector(selector)
        return None

    def getInstance(self):
        """ generated source for method getInstance """
        return getInt(UiSelector.SELECTOR_INSTANCE)

    def getString(self, criterion):
        """ generated source for method getString """
        return str(self.mSelectorAttributes.get(criterion, None))

    def getBoolean(self, criterion):
        """ generated source for method getBoolean """
        return bool(self.mSelectorAttributes.get(criterion, False))

    def getInt(self, criterion):
        """ generated source for method getInt """
        return int(self.mSelectorAttributes.get(criterion, 0))

    def getPattern(self, criterion):
        """ generated source for method getPattern """
        return self.mSelectorAttributes.get(criterion, None)

    def isMatchFor(self, node, index):
        """ generated source for method isMatchFor """
        size = len(self.mSelectorAttributes)
        x = 0
        while x < size:
            s = None
            criterion = self.mSelectorAttributes.keyAt(x)
            if criterion == UiSelector.SELECTOR_INDEX:
                if index != self.getInt(criterion):
                    return False
            elif criterion == UiSelector.SELECTOR_CHECKED:
                if node.isChecked() != self.getBoolean(criterion):
                    return False
            elif criterion == UiSelector.SELECTOR_CLASS:
                s = node.getClassName()
                if s == None or not s.__str__().contentEquals(self.getString(criterion)):
                    return False
            elif criterion == UiSelector.SELECTOR_CLASS_REGEX:
                s = node.getClassName()
                if s == None or not self.getPattern(criterion).matcher(s).matches():
                    return False
            elif criterion == UiSelector.SELECTOR_CLICKABLE:
                if node.isClickable() != self.getBoolean(criterion):
                    return False
            elif criterion == UiSelector.SELECTOR_CHECKABLE:
                if node.isCheckable() != self.getBoolean(criterion):
                    return False
            elif criterion == UiSelector.SELECTOR_LONG_CLICKABLE:
                if node.isLongClickable() != self.getBoolean(criterion):
                    return False
            elif criterion == UiSelector.SELECTOR_CONTAINS_DESCRIPTION:
                s = node.getContentDescription()
                if s == None or not s.__str__().lower().contains(self.getString(criterion).toLowerCase()):
                    return False
            elif criterion == UiSelector.SELECTOR_START_DESCRIPTION:
                s = node.getContentDescription()
                if s == None or not s.__str__().lower().startsWith(self.getString(criterion).toLowerCase()):
                    return False
            elif criterion == UiSelector.SELECTOR_DESCRIPTION:
                s = node.getContentDescription()
                if s == None or not s.__str__().contentEquals(self.getString(criterion)):
                    return False
            elif criterion == UiSelector.SELECTOR_DESCRIPTION_REGEX:
                s = node.getContentDescription()
                if s == None or not self.getPattern(criterion).matcher(s).matches():
                    return False
            elif criterion == UiSelector.SELECTOR_CONTAINS_TEXT:
                s = node.getText()
                if s == None or not s.__str__().lower().contains(self.getString(criterion).toLowerCase()):
                    return False
            elif criterion == UiSelector.SELECTOR_START_TEXT:
                s = node.getText()
                if s == None or not s.__str__().lower().startsWith(self.getString(criterion).toLowerCase()):
                    return False
            elif criterion == UiSelector.SELECTOR_TEXT:
                s = node.getText()
                if s == None or not s.__str__().contentEquals(self.getString(criterion)):
                    return False
            elif criterion == UiSelector.SELECTOR_TEXT_REGEX:
                s = node.getText()
                if s == None or not self.getPattern(criterion).matcher(s).matches():
                    return False
            elif criterion == UiSelector.SELECTOR_ENABLED:
                if node.isEnabled() != self.getBoolean(criterion):
                    return False
            elif criterion == UiSelector.SELECTOR_FOCUSABLE:
                if node.isFocusable() != self.getBoolean(criterion):
                    return False
            elif criterion == UiSelector.SELECTOR_FOCUSED:
                if node.isFocused() != self.getBoolean(criterion):
                    return False
            elif criterion == UiSelector.SELECTOR_ID:
            elif criterion == UiSelector.SELECTOR_PACKAGE_NAME:
                s = node.getPackageName()
                if s == None or not s.__str__().contentEquals(self.getString(criterion)):
                    return False
            elif criterion == UiSelector.SELECTOR_PACKAGE_NAME_REGEX:
                s = node.getPackageName()
                if s == None or not self.getPattern(criterion).matcher(s).matches():
                    return False
            elif criterion == UiSelector.SELECTOR_SCROLLABLE:
                if node.isScrollable() != self.getBoolean(criterion):
                    return False
            elif criterion == UiSelector.SELECTOR_SELECTED:
                if node.isSelected() != self.getBoolean(criterion):
                    return False
            elif criterion == UiSelector.SELECTOR_RESOURCE_ID:
                s = node.getViewIdResourceName()
                if s == None or not s.__str__().contentEquals(self.getString(criterion)):
                    return False
            elif criterion == UiSelector.SELECTOR_RESOURCE_ID_REGEX:
                s = node.getViewIdResourceName()
                if s == None or not self.getPattern(criterion).matcher(s).matches():
                    return False
            x += 1
        return matchOrUpdateInstance()

    def matchOrUpdateInstance(self):
        """ generated source for method matchOrUpdateInstance """
        currentSelectorCounter = 0
        currentSelectorInstance = 0
        if self.mSelectorAttributes.indexOfKey(UiSelector.SELECTOR_INSTANCE) >= 0:
            currentSelectorInstance = int(self.mSelectorAttributes.get(UiSelector.SELECTOR_INSTANCE))
        if self.mSelectorAttributes.indexOfKey(UiSelector.SELECTOR_COUNT) >= 0:
            currentSelectorCounter = int(self.mSelectorAttributes.get(UiSelector.SELECTOR_COUNT))
        if currentSelectorInstance == currentSelectorCounter:
            return True
        if currentSelectorInstance > currentSelectorCounter:
        currentSelectorCounter += 1
            self.mSelectorAttributes.put(UiSelector.SELECTOR_COUNT, currentSelectorCounter)
        return False

    def isLeaf(self):
        """ generated source for method isLeaf """
        if self.mSelectorAttributes.indexOfKey(UiSelector.SELECTOR_CHILD) < 0 and self.mSelectorAttributes.indexOfKey(UiSelector.SELECTOR_PARENT) < 0:
            return True
        return False

    def hasChildSelector(self):
        """ generated source for method hasChildSelector """
        if self.mSelectorAttributes.indexOfKey(UiSelector.SELECTOR_CHILD) < 0:
            return False
        return True

    def hasPatternSelector(self):
        """ generated source for method hasPatternSelector """
        if self.mSelectorAttributes.indexOfKey(UiSelector.SELECTOR_PATTERN) < 0:
            return False
        return True

    def hasContainerSelector(self):
        """ generated source for method hasContainerSelector """
        if self.mSelectorAttributes.indexOfKey(UiSelector.SELECTOR_CONTAINER) < 0:
            return False
        return True

    def hasParentSelector(self):
        """ generated source for method hasParentSelector """
        if self.mSelectorAttributes.indexOfKey(UiSelector.SELECTOR_PARENT) < 0:
            return False
        return True

    def getLastSubSelector(self):
        """ generated source for method getLastSubSelector """
        if self.mSelectorAttributes.indexOfKey(UiSelector.SELECTOR_CHILD) >= 0:
            child = self.mSelectorAttributes.get(UiSelector.SELECTOR_CHILD)
            if child.getLastSubSelector() == None:
                return child
            return child.getLastSubSelector()
        elif self.mSelectorAttributes.indexOfKey(UiSelector.SELECTOR_PARENT) >= 0:
            parent = self.mSelectorAttributes.get(UiSelector.SELECTOR_PARENT)
            if parent.getLastSubSelector() == None:
                return parent
            return parent.getLastSubSelector()
        return self

    def __str__(self):
        """ generated source for method toString """
        return dumpToString(True)

    def dumpToString(self, all):
        """ generated source for method dumpToString """
        builder = StringBuilder()
        builder.append(UiSelector.__class__.getSimpleName() + "[")
        criterionCount = len(self.mSelectorAttributes)
        i = 0
        while i < criterionCount:
            if i > 0:
                builder.append(", ")
            criterion = self.mSelectorAttributes.keyAt(i)
            if criterion == self.SELECTOR_TEXT:
                builder.append("TEXT=").append(self.mSelectorAttributes.valueAt(i))
            elif criterion == self.SELECTOR_TEXT_REGEX:
                builder.append("TEXT_REGEX=").append(self.mSelectorAttributes.valueAt(i))
            elif criterion == self.SELECTOR_START_TEXT:
                builder.append("START_TEXT=").append(self.mSelectorAttributes.valueAt(i))
            elif criterion == self.SELECTOR_CONTAINS_TEXT:
                builder.append("CONTAINS_TEXT=").append(self.mSelectorAttributes.valueAt(i))
            elif criterion == self.SELECTOR_CLASS:
                builder.append("CLASS=").append(self.mSelectorAttributes.valueAt(i))
            elif criterion == self.SELECTOR_CLASS_REGEX:
                builder.append("CLASS_REGEX=").append(self.mSelectorAttributes.valueAt(i))
            elif criterion == self.SELECTOR_DESCRIPTION:
                builder.append("DESCRIPTION=").append(self.mSelectorAttributes.valueAt(i))
            elif criterion == self.SELECTOR_DESCRIPTION_REGEX:
                builder.append("DESCRIPTION_REGEX=").append(self.mSelectorAttributes.valueAt(i))
            elif criterion == self.SELECTOR_START_DESCRIPTION:
                builder.append("START_DESCRIPTION=").append(self.mSelectorAttributes.valueAt(i))
            elif criterion == self.SELECTOR_CONTAINS_DESCRIPTION:
                builder.append("CONTAINS_DESCRIPTION=").append(self.mSelectorAttributes.valueAt(i))
            elif criterion == self.SELECTOR_INDEX:
                builder.append("INDEX=").append(self.mSelectorAttributes.valueAt(i))
            elif criterion == self.SELECTOR_INSTANCE:
                builder.append("INSTANCE=").append(self.mSelectorAttributes.valueAt(i))
            elif criterion == self.SELECTOR_ENABLED:
                builder.append("ENABLED=").append(self.mSelectorAttributes.valueAt(i))
            elif criterion == self.SELECTOR_FOCUSED:
                builder.append("FOCUSED=").append(self.mSelectorAttributes.valueAt(i))
            elif criterion == self.SELECTOR_FOCUSABLE:
                builder.append("FOCUSABLE=").append(self.mSelectorAttributes.valueAt(i))
            elif criterion == self.SELECTOR_SCROLLABLE:
                builder.append("SCROLLABLE=").append(self.mSelectorAttributes.valueAt(i))
            elif criterion == self.SELECTOR_CLICKABLE:
                builder.append("CLICKABLE=").append(self.mSelectorAttributes.valueAt(i))
            elif criterion == self.SELECTOR_CHECKABLE:
                builder.append("CHECKABLE=").append(self.mSelectorAttributes.valueAt(i))
            elif criterion == self.SELECTOR_LONG_CLICKABLE:
                builder.append("LONG_CLICKABLE=").append(self.mSelectorAttributes.valueAt(i))
            elif criterion == self.SELECTOR_CHECKED:
                builder.append("CHECKED=").append(self.mSelectorAttributes.valueAt(i))
            elif criterion == self.SELECTOR_SELECTED:
                builder.append("SELECTED=").append(self.mSelectorAttributes.valueAt(i))
            elif criterion == self.SELECTOR_ID:
                builder.append("ID=").append(self.mSelectorAttributes.valueAt(i))
            elif criterion == self.SELECTOR_CHILD:
                if all:
                    builder.append("CHILD=").append(self.mSelectorAttributes.valueAt(i))
                else:
                    builder.append("CHILD[..]")
            elif criterion == self.SELECTOR_PATTERN:
                if all:
                    builder.append("PATTERN=").append(self.mSelectorAttributes.valueAt(i))
                else:
                    builder.append("PATTERN[..]")
            elif criterion == self.SELECTOR_CONTAINER:
                if all:
                    builder.append("CONTAINER=").append(self.mSelectorAttributes.valueAt(i))
                else:
                    builder.append("CONTAINER[..]")
            elif criterion == self.SELECTOR_PARENT:
                if all:
                    builder.append("PARENT=").append(self.mSelectorAttributes.valueAt(i))
                else:
                    builder.append("PARENT[..]")
            elif criterion == self.SELECTOR_COUNT:
                builder.append("COUNT=").append(self.mSelectorAttributes.valueAt(i))
            elif criterion == self.SELECTOR_PACKAGE_NAME:
                builder.append("PACKAGE NAME=").append(self.mSelectorAttributes.valueAt(i))
            elif criterion == self.SELECTOR_PACKAGE_NAME_REGEX:
                builder.append("PACKAGE_NAME_REGEX=").append(self.mSelectorAttributes.valueAt(i))
            elif criterion == self.SELECTOR_RESOURCE_ID:
                builder.append("RESOURCE_ID=").append(self.mSelectorAttributes.valueAt(i))
            elif criterion == self.SELECTOR_RESOURCE_ID_REGEX:
                builder.append("RESOURCE_ID_REGEX=").append(self.mSelectorAttributes.valueAt(i))
            else:
                builder.append("UNDEFINED=" + criterion + " ").append(self.mSelectorAttributes.valueAt(i))
            i += 1
        builder.append("]")
        return builder.__str__()

