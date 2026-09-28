# 供应商分析F7-src_supplieranalyf7

## 供应商分析F7-主表 t_src_supplieranaly

- **表名称：** 供应商分析F7-主表
- **表名：** t_src_supplieranaly

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 4 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | 'A' |  |
| 5 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 6 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 7 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 8 | fschemeid | 分析方案 | int8 | 64 |  | √ | 0 | 方案配置 src_scheme |
| 9 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 10 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 11 | fdescription | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 12 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 13 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 14 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 15 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 16 | fbillno | 编号 | varchar | 30 |  | √ | ' ' | 编号 |
| 17 | ftemplate | ftemplate | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_supplieranaly_pid |  | fparentid |
| 2 | idx_src_supplieranaly_sid |  | fschemeid |
| 3 | pk_src_supplieranaly |  | fid |
| 4 | idx_src_supplieranaly_proid |  | fprojectid |
