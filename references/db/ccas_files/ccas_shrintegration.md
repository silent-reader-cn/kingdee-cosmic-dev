# s-HR集成配置-ccas_shrintegration

## s-HR集成配置-主表 t_ccas_shrintegration

- **表名称：** s-HR集成配置-主表
- **表名：** t_ccas_shrintegration

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :启用 |
| 5 | fconfigstatus | 集成配置状态 | varchar | 30 |  | √ | ' ' | 集成配置状态,枚举: A :暂存 B :禁用 C :启用 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fsecretvalue | s-HR接口密钥 | varchar | 255 |  | √ | ' ' | s-HR接口密钥 |
| 8 | fserverurl | s-HR接口地址 | varchar | 255 |  | √ | ' ' | s-HR接口地址 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 11 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccas_shrintegration_serurl |  | fserverurl |
| 2 | pk_t_ccas_shrintegration |  | fid |
