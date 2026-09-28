# 服务注册-ap_service_register

## 服务注册-主表 t_ap_service_register

- **表名称：** 服务注册-主表
- **表名：** t_ap_service_register

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foperationname | 操作名称(后台) | varchar | 2000 |  | √ | ' ' | 操作名称(后台) |
| 3 | fservicetype | 服务类型 | varchar | 50 |  | √ | ' ' | 服务类型,枚举: |
| 4 | fbilltype | 注册服务单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 5 | foperationcode | 操作名称 | varchar | 50 |  | √ | ' ' | 操作名称,枚举: |
| 6 | fservicetypename | 服务类型名称 | varchar | 50 |  | √ | ' ' | 服务类型名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_ser_reg_billtype |  | fbilltype |
| 2 | pk_t_ap_service_register |  | fid |
