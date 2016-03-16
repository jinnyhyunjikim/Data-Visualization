class AddPhotoToFriends < ActiveRecord::Migration
  def change
    add_column :friends, :photo, :string
  end
end
