
---------
LMEDS
---------

.. image:: https://travis-ci.org/timmahrt/LMEDS.svg?branch=master
    :target: https://travis-ci.org/timmahrt/LMEDS

.. image:: https://coveralls.io/repos/github/timmahrt/LMEDS/badge.svg?branch=master
    :target: https://coveralls.io/github/timmahrt/LMEDS?branch=master
    
.. image:: https://img.shields.io/badge/license-MIT-blue.svg?
   :target: http://opensource.org/licenses/MIT

A web platform for collecting text annotation and experiment data online.

LMEDS was originally developed for conducting Rapid Prosody Transcription annotations
over the internet.  Since then it has been extended for doing a number of
different types of perceptual experiments (memory tasks, AXB-type tasks, etc.).

.. sectnum::
.. contents::

Major revisions
================

Ver 2.4 (Nov 02, 2016)

- stimulus presentation can now be automatically randomized for each user

    - post-processing scripts unscramble the individual output orders
      while marking the order users did the task in
      
- task timeout and media-less support (i.e. reading tasks) added to
  media_choice pages

- limits can be set on the minimum and maximum number of prominences
  and boundaries that can be made on a text in prominence- and boundary-
  marking- pages.
  
- keyboard keys can be bound to buttons on a page (e.g. the 'p' button can
  be used to play audio or 'enter' can be pressed to submit a response)
  
- numerous bugfixes and code cleanup

Ver 2.3 (May 17, 2016)

- Video now supported with the same controls and functionality as audio

- User scripts utilities can now be run from a web browser for great ease of use

- Sliding scales are now a supported widget

- New syllable-marking page (branch of prominence-marking pages)

- Experiment participants can now relogin and resume from where they left off

- Integration tests added for greater reliability.  Also, numerous bugfixes.

Ver 2.2 (Dec 15, 2015)

- Added support for python 3.x (tested on 3.5)

Ver 2.1 (Sep 18, 2015)

- Replaced the many AXB page classes with one flexible audio_choice class

Ver 2.0 (Aug 12, 2015)

- First public release.  

- Inclusion of user script utilities.

- Numerous bugfixes and stability improvements (audio is significantly less error prone).  

- Offline server for running experiments locally.

- Companion website.


Ver 1.5 (May 19, 2014)

- Object oriented refactor

- Numerous bugfix and stability improvements.


Ver 1.0 (December 04, 2013)

- First stable release


Requirements
==============

``Python 2.6.*`` or above

``Python 3.3.*`` or above

`Click here to see the specific versions of python that praatIO is tested under <https://travis-ci.org/timmahrt/LMEDS>`_


Usage
=========

LMEDS needs to be installed on a server and probably needs to be done by someone
with a technical background. Once installed, experiments can be built with no 
programming experience.  Please see the document LMEDS_manual.pdf for instructions 
on installation and use.


Installation
================

Please see the manual for instructions on installing LMEDS on a server, running
LMEDS on a local computer (no server required), or for using the included user scripts.


Citing LMEDS
===============

If you use LMEDS in your research, please cite it like so:

Tim Mahrt. LMEDS: Language markup and experimental design software.
https://github.com/timmahrt/LMEDS, 2016.


Acknowledgements
================

Development of LMEDS was possible thanks to NSF grant **BCS 12-51343** to
Jennifer Cole, José I. Hualde, and Caroline Smith and to the A*MIDEX project
(n° **ANR-11-IDEX-0001-02**) to James Sneed German funded by the
Investissements d'Avenir French Government program,
managed by the French National Research Agency (ANR).
