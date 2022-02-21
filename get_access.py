import tweepy
import http.server
import http.client
import urllib.parse
import json
import os
import re
import ast

# TODO: replace "XXXXX" with your consumer token and secret. 
# These can be found in the Twitter Developer Portal.

CONSUMER_TOKEN = "XXXXX"
CONSUMER_SECRET = "XXXXX"

class TwitterHandler( http.server.SimpleHTTPRequestHandler ):

    def session_store( self, token ):
        self.send_header( 'Set-Cookie', 'auth={};'.format( token ) )


    def session_retrieve( self ):
        return ast.literal_eval(self.headers.get( 'Cookie' ).split( 'auth=' )[ 1 ])# bit ugly, but gets stored token from cookie

    def do_GET( self ):

        req  = urllib.parse.urlparse( 'http://localhost:8080' + self.path )
        auth = tweepy.OAuthHandler( CONSUMER_TOKEN, CONSUMER_SECRET, 'http://localhost:8080' )

        if req.query:
            auth.request_token = self.session_retrieve()
            
            qs = urllib.parse.parse_qs( req.query )
            oauth_verifier = qs[ 'oauth_verifier' ][ 0 ]

            try:
                auth.get_access_token( oauth_verifier )
            except tweepy.TweepError as e:
                print( 'Unable to exchange request token for access token.' )
            

            print( "Access Token: {}\nAccess Token Secret: {}".format( auth.access_token, auth.access_token_secret ) )
            
            quit()

        else:

            try:
                redirect_url = auth.get_authorization_url()
            except tweepy.TweepError:
                print( 'Unable to fetch request token to build authorization redirect_url.' )
                exit()

            self.send_response( 307 )
            self.send_header( 'Location', redirect_url )
            self.session_store( auth.request_token )
            self.end_headers()


def run( server_class = http.server.HTTPServer, handler_class = TwitterHandler ):
    print("Please go to \"localhost:8080\" in your web browser to authenticate.")
    server_address = ( 'localhost', 8080 )
    httpd = server_class( server_address, handler_class )
    httpd.serve_forever()


if __name__ == '__main__':
    run()
