# 参数值字典-xkbm_param_value

## 参数值字典-主表 t_xkbm_param_value

- **表名称：** 参数值字典-主表
- **表名：** t_xkbm_param_value

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparamvalue | 参数值 | int8 | 64 |  | √ | 0 | 参数值 |
| 3 | fparamtype | 参数类型 | bpchar | 1 |  | √ | ' ' | 参数类型,枚举: 0 :spreadjson长度大小 1 :填充单元格个数 2 :调整单个数 3 :调整单明细个数 4 :上传文件大小 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_param_value |  | fparamtype |
| 2 | pk_t_xkbm_param_value |  | fid |
