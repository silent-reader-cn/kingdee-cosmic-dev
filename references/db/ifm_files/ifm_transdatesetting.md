# 交易日期设置-ifm_transdatesetting

## 交易日期设置-主表 t_ifm_transdatesetting

- **表名称：** 交易日期设置-主表
- **表名：** t_ifm_transdatesetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | ffixationdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 6 | ftransdatetype | 交易时间类型 | varchar | 30 |  | √ | ' ' | 交易时间类型,枚举: A :自然日期 C :顺序日期 B :固定日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ifm_transdatesetting |  | ftransdatetype |
| 2 | pk_t_ifm_transdatesetting |  | fid |
