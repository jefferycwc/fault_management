upf_list = ['rm /dev/mqueue/*\n','cd /home/jeffery/all_in_one/src/upf/lib/libgtp5gnl/tools\n','./gtp5g-link del upfgtp0\n','cd /home/jeffery/all_in_one/src/upf/build\n','nohup ./bin/free5gc-upfd\n','exit\n']
nrf_list = ['nohup ./all_in_one/bin/nrf\n','exit\n']
amf_list = ['nohup ./all_in_one/bin/amf\n','exit\n']
smf_list = ['nohup ./all_in_one/bin/smf\n','exit\n']
udr_list = ['nohup ./all_in_one/bin/udr\n','exit\n']
pcf_list = ['nohup ./all_in_one/bin/pcf\n','exit\n']
udm_list = ['nohup ./all_in_one/bin/udm\n','exit\n']
nssf_list = ['nohup ./all_in_one/bin/nssf\n','exit\n']
ausf_list = ['nohup ./all_in_one/bin/ausf\n','exit\n']
cmds_dict = {'upf':upf_list,'nrf':nrf_list,'amf':amf_list,'smf':smf_list,'udr':udr_list,'pcf':pcf_list,'udm':udm_list,'nssf':nssf_list,'ausf':ausf_list}
