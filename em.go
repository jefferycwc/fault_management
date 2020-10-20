package main
import (
	"sync"
	"os/exec"
)
var wg sync.WaitGroup
func main(){
	wg.Add(1)
	go nrf_detect()
	wg.Add(1)
	go amf_detect()
	wg.Add(1)
	go smf_detect()
}

func nrf_detect(){
	exec.Command("python nrf_detect.py")
}
func amf_detect(){
	exec.Command("python amf_detect.py")
}
func smf_detect(){
	exec.Command("python smf_detect.py")
}