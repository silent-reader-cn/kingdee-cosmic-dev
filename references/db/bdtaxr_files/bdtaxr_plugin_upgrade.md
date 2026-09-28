# 数据插件升级记录表-bdtaxr_plugin_upgrade

## 数据插件升级记录表-主表 t_bdtaxr_plugin_upgrade

- **表名称：** 数据插件升级记录表-主表
- **表名：** t_bdtaxr_plugin_upgrade

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsuccess | 是否成功 | varchar | 50 |  | √ | ' ' | 是否成功,枚举: 1 :成功 0 :失败 |
| 3 | ftype | 升级类型 | varchar | 50 |  | √ | ' ' | 升级类型 |
| 4 | fcreatetime | 升级时间 | timestamp | 0 |  |  | null | 升级时间 |
| 5 | ftable | 表名 | varchar | 50 |  | √ | ' ' | 表名 |
| 6 | fkey | id | varchar | 50 |  | √ | ' ' | id |
| 7 | flog | 日志 | varchar | 1000 |  | √ | ' ' | 日志 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bdtaxr_plugin_upgrade |  | ftype,ftable,fkey |
| 2 | pk_bdtaxr_plugin_upgrade |  | fid |
