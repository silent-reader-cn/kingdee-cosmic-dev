# 值集弹性域数据表-fah_flex_valueset

## 值集弹性域数据表-主表 t_fah_flex_valueset

- **表名称：** 值集弹性域数据表-主表
- **表名：** t_fah_flex_valueset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fseq | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 3 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 4 | fexpiredate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 5 | ftxtattr12 | 文本12 | varchar | 150 |  | √ | ' ' | 文本12 |
| 6 | ftxtattr13 | 文本13 | varchar | 150 |  | √ | ' ' | 文本13 |
| 7 | ftxtattr14 | 文本14 | varchar | 150 |  | √ | ' ' | 文本14 |
| 8 | ftxtattr15 | 文本15 | varchar | 150 |  | √ | ' ' | 文本15 |
| 9 | ftxtattr10 | 文本10 | varchar | 150 |  | √ | ' ' | 文本10 |
| 10 | ftxtattr11 | 文本11 | varchar | 150 |  | √ | ' ' | 文本11 |
| 11 | ftxtattr2 | 文本2 | varchar | 150 |  | √ | ' ' | 文本2 |
| 12 | fname | 名称 | varchar | 150 |  | √ | ' ' | 名称 |
| 13 | ftxtattr1 | 文本1 | varchar | 150 |  | √ | ' ' | 文本1 |
| 14 | ftxtattr16 | 文本16 | varchar | 150 |  | √ | ' ' | 文本16 |
| 15 | ftxtattr17 | 文本17 | varchar | 150 |  | √ | ' ' | 文本17 |
| 16 | ftxtattr18 | 文本18 | varchar | 150 |  | √ | ' ' | 文本18 |
| 17 | ftxtattr19 | 文本19 | varchar | 150 |  | √ | ' ' | 文本19 |
| 18 | ftxtattr9 | 文本9 | varchar | 150 |  | √ | ' ' | 文本9 |
| 19 | ftxtattr8 | 文本8 | varchar | 150 |  | √ | ' ' | 文本8 |
| 20 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 21 | ftxtattr7 | 文本7 | varchar | 150 |  | √ | ' ' | 文本7 |
| 22 | ftxtattr6 | 文本6 | varchar | 150 |  | √ | ' ' | 文本6 |
| 23 | ftxtattr5 | 文本5 | varchar | 150 |  | √ | ' ' | 文本5 |
| 24 | ftxtattr4 | 文本4 | varchar | 150 |  | √ | ' ' | 文本4 |
| 25 | ftxtattr3 | 文本3 | varchar | 150 |  | √ | ' ' | 文本3 |
| 26 | fvaluesettypeid | 引用值集类型的ID | int8 | 64 |  | √ | 0 | [外部数据值集 fah_valueset_type](../edah_files/fah_valueset_type.md) |
| 27 | fenable | 启用状态 | bpchar | 1 |  | √ | ' ' | 启用状态 |
| 28 | fnumber | 值 | varchar | 150 |  | √ | ' ' | 值 |
| 29 | ftxtattr20 | 文本20 | varchar | 150 |  | √ | ' ' | 文本20 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fah_flex_valueset |  | fid |
| 2 | idx_fah_flex_valueset_no |  | fvaluesettypeid,fnumber |
