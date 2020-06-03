size(Size, ID) :- item(ID, _, Size).
value(Value, ID) :- item(ID, Value, _).

overall_size([], 0).
overall_size([ItemID|Tail], Size) :-
    item(ItemID, _, ItemSize)
  , overall_size(Tail, TailSize)
  , Size is ItemSize + TailSize
  .

overall_value([], 0).
overall_value([ItemID|Tail], Size) :-
    item(ItemID, ItemSize, _)
  , overall_value(Tail, TailSize)
  , Size is ItemSize + TailSize
  .

ryggsakk([], _, [], 0).
ryggsakk([ItemID|FreshList], MaxSize, [ItemID|UsedList]) :-
    ryggsakk(FreshList, MaxSize, UsedList)
  , overall_size([ItemID|UsedList], UsedSize)
  , UsedSize =< MaxSize
  .
ryggsakk([_|MaxItems], MaxSize, ItemIDs) :-
  ryggsakk(MaxItems, MaxSize, ItemIDs).
