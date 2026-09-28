# 预缴计提税款分摊单据-tccit_seasonal_split_sjjt

## 预缴计提税款分摊单据-主表 t_tccit_seasonal_split_sj

- **表名称：** 预缴计提税款分摊单据-主表
- **表名：** t_tccit_seasonal_split_sj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbranchspiltratio | 分支机构本期分摊比例 | numeric | 23 | 10 | √ | 0 | 分支机构本期分摊比例 |
| 3 | fbranchybtse | 分支机构本期分摊应补（退）所得税额 | numeric | 23 | 10 | √ | 0 | 分支机构本期分摊应补（退）所得税额 |
| 4 | fdraftnumber | 底稿编码 | varchar | 100 |  | √ | ' ' | 底稿编码 |
| 5 | fqbfzjgftbl | 政策确认-全部分支机构分摊比例 | numeric | 23 | 10 | √ | 0 | 政策确认-全部分支机构分摊比例 |
| 6 | fskssqq | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 7 | fitemno15sum | 税额计算总览表15行值 | numeric | 23 | 10 | √ | 0 | 税额计算总览表15行值 |
| 8 | funifiedsocialcode | 分支机构社会统一信用代码 | varchar | 50 |  | √ | ' ' | 分支机构社会统一信用代码 |
| 9 | fsjybtsdse | 实际应补（退）所得税额 | numeric | 23 | 10 | √ | 0 | 实际应补（退）所得税额 |
| 10 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: 1 :总机构类型 2 :分支类型 |
| 11 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 12 | fbranchreductionratio | 民族自治地区企业所得税地方分享部分减征幅度(%) | numeric | 23 | 10 | √ | 0 | 民族自治地区企业所得税地方分享部分减征幅度(%) |
| 13 | ftaxorgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fbranchorgid | 分支机构纳税人 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fbranchreductiontax | 民族自治地区企业所得税地方分享部分减免税额 | numeric | 23 | 10 | √ | 0 | 民族自治地区企业所得税地方分享部分减免税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_seasonal_split_sj |  | fid |
| 2 | idx_tccit_split_sj_orgskss |  | ftaxorgid,fskssqq,fskssqz |
