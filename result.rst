Test suite results
======================================================

   :generated: resulthtmltorst.py
   :filename: result.html

**Test Results**

.. list-table::

   * -  result
     -  passed
   * -  totalTime
     -  6
   * -  numTestTotal
     -  2
   * -  numTestPasses
     -  2
   * -  numTestFailures
     -  0
   * -  numCommandPasses
     -  2
   * -  numCommandFailures
     -  0
   * -  numCommandErrors
     -  0
   * -  Selenium Version
     -  2.15
   * -  Selenium Revision
     -  .0

TestSuite
-----------------------------------------


TestSuite
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**status_passed**

.. list-table::

   * -  google_search_blender
     -  status_passed
   * -  google_search_sphinx
     -  status_passed



google_search_blender.html
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**status_passed**

.. list-table::

   * -  open
     -  http://google.com
     -  
     -  status_done
   * -  type
     -  q
     -  blender
     -  status_done
   * -  click
     -  xpath=//input[@name='btnK']
     -  
     -  status_done
   * -  pause
     -  2000
     -  
     -  status_done
   * -  verifyTextPresent
     -  blender
     -  
     -  status_passed


google_search_sphinx.html
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**status_passed**

.. list-table::

   * -  open
     -  http://google.com
     -  
     -  status_done
   * -  type
     -  q
     -  sphinx
     -  status_done
   * -  click
     -  xpath=//input[@name='btnK']
     -  
     -  status_done
   * -  pause
     -  2000
     -  
     -  status_done
   * -  verifyTextPresent
     -  sphinx
     -  
     -  status_passed

Info
----

::

   
   info: Starting test /selenium-server/tests/google_search_blender.html
   info: Executing: |open | http://google.com |  |
   info: Executing: |type | q | blender |
   info: Executing: |click | xpath=//input[@name=&apos;btnK&apos;] |  |
   info: Executing: |pause | 2000 |  |
   info: Executing: |verifyTextPresent | blender |  |
   info: Starting test /selenium-server/tests/google_search_sphinx.html
   info: Executing: |open | http://google.com |  |
   info: Executing: |type | q | sphinx |
   info: Executing: |click | xpath=//input[@name=&apos;btnK&apos;] |  |
   info: Executing: |pause | 2000 |  |
   info: Executing: |verifyTextPresent | sphinx |  |
   
