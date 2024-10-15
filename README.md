# PLT
_Pig Latin_ is a language game where English words are altered, according to some rules, to obtain their _Pig Latin_ translation. _PLT_ (_Pig Latin Translator_) is an API for translating a phrase from the English language into the _Pig Latin_ one.

You do not need to know more so far. The _User Stories_ section will provide further details.

## Instructions for You
* FORK this project and make sure your forked repository is PUBLIC. Then, IMPORT the forked project into PyCharm.
* If you BELONG to the GAI4-TDD group, you are asked to develop _PLT_ by following TDD WITH the support of **GAI4-TDD**. If you do NOT BELONG to the GAI4-TDD group, you are asked to develop _PLT_ by following TDD WITHOUT the support of **GAI4-TDD**.
* You DO NOT need to develop a GUI.
* You CANNOT change the signature of the provided methods, move the provided methods to other classes, or change the name of the provided classes. However, you CAN add fields, methods (e.g., methods called by the provided methods), or even classes (including other test classes), as long as you comply with the provided API.
* You CAN use the internet to consult Python APIs or QA sites (e.g., StackOverflow).
* You CANNOT use AI tools except for GAI4-TDD.
* You CANNOT interact with your colleagues. Work alone and do your best!
* The _PLT_ requirements are divided into a set of USER STORIES, which serve as a to-do list (see the _User Stories_ section).
* You should be able to incrementally develop _PLT_ without an upfront comprehension of all its requirements. DO NOT read ahead and handle the requirements (specified in the user stories) one at a time in the provided order. Develop _PLT_ by starting from the first story's requirement. When a story is IMPLEMENTED, move on to the NEXT one. A story is implemented when you are confident that your program correctly implements the functionality stipulated by the story's requirement. This implies that all your test cases for that story and all the test cases for the previous stories pass. You may need to review your program as you progress toward more advanced requirements.
* Each time you end a GREEN or REFACTOR phase, COMMIT.
* At the end of the task, PUSH your forked project.

## API Usage
Take some minutes to understand, in broad terms, how the API works. If you do not fully understand the API, do not worry because more details will be given later in the _User Stories_ section. A typical API usage follows.

```python
# Initialize a translator with a phrase
translator = PigLatinTranslator.PigLatinTranslator("This is a phrase")
# Get the phrase
phrase = translator.get_phrase()
# Get the Pig Latin translation
translation = translator.translate()
```

See the provided source files to improve your understanding of the API before starting to implement the user stories. 

## User Stories
Remember to read and implement the user stories once at a time (in the provided order). Therefore, do not read the next user story, if the current one is not implemented yet.
