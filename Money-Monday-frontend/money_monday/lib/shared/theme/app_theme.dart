import 'package:flutter/material.dart';
import 'package:money_monday/shared/colors.dart';
import 'package:money_monday/shared/theme/text_theme.dart';

class AppTheme {
  static final lightTheme = ThemeData(
    colorScheme: ColorScheme.light(
      primary: AppColors.orange,
      secondary: AppColors.cream,
    ),

    scaffoldBackgroundColor: AppColors.orange,

    textTheme: AppTextTheme.lightTextTheme,

    fontFamily: "OpenSans",
  );

  static final darkTheme = ThemeData(
    colorScheme: ColorScheme.dark(
      primary: AppColors.darkBlack,
      secondary: AppColors.orange,
    ),

    scaffoldBackgroundColor: AppColors.darkBlack,

    textTheme: AppTextTheme.darkTextTheme,

    fontFamily: "OpenSans",
  );
}
