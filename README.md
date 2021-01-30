# portfolio

バイトをしていたスーパーでマネージャーが毎日、翌日のタイムスケジュールを作成しているのをみて、これは自動化できるのではないかと思い作成しました。

ヘッダーの当日従業員や当日仕事を変更し、スケジュールの作成をし直すことでスケジュールを変更できます。


基本的にはスケジュール作成日の従業員と仕事をもとに、局所探索法の考え方を真似て作成しました。局所探索法はmake_shift.initで行っています。
私のアルバイトをしていたスーパーは週固定のシフトであるので、Workerクラスに週固定の就業時間を入れ、日付選択とともにDayworkerクラスに継承する形にしました。

