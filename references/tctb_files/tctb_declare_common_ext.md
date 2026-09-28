# 申报公共扩展表-tctb_declare_common_ext

## 申报公共扩展表-主表 t_tctb_declare_ext

- **表名称：** 申报公共扩展表-主表
- **表名：** t_tctb_declare_ext

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftbrq | 填表日期 | timestamp | 0 |  |  | null | 填表日期 |
| 3 | fkszjgxzqh | 跨省总机构行政区划 | varchar | 50 |  | √ | ' ' | 跨省总机构行政区划 |
| 4 | fblrysfzjlx | 办理人员身份证件类型 | varchar | 50 |  | √ | ' ' | 办理人员身份证件类型 |
| 5 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 |
| 6 | fslr | 受理人 | varchar | 50 |  | √ | ' ' | 受理人 |
| 7 | fjbrzyzjhm | 经办人执业证件号码 | varchar | 50 |  | √ | ' ' | 经办人执业证件号码 |
| 8 | fblr | 办理人 | varchar | 50 |  | √ | ' ' | 办理人 |
| 9 | fslrq | 受理日期 | timestamp | 0 |  |  | null | 受理日期 |
| 10 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |
| 11 | fdlsb | 是否代理申报 | varchar | 50 |  | √ | ' ' | 是否代理申报 |
| 12 | fzgswjg | 主管税务机关 | varchar | 50 |  | √ | ' ' | 主管税务机关 |
| 13 | fblrysfzjhm | 办理人员身份证件号码 | varchar | 50 |  | √ | ' ' | 办理人员身份证件号码 |
| 14 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 15 | ffddbrqzrq | 法定代表人签字日期 | timestamp | 0 |  |  | null | 法定代表人签字日期 |
| 16 | fjbr | 经办人 | varchar | 50 |  | √ | ' ' | 经办人 |
| 17 | fdlsbrq | 代理申报日期 | timestamp | 0 |  |  | null | 代理申报日期 |
| 18 | fdlsbzjjg | 代理申报中介机构 | varchar | 50 |  | √ | ' ' | 代理申报中介机构 |
| 19 | fkjzg | 会计主管 | varchar | 50 |  | √ | ' ' | 会计主管 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_declare_ext |  | fsbbid,fewblxh |
| 2 | pk_tctb_declare_ext |  | fid |
