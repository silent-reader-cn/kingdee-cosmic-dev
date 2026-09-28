# 试用配置-dfa_trial_config

## 试用配置-主表 t_dfa_trial_config

- **表名称：** 试用配置-主表
- **表名：** t_dfa_trial_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftrialequityinfo_tag | 试用权益信息_详情 | text | 0 |  |  | null | 试用权益信息_详情 |
| 3 | ftrialequityinfo | 试用权益信息 | varchar | 1024 |  | √ | ' ' | 试用权益信息 |
| 4 | ftrialflag | 试用 | bpchar | 1 |  | √ | '0' | 试用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dfa_trial_config |  | fid |
| 2 | idx_dfa_trial_config_m0 |  | ftrialflag |
