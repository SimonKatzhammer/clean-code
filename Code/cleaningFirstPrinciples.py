public static Date getPreviousDayOfWeek(int weekday, Date from) {
  // check arguments…
  if (!isValidWeekdayCode(weekday)) {
    throw new IllegalArgumentException(
      "Invalid day-of-the-week code."
    );
  }

  // find the date…
  final int adjust;
  final int baseDOW = from.getDayOfWeek();
  if (baseDOW > weekday) {
    adjust = Math.min(0, weekday - baseDOW);
  } else {
    adjust = -7 + Math.max(0, weekday - baseDOW);
  }

  return Date.addDays(adjust, from);
}



# new code:
# my first approach to cleaning the code
public static Date getPreviousDayOfWeek(int weekday, Date from) {
  int targetWeekday = from.getDayOfWeek();

  checkIfValidWeekday(weekday);
  daysBefore(targetWeekday, from);

  return Date.addDays(targetWeekday, from);
}


public static void checkIfValidWeekday(int weekday) {
  if (!isValidWeekdayCode(weekday)) {
      throw new IllegalArgumentException(
        "Invalid day-of-the-week code."
      );
    }
}

public int checkIfValidWeekday(int adjust, int baseDOW) {
  if (baseDOW > weekday) {
    adjust = Math.min(0, weekday - baseDOW);
  } else {
    adjust = -7 + Math.max(0, weekday - baseDOW);
  }
  return adjust;
}