# 统计卡片-bos_nocode_stat_card

## 统计卡片-主表 t_nocode_stat_card

- **表名称：** 统计卡片-主表
- **表名：** t_nocode_stat_card

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftitle | 卡片名称 | varchar | 50 |  | √ | ' ' | 卡片名称 |
| 3 | fconfig | fconfig | text | 0 |  |  | null |  |
| 4 | fcardid | 轻分析卡片ID | varchar | 50 |  | √ | ' ' | 轻分析卡片ID |
| 5 | fuserid | 用户ID | int8 | 64 |  | √ | 0 | 用户ID |
| 6 | fformid | 表单ID | varchar | 50 |  | √ | ' ' | 表单ID |
| 7 | fappid | 应用ID | varchar | 50 |  | √ | ' ' | 应用ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_nc_sc_afu |  | fappid,fformid,fuserid |
| 2 | pk_nocode_stat_card |  | fid |
