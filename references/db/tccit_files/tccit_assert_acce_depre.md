# 资产加速折旧/摊销-tccit_assert_acce_depre

## 资产加速折旧/摊销-主表 t_tccit_assert_acce_depre

- **表名称：** 资产加速折旧/摊销-主表
- **表名：** t_tccit_assert_acce_depre

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织ID | varchar | 100 |  | √ | ' ' | 组织ID |
| 3 | faccethisseason | 加速本季度取值 | numeric | 23 | 10 | √ | 0.0000000000 | 加速本季度取值 |
| 4 | ftaxthisseason | 税法本季度取值 | numeric | 23 | 10 | √ | 0.0000000000 | 税法本季度取值 |
| 5 | fbntotalsfdepre | 本年累计税法折旧\摊销 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计税法折旧\摊销 |
| 6 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 7 | fassertvalue | 资产原值 | numeric | 23 | 10 | √ | 0.0000000000 | 资产原值 |
| 8 | fbntotalzzdepre | 本年累计账载折旧\摊销 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计账载折旧\摊销 |
| 9 | ftotalacce1 | 累计加速折旧季度一 | numeric | 23 | 10 | √ | 0.0000000000 | 累计加速折旧季度一 |
| 10 | faccedepretype | 加速折旧类型 | varchar | 30 |  | √ | ' ' | 加速折旧类型 |
| 11 | freprintthisseason | 帐载本季度取值 | numeric | 23 | 10 | √ | 0.0000000000 | 帐载本季度取值 |
| 12 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 13 | ftotalreprint4 | 累计帐载折旧季度四 | numeric | 23 | 10 | √ | 0.0000000000 | 累计帐载折旧季度四 |
| 14 | fyear | 年份 | int8 | 64 |  | √ | 0 | 年份 |
| 15 | ftotalacce2 | 累计加速折旧季度二 | numeric | 23 | 10 | √ | 0.0000000000 | 累计加速折旧季度二 |
| 16 | ftotaltaxdepre3 | 累计税法折旧季度三 | numeric | 23 | 10 | √ | 0.0000000000 | 累计税法折旧季度三 |
| 17 | fbntotaljsdepre | 本年累计加速折旧\摊销 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计加速折旧\摊销 |
| 18 | ftotalacce3 | 累计加速折旧季度三 | numeric | 23 | 10 | √ | 0.0000000000 | 累计加速折旧季度三 |
| 19 | ftotaltaxdepre4 | 累计税法折旧季度四 | numeric | 23 | 10 | √ | 0.0000000000 | 累计税法折旧季度四 |
| 20 | ftotalacce4 | 累计加速折旧季度四 | numeric | 23 | 10 | √ | 0.0000000000 | 累计加速折旧季度四 |
| 21 | ftotaltaxdepre1 | 累计税法折旧季度一 | numeric | 23 | 10 | √ | 0.0000000000 | 累计税法折旧季度一 |
| 22 | fassertname | 资产名称 | varchar | 100 |  | √ | ' ' | 资产名称 |
| 23 | ftotaltaxdepre2 | 累计税法折旧季度二 | numeric | 23 | 10 | √ | 0.0000000000 | 累计税法折旧季度二 |
| 24 | ftotalreprint1 | 累计帐载折旧季度一 | numeric | 23 | 10 | √ | 0.0000000000 | 累计帐载折旧季度一 |
| 25 | ftotalreprint3 | 累计帐载折旧季度三 | numeric | 23 | 10 | √ | 0.0000000000 | 累计帐载折旧季度三 |
| 26 | ftotalreprint2 | 累计帐载折旧季度二 | numeric | 23 | 10 | √ | 0.0000000000 | 累计帐载折旧季度二 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tccit_assert_acce_depre_pkey |  | fid |
| 2 | idx_tccit_assert_acce_depre |  | forgid,fyear |
