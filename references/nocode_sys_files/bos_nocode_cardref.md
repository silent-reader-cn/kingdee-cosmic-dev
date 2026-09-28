# 卡片引用-bos_nocode_cardref

## 卡片引用-主表 t_nocode_cardref

- **表名称：** 卡片引用-主表
- **表名：** t_nocode_cardref

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftype | 引用类型 | bpchar | 1 |  | √ | ' ' | 引用类型,枚举: |
| 3 | fcardid | 卡片ID | int8 | 64 |  | √ | 0 | 卡片ID |
| 4 | fuserid | 用户ID | int8 | 64 |  | √ | 0 | 用户ID |
| 5 | fschemaid | 方案ID | int8 | 64 |  | √ | 0 | 方案ID |
| 6 | fformid | 表单ID | varchar | 50 |  | √ | ' ' | 表单ID |
| 7 | fappid | 应用ID | varchar | 50 |  | √ | ' ' | 应用ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_nocode_cardref |  | fid |
| 2 | idx_nc_cr_cardid |  | fcardid |
