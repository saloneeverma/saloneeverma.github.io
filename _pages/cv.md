---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<style>
.cv-iframe {
  width: 100%;
  min-height: min(74vh, 960px);
  border: 0;
  background: #fff;
}
@media (max-width: 768px) {
  .cv-iframe { min-height: 65vh; }
}
.cv-fallback-note {
  margin: 0.45rem 0 0;
  font-size: 0.8em;
}
</style>

<iframe class="cv-iframe" src="{{ base_path }}/files/cv.pdf#view=FitH" title="Salonee Verma CV" loading="lazy"></iframe>

<p class="cv-fallback-note">If the embedded preview does not load in your browser, <a href="{{ base_path }}/files/cv.pdf">open the PDF directly</a>.</p>


<!-- Education
======
* Ph.D in Version Control Theory, GitHub University, 2018 (expected)
* M.S. in Jekyll, GitHub University, 2014
* B.S. in GitHub, GitHub University, 2012

Work experience
======
* Spring 2024: Academic Pages Collaborator
  * GitHub University
  * Duties includes: Updates and improvements to template
  * Supervisor: The Users

* Fall 2015: Research Assistant
  * GitHub University
  * Duties included: Merging pull requests
  * Supervisor: Professor Hub

* Summer 2015: Research Assistant
  * GitHub University
  * Duties included: Tagging issues
  * Supervisor: Professor Git
  
Skills
======
* Skill 1
* Skill 2
  * Sub-skill 2.1
  * Sub-skill 2.2
  * Sub-skill 2.3
* Skill 3

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Service and leadership
======
* Currently signed in to 43 different slack teams -->
