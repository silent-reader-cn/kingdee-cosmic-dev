# 风险项异常维度-didc_warn_dimension

## 风险项异常维度-主表 t_didc_warn_dimension

- **表名称：** 风险项异常维度-主表
- **表名：** t_didc_warn_dimension

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建时间 |
| 5 | fauditdate | 审核日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 审核日期 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 修改时间 |
| 7 | fcatalogueid | 目录id | varchar | 255 |  | √ | ' ' | 目录id |
| 8 | fplanid | 风险项id | int8 | 64 |  | √ | 0 | 风险项id |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fdimensionvalue | 维度值 | varchar | 255 |  | √ | ' ' | 维度值 |
| 11 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 12 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fdimension | 维度 | varchar | 255 |  | √ | ' ' | 维度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_didc_dimension |  | fcatalogueid |
| 2 | pk_t_didc_warn_dimension |  | fid |
