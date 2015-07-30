## Template Inheritance

* Template inheritance allows you to build a base “skeleton” template that contains all the common elements of your site and defines blocks that child templates can override

* You create template blocks with the `{% block <block-name >%}` tag
    *  Each block tag has a block-name allowing you to differentiate between the block tags
    * Block tags have opening and closing tags `{% endblock <block-name> %}`

* You call your base (skeleton) template with the extends tag `{% extends <template-to-extend >%}`
