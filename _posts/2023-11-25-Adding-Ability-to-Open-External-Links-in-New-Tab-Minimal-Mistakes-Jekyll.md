---
date: 2023-11-25
header:
  teaser: /img/MinimalMistakesHeader.png
  overlay_image: /img/MinimalMistakesHeader.png
  overlay_filter: 0.8
toc: true
toc_label: "Contents"
--- 
# Add the ability to open external links in a new tab instead of navigating away from your site.

### I know, minimal mistakes has a mistake in the image. That was GPT, not me.

I found a way of adding the ability to have external links open in a new tab when clicked in minimal mistakes jekyll theme. I wanted to add this to a post for my future reference and anyone else looking. 

There are a couple changes needed for this. First is to create a JS file in /assets/js called externalLinksHandler.js. The contents of the file is:

```
class ExternalLinksHandler {
    constructor() {
        this.addAttributesToExternalLinks();
    }

    addAttributesToExternalLinks() {
        // Select all anchor tags
        const links = document.querySelectorAll('a[href]');

        // Iterate over each link
        links.forEach(link => {
            // Check if the link is external
            if (this.isExternalLink(link)) {
                // Add target and rel attributes
                link.setAttribute("target", "_blank");
                link.setAttribute("rel", "noopener noreferrer");
            }
        });
    }

    isExternalLink(link) {
        // Get the location of the current document
        const currentLocation = window.location.hostname;

        // Extract the domain from the link's href attribute
        const linkDomain = new URL(link.href).hostname;

        // Check if the link's domain is different from the current location's domain
        return currentLocation !== linkDomain;
    }
}

// Initialize the ExternalLinksHandler when the DOM is fully loaded
document.addEventListener("DOMContentLoaded", function() {
    new ExternalLinksHandler();
});

```

Then add this line to the /layouts/default.html file:

```
 <script src="{{ site.baseurl }}/assets/js/externalLinksHandler.js"></script>
```

Then, if nothing else was added and it is the default layout already, it will look like this:
```
---
---

<!doctype html>
<!--
  Minimal Mistakes Jekyll Theme 4.24.0 by Michael Rose
  Copyright 2013-2020 Michael Rose - mademistakes.com | @mmistakes
  Free for personal and commercial use under the MIT license
  https://github.com/mmistakes/minimal-mistakes/blob/master/LICENSE
-->
<html lang="{{ site.locale | slice: 0,2 | default: "en" }}" class="no-js">
  <head>
    {% include head.html %}
    {% include head/custom.html %}
  </head>

  <body class="layout--{{ page.layout | default: layout.layout }}{% if page.classes or layout.classes %}{{ page.classes | default: layout.classes | join: ' ' | prepend: ' ' }}{% endif %}">
    {% include_cached skip-links.html %}
    {% include_cached masthead.html %}

    <div class="initial-content">
      {{ content }}
    </div>

    {% if site.search == true %}
      <div class="search-content">
        {% include_cached search/search_form.html %}
      </div>
    {% endif %}

    <div id="footer" class="page__footer">
      <footer>
        {% include footer/custom.html %}
        {% include_cached footer.html %}
      </footer>
    </div>

    {% include scripts.html %}
    <script src="{{ site.baseurl }}/assets/js/externalLinksHandler.js"></script>
  </body>
</html>

```

After that, you can open an external link without navigating away from your site. Like this [Link here](https://chat.openai.com/g/g-xFXaIXZvo-flowmaid-your-mermaid-flowchart-assistant)

Ahh, perfect an little work. Just hwo it should have worked in the first place.