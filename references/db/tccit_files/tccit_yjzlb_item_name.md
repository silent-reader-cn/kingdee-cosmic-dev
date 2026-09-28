# 预缴总览表项目名称-tccit_yjzlb_item_name

## 预缴总览表项目名称-主表 t_tccit_yjzlb_item_name

- **表名称：** 预缴总览表项目名称-主表
- **表名：** t_tccit_yjzlb_item_name

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | findex | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 3 | fitemname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |
| 4 | frowno | 行号 | varchar | 50 |  | √ | ' ' | 行号 |
| 5 | fdrafttype | 底稿类型 | varchar | 50 |  | √ | ' ' | 底稿类型,枚举: 1 :普通 2 :查账征收 3 :核定征收 |
| 6 | fdraftpurpose | 底稿用途 | varchar | 50 |  | √ | ' ' | 底稿用途,枚举: :通用 nssb :纳税申报 sjjt :税金计提 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_yjzlb_item_name |  | fid |
| 2 | idx_tccit_yjzlb_item_name_1 |  | frowno |
| 3 | idx_tccit_yjzlb_item_name_2 |  | findex |
