# 核算余额表设置-cal_balance_setting

## 核算余额表设置-主表 t_cal_balsetting

- **表名称：** 核算余额表设置-主表
- **表名：** t_cal_balsetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdividebasis | 划分依据 | varchar | 255 |  | √ | ' ' | 划分依据 |
| 3 | fcaldimension | 核算维度 | varchar | 255 |  | √ | ' ' | 核算维度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_balsetting_pkey |  | fid |
| 2 | idx_cal_balset_divide |  | fdividebasis |
