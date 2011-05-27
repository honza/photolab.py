{% extends "base.tpl" %}

{% block main %}
    {% for image in pictures  %}
        <div class="image-box">
            <div class="image-controls">
                <a href="#" class="discard">
                    <img src="/static/close.png" />
                </a>
                <a href="#" class="keep">
                    <img src="/static/plus.png" />
                </a>
            </div>
            <div class="image">
                <img id="{{ image }}" src="/media/{{ image }}" />
            </div>
        </div>
    {% endfor %}
{% endblock %}
