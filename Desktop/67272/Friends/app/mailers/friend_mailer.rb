class FriendMailer < ApplicationMailer

  def new_friend_msg(friend)
    @friend = friend
    mail(:to => friend.email, :subject => "My New Friend")
	end	

  def remove_friend_msg(friend)
    @friend = friend
    mail(:to => friend.email, :subject => "My Old Friend")
	end		
end
