import 'package:flutter/material.dart';
import 'package:money_monday/shared/colors.dart';

class AppTextTheme {
  static const lightTextTheme = TextTheme(
    headlineLarge: TextStyle(color: AppColors.lightBlack),

    headlineMedium: TextStyle(color: AppColors.lightBlack),

    bodyMedium: TextStyle(color: AppColors.lightBlack),

    bodySmall: TextStyle(color: AppColors.lightBlack),
  );

  static const darkTextTheme = TextTheme(
    headlineLarge: TextStyle(color: AppColors.cream),

    headlineMedium: TextStyle(color: AppColors.cream),

    bodyMedium: TextStyle(color: AppColors.cream),

    bodySmall: TextStyle(color: AppColors.cream),
  );
}
