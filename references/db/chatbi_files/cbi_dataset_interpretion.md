# 数据解读配置-cbi_dataset_interpretion

## 数据解读配置-主表 t_cbi_dataset_interpretio

- **表名称：** 数据解读配置-主表
- **表名：** t_cbi_dataset_interpretio

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisdatainterpret | 复选框 | bpchar | 1 |  | √ | '0' | 复选框 |
| 3 | fthemeid | 长整数 | int8 | 64 |  | √ | 0 | 长整数 |
| 4 | fdatainterpretideastext | 数据解读内容 | varchar | 2000 |  | √ | ' ' | 数据解读内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_dataset_interpretio |  | fid |
| 2 | idx_theme_interpretio_fthemeid |  | fthemeid |
