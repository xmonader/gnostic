
build:	
	go get golang.org/x/tools/cmd/goimports
	go install github.com/googleapis/gnostic
	go install github.com/googleapis/gnostic/plugins/gnostic-snake-generator
	rm -f $(GOPATH)/bin/gnostic-snake-client $(GOPATH)/bin/gnostic-snake-server
	ln -s $(GOPATH)/bin/gnostic-snake-generator $(GOPATH)/bin/gnostic-snake-client
	ln -s $(GOPATH)/bin/gnostic-snake-generator $(GOPATH)/bin/gnostic-snake-server

