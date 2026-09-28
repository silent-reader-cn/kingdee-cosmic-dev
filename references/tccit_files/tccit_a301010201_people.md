# 其中：高新技术企业相关人员计算底稿-tccit_a301010201_people

## 其中：高新技术企业相关人员计算底稿-主表 t_tccit_a301010201_people

- **表名称：** 其中：高新技术企业相关人员计算底稿-主表
- **表名：** t_tccit_a301010201_people

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 3 | fpeopletype | 项目 | varchar | 50 |  | √ | ' ' | 项目,枚举: |
| 4 | fitemtype | 项目 | varchar | 50 |  | √ | ' ' | 项目 |
| 5 | fname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |
| 6 | fpeopleamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 7 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 8 | fitemnumber | 项目编码 | varchar | 50 |  | √ | ' ' | 项目编码 |
| 9 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 10 | fruleid | 规则id | int8 | 64 |  | √ | 0 | 规则id |
| 11 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_a301010201_people |  | forgid,fskssqz,fskssqq,fpeopletype |
| 2 | pk_tccit_a301010201_people |  | fid |
