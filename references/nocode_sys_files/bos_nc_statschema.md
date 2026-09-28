# 统计卡片和视图映射-bos_nc_statschema

## 统计卡片和视图映射-主表 t_nocode_statschema

- **表名称：** 统计卡片和视图映射-主表
- **表名：** t_nocode_statschema

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdisplay | 是否显示 | bpchar | 1 |  | √ | '0' | 是否显示 |
| 3 | findex | 顺序 | int8 | 64 |  | √ | 0 | 顺序 |
| 4 | fcardid | 轻分析卡片ID | varchar | 50 |  | √ | ' ' | 轻分析卡片ID |
| 5 | fschemaid | 视图ID | int8 | 64 |  | √ | 0 | 视图ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_nocode_statschema |  | fid |
| 2 | idx_nc_ss_fschemaid |  | fschemaid |
