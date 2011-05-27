{% extends "base.tpl" %}

{% block main %}

<h3>No thumbnails</h3>


<input type="button" id="proceed" value="Create thumbnails" />

<div id="empty">
    {% for pic in pictures %}
        <p>{{ pic }}</p>
    {% endfor %}
</div<



{% endblock %}
