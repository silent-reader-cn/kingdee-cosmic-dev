# 应用启用配置-bos_smc_appconfig

## 应用启用配置-主表 t_smc_appconfig

- **表名称：** 应用启用配置-主表
- **表名：** t_smc_appconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | ftype | 类型 | varchar | 36 |  | √ | ' ' | 类型,枚举: bizcloud :云 bizapp :应用 |
| 4 | fbizcloudid | 业务云 | varchar | 50 |  | √ | ' ' | [业务云 bos_devportal_bizcloud](../mdl_files/bos_devportal_bizcloud.md) |
| 5 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 2 :不可禁用 |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fbizappid | 业务应用 | varchar | 50 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | ux_t_smc_appconfig |  | ftype,fbizcloudid,fbizappid |
| 2 | pk_t_smc_appconfig |  | fid |
