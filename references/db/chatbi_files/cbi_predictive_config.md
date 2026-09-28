# 预测分析配置-cbi_predictive_config

## 预测分析配置-主表 t_cbi_predictive_cnf

- **表名称：** 预测分析配置-主表
- **表名：** t_cbi_predictive_cnf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdatasetid | 基础资料 | int8 | 64 |  | √ | 0 | [数据集 gai_cbi_dataset](../chatbi_files/gai_cbi_dataset.md) |
| 3 | fradiogroupfield | 单选按钮组 | varchar | 50 |  | √ | ' ' | 单选按钮组,枚举: 1 :Prophet模型 2 :ARIMA模型 |
| 4 | fisusepredictive | 复选框 | varchar | 1 |  | √ | ' ' | 复选框 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cbi_predict_idx_new |  | fdatasetid |
| 2 | pk_cbi_predictive_cnf |  | fid |
