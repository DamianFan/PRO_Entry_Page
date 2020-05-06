


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>cytoscape.js/src/plugins/jquery.cytoscape-panzoom.js at master · cytoscape/cytoscape.js</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <link rel="logo" type="image/svg" href="https://github-media-downloads.s3.amazonaws.com/github-logo.svg" />
    <meta property="og:image" content="https://github.global.ssl.fastly.net/images/modules/logos_page/Octocat.png">
    <meta name="hostname" content="fe18.rs.github.com">
    <link rel="assets" href="https://github.global.ssl.fastly.net/">
    <link rel="xhr-socket" href="/_sockets" />
    
    


    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="5094632" name="octolytics-actor-id" /><meta content="JiaR" name="octolytics-actor-login" /><meta content="1189f12e3650a2dad7f38b031b9b377de2f6bd408a1e306fbe9ba3741bea23a9" name="octolytics-actor-hash" />

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="b6PI8n1MOG0/6u4nhmqVIGsfzD7Z/r0YEpsC1jIUt2s=" name="csrf-token" />

    <link href="https://github.global.ssl.fastly.net/assets/github-c6ca95663cba6496fe7a5bdd98671b82cd956df3.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://github.global.ssl.fastly.net/assets/github2-d35b02ba3940bde9b9f2c3e58f2dfb1ceff5886c.css" media="all" rel="stylesheet" type="text/css" />
    


      <script src="https://github.global.ssl.fastly.net/assets/frameworks-eae23340ab2a6ba722166712e699c87aaf60ad8f.js" type="text/javascript"></script>
      <script src="https://github.global.ssl.fastly.net/assets/github-a72a714a307592a4803dc7bed1e49523e71ff53e.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="babad972cb81ce7ba9200a9ccc34ae98">

        <link data-pjax-transient rel='permalink' href='/cytoscape/cytoscape.js/blob/bd02cc81c3c86694c0a0064e4aa539efe0bef31d/src/plugins/jquery.cytoscape-panzoom.js'>
  <meta property="og:title" content="cytoscape.js"/>
  <meta property="og:type" content="githubog:gitrepository"/>
  <meta property="og:url" content="https://github.com/cytoscape/cytoscape.js"/>
  <meta property="og:image" content="https://github.global.ssl.fastly.net/images/gravatars/gravatar-user-420.png"/>
  <meta property="og:site_name" content="GitHub"/>
  <meta property="og:description" content="cytoscape.js - A JavaScript graph library for analysis and visualisation (compatible with Node.js, jQuery 1.4+, and plain JavaScript)"/>

  <meta name="description" content="cytoscape.js - A JavaScript graph library for analysis and visualisation (compatible with Node.js, jQuery 1.4+, and plain JavaScript)" />

  <meta content="956141" name="octolytics-dimension-user_id" /><meta content="cytoscape" name="octolytics-dimension-user_login" /><meta content="2255947" name="octolytics-dimension-repository_id" /><meta content="cytoscape/cytoscape.js" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="2255947" name="octolytics-dimension-repository_network_root_id" /><meta content="cytoscape/cytoscape.js" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/cytoscape/cytoscape.js/commits/master.atom" rel="alternate" title="Recent Commits to cytoscape.js:master" type="application/atom+xml" />

  </head>


  <body class="logged_in page-blob windows vis-public env-production ">

    <div class="wrapper">
      
      
      


      <div class="header header-logged-in true">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/">
  <span class="mega-octicon octicon-mark-github"></span>
</a>

    <div class="divider-vertical"></div>

      <a href="/notifications" class="notification-indicator tooltipped downwards" title="You have no unread notifications">
    <span class="mail-status all-read"></span>
  </a>
  <div class="divider-vertical"></div>


      <div class="command-bar js-command-bar  in-repository">
          <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<input type="text" data-hotkey="/ s" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    data-username="JiaR"
      data-repo="cytoscape/cytoscape.js"
      data-branch="master"
      data-sha="16069522f29b31af77efd3a735752ea2342e68f8"
  >

    <input type="hidden" name="nwo" value="cytoscape/cytoscape.js" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="octicon help tooltipped downwards" title="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
        <ul class="top-nav">
            <li class="explore"><a href="/explore">Explore</a></li>
            <li><a href="https://gist.github.com">Gist</a></li>
            <li><a href="/blog">Blog</a></li>
          <li><a href="https://help.github.com">Help</a></li>
        </ul>
      </div>

    

  

    <ul id="user-links">
      <li>
        <a href="/JiaR" class="name">
          <img height="20" src="https://secure.gravatar.com/avatar/0a4c4abdd32aae556659e532572c324d?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /> JiaR
        </a>
      </li>

        <li>
          <a href="/new" id="new_repo" class="tooltipped downwards" title="Create a new repo" aria-label="Create a new repo">
            <span class="octicon octicon-repo-create"></span>
          </a>
        </li>

        <li>
          <a href="/settings/profile" id="account_settings"
            class="tooltipped downwards"
            aria-label="Account settings "
            title="Account settings ">
            <span class="octicon octicon-tools"></span>
          </a>
        </li>
        <li>
          <a class="tooltipped downwards" href="/logout" data-method="post" id="logout" title="Sign out" aria-label="Sign out">
            <span class="octicon octicon-log-out"></span>
          </a>
        </li>

    </ul>


<div class="js-new-dropdown-contents hidden">
  

<ul class="dropdown-menu">
  <li>
    <a href="/new"><span class="octicon octicon-repo-create"></span> New repository</a>
  </li>
  <li>
    <a href="/organizations/new"><span class="octicon octicon-organization"></span> New organization</a>
  </li>



    <li class="section-title">
      <span title="cytoscape/cytoscape.js">This repository</span>
    </li>
    <li>
      <a href="/cytoscape/cytoscape.js/issues/new"><span class="octicon octicon-issue-opened"></span> New issue</a>
    </li>
</ul>

</div>


    
  </div>
</div>

      

      




          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        

<ul class="pagehead-actions">

    <li class="subscription">
      <form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="b6PI8n1MOG0/6u4nhmqVIGsfzD7Z/r0YEpsC1jIUt2s=" /></div>  <input id="repository_id" name="repository_id" type="hidden" value="2255947" />

    <div class="select-menu js-menu-container js-select-menu">
        <a class="social-count js-social-count" href="/cytoscape/cytoscape.js/watchers">
          49
        </a>
      <span class="minibutton select-menu-button with-count js-menu-target">
        <span class="js-select-button">
          <span class="octicon octicon-eye-watch"></span>
          Watch
        </span>
      </span>

      <div class="select-menu-modal-holder">
        <div class="select-menu-modal subscription-menu-modal js-menu-content">
          <div class="select-menu-header">
            <span class="select-menu-title">Notification status</span>
            <span class="octicon octicon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-list js-navigation-container">

            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input checked="checked" id="do_included" name="do" type="radio" value="included" />
                <h4>Not watching</h4>
                <span class="description">You only receive notifications for discussions in which you participate or are @mentioned.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye-watch"></span>
                  Watch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_subscribed" name="do" type="radio" value="subscribed" />
                <h4>Watching</h4>
                <span class="description">You receive notifications for all discussions in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye-unwatch"></span>
                  Unwatch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_ignore" name="do" type="radio" value="ignore" />
                <h4>Ignoring</h4>
                <span class="description">You do not receive any notifications for discussions in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-mute"></span>
                  Stop ignoring
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

</form>
    </li>

  <li>
  
<div class="js-toggler-container js-social-container starring-container ">
  <a href="/cytoscape/cytoscape.js/unstar" class="minibutton with-count js-toggler-target star-button starred upwards" title="Unstar this repo" data-remote="true" data-method="post" rel="nofollow">
    <span class="octicon octicon-star-delete"></span><span class="text">Unstar</span>
  </a>
  <a href="/cytoscape/cytoscape.js/star" class="minibutton with-count js-toggler-target star-button unstarred upwards " title="Star this repo" data-remote="true" data-method="post" rel="nofollow">
    <span class="octicon octicon-star"></span><span class="text">Star</span>
  </a>
  <a class="social-count js-social-count" href="/cytoscape/cytoscape.js/stargazers">481</a>
</div>

  </li>


        <li>
          <a href="/cytoscape/cytoscape.js/fork" class="minibutton with-count js-toggler-target fork-button lighter upwards" title="Fork this repo" rel="nofollow" data-method="post">
            <span class="octicon octicon-git-branch-create"></span><span class="text">Fork</span>
          </a>
          <a href="/cytoscape/cytoscape.js/network" class="social-count">49</a>
        </li>


</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="repo-label"><span>public</span></span>
          <span class="mega-octicon octicon-repo"></span>
          <span class="author">
            <a href="/cytoscape" class="url fn" itemprop="url" rel="author"><span itemprop="title">cytoscape</span></a></span
          ><span class="repohead-name-divider">/</span><strong
          ><a href="/cytoscape/cytoscape.js" class="js-current-repository js-repo-home-link">cytoscape.js</a></strong>

          <span class="page-context-loader">
            <img alt="Octocat-spinner-32" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">

      <div class="repository-with-sidebar repo-container ">

        <div class="repository-sidebar">
            

<div class="repo-nav repo-nav-full js-repository-container-pjax js-octicon-loaders">
  <div class="repo-nav-contents">
    <ul class="repo-menu">
      <li class="tooltipped leftwards" title="Code">
        <a href="/cytoscape/cytoscape.js" aria-label="Code" class="js-selected-navigation-item selected" data-gotokey="c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_tags repo_branches /cytoscape/cytoscape.js">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

        <li class="tooltipped leftwards" title="Issues">
          <a href="/cytoscape/cytoscape.js/issues" aria-label="Issues" class="js-selected-navigation-item js-disable-pjax" data-gotokey="i" data-selected-links="repo_issues /cytoscape/cytoscape.js/issues">
            <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
            <span class='counter'>34</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>

      <li class="tooltipped leftwards" title="Pull Requests"><a href="/cytoscape/cytoscape.js/pulls" aria-label="Pull Requests" class="js-selected-navigation-item js-disable-pjax" data-gotokey="p" data-selected-links="repo_pulls /cytoscape/cytoscape.js/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class='counter'>0</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


        <li class="tooltipped leftwards" title="Wiki">
          <a href="/cytoscape/cytoscape.js/wiki" aria-label="Wiki" class="js-selected-navigation-item " data-pjax="true" data-selected-links="repo_wiki /cytoscape/cytoscape.js/wiki">
            <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>
    </ul>
    <div class="repo-menu-separator"></div>
    <ul class="repo-menu">

      <li class="tooltipped leftwards" title="Pulse">
        <a href="/cytoscape/cytoscape.js/pulse" aria-label="Pulse" class="js-selected-navigation-item " data-pjax="true" data-selected-links="pulse /cytoscape/cytoscape.js/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Graphs">
        <a href="/cytoscape/cytoscape.js/graphs" aria-label="Graphs" class="js-selected-navigation-item " data-pjax="true" data-selected-links="repo_graphs repo_contributors /cytoscape/cytoscape.js/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Network">
        <a href="/cytoscape/cytoscape.js/network" aria-label="Network" class="js-selected-navigation-item js-disable-pjax" data-selected-links="repo_network /cytoscape/cytoscape.js/network">
          <span class="octicon octicon-git-branch"></span> <span class="full-word">Network</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

    </ul>

  </div>
</div>

            <div class="only-with-full-nav">
              

  

<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><strong>HTTPS</strong> clone URL</h3>

  <input type="text" class="clone js-url-field"
         value="https://github.com/cytoscape/cytoscape.js.git" readonly="readonly">

  <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/cytoscape/cytoscape.js.git" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
</div>

  

<div class="clone-url "
  data-protocol-type="ssh"
  data-url="/users/set_protocol?protocol_selector=ssh&amp;protocol_type=clone">
  <h3><strong>SSH</strong> clone URL</h3>

  <input type="text" class="clone js-url-field"
         value="git@github.com:cytoscape/cytoscape.js.git" readonly="readonly">

  <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="git@github.com:cytoscape/cytoscape.js.git" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><strong>Subversion</strong> checkout URL</h3>

  <input type="text" class="clone js-url-field"
         value="https://github.com/cytoscape/cytoscape.js" readonly="readonly">

  <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/cytoscape/cytoscape.js" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
</div>



<p class="clone-options">You can clone with
    <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>,
    <a href="#" class="js-clone-selector" data-protocol="ssh">SSH</a>,
    <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>,
  and <a href="https://help.github.com/articles/which-remote-url-should-i-use">other methods.</a>
</p>


  <a href="http://windows.github.com" class="minibutton sidebar-button">
    <span class="octicon octicon-device-desktop"></span>
    Clone in Desktop
  </a>

                <a href="/cytoscape/cytoscape.js/archive/master.zip"
                   class="minibutton sidebar-button"
                   title="Download this repository as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
            </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:391b4cd835be78f1fd4b1f627390a339 -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:391b4cd835be78f1fd4b1f627390a339 -->

<p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

<a href="/cytoscape/cytoscape.js/find/master" data-pjax data-hotkey="t" style="display:none">Show File Finder</a>

<div class="file-navigation">
  


<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target" data-hotkey="w"
    data-master-branch="master"
    data-ref="master">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-remove-close js-menu-close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/cytoscape/cytoscape.js/blob/gh-pages/src/plugins/jquery.cytoscape-panzoom.js" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="gh-pages" data-skip-pjax="true" rel="nofollow" title="gh-pages">gh-pages</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/cytoscape/cytoscape.js/blob/master/src/plugins/jquery.cytoscape-panzoom.js" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="master" data-skip-pjax="true" rel="nofollow" title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/cytoscape/cytoscape.js/blob/v2.0.2/src/plugins/jquery.cytoscape-panzoom.js" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="v2.0.2" data-skip-pjax="true" rel="nofollow" title="v2.0.2">v2.0.2</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/cytoscape/cytoscape.js/blob/v2.0.1/src/plugins/jquery.cytoscape-panzoom.js" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="v2.0.1" data-skip-pjax="true" rel="nofollow" title="v2.0.1">v2.0.1</a>
            </div> <!-- /.select-menu-item -->
        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/cytoscape/cytoscape.js" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">cytoscape.js</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/cytoscape/cytoscape.js/tree/master/src" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">src</span></a></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/cytoscape/cytoscape.js/tree/master/src/plugins" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">plugins</span></a></span><span class="separator"> / </span><strong class="final-path">jquery.cytoscape-panzoom.js</strong> <span class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="src/plugins/jquery.cytoscape-panzoom.js" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>


  
  <div class="commit file-history-tease">
    <img class="main-avatar" height="24" src="https://secure.gravatar.com/avatar/4bbad4ebb2a8dc06bf3c01959db6b2fa?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
    <span class="author"><a href="/maxkfranz" rel="author">maxkfranz</a></span>
    <time class="js-relative-date" datetime="2013-08-01T12:46:42-07:00" title="2013-08-01 12:46:42">August 01, 2013</time>
    <div class="commit-title">
        <a href="/cytoscape/cytoscape.js/commit/0c536074c97a2f5a4ff0488c3b4f4e22149b6f0e" class="message" data-pjax="true" title="fix #302 (fit issue)">fix</a> <a href="https://github.com/cytoscape/cytoscape.js/issues/302" class="issue-link" title="Fit on panzoom is broken">#302</a> <a href="/cytoscape/cytoscape.js/commit/0c536074c97a2f5a4ff0488c3b4f4e22149b6f0e" class="message" data-pjax="true" title="fix #302 (fit issue)">(fit issue)</a>
    </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>2</strong> contributors</a></p>
          <a class="avatar tooltipped downwards" title="maxkfranz" href="/cytoscape/cytoscape.js/commits/master/src/plugins/jquery.cytoscape-panzoom.js?author=maxkfranz"><img height="20" src="https://secure.gravatar.com/avatar/4bbad4ebb2a8dc06bf3c01959db6b2fa?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>
    <a class="avatar tooltipped downwards" title="yuedong2" href="/cytoscape/cytoscape.js/commits/master/src/plugins/jquery.cytoscape-panzoom.js?author=yuedong2"><img height="20" src="https://secure.gravatar.com/avatar/10c1ab926a4df33ea21ebe87983e61f2?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>


    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
        <li class="facebox-user-list-item">
          <img height="24" src="https://secure.gravatar.com/avatar/4bbad4ebb2a8dc06bf3c01959db6b2fa?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/maxkfranz">maxkfranz</a>
        </li>
        <li class="facebox-user-list-item">
          <img height="24" src="https://secure.gravatar.com/avatar/10c1ab926a4df33ea21ebe87983e61f2?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/yuedong2">yuedong2</a>
        </li>
      </ul>
    </div>
  </div>


<div id="files" class="bubble">
  <div class="file">
    <div class="meta">
      <div class="info">
        <span class="icon"><b class="octicon octicon-file-text"></b></span>
        <span class="mode" title="File Mode">file</span>
          <span>461 lines (347 sloc)</span>
        <span>13.04 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
                <a class="minibutton tooltipped leftwards"
                   title="Clicking this button will automatically fork this project so you can edit the file"
                   href="/cytoscape/cytoscape.js/edit/master/src/plugins/jquery.cytoscape-panzoom.js"
                   data-method="post" rel="nofollow">Edit</a>
          <a href="/cytoscape/cytoscape.js/raw/master/src/plugins/jquery.cytoscape-panzoom.js" class="button minibutton " id="raw-url">Raw</a>
            <a href="/cytoscape/cytoscape.js/blame/master/src/plugins/jquery.cytoscape-panzoom.js" class="button minibutton ">Blame</a>
          <a href="/cytoscape/cytoscape.js/commits/master/src/plugins/jquery.cytoscape-panzoom.js" class="button minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->
            <a class="minibutton danger empty-icon tooltipped downwards"
               href="/cytoscape/cytoscape.js/delete/master/src/plugins/jquery.cytoscape-panzoom.js"
               title="Fork this project and delete file" data-method="post" rel="nofollow">
            Delete
          </a>
      </div><!-- /.actions -->

    </div>
        <div class="blob-wrapper data type-javascript js-blob-data">
      <table class="file-code file-diff">
        <tr class="file-code-line">
          <td class="blob-line-nums">
            <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>
<span id="L199" rel="#L199">199</span>
<span id="L200" rel="#L200">200</span>
<span id="L201" rel="#L201">201</span>
<span id="L202" rel="#L202">202</span>
<span id="L203" rel="#L203">203</span>
<span id="L204" rel="#L204">204</span>
<span id="L205" rel="#L205">205</span>
<span id="L206" rel="#L206">206</span>
<span id="L207" rel="#L207">207</span>
<span id="L208" rel="#L208">208</span>
<span id="L209" rel="#L209">209</span>
<span id="L210" rel="#L210">210</span>
<span id="L211" rel="#L211">211</span>
<span id="L212" rel="#L212">212</span>
<span id="L213" rel="#L213">213</span>
<span id="L214" rel="#L214">214</span>
<span id="L215" rel="#L215">215</span>
<span id="L216" rel="#L216">216</span>
<span id="L217" rel="#L217">217</span>
<span id="L218" rel="#L218">218</span>
<span id="L219" rel="#L219">219</span>
<span id="L220" rel="#L220">220</span>
<span id="L221" rel="#L221">221</span>
<span id="L222" rel="#L222">222</span>
<span id="L223" rel="#L223">223</span>
<span id="L224" rel="#L224">224</span>
<span id="L225" rel="#L225">225</span>
<span id="L226" rel="#L226">226</span>
<span id="L227" rel="#L227">227</span>
<span id="L228" rel="#L228">228</span>
<span id="L229" rel="#L229">229</span>
<span id="L230" rel="#L230">230</span>
<span id="L231" rel="#L231">231</span>
<span id="L232" rel="#L232">232</span>
<span id="L233" rel="#L233">233</span>
<span id="L234" rel="#L234">234</span>
<span id="L235" rel="#L235">235</span>
<span id="L236" rel="#L236">236</span>
<span id="L237" rel="#L237">237</span>
<span id="L238" rel="#L238">238</span>
<span id="L239" rel="#L239">239</span>
<span id="L240" rel="#L240">240</span>
<span id="L241" rel="#L241">241</span>
<span id="L242" rel="#L242">242</span>
<span id="L243" rel="#L243">243</span>
<span id="L244" rel="#L244">244</span>
<span id="L245" rel="#L245">245</span>
<span id="L246" rel="#L246">246</span>
<span id="L247" rel="#L247">247</span>
<span id="L248" rel="#L248">248</span>
<span id="L249" rel="#L249">249</span>
<span id="L250" rel="#L250">250</span>
<span id="L251" rel="#L251">251</span>
<span id="L252" rel="#L252">252</span>
<span id="L253" rel="#L253">253</span>
<span id="L254" rel="#L254">254</span>
<span id="L255" rel="#L255">255</span>
<span id="L256" rel="#L256">256</span>
<span id="L257" rel="#L257">257</span>
<span id="L258" rel="#L258">258</span>
<span id="L259" rel="#L259">259</span>
<span id="L260" rel="#L260">260</span>
<span id="L261" rel="#L261">261</span>
<span id="L262" rel="#L262">262</span>
<span id="L263" rel="#L263">263</span>
<span id="L264" rel="#L264">264</span>
<span id="L265" rel="#L265">265</span>
<span id="L266" rel="#L266">266</span>
<span id="L267" rel="#L267">267</span>
<span id="L268" rel="#L268">268</span>
<span id="L269" rel="#L269">269</span>
<span id="L270" rel="#L270">270</span>
<span id="L271" rel="#L271">271</span>
<span id="L272" rel="#L272">272</span>
<span id="L273" rel="#L273">273</span>
<span id="L274" rel="#L274">274</span>
<span id="L275" rel="#L275">275</span>
<span id="L276" rel="#L276">276</span>
<span id="L277" rel="#L277">277</span>
<span id="L278" rel="#L278">278</span>
<span id="L279" rel="#L279">279</span>
<span id="L280" rel="#L280">280</span>
<span id="L281" rel="#L281">281</span>
<span id="L282" rel="#L282">282</span>
<span id="L283" rel="#L283">283</span>
<span id="L284" rel="#L284">284</span>
<span id="L285" rel="#L285">285</span>
<span id="L286" rel="#L286">286</span>
<span id="L287" rel="#L287">287</span>
<span id="L288" rel="#L288">288</span>
<span id="L289" rel="#L289">289</span>
<span id="L290" rel="#L290">290</span>
<span id="L291" rel="#L291">291</span>
<span id="L292" rel="#L292">292</span>
<span id="L293" rel="#L293">293</span>
<span id="L294" rel="#L294">294</span>
<span id="L295" rel="#L295">295</span>
<span id="L296" rel="#L296">296</span>
<span id="L297" rel="#L297">297</span>
<span id="L298" rel="#L298">298</span>
<span id="L299" rel="#L299">299</span>
<span id="L300" rel="#L300">300</span>
<span id="L301" rel="#L301">301</span>
<span id="L302" rel="#L302">302</span>
<span id="L303" rel="#L303">303</span>
<span id="L304" rel="#L304">304</span>
<span id="L305" rel="#L305">305</span>
<span id="L306" rel="#L306">306</span>
<span id="L307" rel="#L307">307</span>
<span id="L308" rel="#L308">308</span>
<span id="L309" rel="#L309">309</span>
<span id="L310" rel="#L310">310</span>
<span id="L311" rel="#L311">311</span>
<span id="L312" rel="#L312">312</span>
<span id="L313" rel="#L313">313</span>
<span id="L314" rel="#L314">314</span>
<span id="L315" rel="#L315">315</span>
<span id="L316" rel="#L316">316</span>
<span id="L317" rel="#L317">317</span>
<span id="L318" rel="#L318">318</span>
<span id="L319" rel="#L319">319</span>
<span id="L320" rel="#L320">320</span>
<span id="L321" rel="#L321">321</span>
<span id="L322" rel="#L322">322</span>
<span id="L323" rel="#L323">323</span>
<span id="L324" rel="#L324">324</span>
<span id="L325" rel="#L325">325</span>
<span id="L326" rel="#L326">326</span>
<span id="L327" rel="#L327">327</span>
<span id="L328" rel="#L328">328</span>
<span id="L329" rel="#L329">329</span>
<span id="L330" rel="#L330">330</span>
<span id="L331" rel="#L331">331</span>
<span id="L332" rel="#L332">332</span>
<span id="L333" rel="#L333">333</span>
<span id="L334" rel="#L334">334</span>
<span id="L335" rel="#L335">335</span>
<span id="L336" rel="#L336">336</span>
<span id="L337" rel="#L337">337</span>
<span id="L338" rel="#L338">338</span>
<span id="L339" rel="#L339">339</span>
<span id="L340" rel="#L340">340</span>
<span id="L341" rel="#L341">341</span>
<span id="L342" rel="#L342">342</span>
<span id="L343" rel="#L343">343</span>
<span id="L344" rel="#L344">344</span>
<span id="L345" rel="#L345">345</span>
<span id="L346" rel="#L346">346</span>
<span id="L347" rel="#L347">347</span>
<span id="L348" rel="#L348">348</span>
<span id="L349" rel="#L349">349</span>
<span id="L350" rel="#L350">350</span>
<span id="L351" rel="#L351">351</span>
<span id="L352" rel="#L352">352</span>
<span id="L353" rel="#L353">353</span>
<span id="L354" rel="#L354">354</span>
<span id="L355" rel="#L355">355</span>
<span id="L356" rel="#L356">356</span>
<span id="L357" rel="#L357">357</span>
<span id="L358" rel="#L358">358</span>
<span id="L359" rel="#L359">359</span>
<span id="L360" rel="#L360">360</span>
<span id="L361" rel="#L361">361</span>
<span id="L362" rel="#L362">362</span>
<span id="L363" rel="#L363">363</span>
<span id="L364" rel="#L364">364</span>
<span id="L365" rel="#L365">365</span>
<span id="L366" rel="#L366">366</span>
<span id="L367" rel="#L367">367</span>
<span id="L368" rel="#L368">368</span>
<span id="L369" rel="#L369">369</span>
<span id="L370" rel="#L370">370</span>
<span id="L371" rel="#L371">371</span>
<span id="L372" rel="#L372">372</span>
<span id="L373" rel="#L373">373</span>
<span id="L374" rel="#L374">374</span>
<span id="L375" rel="#L375">375</span>
<span id="L376" rel="#L376">376</span>
<span id="L377" rel="#L377">377</span>
<span id="L378" rel="#L378">378</span>
<span id="L379" rel="#L379">379</span>
<span id="L380" rel="#L380">380</span>
<span id="L381" rel="#L381">381</span>
<span id="L382" rel="#L382">382</span>
<span id="L383" rel="#L383">383</span>
<span id="L384" rel="#L384">384</span>
<span id="L385" rel="#L385">385</span>
<span id="L386" rel="#L386">386</span>
<span id="L387" rel="#L387">387</span>
<span id="L388" rel="#L388">388</span>
<span id="L389" rel="#L389">389</span>
<span id="L390" rel="#L390">390</span>
<span id="L391" rel="#L391">391</span>
<span id="L392" rel="#L392">392</span>
<span id="L393" rel="#L393">393</span>
<span id="L394" rel="#L394">394</span>
<span id="L395" rel="#L395">395</span>
<span id="L396" rel="#L396">396</span>
<span id="L397" rel="#L397">397</span>
<span id="L398" rel="#L398">398</span>
<span id="L399" rel="#L399">399</span>
<span id="L400" rel="#L400">400</span>
<span id="L401" rel="#L401">401</span>
<span id="L402" rel="#L402">402</span>
<span id="L403" rel="#L403">403</span>
<span id="L404" rel="#L404">404</span>
<span id="L405" rel="#L405">405</span>
<span id="L406" rel="#L406">406</span>
<span id="L407" rel="#L407">407</span>
<span id="L408" rel="#L408">408</span>
<span id="L409" rel="#L409">409</span>
<span id="L410" rel="#L410">410</span>
<span id="L411" rel="#L411">411</span>
<span id="L412" rel="#L412">412</span>
<span id="L413" rel="#L413">413</span>
<span id="L414" rel="#L414">414</span>
<span id="L415" rel="#L415">415</span>
<span id="L416" rel="#L416">416</span>
<span id="L417" rel="#L417">417</span>
<span id="L418" rel="#L418">418</span>
<span id="L419" rel="#L419">419</span>
<span id="L420" rel="#L420">420</span>
<span id="L421" rel="#L421">421</span>
<span id="L422" rel="#L422">422</span>
<span id="L423" rel="#L423">423</span>
<span id="L424" rel="#L424">424</span>
<span id="L425" rel="#L425">425</span>
<span id="L426" rel="#L426">426</span>
<span id="L427" rel="#L427">427</span>
<span id="L428" rel="#L428">428</span>
<span id="L429" rel="#L429">429</span>
<span id="L430" rel="#L430">430</span>
<span id="L431" rel="#L431">431</span>
<span id="L432" rel="#L432">432</span>
<span id="L433" rel="#L433">433</span>
<span id="L434" rel="#L434">434</span>
<span id="L435" rel="#L435">435</span>
<span id="L436" rel="#L436">436</span>
<span id="L437" rel="#L437">437</span>
<span id="L438" rel="#L438">438</span>
<span id="L439" rel="#L439">439</span>
<span id="L440" rel="#L440">440</span>
<span id="L441" rel="#L441">441</span>
<span id="L442" rel="#L442">442</span>
<span id="L443" rel="#L443">443</span>
<span id="L444" rel="#L444">444</span>
<span id="L445" rel="#L445">445</span>
<span id="L446" rel="#L446">446</span>
<span id="L447" rel="#L447">447</span>
<span id="L448" rel="#L448">448</span>
<span id="L449" rel="#L449">449</span>
<span id="L450" rel="#L450">450</span>
<span id="L451" rel="#L451">451</span>
<span id="L452" rel="#L452">452</span>
<span id="L453" rel="#L453">453</span>
<span id="L454" rel="#L454">454</span>
<span id="L455" rel="#L455">455</span>
<span id="L456" rel="#L456">456</span>
<span id="L457" rel="#L457">457</span>
<span id="L458" rel="#L458">458</span>
<span id="L459" rel="#L459">459</span>
<span id="L460" rel="#L460">460</span>
<span id="L461" rel="#L461">461</span>

          </td>
          <td class="blob-line-code">
                  <div class="highlight"><pre><div class='line' id='LC1'><span class="p">;(</span><span class="kd">function</span><span class="p">(</span><span class="nx">$</span><span class="p">){</span></div><div class='line' id='LC2'><br/></div><div class='line' id='LC3'>	<span class="kd">var</span> <span class="nx">defaults</span> <span class="o">=</span> <span class="p">{</span></div><div class='line' id='LC4'>		<span class="nx">zoomFactor</span><span class="o">:</span> <span class="mf">0.05</span><span class="p">,</span> <span class="c1">// zoom factor per zoom tick</span></div><div class='line' id='LC5'>		<span class="nx">zoomDelay</span><span class="o">:</span> <span class="mi">45</span><span class="p">,</span> <span class="c1">// how many ms between zoom ticks</span></div><div class='line' id='LC6'>		<span class="nx">minZoom</span><span class="o">:</span> <span class="mf">0.1</span><span class="p">,</span> <span class="c1">// min zoom level</span></div><div class='line' id='LC7'>		<span class="nx">maxZoom</span><span class="o">:</span> <span class="mi">10</span><span class="p">,</span> <span class="c1">// max zoom level</span></div><div class='line' id='LC8'>		<span class="nx">fitPadding</span><span class="o">:</span> <span class="mi">50</span><span class="p">,</span> <span class="c1">// padding when fitting</span></div><div class='line' id='LC9'>		<span class="nx">panSpeed</span><span class="o">:</span> <span class="mi">10</span><span class="p">,</span> <span class="c1">// how many ms in between pan ticks</span></div><div class='line' id='LC10'>		<span class="nx">panDistance</span><span class="o">:</span> <span class="mi">10</span><span class="p">,</span> <span class="c1">// max pan distance per tick</span></div><div class='line' id='LC11'>		<span class="nx">panDragAreaSize</span><span class="o">:</span> <span class="mi">75</span><span class="p">,</span> <span class="c1">// the length of the pan drag box in which the vector for panning is calculated (bigger = finer control of pan speed and direction)</span></div><div class='line' id='LC12'>		<span class="nx">panMinPercentSpeed</span><span class="o">:</span> <span class="mf">0.25</span><span class="p">,</span> <span class="c1">// the slowest speed we can pan by (as a percent of panSpeed)</span></div><div class='line' id='LC13'>		<span class="nx">panInactiveArea</span><span class="o">:</span> <span class="mi">8</span><span class="p">,</span> <span class="c1">// radius of inactive area in pan drag box</span></div><div class='line' id='LC14'>		<span class="nx">panIndicatorMinOpacity</span><span class="o">:</span> <span class="mf">0.5</span><span class="p">,</span> <span class="c1">// min opacity of pan indicator (the draggable nib); scales from this to 1.0</span></div><div class='line' id='LC15'>		<span class="nx">autodisableForMobile</span><span class="o">:</span> <span class="kc">true</span><span class="p">,</span> <span class="c1">// disable the panzoom completely for mobile (since we don&#39;t really need it with gestures like pinch to zoom)</span></div><div class='line' id='LC16'>		<span class="nx">sliderHandleIcon</span><span class="o">:</span> <span class="s1">&#39;icon-minus&#39;</span><span class="p">,</span></div><div class='line' id='LC17'>		<span class="nx">zoomInIcon</span><span class="o">:</span> <span class="s1">&#39;icon-plus&#39;</span><span class="p">,</span></div><div class='line' id='LC18'>		<span class="nx">zoomOutIcon</span><span class="o">:</span> <span class="s1">&#39;icon-minus&#39;</span><span class="p">,</span></div><div class='line' id='LC19'>		<span class="nx">resetIcon</span><span class="o">:</span> <span class="s1">&#39;icon-resize-full&#39;</span></div><div class='line' id='LC20'>	<span class="p">};</span></div><div class='line' id='LC21'><br/></div><div class='line' id='LC22'>	<span class="nx">$</span><span class="p">.</span><span class="nx">fn</span><span class="p">.</span><span class="nx">cytoscapePanzoom</span> <span class="o">=</span> <span class="kd">function</span><span class="p">(</span><span class="nx">params</span><span class="p">){</span></div><div class='line' id='LC23'>		<span class="kd">var</span> <span class="nx">options</span> <span class="o">=</span> <span class="nx">$</span><span class="p">.</span><span class="nx">extend</span><span class="p">(</span><span class="kc">true</span><span class="p">,</span> <span class="p">{},</span> <span class="nx">defaults</span><span class="p">,</span> <span class="nx">params</span><span class="p">);</span></div><div class='line' id='LC24'>		<span class="kd">var</span> <span class="nx">fn</span> <span class="o">=</span> <span class="nx">params</span><span class="p">;</span></div><div class='line' id='LC25'><br/></div><div class='line' id='LC26'>		<span class="kd">var</span> <span class="nx">functions</span> <span class="o">=</span> <span class="p">{</span></div><div class='line' id='LC27'>			<span class="nx">destroy</span><span class="o">:</span> <span class="kd">function</span><span class="p">(){</span></div><div class='line' id='LC28'>				<span class="kd">var</span> <span class="nx">$this</span> <span class="o">=</span> <span class="nx">$</span><span class="p">(</span><span class="k">this</span><span class="p">);</span></div><div class='line' id='LC29'><br/></div><div class='line' id='LC30'>				<span class="nx">$this</span><span class="p">.</span><span class="nx">find</span><span class="p">(</span><span class="s2">&quot;.ui-cytoscape-panzoom&quot;</span><span class="p">).</span><span class="nx">remove</span><span class="p">();</span></div><div class='line' id='LC31'>			<span class="p">},</span></div><div class='line' id='LC32'><br/></div><div class='line' id='LC33'>			<span class="nx">init</span><span class="o">:</span> <span class="kd">function</span><span class="p">(){</span></div><div class='line' id='LC34'>				<span class="kd">var</span> <span class="nx">browserIsMobile</span> <span class="o">=</span> <span class="s1">&#39;ontouchstart&#39;</span> <span class="k">in</span> <span class="nb">window</span><span class="p">;</span></div><div class='line' id='LC35'><br/></div><div class='line' id='LC36'>				<span class="k">if</span><span class="p">(</span> <span class="nx">browserIsMobile</span> <span class="o">&amp;&amp;</span> <span class="nx">options</span><span class="p">.</span><span class="nx">autodisableForMobile</span> <span class="p">){</span></div><div class='line' id='LC37'>					<span class="k">return</span> <span class="nx">$</span><span class="p">(</span><span class="k">this</span><span class="p">);</span></div><div class='line' id='LC38'>				<span class="p">}</span></div><div class='line' id='LC39'><br/></div><div class='line' id='LC40'>				<span class="k">return</span> <span class="nx">$</span><span class="p">(</span><span class="k">this</span><span class="p">).</span><span class="nx">each</span><span class="p">(</span><span class="kd">function</span><span class="p">(){</span></div><div class='line' id='LC41'>					<span class="kd">var</span> <span class="nx">$container</span> <span class="o">=</span> <span class="nx">$</span><span class="p">(</span><span class="k">this</span><span class="p">);</span></div><div class='line' id='LC42'><br/></div><div class='line' id='LC43'>					<span class="kd">var</span> <span class="nx">$panzoom</span> <span class="o">=</span> <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;&lt;div class=&quot;ui-cytoscape-panzoom&quot;&gt;&lt;/div&gt;&#39;</span><span class="p">);</span></div><div class='line' id='LC44'>					<span class="nx">$container</span><span class="p">.</span><span class="nx">append</span><span class="p">(</span> <span class="nx">$panzoom</span> <span class="p">);</span></div><div class='line' id='LC45'><br/></div><div class='line' id='LC46'>					<span class="k">if</span><span class="p">(</span> <span class="nx">options</span><span class="p">.</span><span class="nx">staticPosition</span> <span class="p">){</span></div><div class='line' id='LC47'>						<span class="nx">$panzoom</span><span class="p">.</span><span class="nx">addClass</span><span class="p">(</span><span class="s2">&quot;ui-cytoscape-panzoom-static&quot;</span><span class="p">);</span></div><div class='line' id='LC48'>					<span class="p">}</span></div><div class='line' id='LC49'><br/></div><div class='line' id='LC50'>					<span class="c1">// add base html elements</span></div><div class='line' id='LC51'>					<span class="c1">/////////////////////////</span></div><div class='line' id='LC52'><br/></div><div class='line' id='LC53'>					<span class="kd">var</span> <span class="nx">$zoomIn</span> <span class="o">=</span> <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;&lt;div class=&quot;ui-cytoscape-panzoom-zoom-in ui-cytoscape-panzoom-zoom-button&quot;&gt;&lt;span class=&quot;icon &#39;</span><span class="o">+</span> <span class="nx">options</span><span class="p">.</span><span class="nx">zoomInIcon</span> <span class="o">+</span><span class="s1">&#39;&quot;&gt;&lt;/span&gt;&lt;/div&gt;&#39;</span><span class="p">);</span></div><div class='line' id='LC54'>					<span class="nx">$panzoom</span><span class="p">.</span><span class="nx">append</span><span class="p">(</span> <span class="nx">$zoomIn</span> <span class="p">);</span></div><div class='line' id='LC55'><br/></div><div class='line' id='LC56'>					<span class="kd">var</span> <span class="nx">$zoomOut</span> <span class="o">=</span> <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;&lt;div class=&quot;ui-cytoscape-panzoom-zoom-out ui-cytoscape-panzoom-zoom-button&quot;&gt;&lt;span class=&quot;icon &#39;</span> <span class="o">+</span> <span class="nx">options</span><span class="p">.</span><span class="nx">zoomOutIcon</span> <span class="o">+</span> <span class="s1">&#39;&quot;&gt;&lt;/span&gt;&lt;/div&gt;&#39;</span><span class="p">);</span></div><div class='line' id='LC57'>					<span class="nx">$panzoom</span><span class="p">.</span><span class="nx">append</span><span class="p">(</span> <span class="nx">$zoomOut</span> <span class="p">);</span></div><div class='line' id='LC58'><br/></div><div class='line' id='LC59'>					<span class="kd">var</span> <span class="nx">$reset</span> <span class="o">=</span> <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;&lt;div class=&quot;ui-cytoscape-panzoom-reset ui-cytoscape-panzoom-zoom-button&quot;&gt;&lt;span class=&quot;icon &#39;</span> <span class="o">+</span> <span class="nx">options</span><span class="p">.</span><span class="nx">resetIcon</span> <span class="o">+</span> <span class="s1">&#39;&quot;&gt;&lt;/span&gt;&lt;/div&gt;&#39;</span><span class="p">);</span></div><div class='line' id='LC60'>					<span class="nx">$panzoom</span><span class="p">.</span><span class="nx">append</span><span class="p">(</span> <span class="nx">$reset</span> <span class="p">);</span></div><div class='line' id='LC61'><br/></div><div class='line' id='LC62'>					<span class="kd">var</span> <span class="nx">$slider</span> <span class="o">=</span> <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;&lt;div class=&quot;ui-cytoscape-panzoom-slider&quot;&gt;&lt;/div&gt;&#39;</span><span class="p">);</span></div><div class='line' id='LC63'>					<span class="nx">$panzoom</span><span class="p">.</span><span class="nx">append</span><span class="p">(</span> <span class="nx">$slider</span> <span class="p">);</span></div><div class='line' id='LC64'><br/></div><div class='line' id='LC65'>					<span class="nx">$slider</span><span class="p">.</span><span class="nx">append</span><span class="p">(</span><span class="s1">&#39;&lt;div class=&quot;ui-cytoscape-panzoom-slider-background&quot;&gt;&lt;/div&gt;&#39;</span><span class="p">);</span></div><div class='line' id='LC66'><br/></div><div class='line' id='LC67'>					<span class="kd">var</span> <span class="nx">$sliderHandle</span> <span class="o">=</span> <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;&lt;div class=&quot;ui-cytoscape-panzoom-slider-handle&quot;&gt;&lt;span class=&quot;icon &#39;</span> <span class="o">+</span> <span class="nx">options</span><span class="p">.</span><span class="nx">sliderHandleIcon</span> <span class="o">+</span> <span class="s1">&#39;&quot;&gt;&lt;/span&gt;&lt;/div&gt;&#39;</span><span class="p">);</span></div><div class='line' id='LC68'>					<span class="nx">$slider</span><span class="p">.</span><span class="nx">append</span><span class="p">(</span> <span class="nx">$sliderHandle</span> <span class="p">);</span></div><div class='line' id='LC69'><br/></div><div class='line' id='LC70'>					<span class="kd">var</span> <span class="nx">$noZoomTick</span> <span class="o">=</span> <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;&lt;div class=&quot;ui-cytoscape-panzoom-no-zoom-tick&quot;&gt;&lt;/div&gt;&#39;</span><span class="p">);</span></div><div class='line' id='LC71'>					<span class="nx">$slider</span><span class="p">.</span><span class="nx">append</span><span class="p">(</span> <span class="nx">$noZoomTick</span> <span class="p">);</span></div><div class='line' id='LC72'><br/></div><div class='line' id='LC73'>					<span class="kd">var</span> <span class="nx">$panner</span> <span class="o">=</span> <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;&lt;div class=&quot;ui-cytoscape-panzoom-panner&quot;&gt;&lt;/div&gt;&#39;</span><span class="p">);</span></div><div class='line' id='LC74'>					<span class="nx">$panzoom</span><span class="p">.</span><span class="nx">append</span><span class="p">(</span> <span class="nx">$panner</span> <span class="p">);</span></div><div class='line' id='LC75'><br/></div><div class='line' id='LC76'>					<span class="kd">var</span> <span class="nx">$pHandle</span> <span class="o">=</span> <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;&lt;div class=&quot;ui-cytoscape-panzoom-panner-handle&quot;&gt;&lt;/div&gt;&#39;</span><span class="p">);</span></div><div class='line' id='LC77'>					<span class="nx">$panner</span><span class="p">.</span><span class="nx">append</span><span class="p">(</span> <span class="nx">$pHandle</span> <span class="p">);</span></div><div class='line' id='LC78'><br/></div><div class='line' id='LC79'>					<span class="kd">var</span> <span class="nx">$pUp</span> <span class="o">=</span> <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;&lt;div class=&quot;ui-cytoscape-panzoom-pan-up ui-cytoscape-panzoom-pan-button&quot;&gt;&lt;/div&gt;&#39;</span><span class="p">);</span></div><div class='line' id='LC80'>					<span class="kd">var</span> <span class="nx">$pDown</span> <span class="o">=</span> <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;&lt;div class=&quot;ui-cytoscape-panzoom-pan-down ui-cytoscape-panzoom-pan-button&quot;&gt;&lt;/div&gt;&#39;</span><span class="p">);</span></div><div class='line' id='LC81'>					<span class="kd">var</span> <span class="nx">$pLeft</span> <span class="o">=</span> <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;&lt;div class=&quot;ui-cytoscape-panzoom-pan-left ui-cytoscape-panzoom-pan-button&quot;&gt;&lt;/div&gt;&#39;</span><span class="p">);</span></div><div class='line' id='LC82'>					<span class="kd">var</span> <span class="nx">$pRight</span> <span class="o">=</span> <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;&lt;div class=&quot;ui-cytoscape-panzoom-pan-right ui-cytoscape-panzoom-pan-button&quot;&gt;&lt;/div&gt;&#39;</span><span class="p">);</span></div><div class='line' id='LC83'>					<span class="nx">$panner</span><span class="p">.</span><span class="nx">append</span><span class="p">(</span> <span class="nx">$pUp</span> <span class="p">).</span><span class="nx">append</span><span class="p">(</span> <span class="nx">$pDown</span> <span class="p">).</span><span class="nx">append</span><span class="p">(</span> <span class="nx">$pLeft</span> <span class="p">).</span><span class="nx">append</span><span class="p">(</span> <span class="nx">$pRight</span> <span class="p">);</span></div><div class='line' id='LC84'><br/></div><div class='line' id='LC85'>					<span class="kd">var</span> <span class="nx">$pIndicator</span> <span class="o">=</span> <span class="nx">$</span><span class="p">(</span><span class="s1">&#39;&lt;div class=&quot;ui-cytoscape-panzoom-pan-indicator&quot;&gt;&lt;/div&gt;&#39;</span><span class="p">);</span></div><div class='line' id='LC86'>					<span class="nx">$panner</span><span class="p">.</span><span class="nx">append</span><span class="p">(</span> <span class="nx">$pIndicator</span> <span class="p">);</span></div><div class='line' id='LC87'><br/></div><div class='line' id='LC88'>					<span class="c1">// functions for calculating panning</span></div><div class='line' id='LC89'>					<span class="c1">////////////////////////////////////</span></div><div class='line' id='LC90'><br/></div><div class='line' id='LC91'>					<span class="kd">function</span> <span class="nx">handle2pan</span><span class="p">(</span><span class="nx">e</span><span class="p">){</span></div><div class='line' id='LC92'>						<span class="kd">var</span> <span class="nx">v</span> <span class="o">=</span> <span class="p">{</span></div><div class='line' id='LC93'>							<span class="nx">x</span><span class="o">:</span> <span class="nx">e</span><span class="p">.</span><span class="nx">originalEvent</span><span class="p">.</span><span class="nx">pageX</span> <span class="o">-</span> <span class="nx">$panner</span><span class="p">.</span><span class="nx">offset</span><span class="p">().</span><span class="nx">left</span> <span class="o">-</span> <span class="nx">$panner</span><span class="p">.</span><span class="nx">width</span><span class="p">()</span><span class="o">/</span><span class="mi">2</span><span class="p">,</span></div><div class='line' id='LC94'>							<span class="nx">y</span><span class="o">:</span> <span class="nx">e</span><span class="p">.</span><span class="nx">originalEvent</span><span class="p">.</span><span class="nx">pageY</span> <span class="o">-</span> <span class="nx">$panner</span><span class="p">.</span><span class="nx">offset</span><span class="p">().</span><span class="nx">top</span> <span class="o">-</span> <span class="nx">$panner</span><span class="p">.</span><span class="nx">height</span><span class="p">()</span><span class="o">/</span><span class="mi">2</span></div><div class='line' id='LC95'>						<span class="p">}</span></div><div class='line' id='LC96'><br/></div><div class='line' id='LC97'>						<span class="kd">var</span> <span class="nx">r</span> <span class="o">=</span> <span class="nx">options</span><span class="p">.</span><span class="nx">panDragAreaSize</span><span class="p">;</span></div><div class='line' id='LC98'>						<span class="kd">var</span> <span class="nx">d</span> <span class="o">=</span> <span class="nb">Math</span><span class="p">.</span><span class="nx">sqrt</span><span class="p">(</span> <span class="nx">v</span><span class="p">.</span><span class="nx">x</span><span class="o">*</span><span class="nx">v</span><span class="p">.</span><span class="nx">x</span> <span class="o">+</span> <span class="nx">v</span><span class="p">.</span><span class="nx">y</span><span class="o">*</span><span class="nx">v</span><span class="p">.</span><span class="nx">y</span> <span class="p">);</span></div><div class='line' id='LC99'>						<span class="kd">var</span> <span class="nx">percent</span> <span class="o">=</span> <span class="nb">Math</span><span class="p">.</span><span class="nx">min</span><span class="p">(</span> <span class="nx">d</span><span class="o">/</span><span class="nx">r</span><span class="p">,</span> <span class="mi">1</span> <span class="p">);</span></div><div class='line' id='LC100'><br/></div><div class='line' id='LC101'>						<span class="k">if</span><span class="p">(</span> <span class="nx">d</span> <span class="o">&lt;</span> <span class="nx">options</span><span class="p">.</span><span class="nx">panInactiveArea</span> <span class="p">){</span></div><div class='line' id='LC102'>							<span class="k">return</span> <span class="p">{</span></div><div class='line' id='LC103'>								<span class="nx">x</span><span class="o">:</span> <span class="kc">NaN</span><span class="p">,</span></div><div class='line' id='LC104'>								<span class="nx">y</span><span class="o">:</span> <span class="kc">NaN</span></div><div class='line' id='LC105'>							<span class="p">};</span></div><div class='line' id='LC106'>						<span class="p">}</span></div><div class='line' id='LC107'><br/></div><div class='line' id='LC108'>						<span class="nx">v</span> <span class="o">=</span> <span class="p">{</span></div><div class='line' id='LC109'>							<span class="nx">x</span><span class="o">:</span> <span class="nx">v</span><span class="p">.</span><span class="nx">x</span><span class="o">/</span><span class="nx">d</span><span class="p">,</span></div><div class='line' id='LC110'>							<span class="nx">y</span><span class="o">:</span> <span class="nx">v</span><span class="p">.</span><span class="nx">y</span><span class="o">/</span><span class="nx">d</span></div><div class='line' id='LC111'>						<span class="p">};</span></div><div class='line' id='LC112'><br/></div><div class='line' id='LC113'>						<span class="nx">percent</span> <span class="o">=</span> <span class="nb">Math</span><span class="p">.</span><span class="nx">max</span><span class="p">(</span> <span class="nx">options</span><span class="p">.</span><span class="nx">panMinPercentSpeed</span><span class="p">,</span> <span class="nx">percent</span> <span class="p">);</span></div><div class='line' id='LC114'><br/></div><div class='line' id='LC115'>						<span class="kd">var</span> <span class="nx">vnorm</span> <span class="o">=</span> <span class="p">{</span></div><div class='line' id='LC116'>							<span class="nx">x</span><span class="o">:</span> <span class="o">-</span><span class="mi">1</span> <span class="o">*</span> <span class="nx">v</span><span class="p">.</span><span class="nx">x</span> <span class="o">*</span> <span class="p">(</span><span class="nx">percent</span> <span class="o">*</span> <span class="nx">options</span><span class="p">.</span><span class="nx">panDistance</span><span class="p">),</span></div><div class='line' id='LC117'>							<span class="nx">y</span><span class="o">:</span> <span class="o">-</span><span class="mi">1</span> <span class="o">*</span> <span class="nx">v</span><span class="p">.</span><span class="nx">y</span> <span class="o">*</span> <span class="p">(</span><span class="nx">percent</span> <span class="o">*</span> <span class="nx">options</span><span class="p">.</span><span class="nx">panDistance</span><span class="p">)</span></div><div class='line' id='LC118'>						<span class="p">};</span></div><div class='line' id='LC119'><br/></div><div class='line' id='LC120'>						<span class="k">return</span> <span class="nx">vnorm</span><span class="p">;</span></div><div class='line' id='LC121'>					<span class="p">}</span></div><div class='line' id='LC122'><br/></div><div class='line' id='LC123'>					<span class="kd">function</span> <span class="nx">donePanning</span><span class="p">(){</span></div><div class='line' id='LC124'>						<span class="nx">clearInterval</span><span class="p">(</span><span class="nx">panInterval</span><span class="p">);</span></div><div class='line' id='LC125'>						<span class="nx">$</span><span class="p">(</span><span class="nb">window</span><span class="p">).</span><span class="nx">unbind</span><span class="p">(</span><span class="s2">&quot;mousemove&quot;</span><span class="p">,</span> <span class="nx">handler</span><span class="p">);</span></div><div class='line' id='LC126'><br/></div><div class='line' id='LC127'>						<span class="nx">$pIndicator</span><span class="p">.</span><span class="nx">hide</span><span class="p">();</span></div><div class='line' id='LC128'>					<span class="p">}</span></div><div class='line' id='LC129'><br/></div><div class='line' id='LC130'>					<span class="kd">function</span> <span class="nx">positionIndicator</span><span class="p">(</span><span class="nx">pan</span><span class="p">){</span></div><div class='line' id='LC131'>						<span class="kd">var</span> <span class="nx">v</span> <span class="o">=</span> <span class="nx">pan</span><span class="p">;</span></div><div class='line' id='LC132'>						<span class="kd">var</span> <span class="nx">d</span> <span class="o">=</span> <span class="nb">Math</span><span class="p">.</span><span class="nx">sqrt</span><span class="p">(</span> <span class="nx">v</span><span class="p">.</span><span class="nx">x</span><span class="o">*</span><span class="nx">v</span><span class="p">.</span><span class="nx">x</span> <span class="o">+</span> <span class="nx">v</span><span class="p">.</span><span class="nx">y</span><span class="o">*</span><span class="nx">v</span><span class="p">.</span><span class="nx">y</span> <span class="p">);</span></div><div class='line' id='LC133'>						<span class="kd">var</span> <span class="nx">vnorm</span> <span class="o">=</span> <span class="p">{</span></div><div class='line' id='LC134'>							<span class="nx">x</span><span class="o">:</span> <span class="o">-</span><span class="mi">1</span> <span class="o">*</span> <span class="nx">v</span><span class="p">.</span><span class="nx">x</span><span class="o">/</span><span class="nx">d</span><span class="p">,</span></div><div class='line' id='LC135'>							<span class="nx">y</span><span class="o">:</span> <span class="o">-</span><span class="mi">1</span> <span class="o">*</span> <span class="nx">v</span><span class="p">.</span><span class="nx">y</span><span class="o">/</span><span class="nx">d</span></div><div class='line' id='LC136'>						<span class="p">};</span></div><div class='line' id='LC137'><br/></div><div class='line' id='LC138'>						<span class="kd">var</span> <span class="nx">w</span> <span class="o">=</span> <span class="nx">$panner</span><span class="p">.</span><span class="nx">width</span><span class="p">();</span></div><div class='line' id='LC139'>						<span class="kd">var</span> <span class="nx">h</span> <span class="o">=</span> <span class="nx">$panner</span><span class="p">.</span><span class="nx">height</span><span class="p">();</span></div><div class='line' id='LC140'>						<span class="kd">var</span> <span class="nx">percent</span> <span class="o">=</span> <span class="nx">d</span><span class="o">/</span><span class="nx">options</span><span class="p">.</span><span class="nx">panDistance</span><span class="p">;</span></div><div class='line' id='LC141'>						<span class="kd">var</span> <span class="nx">opacity</span> <span class="o">=</span> <span class="nb">Math</span><span class="p">.</span><span class="nx">max</span><span class="p">(</span> <span class="nx">options</span><span class="p">.</span><span class="nx">panIndicatorMinOpacity</span><span class="p">,</span> <span class="nx">percent</span> <span class="p">);</span></div><div class='line' id='LC142'>						<span class="kd">var</span> <span class="nx">color</span> <span class="o">=</span> <span class="mi">255</span> <span class="o">-</span> <span class="nb">Math</span><span class="p">.</span><span class="nx">round</span><span class="p">(</span> <span class="nx">opacity</span> <span class="o">*</span> <span class="mi">255</span> <span class="p">);</span></div><div class='line' id='LC143'><br/></div><div class='line' id='LC144'>						<span class="nx">$pIndicator</span><span class="p">.</span><span class="nx">show</span><span class="p">().</span><span class="nx">css</span><span class="p">({</span></div><div class='line' id='LC145'>							<span class="nx">left</span><span class="o">:</span> <span class="nx">w</span><span class="o">/</span><span class="mi">2</span> <span class="o">*</span> <span class="nx">vnorm</span><span class="p">.</span><span class="nx">x</span> <span class="o">+</span> <span class="nx">w</span><span class="o">/</span><span class="mi">2</span><span class="p">,</span></div><div class='line' id='LC146'>							<span class="nx">top</span><span class="o">:</span> <span class="nx">h</span><span class="o">/</span><span class="mi">2</span> <span class="o">*</span> <span class="nx">vnorm</span><span class="p">.</span><span class="nx">y</span> <span class="o">+</span> <span class="nx">h</span><span class="o">/</span><span class="mi">2</span><span class="p">,</span></div><div class='line' id='LC147'>							<span class="nx">background</span><span class="o">:</span> <span class="s2">&quot;rgb(&quot;</span> <span class="o">+</span> <span class="nx">color</span> <span class="o">+</span> <span class="s2">&quot;, &quot;</span> <span class="o">+</span> <span class="nx">color</span> <span class="o">+</span> <span class="s2">&quot;, &quot;</span> <span class="o">+</span> <span class="nx">color</span> <span class="o">+</span> <span class="s2">&quot;)&quot;</span></div><div class='line' id='LC148'>						<span class="p">});</span></div><div class='line' id='LC149'>					<span class="p">}</span></div><div class='line' id='LC150'><br/></div><div class='line' id='LC151'>					<span class="kd">function</span> <span class="nx">calculateZoomCenterPoint</span><span class="p">(){</span></div><div class='line' id='LC152'>						<span class="kd">var</span> <span class="nx">cy</span> <span class="o">=</span> <span class="nx">$container</span><span class="p">.</span><span class="nx">cytoscape</span><span class="p">(</span><span class="s2">&quot;get&quot;</span><span class="p">);</span></div><div class='line' id='LC153'>						<span class="kd">var</span> <span class="nx">pan</span> <span class="o">=</span> <span class="nx">cy</span><span class="p">.</span><span class="nx">pan</span><span class="p">();</span></div><div class='line' id='LC154'>						<span class="kd">var</span> <span class="nx">zoom</span> <span class="o">=</span> <span class="nx">cy</span><span class="p">.</span><span class="nx">zoom</span><span class="p">();</span></div><div class='line' id='LC155'><br/></div><div class='line' id='LC156'>						<span class="nx">zx</span> <span class="o">=</span> <span class="nx">$container</span><span class="p">.</span><span class="nx">width</span><span class="p">()</span><span class="o">/</span><span class="mi">2</span><span class="p">;</span></div><div class='line' id='LC157'>						<span class="nx">zy</span> <span class="o">=</span> <span class="nx">$container</span><span class="p">.</span><span class="nx">height</span><span class="p">()</span><span class="o">/</span><span class="mi">2</span><span class="p">;</span></div><div class='line' id='LC158'>					<span class="p">}</span></div><div class='line' id='LC159'><br/></div><div class='line' id='LC160'>					<span class="kd">var</span> <span class="nx">zooming</span> <span class="o">=</span> <span class="kc">false</span><span class="p">;</span></div><div class='line' id='LC161'>					<span class="kd">function</span> <span class="nx">startZooming</span><span class="p">(){</span></div><div class='line' id='LC162'>						<span class="nx">zooming</span> <span class="o">=</span> <span class="kc">true</span><span class="p">;</span></div><div class='line' id='LC163'><br/></div><div class='line' id='LC164'>						<span class="nx">calculateZoomCenterPoint</span><span class="p">();</span></div><div class='line' id='LC165'>					<span class="p">}</span></div><div class='line' id='LC166'><br/></div><div class='line' id='LC167'><br/></div><div class='line' id='LC168'>					<span class="kd">function</span> <span class="nx">endZooming</span><span class="p">(){</span></div><div class='line' id='LC169'>						<span class="nx">zooming</span> <span class="o">=</span> <span class="kc">false</span><span class="p">;</span></div><div class='line' id='LC170'>					<span class="p">}</span></div><div class='line' id='LC171'><br/></div><div class='line' id='LC172'>					<span class="kd">var</span> <span class="nx">zx</span><span class="p">,</span> <span class="nx">zy</span><span class="p">;</span></div><div class='line' id='LC173'>					<span class="kd">function</span> <span class="nx">zoomTo</span><span class="p">(</span><span class="nx">level</span><span class="p">){</span></div><div class='line' id='LC174'>						<span class="kd">var</span> <span class="nx">cy</span> <span class="o">=</span> <span class="nx">$container</span><span class="p">.</span><span class="nx">cytoscape</span><span class="p">(</span><span class="s2">&quot;get&quot;</span><span class="p">);</span></div><div class='line' id='LC175'><br/></div><div class='line' id='LC176'>						<span class="k">if</span><span class="p">(</span> <span class="o">!</span><span class="nx">zooming</span> <span class="p">){</span> <span class="c1">// for non-continuous zooming (e.g. click slider at pt)</span></div><div class='line' id='LC177'>							<span class="nx">calculateZoomCenterPoint</span><span class="p">();</span></div><div class='line' id='LC178'>						<span class="p">}</span></div><div class='line' id='LC179'><br/></div><div class='line' id='LC180'>						<span class="nx">cy</span><span class="p">.</span><span class="nx">zoom</span><span class="p">({</span></div><div class='line' id='LC181'>							<span class="nx">level</span><span class="o">:</span> <span class="nx">level</span><span class="p">,</span></div><div class='line' id='LC182'>							<span class="nx">position</span><span class="o">:</span> <span class="p">{</span> <span class="nx">x</span><span class="o">:</span> <span class="nx">zx</span><span class="p">,</span> <span class="nx">y</span><span class="o">:</span> <span class="nx">zy</span> <span class="p">}</span></div><div class='line' id='LC183'>						<span class="p">});</span></div><div class='line' id='LC184'>					<span class="p">}</span></div><div class='line' id='LC185'><br/></div><div class='line' id='LC186'>					<span class="kd">var</span> <span class="nx">panInterval</span><span class="p">;</span></div><div class='line' id='LC187'><br/></div><div class='line' id='LC188'>					<span class="kd">var</span> <span class="nx">handler</span> <span class="o">=</span> <span class="kd">function</span><span class="p">(</span><span class="nx">e</span><span class="p">){</span></div><div class='line' id='LC189'>						<span class="nx">e</span><span class="p">.</span><span class="nx">stopPropagation</span><span class="p">();</span> <span class="c1">// don&#39;t trigger dragging of panzoom</span></div><div class='line' id='LC190'>						<span class="nx">e</span><span class="p">.</span><span class="nx">preventDefault</span><span class="p">();</span> <span class="c1">// don&#39;t cause text selection</span></div><div class='line' id='LC191'>						<span class="nx">clearInterval</span><span class="p">(</span><span class="nx">panInterval</span><span class="p">);</span></div><div class='line' id='LC192'><br/></div><div class='line' id='LC193'>						<span class="kd">var</span> <span class="nx">pan</span> <span class="o">=</span> <span class="nx">handle2pan</span><span class="p">(</span><span class="nx">e</span><span class="p">);</span></div><div class='line' id='LC194'><br/></div><div class='line' id='LC195'>						<span class="k">if</span><span class="p">(</span> <span class="nb">isNaN</span><span class="p">(</span><span class="nx">pan</span><span class="p">.</span><span class="nx">x</span><span class="p">)</span> <span class="o">||</span> <span class="nb">isNaN</span><span class="p">(</span><span class="nx">pan</span><span class="p">.</span><span class="nx">y</span><span class="p">)</span> <span class="p">){</span></div><div class='line' id='LC196'>							<span class="nx">$pIndicator</span><span class="p">.</span><span class="nx">hide</span><span class="p">();</span></div><div class='line' id='LC197'>							<span class="k">return</span><span class="p">;</span></div><div class='line' id='LC198'>						<span class="p">}</span></div><div class='line' id='LC199'><br/></div><div class='line' id='LC200'>						<span class="nx">positionIndicator</span><span class="p">(</span><span class="nx">pan</span><span class="p">);</span></div><div class='line' id='LC201'>						<span class="nx">panInterval</span> <span class="o">=</span> <span class="nx">setInterval</span><span class="p">(</span><span class="kd">function</span><span class="p">(){</span></div><div class='line' id='LC202'>							<span class="nx">$container</span><span class="p">.</span><span class="nx">cytoscape</span><span class="p">(</span><span class="s2">&quot;get&quot;</span><span class="p">).</span><span class="nx">panBy</span><span class="p">(</span><span class="nx">pan</span><span class="p">);</span></div><div class='line' id='LC203'>						<span class="p">},</span> <span class="nx">options</span><span class="p">.</span><span class="nx">panSpeed</span><span class="p">);</span></div><div class='line' id='LC204'>					<span class="p">};</span></div><div class='line' id='LC205'><br/></div><div class='line' id='LC206'>					<span class="nx">$pHandle</span><span class="p">.</span><span class="nx">bind</span><span class="p">(</span><span class="s2">&quot;mousedown&quot;</span><span class="p">,</span> <span class="kd">function</span><span class="p">(</span><span class="nx">e</span><span class="p">){</span></div><div class='line' id='LC207'>						<span class="c1">// handle click of icon</span></div><div class='line' id='LC208'>						<span class="nx">handler</span><span class="p">(</span><span class="nx">e</span><span class="p">);</span></div><div class='line' id='LC209'><br/></div><div class='line' id='LC210'>						<span class="c1">// update on mousemove</span></div><div class='line' id='LC211'>						<span class="nx">$</span><span class="p">(</span><span class="nb">window</span><span class="p">).</span><span class="nx">bind</span><span class="p">(</span><span class="s2">&quot;mousemove&quot;</span><span class="p">,</span> <span class="nx">handler</span><span class="p">);</span></div><div class='line' id='LC212'>					<span class="p">});</span></div><div class='line' id='LC213'><br/></div><div class='line' id='LC214'>					<span class="nx">$pHandle</span><span class="p">.</span><span class="nx">bind</span><span class="p">(</span><span class="s2">&quot;mouseup&quot;</span><span class="p">,</span> <span class="kd">function</span><span class="p">(){</span></div><div class='line' id='LC215'>						<span class="nx">donePanning</span><span class="p">();</span></div><div class='line' id='LC216'>					<span class="p">});</span></div><div class='line' id='LC217'><br/></div><div class='line' id='LC218'>					<span class="nx">$</span><span class="p">(</span><span class="nb">window</span><span class="p">).</span><span class="nx">bind</span><span class="p">(</span><span class="s2">&quot;mouseup blur&quot;</span><span class="p">,</span> <span class="kd">function</span><span class="p">(){</span></div><div class='line' id='LC219'>						<span class="nx">donePanning</span><span class="p">();</span></div><div class='line' id='LC220'>					<span class="p">});</span></div><div class='line' id='LC221'><br/></div><div class='line' id='LC222'><br/></div><div class='line' id='LC223'><br/></div><div class='line' id='LC224'>					<span class="c1">// set up slider behaviour</span></div><div class='line' id='LC225'>					<span class="c1">//////////////////////////</span></div><div class='line' id='LC226'><br/></div><div class='line' id='LC227'>					<span class="nx">$slider</span><span class="p">.</span><span class="nx">bind</span><span class="p">(</span><span class="s1">&#39;mousedown&#39;</span><span class="p">,</span> <span class="kd">function</span><span class="p">(){</span></div><div class='line' id='LC228'>						<span class="k">return</span> <span class="kc">false</span><span class="p">;</span> <span class="c1">// so we don&#39;t pan close to the slider handle</span></div><div class='line' id='LC229'>					<span class="p">});</span></div><div class='line' id='LC230'><br/></div><div class='line' id='LC231'>					<span class="kd">var</span> <span class="nx">sliderVal</span><span class="p">;</span></div><div class='line' id='LC232'>					<span class="kd">var</span> <span class="nx">sliding</span> <span class="o">=</span> <span class="kc">false</span><span class="p">;</span></div><div class='line' id='LC233'>					<span class="kd">var</span> <span class="nx">sliderPadding</span> <span class="o">=</span> <span class="mi">2</span><span class="p">;</span></div><div class='line' id='LC234'><br/></div><div class='line' id='LC235'>					<span class="kd">function</span> <span class="nx">setSliderFromMouse</span><span class="p">(</span><span class="nx">evt</span><span class="p">,</span> <span class="nx">handleOffset</span><span class="p">){</span></div><div class='line' id='LC236'>						<span class="k">if</span><span class="p">(</span> <span class="nx">handleOffset</span> <span class="o">===</span> <span class="kc">undefined</span> <span class="p">){</span></div><div class='line' id='LC237'>							<span class="nx">handleOffset</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span></div><div class='line' id='LC238'>						<span class="p">}</span></div><div class='line' id='LC239'><br/></div><div class='line' id='LC240'>						<span class="kd">var</span> <span class="nx">padding</span> <span class="o">=</span> <span class="nx">sliderPadding</span><span class="p">;</span></div><div class='line' id='LC241'>						<span class="kd">var</span> <span class="nx">min</span> <span class="o">=</span> <span class="mi">0</span> <span class="o">+</span> <span class="nx">padding</span><span class="p">;</span></div><div class='line' id='LC242'>						<span class="kd">var</span> <span class="nx">max</span> <span class="o">=</span> <span class="nx">$slider</span><span class="p">.</span><span class="nx">height</span><span class="p">()</span> <span class="o">-</span> <span class="nx">$sliderHandle</span><span class="p">.</span><span class="nx">height</span><span class="p">()</span> <span class="o">-</span> <span class="mi">2</span><span class="o">*</span><span class="nx">padding</span><span class="p">;</span></div><div class='line' id='LC243'>						<span class="kd">var</span> <span class="nx">top</span> <span class="o">=</span> <span class="nx">evt</span><span class="p">.</span><span class="nx">pageY</span> <span class="o">-</span> <span class="nx">$slider</span><span class="p">.</span><span class="nx">offset</span><span class="p">().</span><span class="nx">top</span> <span class="o">-</span> <span class="nx">handleOffset</span><span class="p">;</span></div><div class='line' id='LC244'><br/></div><div class='line' id='LC245'>						<span class="c1">// constrain to slider bounds</span></div><div class='line' id='LC246'>						<span class="k">if</span><span class="p">(</span> <span class="nx">top</span> <span class="o">&lt;</span> <span class="nx">min</span> <span class="p">){</span> <span class="nx">top</span> <span class="o">=</span> <span class="nx">min</span> <span class="p">}</span></div><div class='line' id='LC247'>						<span class="k">if</span><span class="p">(</span> <span class="nx">top</span> <span class="o">&gt;</span> <span class="nx">max</span> <span class="p">){</span> <span class="nx">top</span> <span class="o">=</span> <span class="nx">max</span> <span class="p">}</span></div><div class='line' id='LC248'><br/></div><div class='line' id='LC249'>						<span class="kd">var</span> <span class="nx">percent</span> <span class="o">=</span> <span class="mi">1</span> <span class="o">-</span> <span class="p">(</span><span class="nx">top</span> <span class="o">-</span> <span class="nx">min</span><span class="p">)</span> <span class="o">/</span> <span class="p">(</span> <span class="nx">max</span> <span class="o">-</span> <span class="nx">min</span> <span class="p">);</span></div><div class='line' id='LC250'><br/></div><div class='line' id='LC251'>						<span class="c1">// move the handle</span></div><div class='line' id='LC252'>						<span class="nx">$sliderHandle</span><span class="p">.</span><span class="nx">css</span><span class="p">(</span><span class="s1">&#39;top&#39;</span><span class="p">,</span> <span class="nx">top</span><span class="p">);</span></div><div class='line' id='LC253'><br/></div><div class='line' id='LC254'>						<span class="kd">var</span> <span class="nx">zmin</span> <span class="o">=</span> <span class="nx">options</span><span class="p">.</span><span class="nx">minZoom</span><span class="p">;</span></div><div class='line' id='LC255'>						<span class="kd">var</span> <span class="nx">zmax</span> <span class="o">=</span> <span class="nx">options</span><span class="p">.</span><span class="nx">maxZoom</span><span class="p">;</span></div><div class='line' id='LC256'><br/></div><div class='line' id='LC257'>						<span class="c1">// assume (zoom = zmax ^ p) where p ranges on (x, 1) with x negative</span></div><div class='line' id='LC258'>						<span class="kd">var</span> <span class="nx">x</span> <span class="o">=</span> <span class="nb">Math</span><span class="p">.</span><span class="nx">log</span><span class="p">(</span><span class="nx">zmin</span><span class="p">)</span> <span class="o">/</span> <span class="nb">Math</span><span class="p">.</span><span class="nx">log</span><span class="p">(</span><span class="nx">zmax</span><span class="p">);</span></div><div class='line' id='LC259'>						<span class="kd">var</span> <span class="nx">p</span> <span class="o">=</span> <span class="p">(</span><span class="mi">1</span> <span class="o">-</span> <span class="nx">x</span><span class="p">)</span><span class="o">*</span><span class="nx">percent</span> <span class="o">+</span> <span class="nx">x</span><span class="p">;</span></div><div class='line' id='LC260'><br/></div><div class='line' id='LC261'>						<span class="c1">// change the zoom level</span></div><div class='line' id='LC262'>						<span class="kd">var</span> <span class="nx">z</span> <span class="o">=</span> <span class="nb">Math</span><span class="p">.</span><span class="nx">pow</span><span class="p">(</span> <span class="nx">zmax</span><span class="p">,</span> <span class="nx">p</span> <span class="p">);</span></div><div class='line' id='LC263'><br/></div><div class='line' id='LC264'>						<span class="c1">// bound the zoom value in case of floating pt rounding error</span></div><div class='line' id='LC265'>						<span class="k">if</span><span class="p">(</span> <span class="nx">z</span> <span class="o">&lt;</span> <span class="nx">zmin</span> <span class="p">){</span></div><div class='line' id='LC266'>							<span class="nx">z</span> <span class="o">=</span> <span class="nx">zmin</span><span class="p">;</span></div><div class='line' id='LC267'>						<span class="p">}</span> <span class="k">else</span> <span class="k">if</span><span class="p">(</span> <span class="nx">z</span> <span class="o">&gt;</span> <span class="nx">zmax</span> <span class="p">){</span></div><div class='line' id='LC268'>							<span class="nx">z</span> <span class="o">=</span> <span class="nx">zmax</span><span class="p">;</span></div><div class='line' id='LC269'>						<span class="p">}</span></div><div class='line' id='LC270'><br/></div><div class='line' id='LC271'>						<span class="nx">zoomTo</span><span class="p">(</span> <span class="nx">z</span> <span class="p">);</span></div><div class='line' id='LC272'>					<span class="p">}</span></div><div class='line' id='LC273'><br/></div><div class='line' id='LC274'>					<span class="kd">var</span> <span class="nx">sliderMdownHandler</span><span class="p">,</span> <span class="nx">sliderMmoveHandler</span><span class="p">;</span></div><div class='line' id='LC275'>					<span class="nx">$sliderHandle</span><span class="p">.</span><span class="nx">bind</span><span class="p">(</span><span class="s1">&#39;mousedown&#39;</span><span class="p">,</span> <span class="nx">sliderMdownHandler</span> <span class="o">=</span> <span class="kd">function</span><span class="p">(</span> <span class="nx">mdEvt</span> <span class="p">){</span></div><div class='line' id='LC276'>						<span class="kd">var</span> <span class="nx">handleOffset</span> <span class="o">=</span> <span class="nx">mdEvt</span><span class="p">.</span><span class="nx">target</span> <span class="o">===</span> <span class="nx">$sliderHandle</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">?</span> <span class="nx">mdEvt</span><span class="p">.</span><span class="nx">offsetY</span> <span class="o">:</span> <span class="mi">0</span><span class="p">;</span></div><div class='line' id='LC277'>						<span class="nx">sliding</span> <span class="o">=</span> <span class="kc">true</span><span class="p">;</span></div><div class='line' id='LC278'><br/></div><div class='line' id='LC279'>						<span class="nx">startZooming</span><span class="p">();</span></div><div class='line' id='LC280'>						<span class="nx">$sliderHandle</span><span class="p">.</span><span class="nx">addClass</span><span class="p">(</span><span class="s2">&quot;active&quot;</span><span class="p">);</span></div><div class='line' id='LC281'><br/></div><div class='line' id='LC282'>						<span class="kd">var</span> <span class="nx">lastMove</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span></div><div class='line' id='LC283'>						<span class="nx">$</span><span class="p">(</span><span class="nb">window</span><span class="p">).</span><span class="nx">bind</span><span class="p">(</span><span class="s1">&#39;mousemove&#39;</span><span class="p">,</span> <span class="nx">sliderMmoveHandler</span> <span class="o">=</span> <span class="kd">function</span><span class="p">(</span> <span class="nx">mmEvt</span> <span class="p">){</span></div><div class='line' id='LC284'>							<span class="kd">var</span> <span class="nx">now</span> <span class="o">=</span> <span class="o">+</span><span class="k">new</span> <span class="nb">Date</span><span class="p">;</span></div><div class='line' id='LC285'><br/></div><div class='line' id='LC286'>							<span class="c1">// throttle the zooms every 10 ms so we don&#39;t call zoom too often and cause lag</span></div><div class='line' id='LC287'>							<span class="k">if</span><span class="p">(</span> <span class="nx">now</span> <span class="o">&gt;</span> <span class="nx">lastMove</span> <span class="o">+</span> <span class="mi">10</span> <span class="p">){</span></div><div class='line' id='LC288'>								<span class="nx">lastMove</span> <span class="o">=</span> <span class="nx">now</span><span class="p">;</span></div><div class='line' id='LC289'>							<span class="p">}</span> <span class="k">else</span> <span class="p">{</span></div><div class='line' id='LC290'>								<span class="k">return</span> <span class="kc">false</span><span class="p">;</span></div><div class='line' id='LC291'>							<span class="p">}</span></div><div class='line' id='LC292'><br/></div><div class='line' id='LC293'>							<span class="nx">setSliderFromMouse</span><span class="p">(</span><span class="nx">mmEvt</span><span class="p">,</span> <span class="nx">handleOffset</span><span class="p">);</span></div><div class='line' id='LC294'><br/></div><div class='line' id='LC295'>							<span class="k">return</span> <span class="kc">false</span><span class="p">;</span></div><div class='line' id='LC296'>						<span class="p">});</span></div><div class='line' id='LC297'><br/></div><div class='line' id='LC298'>						<span class="c1">// unbind when </span></div><div class='line' id='LC299'>						<span class="nx">$</span><span class="p">(</span><span class="nb">window</span><span class="p">).</span><span class="nx">bind</span><span class="p">(</span><span class="s1">&#39;mouseup&#39;</span><span class="p">,</span> <span class="kd">function</span><span class="p">(){</span></div><div class='line' id='LC300'>							<span class="nx">$</span><span class="p">(</span><span class="nb">window</span><span class="p">).</span><span class="nx">unbind</span><span class="p">(</span><span class="s1">&#39;mousemove&#39;</span><span class="p">,</span> <span class="nx">sliderMmoveHandler</span><span class="p">);</span></div><div class='line' id='LC301'>							<span class="nx">sliding</span> <span class="o">=</span> <span class="kc">false</span><span class="p">;</span></div><div class='line' id='LC302'><br/></div><div class='line' id='LC303'>							<span class="nx">$sliderHandle</span><span class="p">.</span><span class="nx">removeClass</span><span class="p">(</span><span class="s2">&quot;active&quot;</span><span class="p">);</span></div><div class='line' id='LC304'>							<span class="nx">endZooming</span><span class="p">();</span></div><div class='line' id='LC305'>						<span class="p">});</span></div><div class='line' id='LC306'><br/></div><div class='line' id='LC307'>						<span class="k">return</span> <span class="kc">false</span><span class="p">;</span></div><div class='line' id='LC308'>					<span class="p">});</span>				</div><div class='line' id='LC309'><br/></div><div class='line' id='LC310'>					<span class="nx">$slider</span><span class="p">.</span><span class="nx">bind</span><span class="p">(</span><span class="s1">&#39;mousedown&#39;</span><span class="p">,</span> <span class="kd">function</span><span class="p">(</span><span class="nx">e</span><span class="p">){</span></div><div class='line' id='LC311'>						<span class="k">if</span><span class="p">(</span> <span class="nx">e</span><span class="p">.</span><span class="nx">target</span> <span class="o">!==</span> <span class="nx">$sliderHandle</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="p">){</span></div><div class='line' id='LC312'>							<span class="nx">sliderMdownHandler</span><span class="p">(</span><span class="nx">e</span><span class="p">);</span></div><div class='line' id='LC313'>							<span class="nx">setSliderFromMouse</span><span class="p">(</span><span class="nx">e</span><span class="p">);</span></div><div class='line' id='LC314'>						<span class="p">}</span></div><div class='line' id='LC315'>					<span class="p">});</span></div><div class='line' id='LC316'><br/></div><div class='line' id='LC317'>					<span class="kd">function</span> <span class="nx">positionSliderFromZoom</span><span class="p">(){</span></div><div class='line' id='LC318'>						<span class="kd">var</span> <span class="nx">cy</span> <span class="o">=</span> <span class="nx">$container</span><span class="p">.</span><span class="nx">cytoscape</span><span class="p">(</span><span class="s2">&quot;get&quot;</span><span class="p">);</span></div><div class='line' id='LC319'>						<span class="kd">var</span> <span class="nx">z</span> <span class="o">=</span> <span class="nx">cy</span><span class="p">.</span><span class="nx">zoom</span><span class="p">();</span></div><div class='line' id='LC320'>						<span class="kd">var</span> <span class="nx">zmin</span> <span class="o">=</span> <span class="nx">options</span><span class="p">.</span><span class="nx">minZoom</span><span class="p">;</span></div><div class='line' id='LC321'>						<span class="kd">var</span> <span class="nx">zmax</span> <span class="o">=</span> <span class="nx">options</span><span class="p">.</span><span class="nx">maxZoom</span><span class="p">;</span></div><div class='line' id='LC322'><br/></div><div class='line' id='LC323'>						<span class="c1">// assume (zoom = zmax ^ p) where p ranges on (x, 1) with x negative</span></div><div class='line' id='LC324'>						<span class="kd">var</span> <span class="nx">x</span> <span class="o">=</span> <span class="nb">Math</span><span class="p">.</span><span class="nx">log</span><span class="p">(</span><span class="nx">zmin</span><span class="p">)</span> <span class="o">/</span> <span class="nb">Math</span><span class="p">.</span><span class="nx">log</span><span class="p">(</span><span class="nx">zmax</span><span class="p">);</span></div><div class='line' id='LC325'>						<span class="kd">var</span> <span class="nx">p</span> <span class="o">=</span> <span class="nb">Math</span><span class="p">.</span><span class="nx">log</span><span class="p">(</span><span class="nx">z</span><span class="p">)</span> <span class="o">/</span> <span class="nb">Math</span><span class="p">.</span><span class="nx">log</span><span class="p">(</span><span class="nx">zmax</span><span class="p">);</span></div><div class='line' id='LC326'>						<span class="kd">var</span> <span class="nx">percent</span> <span class="o">=</span> <span class="mi">1</span> <span class="o">-</span> <span class="p">(</span><span class="nx">p</span> <span class="o">-</span> <span class="nx">x</span><span class="p">)</span> <span class="o">/</span> <span class="p">(</span><span class="mi">1</span> <span class="o">-</span> <span class="nx">x</span><span class="p">);</span> <span class="c1">// the 1- bit at the front b/c up is in the -ve y direction</span></div><div class='line' id='LC327'><br/></div><div class='line' id='LC328'>						<span class="kd">var</span> <span class="nx">min</span> <span class="o">=</span> <span class="nx">sliderPadding</span><span class="p">;</span></div><div class='line' id='LC329'>						<span class="kd">var</span> <span class="nx">max</span> <span class="o">=</span> <span class="nx">$slider</span><span class="p">.</span><span class="nx">height</span><span class="p">()</span> <span class="o">-</span> <span class="nx">$sliderHandle</span><span class="p">.</span><span class="nx">height</span><span class="p">()</span> <span class="o">-</span> <span class="mi">2</span><span class="o">*</span><span class="nx">sliderPadding</span><span class="p">;</span></div><div class='line' id='LC330'>						<span class="kd">var</span> <span class="nx">top</span> <span class="o">=</span> <span class="nx">percent</span> <span class="o">*</span> <span class="p">(</span> <span class="nx">max</span> <span class="o">-</span> <span class="nx">min</span> <span class="p">);</span></div><div class='line' id='LC331'><br/></div><div class='line' id='LC332'>						<span class="c1">// constrain to slider bounds</span></div><div class='line' id='LC333'>						<span class="k">if</span><span class="p">(</span> <span class="nx">top</span> <span class="o">&lt;</span> <span class="nx">min</span> <span class="p">){</span> <span class="nx">top</span> <span class="o">=</span> <span class="nx">min</span> <span class="p">}</span></div><div class='line' id='LC334'>						<span class="k">if</span><span class="p">(</span> <span class="nx">top</span> <span class="o">&gt;</span> <span class="nx">max</span> <span class="p">){</span> <span class="nx">top</span> <span class="o">=</span> <span class="nx">max</span> <span class="p">}</span></div><div class='line' id='LC335'><br/></div><div class='line' id='LC336'>						<span class="c1">// move the handle</span></div><div class='line' id='LC337'>						<span class="nx">$sliderHandle</span><span class="p">.</span><span class="nx">css</span><span class="p">(</span><span class="s1">&#39;top&#39;</span><span class="p">,</span> <span class="nx">top</span><span class="p">);</span></div><div class='line' id='LC338'>					<span class="p">}</span></div><div class='line' id='LC339'><br/></div><div class='line' id='LC340'>					<span class="nx">positionSliderFromZoom</span><span class="p">();</span></div><div class='line' id='LC341'><br/></div><div class='line' id='LC342'>					<span class="kd">var</span> <span class="nx">cy</span> <span class="o">=</span> <span class="nx">$container</span><span class="p">.</span><span class="nx">cytoscape</span><span class="p">(</span><span class="s2">&quot;get&quot;</span><span class="p">);</span></div><div class='line' id='LC343'>					<span class="nx">cy</span><span class="p">.</span><span class="nx">on</span><span class="p">(</span><span class="s1">&#39;zoom&#39;</span><span class="p">,</span> <span class="kd">function</span><span class="p">(){</span></div><div class='line' id='LC344'>						<span class="k">if</span><span class="p">(</span> <span class="o">!</span><span class="nx">sliding</span> <span class="p">){</span></div><div class='line' id='LC345'>							<span class="nx">positionSliderFromZoom</span><span class="p">();</span></div><div class='line' id='LC346'>						<span class="p">}</span></div><div class='line' id='LC347'>					<span class="p">});</span></div><div class='line' id='LC348'><br/></div><div class='line' id='LC349'>					<span class="c1">// set the position of the zoom=1 tick</span></div><div class='line' id='LC350'>					<span class="p">(</span><span class="kd">function</span><span class="p">(){</span></div><div class='line' id='LC351'>						<span class="kd">var</span> <span class="nx">z</span> <span class="o">=</span> <span class="mi">1</span><span class="p">;</span></div><div class='line' id='LC352'>						<span class="kd">var</span> <span class="nx">zmin</span> <span class="o">=</span> <span class="nx">options</span><span class="p">.</span><span class="nx">minZoom</span><span class="p">;</span></div><div class='line' id='LC353'>						<span class="kd">var</span> <span class="nx">zmax</span> <span class="o">=</span> <span class="nx">options</span><span class="p">.</span><span class="nx">maxZoom</span><span class="p">;</span></div><div class='line' id='LC354'><br/></div><div class='line' id='LC355'>						<span class="c1">// assume (zoom = zmax ^ p) where p ranges on (x, 1) with x negative</span></div><div class='line' id='LC356'>						<span class="kd">var</span> <span class="nx">x</span> <span class="o">=</span> <span class="nb">Math</span><span class="p">.</span><span class="nx">log</span><span class="p">(</span><span class="nx">zmin</span><span class="p">)</span> <span class="o">/</span> <span class="nb">Math</span><span class="p">.</span><span class="nx">log</span><span class="p">(</span><span class="nx">zmax</span><span class="p">);</span></div><div class='line' id='LC357'>						<span class="kd">var</span> <span class="nx">p</span> <span class="o">=</span> <span class="nb">Math</span><span class="p">.</span><span class="nx">log</span><span class="p">(</span><span class="nx">z</span><span class="p">)</span> <span class="o">/</span> <span class="nb">Math</span><span class="p">.</span><span class="nx">log</span><span class="p">(</span><span class="nx">zmax</span><span class="p">);</span></div><div class='line' id='LC358'>						<span class="kd">var</span> <span class="nx">percent</span> <span class="o">=</span> <span class="mi">1</span> <span class="o">-</span> <span class="p">(</span><span class="nx">p</span> <span class="o">-</span> <span class="nx">x</span><span class="p">)</span> <span class="o">/</span> <span class="p">(</span><span class="mi">1</span> <span class="o">-</span> <span class="nx">x</span><span class="p">);</span> <span class="c1">// the 1- bit at the front b/c up is in the -ve y direction</span></div><div class='line' id='LC359'><br/></div><div class='line' id='LC360'>						<span class="k">if</span><span class="p">(</span> <span class="nx">percent</span> <span class="o">&gt;</span> <span class="mi">1</span> <span class="o">||</span> <span class="nx">percent</span> <span class="o">&lt;</span> <span class="mi">0</span> <span class="p">){</span></div><div class='line' id='LC361'>							<span class="nx">$noZoomTick</span><span class="p">.</span><span class="nx">hide</span><span class="p">();</span></div><div class='line' id='LC362'>							<span class="k">return</span><span class="p">;</span></div><div class='line' id='LC363'>						<span class="p">}</span></div><div class='line' id='LC364'><br/></div><div class='line' id='LC365'>						<span class="kd">var</span> <span class="nx">min</span> <span class="o">=</span> <span class="nx">sliderPadding</span><span class="p">;</span></div><div class='line' id='LC366'>						<span class="kd">var</span> <span class="nx">max</span> <span class="o">=</span> <span class="nx">$slider</span><span class="p">.</span><span class="nx">height</span><span class="p">()</span> <span class="o">-</span> <span class="nx">$sliderHandle</span><span class="p">.</span><span class="nx">height</span><span class="p">()</span> <span class="o">-</span> <span class="mi">2</span><span class="o">*</span><span class="nx">sliderPadding</span><span class="p">;</span></div><div class='line' id='LC367'>						<span class="kd">var</span> <span class="nx">top</span> <span class="o">=</span> <span class="nx">percent</span> <span class="o">*</span> <span class="p">(</span> <span class="nx">max</span> <span class="o">-</span> <span class="nx">min</span> <span class="p">);</span></div><div class='line' id='LC368'><br/></div><div class='line' id='LC369'>						<span class="c1">// constrain to slider bounds</span></div><div class='line' id='LC370'>						<span class="k">if</span><span class="p">(</span> <span class="nx">top</span> <span class="o">&lt;</span> <span class="nx">min</span> <span class="p">){</span> <span class="nx">top</span> <span class="o">=</span> <span class="nx">min</span> <span class="p">}</span></div><div class='line' id='LC371'>						<span class="k">if</span><span class="p">(</span> <span class="nx">top</span> <span class="o">&gt;</span> <span class="nx">max</span> <span class="p">){</span> <span class="nx">top</span> <span class="o">=</span> <span class="nx">max</span> <span class="p">}</span></div><div class='line' id='LC372'><br/></div><div class='line' id='LC373'>						<span class="nx">$noZoomTick</span><span class="p">.</span><span class="nx">css</span><span class="p">(</span><span class="s1">&#39;top&#39;</span><span class="p">,</span> <span class="nx">top</span><span class="p">);</span></div><div class='line' id='LC374'>					<span class="p">})();</span></div><div class='line' id='LC375'><br/></div><div class='line' id='LC376'>					<span class="c1">// set up zoom in/out buttons</span></div><div class='line' id='LC377'>					<span class="c1">/////////////////////////////</span></div><div class='line' id='LC378'><br/></div><div class='line' id='LC379'>					<span class="kd">function</span> <span class="nx">bindButton</span><span class="p">(</span><span class="nx">$button</span><span class="p">,</span> <span class="nx">factor</span><span class="p">){</span></div><div class='line' id='LC380'>						<span class="kd">var</span> <span class="nx">zoomInterval</span><span class="p">;</span></div><div class='line' id='LC381'><br/></div><div class='line' id='LC382'>						<span class="nx">$button</span><span class="p">.</span><span class="nx">bind</span><span class="p">(</span><span class="s2">&quot;mousedown&quot;</span><span class="p">,</span> <span class="kd">function</span><span class="p">(</span><span class="nx">e</span><span class="p">){</span></div><div class='line' id='LC383'>							<span class="nx">e</span><span class="p">.</span><span class="nx">preventDefault</span><span class="p">();</span></div><div class='line' id='LC384'>							<span class="nx">e</span><span class="p">.</span><span class="nx">stopPropagation</span><span class="p">();</span></div><div class='line' id='LC385'><br/></div><div class='line' id='LC386'>							<span class="k">if</span><span class="p">(</span> <span class="nx">e</span><span class="p">.</span><span class="nx">button</span> <span class="o">!=</span> <span class="mi">0</span> <span class="p">){</span></div><div class='line' id='LC387'>								<span class="k">return</span><span class="p">;</span></div><div class='line' id='LC388'>							<span class="p">}</span></div><div class='line' id='LC389'><br/></div><div class='line' id='LC390'>							<span class="kd">var</span> <span class="nx">cy</span> <span class="o">=</span> <span class="nx">$container</span><span class="p">.</span><span class="nx">cytoscape</span><span class="p">(</span><span class="s2">&quot;get&quot;</span><span class="p">);</span></div><div class='line' id='LC391'><br/></div><div class='line' id='LC392'>							<span class="nx">startZooming</span><span class="p">();</span></div><div class='line' id='LC393'>							<span class="nx">zoomInterval</span> <span class="o">=</span> <span class="nx">setInterval</span><span class="p">(</span><span class="kd">function</span><span class="p">(){</span></div><div class='line' id='LC394'>								<span class="kd">var</span> <span class="nx">zoom</span> <span class="o">=</span> <span class="nx">cy</span><span class="p">.</span><span class="nx">zoom</span><span class="p">();</span></div><div class='line' id='LC395'>								<span class="kd">var</span> <span class="nx">lvl</span> <span class="o">=</span> <span class="nx">cy</span><span class="p">.</span><span class="nx">zoom</span><span class="p">()</span> <span class="o">*</span> <span class="nx">factor</span><span class="p">;</span></div><div class='line' id='LC396'><br/></div><div class='line' id='LC397'>								<span class="k">if</span><span class="p">(</span> <span class="nx">lvl</span> <span class="o">&lt;</span> <span class="nx">options</span><span class="p">.</span><span class="nx">minZoom</span> <span class="p">){</span></div><div class='line' id='LC398'>									<span class="nx">lvl</span> <span class="o">=</span> <span class="nx">options</span><span class="p">.</span><span class="nx">minZoom</span><span class="p">;</span></div><div class='line' id='LC399'>								<span class="p">}</span></div><div class='line' id='LC400'><br/></div><div class='line' id='LC401'>								<span class="k">if</span><span class="p">(</span> <span class="nx">lvl</span> <span class="o">&gt;</span> <span class="nx">options</span><span class="p">.</span><span class="nx">maxZoom</span> <span class="p">){</span></div><div class='line' id='LC402'>									<span class="nx">lvl</span> <span class="o">=</span> <span class="nx">options</span><span class="p">.</span><span class="nx">maxZoom</span><span class="p">;</span></div><div class='line' id='LC403'>								<span class="p">}</span></div><div class='line' id='LC404'><br/></div><div class='line' id='LC405'>								<span class="k">if</span><span class="p">(</span> <span class="p">(</span><span class="nx">lvl</span> <span class="o">==</span> <span class="nx">options</span><span class="p">.</span><span class="nx">maxZoom</span> <span class="o">&amp;&amp;</span> <span class="nx">zoom</span> <span class="o">==</span> <span class="nx">options</span><span class="p">.</span><span class="nx">maxZoom</span><span class="p">)</span> <span class="o">||</span></div><div class='line' id='LC406'>									<span class="p">(</span><span class="nx">lvl</span> <span class="o">==</span> <span class="nx">options</span><span class="p">.</span><span class="nx">minZoom</span> <span class="o">&amp;&amp;</span> <span class="nx">zoom</span> <span class="o">==</span> <span class="nx">options</span><span class="p">.</span><span class="nx">minZoom</span><span class="p">)</span></div><div class='line' id='LC407'>								<span class="p">){</span></div><div class='line' id='LC408'>									<span class="k">return</span><span class="p">;</span></div><div class='line' id='LC409'>								<span class="p">}</span></div><div class='line' id='LC410'><br/></div><div class='line' id='LC411'>								<span class="nx">zoomTo</span><span class="p">(</span><span class="nx">lvl</span><span class="p">);</span></div><div class='line' id='LC412'>							<span class="p">},</span> <span class="nx">options</span><span class="p">.</span><span class="nx">zoomDelay</span><span class="p">);</span></div><div class='line' id='LC413'><br/></div><div class='line' id='LC414'>							<span class="k">return</span> <span class="kc">false</span><span class="p">;</span></div><div class='line' id='LC415'>						<span class="p">});</span></div><div class='line' id='LC416'><br/></div><div class='line' id='LC417'>						<span class="nx">$</span><span class="p">(</span><span class="nb">window</span><span class="p">).</span><span class="nx">bind</span><span class="p">(</span><span class="s2">&quot;mouseup blur&quot;</span><span class="p">,</span> <span class="kd">function</span><span class="p">(){</span></div><div class='line' id='LC418'>							<span class="nx">clearInterval</span><span class="p">(</span><span class="nx">zoomInterval</span><span class="p">);</span></div><div class='line' id='LC419'>							<span class="nx">endZooming</span><span class="p">();</span></div><div class='line' id='LC420'>						<span class="p">});</span></div><div class='line' id='LC421'>					<span class="p">}</span></div><div class='line' id='LC422'><br/></div><div class='line' id='LC423'>					<span class="nx">bindButton</span><span class="p">(</span> <span class="nx">$zoomIn</span><span class="p">,</span> <span class="p">(</span><span class="mi">1</span> <span class="o">+</span> <span class="nx">options</span><span class="p">.</span><span class="nx">zoomFactor</span><span class="p">)</span> <span class="p">);</span></div><div class='line' id='LC424'>					<span class="nx">bindButton</span><span class="p">(</span> <span class="nx">$zoomOut</span><span class="p">,</span> <span class="p">(</span><span class="mi">1</span> <span class="o">-</span> <span class="nx">options</span><span class="p">.</span><span class="nx">zoomFactor</span><span class="p">)</span> <span class="p">);</span></div><div class='line' id='LC425'><br/></div><div class='line' id='LC426'>					<span class="nx">$reset</span><span class="p">.</span><span class="nx">bind</span><span class="p">(</span><span class="s2">&quot;mousedown&quot;</span><span class="p">,</span> <span class="kd">function</span><span class="p">(</span><span class="nx">e</span><span class="p">){</span></div><div class='line' id='LC427'>						<span class="k">if</span><span class="p">(</span> <span class="nx">e</span><span class="p">.</span><span class="nx">button</span> <span class="o">!=</span> <span class="mi">0</span> <span class="p">){</span></div><div class='line' id='LC428'>							<span class="k">return</span><span class="p">;</span></div><div class='line' id='LC429'>						<span class="p">}</span></div><div class='line' id='LC430'><br/></div><div class='line' id='LC431'>						<span class="kd">var</span> <span class="nx">cy</span> <span class="o">=</span> <span class="nx">$container</span><span class="p">.</span><span class="nx">cytoscape</span><span class="p">(</span><span class="s2">&quot;get&quot;</span><span class="p">);</span></div><div class='line' id='LC432'><br/></div><div class='line' id='LC433'>						<span class="k">if</span><span class="p">(</span> <span class="nx">cy</span><span class="p">.</span><span class="nx">elements</span><span class="p">().</span><span class="nx">size</span><span class="p">()</span> <span class="o">===</span> <span class="mi">0</span> <span class="p">){</span></div><div class='line' id='LC434'>							<span class="nx">cy</span><span class="p">.</span><span class="nx">reset</span><span class="p">();</span></div><div class='line' id='LC435'>						<span class="p">}</span> <span class="k">else</span> <span class="p">{</span></div><div class='line' id='LC436'>							<span class="nx">cy</span><span class="p">.</span><span class="nx">fit</span><span class="p">(</span> <span class="nx">options</span><span class="p">.</span><span class="nx">fitPadding</span> <span class="p">);</span></div><div class='line' id='LC437'>						<span class="p">}</span></div><div class='line' id='LC438'><br/></div><div class='line' id='LC439'>						<span class="k">return</span> <span class="kc">false</span><span class="p">;</span></div><div class='line' id='LC440'>					<span class="p">});</span></div><div class='line' id='LC441'><br/></div><div class='line' id='LC442'><br/></div><div class='line' id='LC443'><br/></div><div class='line' id='LC444'>				<span class="p">});</span></div><div class='line' id='LC445'>			<span class="p">}</span></div><div class='line' id='LC446'>		<span class="p">};</span></div><div class='line' id='LC447'><br/></div><div class='line' id='LC448'>		<span class="k">if</span><span class="p">(</span> <span class="nx">functions</span><span class="p">[</span><span class="nx">fn</span><span class="p">]</span> <span class="p">){</span></div><div class='line' id='LC449'>			<span class="k">return</span> <span class="nx">functions</span><span class="p">[</span><span class="nx">fn</span><span class="p">].</span><span class="nx">apply</span><span class="p">(</span><span class="k">this</span><span class="p">,</span> <span class="nb">Array</span><span class="p">.</span><span class="nx">prototype</span><span class="p">.</span><span class="nx">slice</span><span class="p">.</span><span class="nx">call</span><span class="p">(</span> <span class="nx">arguments</span><span class="p">,</span> <span class="mi">1</span> <span class="p">));</span></div><div class='line' id='LC450'>		<span class="p">}</span> <span class="k">else</span> <span class="k">if</span><span class="p">(</span> <span class="k">typeof</span> <span class="nx">fn</span> <span class="o">==</span> <span class="s1">&#39;object&#39;</span> <span class="o">||</span> <span class="o">!</span><span class="nx">fn</span> <span class="p">)</span> <span class="p">{</span></div><div class='line' id='LC451'>			<span class="k">return</span> <span class="nx">functions</span><span class="p">.</span><span class="nx">init</span><span class="p">.</span><span class="nx">apply</span><span class="p">(</span> <span class="k">this</span><span class="p">,</span> <span class="nx">arguments</span> <span class="p">);</span></div><div class='line' id='LC452'>		<span class="p">}</span> <span class="k">else</span> <span class="p">{</span></div><div class='line' id='LC453'>			<span class="nx">$</span><span class="p">.</span><span class="nx">error</span><span class="p">(</span><span class="s2">&quot;No such function `&quot;</span><span class="o">+</span> <span class="nx">fn</span> <span class="o">+</span><span class="s2">&quot;` for jquery.cytoscapePanzoom&quot;</span><span class="p">);</span></div><div class='line' id='LC454'>		<span class="p">}</span></div><div class='line' id='LC455'><br/></div><div class='line' id='LC456'>		<span class="k">return</span> <span class="nx">$</span><span class="p">(</span><span class="k">this</span><span class="p">);</span></div><div class='line' id='LC457'>	<span class="p">};</span></div><div class='line' id='LC458'><br/></div><div class='line' id='LC459'>	<span class="nx">$</span><span class="p">.</span><span class="nx">fn</span><span class="p">.</span><span class="nx">cyPanzoom</span> <span class="o">=</span> <span class="nx">$</span><span class="p">.</span><span class="nx">fn</span><span class="p">.</span><span class="nx">cytoscapePanzoom</span><span class="p">;</span></div><div class='line' id='LC460'><br/></div><div class='line' id='LC461'><span class="p">})(</span><span class="nx">jQuery</span><span class="p">);</span></div></pre></div>
          </td>
        </tr>
      </table>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/">
      <span class="mega-octicon octicon-mark-github"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2013 <span title="0.10234s from fe18.rs.github.com">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/cytoscape/cytoscape.js/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-remove-close close ajax-error-dismiss"></a>
      Something went wrong with that request. Please try again.
    </div>

    
  </body>
</html>

