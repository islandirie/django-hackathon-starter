from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('api/', views.api_examples, name='api'),
    path('steam/', views.steam, name='steam'),
    path('steamDiscountedGames/', views.steamDiscountedGames, name='steamDiscountedGames'),
    path('githubResume/', views.githubResume, name='githubResume'),
    path('githubUser/', views.githubUser, name='githubUser'),
    path('githubTopRepositories/', views.githubTopRepositories, name='githubTopRepositories'),
    path('tumblr/', views.tumblr, name='tumblr'),
    path('linkedin/', views.linkedin, name='linkedin'),
    path('twilio/', views.twilio, name='twilio'),
    path('instagram/', views.instagram, name='instagram'),
    path('instagram_login/', views.instagram_login, name='instagram_login'),
    path('instagramUser/', views.instagramUser, name='instagramUser'),
    path('instagramMediaByLocation/', views.instagramMediaByLocation, name='instagramMediaByLocation'),#
    path('instagramUserMedia/', views.instagramUserMedia, name='instagramUserMedia'),
    path('twitter/', views.twitter, name='twitter'),
    path('twitterTweets/', views.twitterTweets, name='twitterTweets'),
    path('tumblr_login/', views.tumblr_login, name='tumblr_login'),
    path('twitter_login/', views.twitter_login, name='twitter_login'),
    path('github_login/', views.github_login, name='github_login'),
    path('linkedin_login/', views.linkedin_login, name='linkedin_login'),
    path('facebook_login/', views.facebook_login, name='facebook_login'),
    path('facebook/', views.facebook, name='facebook'),
    path('google_login/', views.google_login, name='google_login'),
    path('google/', views.googlePlus, name='googlePlus'),
    path('dropbox_login/', views.dropbox_login, name='dropbox_login'),
    path('dropbox/', views.dropbox, name='dropbox'),
    path('dropboxSearchFile/', views.dropboxSearchFile, name='dropboxSearchFile'),
    path('foursquare_login/', views.foursquare_login, name='foursquare_login'),
    path('foursquare/', views.foursquare, name='foursquare'),
    path('quandlSnp500/', views.quandlSnp500, name='quandlsnp500'),
    path('quandlNasdaq/', views.quandlNasdaq, name='quandlnasdaq'),
    path('quandlNasdaqdiff/', views.quandlNasdaqdiff, name='quandlnasdaqdiff'),
    path('quandlDowJones/', views.quandlDowJones, name='quandldowjones'),
    path('quandlstocks/', views.quandlstocks, name='quandlstocks'),
    path('quandlapple/', views.quandlapple, name='quandlapple'),
    path('quandlapplediff/', views.quandlapplediff, name='quandlapplediff'),
    path('quandlDowJonesdiff/', views.quandlDowJonesdiff, name='quandldowjonesdiff'),
    path('quandlSnp500diff/', views.quandlSnp500diff, name='quandlsnp500diff'),
    path('nytimespop/', views.nytimespop, name='nytimespop'),
    path('nytimestop/', views.nytimestop, name='nytimestop'),
    path('nytimesarticles/', views.nytimesarticles, name='nytimesarticles'),
    path('meetup/', views.meetup, name='meetup'),
    path('meetupToken/', views.meetupToken, name='meetupToken'),
    path('meetupUser/', views.meetupUser, name='meetupUser'),
    path('yelp/', views.yelp, name='yelp'),
]
