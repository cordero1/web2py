# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - api is an example of Hypermedia API support and access control
#########################################################################

import sys, pdb


def guardar():    
    
    try:
        f=open("C:\Users\Cordero\Desktop\prduino.txt", "r")
        lista=f.readlines()
        f.close()
        lista="".join(lista)
        lista= lista.split(',')
    except: pass
    
    if request.vars.led=='0': #valor[5]== "T":
        try:
            guardar= lista[0]+ ','+ str(lista [1]) + ',' + "0"
            f=open("C:\Users\Cordero\Desktop\prduino.txt", "w")
            f.write(guardar)
            f.close()
            return dict(potenciometro= lista[0], puerta= lista[1], led= lista[2]) 
        except: pass
        
    if request.vars.led=='1': #datos[0]== "False":
        try:
            guardar= lista[0]+ ','+ str(lista [1]) + ',' + "1"
            f=open("C:\Users\Cordero\Desktop\prduino.txt", "w")
            f.write(guardar)
            f.close()
            return dict(potenciometro= lista[0], puerta= lista[1], led= lista[2])
        except:pass
    
    return dict(potenciometro= request.vars.potenciometro, puerta= request.vars.puerta, led= request.vars.led_auxiliar)
    
def index():
    response.flash= 'Bienvenido'
    return dict()



def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_login() 
def api():
    """
    this is example of API with access control
    WEB2PY provides Hypermedia API (Collection+JSON) Experimental
    """
    from gluon.contrib.hypermedia import Collection
    rules = {
        '<tablename>': {'GET':{},'POST':{},'PUT':{},'DELETE':{}},
        }
    return Collection(db).process(request,response,rules)

