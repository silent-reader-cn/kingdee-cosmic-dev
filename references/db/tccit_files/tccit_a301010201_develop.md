# 其中：高新技术企业相关研发计算底稿-tccit_a301010201_develop

## 其中：高新技术企业相关研发计算底稿-主表 t_tccit_a301010201_deve

- **表名称：** 其中：高新技术企业相关研发计算底稿-主表
- **表名：** t_tccit_a301010201_deve

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 3 | fname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |
| 4 | fpretwoyear | 前二年度 | numeric | 23 | 10 | √ | 0.0000000000 | 前二年度 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 6 | fpreoneyear | 前一年度 | numeric | 23 | 10 | √ | 0.0000000000 | 前一年度 |
| 7 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 8 | fcurryear | 本年度 | numeric | 23 | 10 | √ | 0.0000000000 | 本年度 |
| 9 | fitemtype | 项目 | varchar | 50 |  | √ | ' ' | 项目 |
| 10 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 11 | fdeveloptype | 项目 | varchar | 50 |  | √ | ' ' | 项目,枚举: |
| 12 | fitemnumber | 项目编码 | varchar | 50 |  | √ | ' ' | 项目编码 |
| 13 | fsumamount | 合计 | numeric | 23 | 10 | √ | 0.0000000000 | 合计 |
| 14 | fruleid | 规则id | int8 | 64 |  | √ | 0 | 规则id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_a301010201_deve |  | fid |
| 2 | idx_tccit_a301010201_deve |  | forgid,fskssqq,fskssqz,fdeveloptype |
