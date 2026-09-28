# 通道配置信息-tdm_setting_supplier

## 通道配置信息-主表 t_tdm_setting_supplier

- **表名称：** 通道配置信息-主表
- **表名：** t_tdm_setting_supplier

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 3 | fvalue | 值 | varchar | 2000 |  | √ | ' ' | 值 |
| 4 | fvalue_tag | 值_详情 | text | 0 |  |  | null | 值_详情 |
| 5 | fkey | 名称 | varchar | 50 |  | √ | ' ' | 名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_setsup_name |  | fkey |
| 2 | pk_tdm_setting_supplier |  | fid |
