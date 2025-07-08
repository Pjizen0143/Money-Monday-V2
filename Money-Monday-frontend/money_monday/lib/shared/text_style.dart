import 'package:flutter/material.dart';

const String mainFont = "OpenSans";

class AppTextStyle {
  static TextStyle headingStyle(BuildContext context) {
    return Theme.of(context).textTheme.headlineLarge!.copyWith(
          fontFamily: mainFont,
          fontWeight: FontWeight.bold,
          fontSize: 26,
        );
  }

  static TextStyle subheadingStyle(BuildContext context) {
    return Theme.of(context).textTheme.headlineMedium!.copyWith(
          fontFamily: mainFont,
          fontWeight: FontWeight.bold,
          fontSize: 17,
        );
  }

  static TextStyle bodyStyle(BuildContext context) {
    return Theme.of(context).textTheme.bodyMedium!.copyWith(
          fontFamily: mainFont,
          fontSize: 13,
        );
  }

  static TextStyle hintStyle(BuildContext context) {
    return Theme.of(context).textTheme.bodySmall!.copyWith(
          fontFamily: mainFont,
          fontWeight: FontWeight.bold,
          color: Theme.of(context).hintColor,
        );
  }

  static TextStyle inputStyle(BuildContext context) {
    return Theme.of(context).textTheme.bodyMedium!.copyWith(
          fontFamily: mainFont,
          fontWeight: FontWeight.w600,
        );
  }
}
