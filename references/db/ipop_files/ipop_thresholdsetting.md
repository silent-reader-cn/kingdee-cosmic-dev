# 阈值配置-ipop_thresholdsetting

## 阈值配置-主表 t_ipop_thresholdsetting

- **表名称：** 阈值配置-主表
- **表名：** t_ipop_thresholdsetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgrpname | 分组名称 | varchar | 50 |  | √ | ' ' | 分组名称 |
| 3 | fthresholdtype | 阈值类型 | varchar | 50 |  | √ | 'percent' | 阈值类型,枚举: percent :百分比 modulus :绝对值 |
| 4 | fwarning | 预警 | varchar | 1 |  | √ | '1' | 预警 |
| 5 | fgrpnumber | 分组编码 | varchar | 50 |  | √ | ' ' | 分组编码 |
| 6 | fdseq | 排序 | int4 | 32 |  | √ | 0 | 排序 |
| 7 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位 |
| 8 | fwarningvalue | 余量预警值 | int4 | 32 |  | √ | 20 | 余量预警值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ipop_thresholdsetting |  | fid |
| 2 | idx_ipop_thresholdsetting_warning |  | fwarning |
