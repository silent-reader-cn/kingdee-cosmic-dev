# 业务冲突记录-im_mdc_busconflict

## 业务冲突记录-主表 t_im_mdc_busconflict

- **表名称：** 业务冲突记录-主表
- **表名：** t_im_mdc_busconflict

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fconflictentryid | 冲突单据分录id | int8 | 64 |  | √ | 0 | 冲突单据分录id |
| 3 | fbusbillno | 业务单据编号 | varchar | 50 |  | √ | ' ' | 业务单据编号 |
| 4 | fbusbillentryid | 业务单据分录id | int8 | 64 |  | √ | 0 | 业务单据分录id |
| 5 | fconflictid | 冲突单据id | int8 | 64 |  | √ | 0 | 冲突单据id |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fprdorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fsrctype | 来源类型 | varchar | 50 |  | √ | 'A' | 来源类型,枚举: A :生产倒冲 B :委外倒冲 |
| 9 | fbusformid | 业务单据 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fbusbillentryseq | 业务单据分录行号 | int4 | 32 |  | √ | 0 | 业务单据分录行号 |
| 12 | fbusbillid | 业务单据id | int8 | 64 |  | √ | 0 | 业务单据id |
| 13 | fconflictentryseq | 冲突单据分录行号 | int4 | 32 |  | √ | 0 | 冲突单据分录行号 |
| 14 | fconflictformid | 冲突单据 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 15 | fconflictbillno | 冲突单据编号 | varchar | 50 |  | √ | ' ' | 冲突单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_mdc_busconflict_ceid |  | fconflictentryid |
| 2 | idx_im_mdc_busconflict_beid |  | fbusbillentryid |
| 3 | pk_t_im_mdc_busconflict |  | fid |
