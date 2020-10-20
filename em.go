package main
import (
	"sync"
	"os/exec"
	"log"
	"fmt"
)
var wg sync.WaitGroup
func main(){
	cmd := exec.Command("nrf_detect.py")
	out, err := cmd.CombinedOutput()
	if err != nil {
		log.Fatalf("cmd.Run() failed with %s\n", err)
	}
	fmt.Printf("combined out:\n%s\n", string(out))
	/*wg.Add(1)
	go nrf_detect()
	wg.Add(1)
	go amf_detect()
	wg.Add(1)
	go smf_detect()*/
}

/*func nrf_detect(){
	fmt.Printf("nrf detect")
	cmd := exec.Command("python nrf_detect.py")
	out, err := cmd.CombinedOutput()
	if err != nil {
		log.Fatalf("cmd.Run() failed with %s\n", err)
	}
	fmt.Printf("combined out:\n%s\n", string(out))
}
func amf_detect(){
	fmt.Printf("amf detect")
	exec.Command("python amf_detect.py")
}
func smf_detect(){
	fmt.Printf("smf detect")
	exec.Command("python smf_detect.py")
}*/