# 新模型黑名单-bd_new_model_disable

## 新模型黑名单-主表 t_bd_newmode_blacklist

- **表名称：** 新模型黑名单-主表
- **表名：** t_bd_newmode_blacklist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbasedataid | 黑名单资料 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 3 | fbizcloudid | 云 | varchar | 36 |  | √ | ' ' | 业务云 bos_devportal_bizcloud |
| 4 | fistpl | 是否为模板 | bpchar | 1 |  | √ | '0' | 是否为模板 |
| 5 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_newmode_blacklist_basedata |  | fbasedataid |
| 2 | pk_t_bd_newmode_blacklist |  | fid |
