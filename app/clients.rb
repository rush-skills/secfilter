web1 = "http://localhost:8001"
web2 = "http://localhost:8002"

ua1 = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"

calls = [
  "curl -A \"#{ua1}\" #{web1}/index.html",
  "curl -A \"#{ua1}\" #{web2}/index.html",
  "curl -A \"#{ua1}\" #{web1}/asd.html",
  "curl -A \"#{ua1}\" #{web2}/asd.html",
  "curl -A \"#{ua1}\" -e \"http://badsite.com\" #{web1}/index.html",
  "curl -A \"#{ua1}\" -e \"http://badsite.com\" #{web2}/index.html",
  "curl --header \"X-Forwarded-For: 1.2.3.5\" -A \"#{ua1}\" -e \"http://badsite.com\" #{web1}/asd.html",
  "curl --header \"X-Forwarded-For: 1.2.3.5\" -A \"#{ua1}\" -e \"http://badsite.com\" #{web2}/asd.html",
  "curl -X POST #{web1}/index.html",
  "curl -X POST #{web2}/index.html",
  "curl #{web1}/index.html",
  "curl #{web2}/index.html",
  "curl #{web1}/asd.html",
  "curl #{web2}/asd.html",
  "curl --header \"X-Forwarded-For: 1.2.3.5\" #{web1}/index.html",
  "curl --header \"X-Forwarded-For: 1.2.3.6\" #{web2}/index.html",
  "curl --header \"X-Forwarded-For: 1.2.3.7\" #{web1}/asd.html",
  "curl --header \"X-Forwarded-For: 1.2.3.8\" #{web2}/asd.html",
  "curl --header \"X-Forwarded-For: 1.2.3.5\" -e \"http://badsite.com\" #{web1}/index.html",
  "curl -e \"http://badsite.com\" #{web2}/index.html",
  "curl --header \"X-Forwarded-For: 1.2.3.5\" -e \"http://badsite.com\" #{web1}/asd.html",
  "curl -e \"http://badsite.com\" #{web2}/asd.html",
  # HACK: SPOOF XSS
  # "curl -A \"#{ua1}\" #{web1}/index.html",
  # "curl -A \"#{ua1}\" #{web2}/index.html",
]

while true
  puts "loop"
  count = rand(10) + 10
  count.times do |c|
    `#{calls.sample}`
  end
  puts "going to sleep"
  sleep 2
  puts "out of sleep"
end
