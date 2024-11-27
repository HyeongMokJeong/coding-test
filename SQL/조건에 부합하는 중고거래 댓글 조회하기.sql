SELECT 
    board.title, 
    board.board_id, 
    reply.reply_id, 
    reply.writer_id, reply.contents, 
    DATE_FORMAT(reply.created_date, '%Y-%m-%d') created_date
FROM used_goods_board board
JOIN used_goods_reply reply ON reply.board_id = board.board_id
WHERE DATE_FORMAT(board.created_date, '%Y-%m') = '2022-10'
ORDER BY reply.created_date, board.title;