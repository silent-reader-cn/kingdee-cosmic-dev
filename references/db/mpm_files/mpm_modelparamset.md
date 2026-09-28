# AI模型参数设置-mpm_modelparamset

## AI模型参数设置-主表 t_mpm_modelparamset

- **表名称：** AI模型参数设置-主表
- **表名：** t_mpm_modelparamset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftopp | top_p | numeric | 23 | 10 | √ | 0 | top_p |
| 3 | fpenalty | 重复性惩罚 | numeric | 23 | 10 | √ | 0 | 重复性惩罚 |
| 4 | ftemperature | 采样温度 | numeric | 23 | 10 | √ | 0 | 采样温度 |
| 5 | ftopk | top_k | numeric | 23 | 10 | √ | 0 | top_k |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpm_modelparamset |  | fid |
