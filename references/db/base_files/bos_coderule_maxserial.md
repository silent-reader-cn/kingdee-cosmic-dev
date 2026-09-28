# 编码规则最大号-bos_coderule_maxserial

## 编码规则最大号-主表 t_cr_maxserial

- **表名称：** 编码规则最大号-主表
- **表名：** t_cr_maxserial

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fsortitemvalue | 流水号依据 | varchar | 255 |  | √ | ' ' | 流水号依据 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcoderuleid | 编码规则 | varchar | 36 |  | √ | ' ' | 编码规则 bos_coderule |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fmaxserial | 最大流水号 | int8 | 64 |  | √ | 0 | 最大流水号 |
| 7 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | finitserial | 初始流水号 | int8 | 64 |  | √ | 0 | 初始流水号 |
| 9 | fseqsegmententryid | 区间分段分录 | varchar | 36 |  | √ | ' ' | 区间分段分录 |
| 10 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cr_maxserial_fcrid |  | fcoderuleid |
| 2 | idx_cr_maxserial_cridsortitem |  | fcoderuleid,fsortitemvalue |
| 3 | t_cr_maxserial_pkey |  | fid |
