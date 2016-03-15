class CreateFriends < ActiveRecord::Migration
  def change
    create_table :friends do |t|
      t.string :full_name
      t.string :nickname
      t.string :email
      t.integer :phone
      t.string :website
      t.integer :friendship_level

      t.timestamps null: false
    end
  end
end
