# Text Recognition with Adobe Acrobat & ABBYY Finereader

## Introduction to OCR

### Vocabulary

- **PDF** – Portable Document Format
    - Commonly used file format that can inlcude text, images, graphics, and interactive forms.
- **OCR** – Optical Character Recognition
    - The process of using a computer to extract text from an image.

### What are PDFs?  

* PDF (Portable Document Format) files are commonly used to create documents which can combine images, graphics, and text. 
* There are many types of PDFs.

### What is OCR?

* OCR stands for Optical Character Recognition. This is the process of using a computer to extract text from an image. Generally, this is done to PDFs, but OCR can be run on any image with typed text.
* OCR works best on standard type faces, but is not effective at identifying text from handwriting. 

### Good vs Bad PDFs

* Most PDFs that we OCR come from photos or scans of physical items. PDFs created digitally, including journal publications, have a text layer already built-in. We can check if a PDF already has text built-in by trying to copy/paste the text or by searching the PDF (Ctrl+F or Cmd+F).
* The quality of a scanned document has a great effect on the accuracy of the OCR. It's best to scan documents at high quality (600 dpi) and with good, overhead lighting. Book scanners are great for this job.

![](../assets/img/poxLarge.png)

![](../assets/img/badTable.png) ![](../assets/img/skewedImage.png)

![](../assets/img/InterAmerican.png)

## OCR with Adobe Acrobat

Adobe Acrobat is a great entry-level tool for OCR. It works best for good quality PDFs (we'll use ABBYY on our ugly PDFs). It's also free for all current Yale students, faculty, and staff.

>## First Steps with Acrobat
>
>* In the sample data, go to the 'Acrobat' folder and open 'CeremonialMagic_1.pdf' in Adobe Acrobat.
>	* Right-click the file
>	* Select 'Open with' and choose Adobe Acrobat
>	* If this is your first time using Acrobat, you will be asked to sign-in to your account. Use your Yale crendaentials (NetID & password). 
>* Select 'Scan & OCR' from the 'Tools' menu.
> ![Screenshot of Acrobat Tools menu](../assets/img/ScanAndOCR.png)
>* Click the 'Recognize Text' drop-down.
>	* Change 'Settings' and 'language' if necessary.
>	* Click the blue 'Recognize Text' button to begin OCR.

### Fixing errors

Acrobat cannot be 100% accurate with it's OCR. It will highlight words with when it's confidence in the accuracy of the OCR is low. We can manually verify and edit any OCR text.  

>## Correct Text
>
>1. Click the 'Recognize Text' drop-down.
>	* Select 'Correct recognized text'
>2. Each word with a low confidence rating will appear in a red box.
>	![Screenshot of correct text options](../assets/img/CorrectText.png)
>	* Click on words in box.
>	* Correct transcription as necessary.
>	* Selct 'Apply' and move to the next potential error.

### Viewing the Text

After we OCR any PDF, we create a hidden text layer. While invisiable to us, this text layer allows us to copy/paste and search the recognized text. 

>## Hidden Text
>
> We can view the hidden text layer in Acrobat as an additional means of quality control.
>
>1. While the 'Correct recognized text' option is open, check the box for 'Review recognized text'. 
>	* This option will show us the hidden text layer on top of the image of the text.
>2. Now we can edit the text for each word, not just the words that Acrobat identified as potential errors.
>

You'll notice in our example PDF there are several words which are incorretly recognized. These were not identified by Acrobat as potenital issues. It's important to remember that 100% accuracy with OCR software is nearly impossible.

### Bulk processing

>## Using the 'Action Wizard'
>
>Adobe provides a way to create workflows through the Action Wizard. We can save these workflows and apply them to multiple PDFs or entire folders of PDFs.
>1. From 'Tools', select 'Action Wizard'
>![Screenshot of Acrobat Tools Menu](../assets/img/actionWizard.png)
>2. In the next menu, select 'New Action'
>3. There are several settings to change to complete our worflow
>	* Under 'Files to be processed, choose the 'Acrobat' folder. This is the folder where your PDFs to recognize are saved.
>	* From 'Recognize Text', add 'Recognize Text using OCR'.
>	* Under 'Save & Export', add 'Save' twice.
>	* Choose 'Specify Settings' and change 'Output Format' to 'Export File(s) to Alternative Format' and select 'Text (Plain)' form the 'Export to:' drop-down list.
>	![Screenshot of Acrobat Tools Menu](../assets/img/newAction.png)
>4. Rename the process and click 'Save'. We can now apply these steps to any folder and Acrobat will OCR each file and save two versions: one PDF and one Text file.
>

## OCR with ABBYY FineReader

### Enhancing PDFs to improve OCR accuracy

* Even the best qualtiy scan can cause OCR issues. There are several stategies for editing a PDF to help improve OCR quality:
    * Removing background color (black text on a white background).
    * Increasing contrast
    * Straightening & de-skewing text
    * Removing noise or extraneous marks

### OCR with ABBYY Finereader

* ABBYY Finereader for quick conversion of PDFs, including basic OCR
* ABBYY OCR Editor for more OCR options, custom pattern recognition, language selection, and more. 

>## Getting Started with ABBYY
>
>1. Right-click on PDF named 'InterAmerican.pdf', select Open with ABBYY FineReader 14.
>2. Click the 'Recognize Text' drop-down and select 'Open in OCR Editor'.
> ![Screenshot of OCR Editor Menu](../assets/img/OCR_editor.png)

### Viewing OCR output

* After the OCR process is complete, we can compare the original document to the text-only version.
* ABBYY highlights potential errors in blue. We can manually correct or edit the text data before saving/exporting for greater QA.

![Screenshot of OCR Pages Menu](../assets/img/verifyText.png)

**Spend a few minutes manually correcting and verifying highlighted text.** 

### Improving OCR Quality

* ABBYY provides a built-in image editor to correct scans increasing the legibility of the text. 
* The default option will try to intellegently correct the image so the OCR engine can more easily recognize text. You can also edit the scans manually. 

>## Using the Image Editor
>1. Right-click on PDF named 'PlantPestsCT.pdf', select Open with ABBYY FineReader 14. 
>2. Click the 'Recognize Text' drop-down and select 'Open in OCR Editor'.
>	- You'll see the recognized text quality is very low. We can use the built-in image editing tools to improve the accuracy of the OCR. 
>3. Click 'Image Editor'. This will open a new interface in ABBYY for editing images to improve OCR quality.
>4. There are several tasks we can do to improve the OCR quality:
>	- Crop out non-essential features
>	- Change background color to white
>	- Increase contrast or brightness
>	- de-skew words/lines
>	- Remove noise & marks

* Edits can be applied to a single page, even or odd pages, or all pages.

### Creating Templates

Area templates allow us to identify all the text boxes on one page and apply an identical layout to other pages. We can even save these templates for use in other ABBYY projects.

>## Create an Area Template
>
> Many times, the text blocks of scanned books do not line up in the center of the scan. Often, the text for even vs odd pages will be aligned differently on the page. We can account for this with our templates.
>
>1. Choose page 2 and draw a green text box around the main block of text. 
>	- Right-click on any existing grenn text boxes and select 'Delete'. These boxes contain, page numbers, watermarks, and other text we don't want to include (note this will also ignore any images on the page).
>2.  Choose 'Area' from the top menu and select 'Save Area Template'.
>	- Name the template 'trees_even.blk' and save.
>3.  Now select page 3 and repeat the steps 1 and 2 above.
>	- Name the template 'trees_odd.blk'
>4. From the 'Pages' toolbar, click the three dots, 'Select Pages', and then 'Even Pages'.
>	![Screenshot of OCR Pages Menu](../assets/img/SelectOddEven.png)
>5. With the even pages highlighted, choose 'Area' from the top menu, select 'Load Area Template', and choose 'trees_even.blk'.
>6. Repeat steps 4 and 5 using the odd pages and odd tamplate.
>7. 'Recognize' the text again and see how the output changes.
>

## OCR for Non-Standard Text

### Working with Tables

Many PDFs include data in the form of tables. While recognizing the text and numbers in a table is straightforward, maintaing the table structure is more difficult. 

>## From PDF to Excel
>ABBYY can recognize the structure of data tables. It uses the lines seperating rows & columns to idenitify the data in each cell.
>
>1. In the ABBYY folder, right-click to open 'tables.pdf' in ABBYY FineReader.
>2. Click the 'Recognize Text' drop-down and select 'Open in OCR Editor'.
>3. ABBYY should recognize the tables in this PDF. ABBYY designates tables with blue shading.
>4. We can manually adjust columns and rows to match the table structure.
>	- We can split, merge, and create new cells, columns, and rows. 
>	- Add a horizontal divider between rows 1 and 2.
>5. Click 'Save as XLXS', this will open the table in excel. We can edit or save the table from there.
>

![Screenshot of ABBYY recognizing data tables](../assets/img/ABBYY_Tables.png)

### Non-Latin Text

ABBYY is not limited to English or Latin text. ABBYY has a robust list of languages that are supported. You can evern choose multiple languages if a document is multi-lingual.

>## Non-English OCR
>
>1. Right-click on PDF named 'Russian.pdf', select Open with ABBYY FineReader 14.
>2. Click the 'Recognize Text' drop-down and select 'Open in OCR Editor'. 
>3. Select Language as 'Russian' and 'Russian (Old Spelling) if not automatically detected.
>4. Click 'Recgonize' again and see how the results have improved. We can edit this PDF in the same way we would with an English text.
>

### Improving Pattern Recognition

ABBYY comes trained on many different alphabets and languages. Of course, ABBYY does not know every font used through history. Also, special characters or ligatures might not be in ABBYY's dictionaries. 

* We can enhance ABBYY's existing patterns through training. 
* You can custom train ABBYY from scratch or you can add to an existing pattern dictioanry.

>## Pattern Training and Non-Roman Type
> Typically, modern English is printed using Roman typeface. Other types like Blackletter Gothic are no longer popular, but were used in historic text. 
> Many historic texts in English use a combination of old and modern types. We can enhance our existing pattern dictionary by training ABBYY on the meanings of older style type.   
>
>1. Right-click on PDF named 'Non-Latin.pdf', select Open with ABBYY FineReader 14.
>2. Click the 'Recognize Text' drop-down and select 'Open in OCR Editor'. 
>3. In the Options menu, under OCR select 

![Screenshot of ABBYY's Pattern Trainer](../assets/img/patternTraining.png)


Copyright © 2020 by Joshua Dull
This instructional material is made available under the [Creative Commons Attribution license](https://creativecommons.org/licenses/by/4.0/). 