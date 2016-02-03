json.array!(@books) do |book|
  json.extract! book, :id, :title, :year_published, :publisher_id
  json.url book_url(book, format: :json)
end
