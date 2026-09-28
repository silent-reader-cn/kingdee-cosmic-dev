# 编码规则断号-bos_coderule_intermitno

## 编码规则断号-主表 t_cr_intermitno

- **表名称：** 编码规则断号-主表
- **表名：** t_cr_intermitno

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fsortitemvalue | 流水号依据 | varchar | 255 |  | √ | ' ' | 流水号依据 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcoderuleid | 编码规则 | varchar | 36 |  | √ | ' ' | [编码规则 bos_coderule](../base_files/bos_coderule.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fserial | 断号 | int8 | 64 |  | √ | 0 | 断号 |
| 8 | fseqsegmententryid | 区间分段分录 | varchar | 36 |  | √ | ' ' | 区间分段分录 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cr_intermitno_serial |  | fcoderuleid,fsortitemvalue,fserial |
| 2 | t_cr_intermitno_pkey |  | fid |
