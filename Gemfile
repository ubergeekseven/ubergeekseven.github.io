source "https://rubygems.org"
gem "jekyll"
gem "minimal-mistakes-jekyll"
# The following plugins are automatically loaded by the theme-gem:
#   gem "jekyll-paginate"
#   gem "jekyll-sitemap"
#   gem "jekyll-gist"
#   gem "jekyll-feed"
#   gem "jekyll-include-cache"
#
# If you have any other plugins, put them here!
# Cf. https://jekyllrb.com/docs/plugins/installation/
group :jekyll_plugins do
    gem 'faraday-retry', '~> 2.2.0' if ENV["GITHUB_ACTIONS"] != "true"
    gem 'jekyll-target-blank'
end