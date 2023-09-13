
run:
	bash run.sh \
		$(CURDIR)/test/ \
		$(CURDIR)/test/all.cfg \
		$(CURDIR)/test/ \
		$(CURDIR)/test/config/ \
		$(CURDIR)/test/demo.svg \
		default \
		../../../ \
		$(CURDIR)/test/ \
		1
	# gio open http://127.0.0.1:$${port}/config.html & \
	#python -m CGIHTTPServer $${port}

#@pid=`ps -aux|grep 'python3 -m http.server'|grep -v 'grep'|awk '{print $$2}'` ;\
#python3 -m http.server --cgi $${port} &\

genhtml:
	@cd ./cgi-bin ; python3 server.py > ../ul.html

svg:
	cd ./static; python3 svgMap.py 
