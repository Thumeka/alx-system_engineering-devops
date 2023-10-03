#!/usr/bin/env ruby
# Match hbtn not hbbtn

puts ARGV[0].scan(/hb?tn/).join
