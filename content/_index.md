---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: about.biography
    id: about
    content:
      title: Biography
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin

  - block: features
    id: skills
    content:
      title: Skills
      items:
        - name: Statistics
          description: 100%
          icon: chart-line
          icon_pack: fas
        - name: Data Science
          description: 100%
          icon: project-diagram
          icon_pack: fas
        - name: Python
          description: 80%
          icon: python
          icon_pack: fab
        - name: R
          description: 80%
          icon: r-project
          icon_pack: fab
        - name: SQL
          description: 90%
          icon: database
          icon_pack: fas
        - name: Web Scrapping
          description: 80%
          icon: file-code
          icon_pack: fas
      
  - block: experience
    id: experience
    content:
      title: Experiences
      # Date format for experience
      #   Refer to https://wowchemy.com/docs/customization/#date-format
      date_format: Jan 2006
      # Experiences.
      #   Add/remove as many `experience` items below as you like.
      #   Required fields are `title`, `company`, and `date_start`.
      #   Leave `date_end` empty if it's your current employer.
      #   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.
      items:
        - title: Data Scientist
          company: MVS Lab, University of Waterloo
          company_url: 'https://uwaterloo.ca/mechatronic-vehicle-systems-lab/'
          company_logo: mvs-logo
          location: Waterloo, Ontario
          date_start: '2021-10-01'
          date_end: ''
          description: |2-
              Responsibilities include:
              * Analysing
              * Modelling
              * Implementing

        - title: Statistical Consultant
          company: Stats Club, University of Waterloo
          company_url: ''
          company_logo: uw-logo
          location: Waterloo, Ontario
          date_start: '2016-09-01'
          date_end: '2021-08-31'
          description: |2-
              Responsibilities include:
              * Consulting

        - title: Lecturer of Statistics
          company: University of Semnan
          company_url: 'https://english.semnan.ac.ir/'
          company_logo: sem-logo
          location: Semnan
          date_start: '2010-09-01'
          date_end: '2016-08-31'
          description: Taught statistics and probability courses.
    design:
      columns: '2'

  # - block: collection
  #   id: posts
  #   content:
  #     title: Recent Posts
  #     subtitle: ''
  #     text: ''
  #     # Choose how many pages you would like to display (0 = all pages)
  #     count: 5
  #     # Filter on criteria
  #     filters:
  #       folders:
  #         - post
  #       author: ""
  #       category: ""
  #       tag: ""
  #       exclude_featured: false
  #       exclude_future: false
  #       exclude_past: false
  #       publication_type: ""
  #     # Choose how many pages you would like to offset by
  #     offset: 0
  #     # Page order: descending (desc) or ascending (asc) date.
  #     order: desc
  #   design:
  #     # Choose a layout view
  #     view: compact
  #     columns: '2'

  - block: portfolio
    id: projects
    content:
      title: Projects
      filters:
        folders:
          - project
      # Default filter index (e.g. 0 corresponds to the first `filter_button` instance below).
      default_button_index: 0
      # Filter toolbar (optional).
      # Add or remove as many filters (`filter_button` instances) as you like.
      # To show all items, set `tag` to "*".
      # To filter by a specific tag, set `tag` to an existing tag name.
      # To remove the toolbar, delete the entire `filter_button` block.
      buttons:
        - name: All
          tag: '*'
        - name: NLP
          tag: NLP
        - name: Deep Learning
          tag: Deep Learning
        - name: Other
          tag: Demo
    design:
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: '1'
      view: showcase
      # For Showcase view, flip alternate rows?
      flip_alt_rows: false
    
  # - block: collection
  #   id: featured
  #   content:
  #     title: Featured Publications
  #     filters:
  #       folders:
  #         - publication
  #       featured_only: true
  #   design:
  #     columns: '2'
  #     view: card
    
  - block: collection
    id: featured
    content:
      title: Recent Publications
      text: |-
        {{% callout note %}}
        Quickly discover relevant content by [filtering publications](./publication/).
        {{% /callout %}}
      filters:
        folders:
          - publication
        exclude_featured: true
    design:
      columns: '2'
      view: citation
  # - block: collection
  #   id: talks
  #   content:
  #     title: Recent & Upcoming Talks
  #     filters:
  #       folders:
  #         - event
  #   design:
  #     columns: '2'
  #     view: compact

  # - block: tag_cloud
  #   content:
  #     title: Popular Topics
  #   design:
  #     columns: '2'
  
  # - block: markdown
  #   content:
  #     title: Gallery
  #     subtitle: ''
  #     text: |-
  #       {{< gallery album="demo" >}}
  #   design:
  #     columns: '1'

  - block: contact
    id: contact
    content:
      title: Contact
      subtitle:
      text: |-
        Connect with me
      # Contact (add or remove contact options as necessary)
      email: valiollahi.reza@gmail.com
      # phone: 888 888 88 88
      # appointment_url: 'https://calendly.com'
      address:
        # street: 450 Serra Mall
        city: Waterloo
        region: Ontario
        # postcode: '94305'
        country: Canada
        country_code: CAN
      # directions: Enter Building 1 and take the stairs to Office 200 on Floor 2
      # office_hours:
      #   - 'Monday 10:00 to 13:00'
      #   - 'Wednesday 09:00 to 10:00'
      # contact_links:
      #   - icon: twitter
      #     icon_pack: fab
      #     name: DM Me
      #     link: 'https://twitter.com/Twitter'
      #   - icon: skype
      #     icon_pack: fab
      #     name: Skype Me
      #     link: 'skype:echo123?call'
      #   - icon: video
      #     icon_pack: fas
      #     name: Zoom Me
      #     link: 'https://zoom.com'
      # Automatically link email and phone or display as text?
      autolink: true
      # Email form provider
      form:
        provider: netlify
        formspree:
          id:
        netlify:
          # Enable CAPTCHA challenge to reduce spam?
          captcha: false
    design:
      columns: '2'
---
