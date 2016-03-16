json.array!(@friends) do |friend|
  json.extract! friend, :id, :full_name, :nickname, :email, :phone, :website, :friendship_level
  json.url friend_url(friend, format: :json)
end
