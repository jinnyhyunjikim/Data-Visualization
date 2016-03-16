class Friend < ActiveRecord::Base
  mount_uploader :photo, PhotoUploader

	validates_presence_of :full_name, :phone, :email, :friendship_level
	validates_format_of :phone, with: /\A(\d{10}|\(?\d{3}\)?[-. ]\d{3}[-.]\d{4})\z/, message: "should be 10 digits (area code needed) and delimited with dashes only"
	validates_format_of :email, with: /\A[\w]([^@\s,;]+)@(([\w-]+\.)+(com|edu|org|net|gov|mil|biz|info))\z/i, message: "is not a valid format"
	validates_numericality_of :friendship_level,  only_integer: true , greater_than: 0, less_than: 5

	FRIENDSHIP_LEVELS = [ ["Casual", 1], ["Good", 2], ["Close", 3], ["Best", 4] ]

end
