# 财务卡片更新外部配置-fa_externalconfig

## 财务卡片更新外部配置-主表 t_fa_externalconfig

- **表名称：** 财务卡片更新外部配置-主表
- **表名：** t_fa_externalconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftext | 示例 | varchar | 100 |  | √ | ' ' | 示例 |
| 3 | fmethodname | 方法名称 | varchar | 50 |  | √ | ' ' | 方法名称 |
| 4 | fcloudid | 云id | varchar | 50 |  | √ | ' ' | 云id |
| 5 | fservicename | 服务名称 | varchar | 50 |  | √ | ' ' | 服务名称 |
| 6 | fappid | 应用id | varchar | 50 |  | √ | ' ' | 应用id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fa_externalconfig |  | fid |
| 2 | idx_fa_exteranlconfig |  | fcloudid,fappid |
