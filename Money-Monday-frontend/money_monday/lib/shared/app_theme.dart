import 'package:flutter/material.dart';
import 'package:money_monday/shared/colors.dart';

class AppTheme{
  static final lightTheme = ThemeData(
    scaffoldBackgroundColor: AppColors.orange,
    textTheme: const TextTheme(
      headlineLarge: TextStyle(color: AppColors.lightBlack),
      headlineMedium: TextStyle(color: AppColors.lightBlack),
      bodyLarge: TextStyle(color: AppColors.lightBlack),
      bodyMedium: TextStyle(color: AppColors.lightBlack)
    )
  );

  static final darkTheme = ThemeData(
    scaffoldBackgroundColor: AppColors.darkBlack,
    textTheme: TextTheme(
      headlineLarge: TextStyle(color: AppColors.cream),
      headlineMedium: TextStyle(color: AppColors.cream),
      bodyLarge: TextStyle(color: AppColors.cream),
      bodyMedium: TextStyle(color: AppColors.cream)
    )
  );

}