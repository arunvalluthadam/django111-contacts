


{% block content %}


<div class='col-sm-3 col-sm-offset-4' >
<h1>{{title}}</h1>


{% block head_extra %} 
{{form.media}}
{% endblock head_extra %}

<form method='POST' action='' enctype='multipart/form-data'>{% csrf_token %}
{{ form|crispy }}
<input type='submit' class='btn btn-default' value='{{title}}' />
</form>
</div>
{% endblock content %}