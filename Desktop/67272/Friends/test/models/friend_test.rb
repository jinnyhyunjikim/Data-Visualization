require 'test_helper'

class FriendTest < ActiveSupport::TestCase
  # test "the truth" do
  #   assert true
  # end
	should validate_presence_of(:full_name)
	should validate_presence_of(:email)
	should validate_presence_of(:friendship_level)


	should allow_value(1).for(:friendship_level)
	should allow_value(4).for(:friendship_level)
	should_not allow_value(0).for(:friendship_level)
	should_not allow_value(-1).for(:friendship_level)
	should_not allow_value(6).for(:friendship_level)

end
