all:
	go get -a github.com/golang/protobuf/protoc-gen-go
	cd gnostic; protoc gnostic.proto --go_out=plugins=grpc:.
	go get ./server
	go get ./client
	go install ./server
	go install ./client

run:
	killall server
	server &
	sleep 1 # give the server some time to start
	client -m "Remember the milk." -get
	client -m "Testing" -n 3 -update

clean:
	rm ./echo/echo/echo.pb.go
