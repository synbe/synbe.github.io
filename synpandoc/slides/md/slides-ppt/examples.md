%Reveal.js 模板
%Reveal.js 2016

Reveal.js
=========

### The HTML Presentation Framework

Created by [Hakim El Hattab](http://hakim.se) /
[@hakimel](http://twitter.com/hakimel)

Hello There


reveal.js enables you to create beautiful interactive slide decks using
HTML. This presentation will show you examples of what it can do.

Vertical Slides
=========

Slides can be nested inside of each other.

Use the *Space* key to navigate through all slides.

\
 [](#)
Basement Level 1
=========
Nested slides are useful for adding additional detail underneath a high
level horizontal slide.

Basement Level 2
=========

That's it, time to go back up.

\
 [](#/2)
Slides
=========

Not a coder? Not a problem. There's a fully-featured visual editor for
authoring these, try it out at <http://slides.com>.

Point of View
=========

Press **ESC** to enter the slide overview.

Hold down alt and click on any element to zoom in on it using
[zoom.js](http://lab.hakim.se/zoom-js). Alt + click anywhere to zoom
back out.

Touch Optimized
=========

Presentations look great on touch devices, like mobile phones and
tablets. Simply swipe through your slides.

Fragments
=========

Hit the next arrow...

... to step through ...

<span class="fragment">... a</span> <span
class="fragment">fragmented</span> <span class="fragment">slide.</span>

This slide has fragments which are also stepped through in the notes
window.
Fragment Styles
=========

There's different types of fragments, like:

grow

shrink

fade-out

current-visible

highlight-red

highlight-blue

Transition Styles
=========

You can select from different transitions, like:\
 [None](?transition=none#/transitions) -
[Fade](?transition=fade#/transitions) -
[Slide](?transition=slide#/transitions) -
[Convex](?transition=convex#/transitions) -
[Concave](?transition=concave#/transitions) -
[Zoom](?transition=zoom#/transitions)

Themes
=========

reveal.js comes with a few themes built in:\
 [Black (default)](#) - [White](#) - [League](#) - [Sky](#) - [Beige](#)
- [Simple](#)\
 [Serif](#) - [Blood](#) - [Night](#) - [Moon](#) - [Solarized](#)

Slide Backgrounds
=========

Set `data-background="#dddddd"` on a slide to change the background
color. All CSS color formats are supported.

[](#)
Image Backgrounds
=========

    <section data-background="image.png">

Tiled Backgrounds
=========

    <section data-background="image.png" data-background-repeat="repeat" data-background-size="100px">

<div
style="background-color: rgba(0, 0, 0, 0.9); color: #fff; padding: 20px;">

Video Backgrounds
=========

    <section data-background-video="video.mp4,video.webm">

</div>

... and GIFs!
=========

Background Transitions
=========

Different background transitions are available via the
backgroundTransition option. This one's called "zoom".

    Reveal.configure({ backgroundTransition: 'zoom' })

Background Transitions
=========
You can override background transitions per-slide.

    <section data-background-transition="zoom">

Pretty Code
=========

    function linkify( selector ) {
      if( supports3DTransforms ) {

        var nodes = document.querySelectorAll( selector );

        for( var i = 0, len = nodes.length; i < len; i++ ) {
          var node = nodes[i];

          if( !node.className ) {
            node.className += ' roll';
          }
        }
      }
    }
                        

Code syntax highlighting courtesy of
[highlight.js](http://softwaremaniacs.org/soft/highlight/en/description/).

Marvelous List
=========

-   No order here
-   Or here
-   Or here
-   Or here

Fantastic Ordered List
=========

1.  One is smaller than...
2.  Two is smaller than...
3.  Three!

Tabular Tables
=========

Item
Value
Quantity
Apples
\$1
7
Lemonade
\$2
18
Bread
\$3
2
Clever Quotes
=========

These guys come in two forms, inline: ““The nice thing about standards
is that there are so many to choose from”” and block:

> “For years there has been a theory that millions of monkeys typing at
> random on millions of typewriters would reproduce the entire works of
> Shakespeare. The Internet has proven this theory to be untrue.”

Intergalactic Interconnections
=========

You can link between slides internally, [like this](#/2/3).

Speaker View
=========

There's a [speaker
view](https://github.com/hakimel/reveal.js#speaker-notes). It includes a
timer, preview of the upcoming slide as well as your speaker notes.

Press the *S* key to try it out.

Oh hey, these are some notes. They'll be hidden in your presentation,
but you can see them if you open the speaker notes window (hit 's' on
your keyboard).
Export to PDF
=========

Presentations can be [exported to
PDF](https://github.com/hakimel/reveal.js#pdf-export), here's an
example:

Global State
=========

Set `data-state="something"` on a slide and `"something"` will be added
as a class to the document element when the slide is open. This lets you
apply broader style changes, like switching the page background.

State Events
=========

Additionally custom events can be triggered on a per slide basis by
binding to the `data-state` name.

    Reveal.addEventListener( 'customevent', function() {
        console.log( '"customevent" has fired' );
    } );
                        

Take a Moment
=========

Press B or . on your keyboard to pause the presentation. This is helpful
when you're on stage and want to take distracting slides off the screen.

Much more
=========

-   Right-to-left support
-   [Extensive JavaScript API](https://github.com/hakimel/reveal.js#api)
-   [Auto-progression](https://github.com/hakimel/reveal.js#auto-sliding)
-   [Parallax
    backgrounds](https://github.com/hakimel/reveal.js#parallax-background)
-   [Custom keyboard
    bindings](https://github.com/hakimel/reveal.js#keyboard-bindings)

THE END
=======

- [Try the online editor](http://slides.com)\
 - [Source code & documentation](https://github.com/hakimel/reveal.js)

