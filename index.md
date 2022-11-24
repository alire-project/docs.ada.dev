---
layout: default
---

{% assign alphabet= "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z" | split: ' ' %}
{% for letter in alphabet %}
     {% capture filtered_crates %}
         {% for crate in site.data.global_doc_info %}
             {% assign crate_first_letter = crate[0] | slice: 0 | upcase %}
             {% if crate_first_letter == letter %}
             {{ crate[0] }}
             {% endif %}
         {% endfor %}
     {% endcapture %}
    {% assign filtered_list = filtered_crates | split: ' ' %}
    {% if filtered_list != empty %}
<b>{{ letter }}</b>
<ul>
        {% for crate in filtered_list %}
            {% for item in site.data.global_doc_info %}
                {% if item[0]== crate %}
                    {% assign short_description = item.short_description %}
                {% endif %}
            {% endfor %}
<li><a href="{{ "crate/" | append: crate | downcase | relative_url }}">{{ crate }}</a>: {{ short_description }}</li>
        {% endfor %}
</ul>
    {% endif %}
{% endfor %}
