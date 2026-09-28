# 基础资料控制业务基本信息差异-xkbd_auth_diff_base_info

## 基础资料控制业务基本信息差异-主表 t_perm_log_diff_bd_base

- **表名称：** 基础资料控制业务基本信息差异-主表
- **表名：** t_perm_log_diff_bd_base

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpre_controltype | 修改前：控制类型 | bpchar | 1 |  | √ | '0' | 修改前：控制类型 |
| 3 | fperm_logid | 日志id | int8 | 64 |  | √ | 0 | 日志id |
| 4 | fpre_ct_all_perm_ids | 修改前：操作项ids | varchar | 500 |  | √ | ' ' | 修改前：操作项ids |
| 5 | fafter_ct_all_perm_names | 修改后：操作项名称 | varchar | 500 |  | √ | ' ' | 修改后：操作项名称 |
| 6 | fcloud_name | 业务云名称 | varchar | 100 |  | √ | ' ' | 业务云名称 |
| 7 | fbdid | 基础资料 | varchar | 36 |  | √ | ' ' | [业务对象缓存管理 bos_entityobject_cache](../base_files/bos_entityobject_cache.md) |
| 8 | fentity_name | 单据名称 | varchar | 200 |  | √ | ' ' | 单据名称 |
| 9 | fappid | 应用id | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 10 | fbd_name | 基础资料名称 | varchar | 200 |  | √ | ' ' | 基础资料名称 |
| 11 | fpre_enable | 修改前：是否启用 | bpchar | 1 |  | √ | '0' | 修改前：是否启用 |
| 12 | fafter_controltype | 修改后：控制类型 | bpchar | 1 |  | √ | '0' | 修改后：控制类型 |
| 13 | fapp_name | 应用名称 | varchar | 100 |  | √ | ' ' | 应用名称 |
| 14 | fcloudid | 业务云id | varchar | 36 |  | √ | ' ' | [业务云 bos_devportal_bizcloud](../mdl_files/bos_devportal_bizcloud.md) |
| 15 | fsyspreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 16 | fafter_ct_all_perm_ids | 修改后：操作项ids | varchar | 500 |  | √ | ' ' | 修改后：操作项ids |
| 17 | fafter_enable | 修改后：是否启用 | bpchar | 1 |  | √ | '0' | 修改后：是否启用 |
| 18 | fcreat_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fentityid | 单据id | varchar | 36 |  | √ | ' ' | [实体元数据 bos_entitymeta](../mdl_files/bos_entitymeta.md) |
| 20 | fpre_ct_all_perm_names | 修改前：操作项名称 | varchar | 500 |  | √ | ' ' | 修改前：操作项名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_perm_log_diff_bd_base |  | fid |
| 2 | idx_t_perm_log_diff_bd_base |  | fperm_logid |
