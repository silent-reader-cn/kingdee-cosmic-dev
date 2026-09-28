# 税务云参数配置-bdtaxr_param_setting_conf

## 税务云参数配置-主表 t_bdtaxr_par_setting_cof

- **表名称：** 税务云参数配置-主表
- **表名：** t_bdtaxr_par_setting_cof

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftzsmbl | 调整说明必录 | bpchar | 1 |  | √ | '0' | 调整说明必录 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bdtaxr_par_setting_cof |  | ftzsmbl |
| 2 | pk_bdtaxr_par_setting_cof |  | fid |
