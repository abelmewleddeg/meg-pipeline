Data storage
------------

MEG Data storage
################

The MEG data is securely stored on NYU BOX, access is given through invitations.
The *Data* folder is structured in the **BIDS** standardized format.
Please raise an issue on *github* repository if you think the structure does not conform to **BIDS**.

Sign in on NYU Box in the below link

.. admonition:: Link to MEG data (Box Invitation Only)

    `https://nyu.box.com/v/meg-datafiles <https://nyu.box.com/v/meg-datafiles>`_


Or directly from the below widget

.. raw:: html

    <iframe src="https://nyu.app.box.com/embed/s/wefkhu5yn7tzzhw2gcr45zvnsqqnbyuf?sortColumn=name&expandSidebars=true" width="650" height="550" frameborder="0" allowfullscreen webkitallowfullscreen msallowfullscreen></iframe>

If you are unable to access the datasets it means you do not have the permission to. Kindly contact us to get permission.


MRI Data storage
################

MRI data is hosted on Flywheel

.. admonition:: Link to MRI data (Box Invitation Only)

    `https://flywheel.abudhabi.nyu.edu/#/login <https://flywheel.abudhabi.nyu.edu/#/login>`_

Data naming and uploading protocol
----------------------------------

In the following, [SUB_ID] should be replaced with the ID of the subject for naming purposes.
The different data files generated from a MEG experiment are the following.

.. note::
    If you have suggestions to make the naming convention better, please raise an issue on github
    or create a pull request with your proposed modifications.

Laser scan files
################

#. A .fsn filename that should be named ``sub-\[SUB_ID\]_scan.fsn`` : This file is obtained by saving
   the whole fastscan laser project (File Save)

#. Several .txt
    * ``sub-[SUB_ID]_scan.txt``  is the head scan of the participant
    * ``sub-[SUB_ID]_scan_stylus.txt`` is the stylus location file of the participant

KIT-MEG files
#############

Depending on the experiment, many .con files can be produced by the KIT machine.

#. .con files are named:
   * ``sub-[SUB_ID]_[date].con``

#. .mrk files are named:
   * ``sub-[SUB_ID]_[marker_number]_[date].mrk`` where [marker_number] is replaced with the number of the marker (representing the time-order of acquisition of that marker)

OPM files
#########

The OPM system generates a BIDS directory with the .fif files


Data uploading
##############

Data will be uploaded to NYU BOX, to the following link

.. admonition:: Link to MEG data (Box Invitation Only)

    `https://nyu.box.com/v/meg-datafiles <https://nyu.box.com/v/meg-datafiles>`_

Steps

#. Access the folder of NYU Box
#. Identify the project that the data belongs to
#. Access the folder for that project or create a new folder if non-existent

#. Follow the BIDS structure format, within each project file, we find subjects file named by their ID
    * Within each subjects folder we find, *anat*, *meg-kit*, *meg-opm* folders
    * Place the corresponding files into the right folder: all headscan files go to *anat*, the .con and .mrk goes to *meg-kit*, the .fif goes to *meg-opm*

#. Make sure that all files have been uploaded to the folder