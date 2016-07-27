from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^get-articles/$', views.process_words, name='get-articles'),
    url(r'^get-article/$', views.get_full_article, name='get-article'),
)

"""
url(r'^profile/$', views.profile, name='profile'),
url(r'^dashboard/$', views.dashboard, name='dashboard'),
url(r'^contact/$', views.contact, name='contact'),
url(r'^terms/$', views.terms, name='terms'),

url(r'^get-quotes/$', views.get_quotes_for_chart, name='get-quotes'),
url(r'^get-portfolio-performance/$', views.get_portfolio_performance, name='get-portfolio-performance'),

url(r'^edit-portfolio/$', views.edit_portfolio, name='edit-portfolio'),
url(r'^asset-details/(?P<asset_id>[\w\-]+)/$', views.asset_details, name='asset-details'),
url(r'^get-flags/$', views.get_flags, name='get-flags'),
url(r'^about-us/$', views.about, name='about-us'),
url(r'^features/$', views.features, name='features'),

url(r'^suggest-asset/$', views.suggest_asset, name='suggest-asset'),
url(r'^select-asset/$', views.select_asset, name='select-asset'),
url(r'^change-percentage/$', views.change_percentage, name='change-percentage'),
url(r'^delete-asset/$', views.delete_asset, name='delete-asset'),
url(r'^distribute-evenly/$', views.distribute_evenly, name='distribute-evenly'),
url(r'^save-portfolio/$', views.save_portfolio, name='save-portfolio'),

url(r'^pick-portfolio/$', views.pick_portfolio, name='pick-portfolio'),
url(r'^optimize-portfolio/$', views.optimize_portfolio, name='optimize-portfolio'),
url(r'^attempt-optimization/$', views.attempt_optimization, name='attempt-optimization'),
url(r'^apply-optimization/$', views.apply_optimization, name='apply-optimization'),
"""