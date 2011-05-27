<!DOCTYPE html>
<html>
<head>
    <title>Photolab</title>
    <link rel="stylesheet" href="/static/style.css" type="text/css" media="screen" />
    <script src="/static/jquery.js" type="text/javascript"></script>
    <script src="/static/script.js" type="text/javascript"></script>

</head>
<body>
    <div id="bar">
        <span id="logo">photolab</span>
        {% if process %}
            <span id="process"><a href="#" id="process-btn">Process me</a></span>
        {% endif %}
    </div>

    <div id="wrap">
     {% block main %}{% endblock %}
    </div>

</body>
</html>
