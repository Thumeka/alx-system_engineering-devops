#!/usr/bin/env ruby
# Match 10 digits number without spaces or dashes

puts ARGV[0].scan(/^[0-9]{10}$/).join
