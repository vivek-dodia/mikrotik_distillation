# Thread Information
Title: Thread-1121339
Section: RouterOS
Thread ID: 1121339

# Discussion

## Initial Question
Hi, Can someone help me?I have 2 IP addresses on ether1 (192.168.1.1 and 192.168.1.2 with masquerade), and I have to write out in the logs to which address logs in.I'm using winbox and logstash to get logs from Mikrotik, but only I get host IP (192.168.1.1, which sending logs to logstash). It's possible to do it with grok only, or I have to configure Mikrotik?Grok:
```
input{udp{port=>514type=>"syslog"}}filter{grok{match=>{"message"=>"%{DATA:topics} user %{WORD:user_name} logged %{WORD:action} from %{IP:src_ip} via %{WORD:protocol}"}}}output{stdout{codec=>rubydebug}elasticsearch{hosts=>["http://localhost:9200"]index=>"mikrotik-logs-%{+YYYY.MM.dd}"}file{path=>"C:/logs/mikrotik_logs_%{+YYYY-MM-dd}.log"codec=>line{format=>"%{message} TO_IP: %{host}"}}}

---
```

## Response 1
/ip fi ma add action=log chain=input dst-address=192.168.1.1 dst-port=8291 log-prefix=Winbox_x1 protocol=tcp/ip fi ma add action=log chain=input dst-address=192.168.1.2 dst-port=8291 log-prefix=Winbox_x2 protocol=tcp ---