# 匹配企业-ef_match_company

## 匹配企业-主表 t_ef_matchcompany

- **表名称：** 匹配企业-主表
- **表名：** t_ef_matchcompany

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 匹配公司名称 | varchar | 300 |  | √ | ' ' | 匹配公司名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 6 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fpageid | 页面id | varchar | 255 |  | √ | ' ' | 页面id |
| 8 | fmatchtype | 匹配类型 | varchar | 255 |  | √ | ' ' | 匹配类型 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fhistoryname | 曾用名 | varchar | 255 |  | √ | ' ' | 曾用名 |
| 12 | fownertype | 主体类型 | varchar | 255 |  | √ | ' ' | 主体类型 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 关键字 | varchar | 255 |  | √ | ' ' | 关键字 |
| 15 | fcompanyid | 匹配公司id | varchar | 50 |  | √ | ' ' | 匹配公司id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ef_matchcompany_number |  | fnumber |
| 2 | pk_t_ef_matchcompany |  | fid |
