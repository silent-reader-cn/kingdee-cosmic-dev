# 接口全局配置-invsm_apiconfig_setting

## 接口全局配置-主表 t_invsm_apiconfig_setting

- **表名称：** 接口全局配置-主表
- **表名：** t_invsm_apiconfig_setting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdisposelimit | 处理限制 | int8 | 64 |  | √ | 0 | 处理限制 |
| 3 | fdetaillimit | 明细限制 | int8 | 64 |  | √ | 0 | 明细限制 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_invsm_apiconfig_setting |  | fid |
| 2 | idx_invsm_apiconfig_setting |  | fdisposelimit |
